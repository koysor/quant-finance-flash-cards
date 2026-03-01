"""Flask Blueprint with all route handlers."""
import json
import re

from flask import Blueprint, abort, current_app, jsonify, redirect, render_template, request, session, url_for

from app.db import (
    delete_edge,
    get_all_cards,
    get_all_cards_by_date,
    get_all_cards_with_content,
    get_all_edges,
    get_card,
    get_cards_by_date_range,
    get_cards_by_tag,
    get_incoming,
    get_outgoing,
    get_random_card,
    get_topic_cards,
    save_edges_to_file,
)

bp = Blueprint("main", __name__)

# Named topic → colour map (shared with templates via context processor)
TOPIC_COLOURS: dict[str, str] = {
    "Calculus":             "#f59e0b",   # amber
    "Derivatives":          "#3b82f6",   # blue
    "Financial Mathematics":"#10b981",   # emerald
    "Linear Algebra":       "#8b5cf6",   # violet
    "Mathematical Notation":"#f97316",   # orange
    "Probability":          "#f43f5e",   # rose
    "Risk":                 "#ef4444",   # red
    "Statistics":           "#06b6d4",   # cyan
    "Stochastic Processes": "#6366f1",   # indigo
}
_DEFAULT_COLOUR = "#4f9ef8"


def _topic_colour(topic: str) -> str:
    return TOPIC_COLOURS.get(topic, _DEFAULT_COLOUR)


def _card_excerpt(html_content: str) -> str:
    """Return plain-text Definition paragraph for use in meta description tags."""
    m = re.search(
        r'<h2[^>]*>\s*Definition\s*</h2>\s*<p>(.*?)</p>',
        html_content, re.IGNORECASE | re.DOTALL,
    )
    if not m:
        return 'Bite-sized revision flash card for Quantitative Finance.'
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = ' '.join(text.split())
    return text[:157] + '…' if len(text) > 157 else text


@bp.get("/")
def index():
    tag = request.args.get("tag", "").strip()
    topic_filter = request.args.get("topic", "").strip()
    all_cards_list = get_all_cards()

    # All unique tags for the filter strip
    all_tags = sorted({
        t.strip()
        for c in all_cards_list
        for t in c["tags"].split(",")
        if t.strip()
    })

    if tag:
        cards = get_cards_by_tag(tag)
    else:
        cards = all_cards_list

    grouped: dict[str, list] = {}
    for card in cards:
        if topic_filter and card["topic"] != topic_filter:
            continue
        grouped.setdefault(card["topic"], []).append(card)

    return render_template(
        "index.html", grouped=grouped, active_tag=tag,
        active_topic=topic_filter, all_tags=all_tags,
    )


@bp.get("/tag/<tag>")
def tag_page(tag: str):
    cards = get_cards_by_tag(tag)
    if not cards:
        abort(404)

    grouped: dict[str, list] = {}
    for card in cards:
        grouped.setdefault(card["topic"], []).append(card)

    return render_template("tag.html", tag=tag, grouped=grouped, card_count=len(cards))


@bp.get("/random")
def random_card():
    card = get_random_card()
    if card is None:
        abort(404)
    return redirect(url_for("main.card_detail", card_id=card["id"]))


@bp.get("/recent")
def recent():
    start = request.args.get("start", "").strip() or None
    end = request.args.get("end", "").strip() or None
    is_json = (
        request.args.get("format") == "json" or
        request.headers.get("Accept") == "application/json"
    )

    # The database stores dates as 'YYYY-MM-DD HH:MM:SS' when time is present.
    # If start/end are provided as just dates (YYYY-MM-DD), append the earliest/latest time.
    if start and len(start) == 10: # YYYY-MM-DD format
        start = f"{start} 00:00:00"
    if end and len(end) == 10: # YYYY-MM-DD format
        end = f"{end} 23:59:59"

    # Use DESC order by default to show newest cards first
    cards = get_cards_by_date_range(start_date=start, end_date=end, order="DESC")

    if is_json:
        # Convert Row objects to dicts for JSON serialization
        return jsonify([dict(c) for c in cards])

    grouped: dict[str, list] = {}
    for card in cards:
        # Grouping by date might need adjustment if we want to group by date only,
        # but for now, let's keep the date string as is from the DB.
        date = card["created_date"] or "Unknown"
        grouped.setdefault(date, []).append(card)
    return render_template("recent.html", grouped=grouped)

@bp.get("/card/<path:card_id>")
def card_detail(card_id: str):
    card = get_card(card_id)
    if card is None:
        abort(404)

    outgoing = get_outgoing(card_id)
    incoming = get_incoming(card_id)

    # Prev/next within topic
    siblings = get_topic_cards(card["topic"])
    idx = next((i for i, c in enumerate(siblings) if c["id"] == card_id), -1)
    prev_card = dict(siblings[idx - 1]) if idx > 0 else None
    next_card = dict(siblings[idx + 1]) if idx < len(siblings) - 1 else None

    resources = current_app.config["RESOURCES"].get(card_id, {})
    notation = json.loads(card["notation"]) if card["notation"] else []

    return render_template(
        "card.html",
        card=card,
        outgoing=outgoing,
        incoming=incoming,
        prev_card=prev_card,
        next_card=next_card,
        card_tc=_topic_colour(card["topic"]),
        card_excerpt=_card_excerpt(card["html_content"]),
        resources=resources,
        notation=notation,
    )



@bp.post("/card/<path:card_id>/remove-link")
def remove_link(card_id: str):
    token = request.form.get("csrf_token", "")
    if not token or token != session.get("csrf_token"):
        abort(403)

    if get_card(card_id) is None:
        abort(404)

    edge_id = request.form.get("edge_id", "").strip()

    if edge_id:
        delete_edge(int(edge_id))
        save_edges_to_file()

    return redirect(url_for("main.card_detail", card_id=card_id))


_FORMULA_RE = re.compile(
    r'(<h2[^>]*>\s*Key\s+Formul(?:a|ae)\s*</h2>)(.*?)(?=<h2|$)',
    re.IGNORECASE | re.DOTALL,
)


@bp.get("/formulas")
def formulas():
    cards = get_all_cards_with_content()
    grouped: dict[str, list] = {}
    for card in cards:
        m = _FORMULA_RE.search(card["html_content"])
        if not m:
            continue
        formula_html = m.group(1) + m.group(2)
        grouped.setdefault(card["topic"], []).append({
            "name": card["name"],
            "id": card["id"],
            "formula_html": formula_html,
        })
    return render_template("formulas.html", grouped=grouped)


@bp.get("/graph")
def graph_view():
    all_cards = get_all_cards()
    all_edges = get_all_edges()

    # Count edges per node for sizing
    degree: dict[str, int] = {}
    for e in all_edges:
        degree[e["source_id"]] = degree.get(e["source_id"], 0) + 1
        degree[e["target_id"]] = degree.get(e["target_id"], 0) + 1

    # Tag sets per card for edge weight
    tag_sets: dict[str, set[str]] = {
        c["id"]: {t.strip() for t in c["tags"].split(",") if t.strip()}
        for c in all_cards
    }

    nodes = [
        {
            "id":     c["id"],
            "label":  c["name"],
            "title":  c["topic"],
            "color":  _topic_colour(c["topic"]),
            "url":    url_for("main.card_detail", card_id=c["id"]),
            "degree": degree.get(c["id"], 0),
        }
        for c in all_cards
    ]

    edges = [
        {
            "from":        e["source_id"],
            "to":          e["target_id"],
            "label":       e["label"],
            "description": e["description"],
            "arrows":      "to",
            "shared":      len(tag_sets.get(e["source_id"], set()) & tag_sets.get(e["target_id"], set())),
        }
        for e in all_edges
    ]

    legend = [
        {"topic": t, "colour": c}
        for t, c in TOPIC_COLOURS.items()
        if any(n["title"] == t for n in nodes)
    ]

    return render_template(
        "graph.html",
        nodes_json=json.dumps(nodes),
        edges_json=json.dumps(edges),
        legend=legend,
    )
