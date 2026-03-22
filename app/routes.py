"""
Flask Blueprint containing every route handler for the application.

URL map
-------
GET  /                          Card grid; supports ``?tag=`` and ``?topic=`` filters.
GET  /tag/<tag>                 Dedicated page showing all cards with a given tag.
GET  /card/<path:card_id>       Full card detail page.
POST /card/<path:card_id>/remove-link  Delete an outgoing edge (CSRF-protected).
GET  /graph                     Interactive vis.js graph of all cards and edges.
GET  /formulas                  Aggregated Key Formula sections from every card.
GET  /recent                    Reverse-chronological card list (accepts ?start= / ?end=).
GET  /random                    Redirect to a randomly selected card.

Slug-based redirect / disambiguation
-------------------------------------
If a card URL is not found verbatim (e.g. because a card was moved to a new topic
directory), the route extracts the slug (final path segment) and searches for it
across all topics.  One match → 301 permanent redirect.  Multiple matches → 300
response with a disambiguation page so the user can pick the correct card.

Topic colours
-------------
``TOPIC_COLOURS`` is the single source of truth mapping topic names to hex colour
strings.  Adding a new topic requires adding an entry here; the colour cascades
automatically to card tiles, graph nodes, topic badges, and sidebar dots through
the CSS custom property ``--tc`` set inline on elements.
"""
import json
import re

from flask import Blueprint, Response, abort, current_app, jsonify, redirect, render_template, request, session, url_for
from flask.typing import ResponseReturnValue

from app.db import (
    delete_edge,
    find_cards_by_slug,
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

# Topic name → hex colour.  Must be kept in sync with the card ``**Topic:**`` fields.
# The colour is injected into every template via the context processor in __init__.py.
TOPIC_COLOURS: dict[str, str] = {
    "Banking Regulation":              "#a855f7",   # purple
    "Calculus":                        "#f59e0b",   # amber
    "Computational Finance":           "#84cc16",   # lime
    "Derivatives":                     "#3b82f6",   # blue
    "Financial Mathematics":           "#10b981",   # emerald
    "Fixed Income":                    "#0d9488",   # teal-dark
    "Linear Algebra":                  "#8b5cf6",   # violet
    "Mathematical Notation":           "#f97316",   # orange
    "Portfolio Theory & Asset Pricing":"#14b8a6",   # teal
    "Probability":                     "#f43f5e",   # rose
    "Risk":                            "#ef4444",   # red
    "Short Selling":                   "#ec4899",   # pink
    "Statistics":                      "#06b6d4",   # cyan
    "Stochastic Processes":            "#6366f1",   # indigo
    "Volatility":                      "#d946ef",   # fuchsia
}
_DEFAULT_COLOUR = "#4f9ef8"


def _topic_colour(topic: str) -> str:
    """Return the hex colour for *topic*, falling back to a neutral blue if unknown."""
    return TOPIC_COLOURS.get(topic, _DEFAULT_COLOUR)


def _card_excerpt(html_content: str) -> str:
    """
    Extract a plain-text excerpt from a card's Definition section.

    Finds the first paragraph after the ``## Definition`` heading in the
    pre-rendered HTML, strips all HTML tags, collapses whitespace, and
    truncates to 157 characters.  Used for ``<meta name="description">`` and
    Open Graph tags.

    Returns a generic fallback string if no Definition section is found.
    """
    m = re.search(
        r'<h2[^>]*>\s*Definition\s*</h2>\s*<p>(.*?)</p>',
        html_content, re.IGNORECASE | re.DOTALL,
    )
    if not m:
        return 'Bite-sized revision flash card for Quantitative Finance.'
    text = re.sub(r'<[^>]+>', '', m.group(1))
    text = ' '.join(text.split())
    return text[:157] + '…' if len(text) > 157 else text


# Regex to extract the Key Formula section from pre-rendered card HTML.
# Used by the /formulas aggregation page to pull only that section from each card.
_FORMULA_RE = re.compile(
    r'(<h2[^>]*>\s*Key\s+Formul(?:a|ae)\s*</h2>)(.*?)(?=<h2|$)',
    re.IGNORECASE | re.DOTALL,
)

# LaTeX commands that are too visually obvious to need a tooltip on hover.
# Operators like \frac, \sqrt, arrows, and comparison signs are excluded so that
# the notation tooltip only fires on semantically meaningful symbols.
_SKIP_TOOLTIP = {
    "\\frac", "\\binom", "\\sqrt", "\\cdot", "\\times",
    "\\hat", "\\bar", "\\tilde", "\\mathbf",
    "\\log", "\\ln", "\\exp", "\\max", "\\min", "\\lim",
    "\\leq", "\\geq", "\\neq", "\\approx", "\\equiv",
    "\\in", "\\notin", "\\neg",
    "\\infty", "\\sum", "\\prod", "\\int",
    "\\Rightarrow", "\\Leftrightarrow", "\\rightarrow", "\\to",
}


@bp.get("/")
def index() -> str:
    """
    Render the main card grid.

    Supports two optional query parameters:
    - ``?tag=<tag>``     — filter to cards that include the given tag.
    - ``?topic=<topic>`` — further filter to a single topic within the tag results.

    Cards are grouped by topic for display.  The full tag list (from all cards,
    not just the filtered set) is passed for the filter strip.
    """
    tag          = request.args.get("tag",   "").strip()
    topic_filter = request.args.get("topic", "").strip()
    all_cards_list = get_all_cards()

    # Collect every unique tag across all cards for the horizontal filter strip.
    all_tags = sorted({
        t.strip()
        for c in all_cards_list
        for t in c["tags"].split(",")
        if t.strip()
    })

    cards = get_cards_by_tag(tag) if tag else all_cards_list

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
def tag_page(tag: str) -> str:
    """
    Render a dedicated page for all cards sharing a single *tag*.

    Returns 404 if no cards carry that tag.  Cards are grouped by topic.
    """
    cards = get_cards_by_tag(tag)
    if not cards:
        abort(404)

    grouped: dict[str, list] = {}
    for card in cards:
        grouped.setdefault(card["topic"], []).append(card)

    return render_template("tag.html", tag=tag, grouped=grouped, card_count=len(cards))


@bp.get("/barbie")
def barbie_theme() -> Response:
    """Secret Barbie theme — sets a ``theme`` cookie and redirects to the index."""
    resp = redirect(url_for("main.index"))
    resp.set_cookie("theme", "barbie", max_age=60 * 60 * 24 * 365)
    return resp


@bp.get("/random")
def random_card() -> Response:
    """Redirect to a randomly selected card, or 404 if the database is empty."""
    card = get_random_card()
    if card is None:
        abort(404)
    return redirect(url_for("main.card_detail", card_id=card["id"]))


@bp.get("/recent")
def recent() -> Response | str:
    """
    Render a reverse-chronological list of cards, grouped by date.

    Optional query parameters:
    - ``?start=YYYY-MM-DD`` — earliest date (inclusive).
    - ``?end=YYYY-MM-DD``   — latest date (inclusive).
    - ``?format=json``      — return JSON instead of HTML (also triggered by
      an ``Accept: application/json`` header).

    Date strings without a time component are padded to ``00:00:00`` / ``23:59:59``
    so that the database ``>=`` / ``<=`` comparisons work correctly against the
    stored ``YYYY-MM-DD HH:MM:SS`` format.
    """
    start    = request.args.get("start", "").strip() or None
    end      = request.args.get("end",   "").strip() or None
    is_json  = (
        request.args.get("format") == "json" or
        request.headers.get("Accept") == "application/json"
    )

    if start and len(start) == 10:
        start = f"{start} 00:00:00"
    if end and len(end) == 10:
        end = f"{end} 23:59:59"

    cards = get_cards_by_date_range(start_date=start, end_date=end, order="DESC")

    if is_json:
        return jsonify([dict(c) for c in cards])

    grouped: dict[str, list] = {}
    for card in cards:
        date = card["created_date"] or "Unknown"
        grouped.setdefault(date, []).append(card)
    return render_template("recent.html", grouped=grouped)


@bp.get("/card/<path:card_id>")
def card_detail(card_id: str) -> ResponseReturnValue:
    """
    Render the full detail page for a single card.

    If the card is not found by its exact ID, the slug (final path segment) is
    extracted and searched across all topics:
    - Exactly one match → 301 permanent redirect to the correct URL.
    - Multiple matches  → 300 response with a disambiguation page.
    - No matches        → 404.

    Template context includes:
    - ``card``              — the card row (all columns).
    - ``outgoing``          — edges from this card to others ("See also").
    - ``incoming``          — edges from other cards to this one ("Prerequisites").
    - ``prev_card``         — previous card alphabetically within the same topic.
    - ``next_card``         — next card alphabetically within the same topic.
    - ``resources``         — ``{websites, videos}`` dict from ``resources.json``.
    - ``notation``          — list of LaTeX symbol entries for the Notation sidebar box.
    - ``notation_map_json`` — JSON map of symbol → meaning for hover tooltips.
    - ``key_terms``         — list of variable name entries for the Key Terms sidebar box.
    """
    card = get_card(card_id)
    if card is None:
        # Card not found at the exact path — try resolving by slug alone.
        slug    = card_id.rsplit("/", 1)[-1]
        matches = find_cards_by_slug(slug)
        if len(matches) == 1:
            return redirect(url_for("main.card_detail", card_id=matches[0]["id"]), 301)
        if len(matches) > 1:
            return render_template("disambiguate.html", slug=slug, matches=matches), 300
        abort(404)

    outgoing = get_outgoing(card_id)
    incoming = get_incoming(card_id)

    # Determine the previous and next cards within the same topic for arrow-key navigation.
    siblings = get_topic_cards(card["topic"])
    idx      = next((i for i, c in enumerate(siblings) if c["id"] == card_id), -1)
    prev_card = dict(siblings[idx - 1]) if idx > 0             else None
    next_card = dict(siblings[idx + 1]) if idx < len(siblings) - 1 else None

    resources = current_app.config["RESOURCES"].get(card_id, {})
    notation  = json.loads(card["notation"])  if card["notation"]  else []
    key_terms = json.loads(card["key_terms"]) if card["key_terms"] else []

    # Build a filtered symbol→meaning map for the JS tooltip system.
    # Structural commands (fractions, arrows, etc.) are excluded because their
    # meaning is visually obvious and tooltips on them would be distracting.
    notation_map = {
        e["key"]: e["meaning"]
        for e in notation
        if "key" in e and e["key"] not in _SKIP_TOOLTIP
    }

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
        notation_map_json=json.dumps(notation_map),
        key_terms=key_terms,
    )


@bp.post("/card/<path:card_id>/remove-link")
def remove_link(card_id: str) -> Response:
    """
    Delete a single outgoing edge from a card.

    Protected by a session-based CSRF token that must match the hidden form field.
    After deletion the edge is persisted to ``edges.json`` via ``save_edges_to_file()``
    so the committed file stays in sync with the database.

    Returns 403 on CSRF failure, 404 if the card does not exist.
    Redirects back to the card detail page on success.
    """
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


@bp.get("/formulas")
def formulas() -> str:
    """
    Render a page aggregating the Key Formula section from every card.

    Iterates over all cards with content and uses ``_FORMULA_RE`` to extract
    the HTML between the ``## Key Formula`` heading and the next ``<h2>``.
    Cards without a Key Formula section are silently skipped.
    Results are grouped by topic.
    """
    cards   = get_all_cards_with_content()
    grouped: dict[str, list] = {}
    for card in cards:
        m = _FORMULA_RE.search(card["html_content"])
        if not m:
            continue
        formula_html = m.group(1) + m.group(2)
        grouped.setdefault(card["topic"], []).append({
            "name":         card["name"],
            "id":           card["id"],
            "formula_html": formula_html,
        })
    return render_template("formulas.html", grouped=grouped)


@bp.get("/graph")
def graph_view() -> str:
    """
    Render the interactive vis.js knowledge graph.

    Builds two JSON datasets passed to the template:
    - ``nodes_json`` — one entry per card with id, label, colour, URL, and degree
      (total edge count, used to scale node size).
    - ``edges_json`` — one entry per relationship with source, target, label,
      description, and ``shared`` (count of tags in common, used to weight edges).

    Also passes ``legend`` — the subset of TOPIC_COLOURS whose topics actually
    appear in the current node set, for the colour key displayed on the graph page.
    """
    all_cards = get_all_cards()
    all_edges = get_all_edges()

    # Count incoming + outgoing edges per card to size nodes proportionally.
    degree: dict[str, int] = {}
    for e in all_edges:
        degree[e["source_id"]] = degree.get(e["source_id"], 0) + 1
        degree[e["target_id"]] = degree.get(e["target_id"], 0) + 1

    # Pre-compute tag sets so shared-tag edge weights can be calculated in one pass.
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
            # Shared tag count is used by the graph JS to set edge width/opacity.
            "shared": len(
                tag_sets.get(e["source_id"], set()) & tag_sets.get(e["target_id"], set())
            ),
        }
        for e in all_edges
    ]

    # Only include topics that have at least one node in the current graph.
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
