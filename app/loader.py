"""Scan cards/**/*.md, parse metadata, and upsert to the database."""
import datetime
import re
from pathlib import Path

from markdown_it import MarkdownIt

from app.db import delete_card, get_all_card_ids, get_stored_mtime, upsert_card

CARDS_DIR = Path(__file__).parent.parent / "cards"

TITLE_RE = re.compile(r'^#\s+(.+)$', re.MULTILINE)
TOPIC_RE = re.compile(r'^\*\*Topic:\*\*\s*(.+)$', re.MULTILINE)
TAGS_RE     = re.compile(r'^\*\*Tags:\*\*\s*(.+)$', re.MULTILINE)
CREATED_RE  = re.compile(r'^\*\*Created:\*\*\s*(.+)$', re.MULTILINE)
AUTHOR_RE   = re.compile(r'^\*\*Author:\*\*\s*(.+)$', re.MULTILINE)

# Matches display math ($$...$$) and inline math ($...$), non-greedy
_MATH_RE = re.compile(r'(\$\$[\s\S]*?\$\$|\$(?!\s)[^$\n]+?\$)')

_md = MarkdownIt().enable("table")


def _protect_math(text: str) -> str:
    """Double backslashes inside LaTeX math blocks so markdown-it escaping
    does not strip them (e.g. \\! → ! or \\, → ,).  The extra backslash is
    consumed by the Markdown renderer, leaving the original LaTeX intact for
    KaTeX on the client side."""
    def _escape(m: re.Match) -> str:
        return m.group(0).replace("\\", "\\\\")
    return _MATH_RE.sub(_escape, text)


def _parse_card(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    def _require(pattern: re.Pattern, field: str) -> str:
        m = pattern.search(text)
        if not m:
            raise ValueError(f"Missing '{field}' in {path}")
        return m.group(1).strip()

    card_id = path.relative_to(CARDS_DIR.parent / "cards").with_suffix("").as_posix()
    name    = _require(TITLE_RE, "title (#)")
    topic   = _require(TOPIC_RE, "**Topic:**")
    tags    = _require(TAGS_RE,  "**Tags:**")

    # Normalise tags: strip whitespace around each tag
    tags = ",".join(t.strip() for t in tags.split(","))

    # Optional metadata — default gracefully
    m_created = CREATED_RE.search(text)
    created_date = m_created.group(1).strip() if m_created else datetime.date.today().isoformat()

    m_author = AUTHOR_RE.search(text)
    author = m_author.group(1).strip() if m_author else "Unknown"

    html_content = _md.render(_protect_math(text))

    return {
        "id":           card_id,
        "name":         name,
        "topic":        topic,
        "tags":         tags,
        "created_date": created_date,
        "author":       author,
        "html_content": html_content,
        "file_mtime":   path.stat().st_mtime,
    }


def load_all_cards(app=None) -> int:
    """Scan all card files and upsert changed ones. Returns count of cards loaded."""
    paths = sorted(CARDS_DIR.rglob("*.md"))
    loaded = 0

    for path in paths:
        card_id = path.relative_to(CARDS_DIR.parent / "cards").with_suffix("").as_posix()
        current_mtime = path.stat().st_mtime
        stored_mtime  = get_stored_mtime(card_id)

        if stored_mtime is not None and abs(current_mtime - stored_mtime) < 0.001:
            continue  # unchanged

        card = _parse_card(path)  # raises ValueError loudly on bad card
        upsert_card(card)
        loaded += 1

    # Remove cards whose files have been deleted
    live_ids = {
        p.relative_to(CARDS_DIR.parent / "cards").with_suffix("").as_posix()
        for p in paths
    }
    stale = get_all_card_ids() - live_ids
    for card_id in stale:
        delete_card(card_id)

    total = len(paths)
    msg = f"Cards: {total} total, {loaded} reloaded, {len(stale)} removed."
    if app:
        app.logger.info(msg)
    else:
        print(msg)

    return total
