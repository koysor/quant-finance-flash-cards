"""
Card loader: scan ``cards/**/*.md``, parse metadata and content, upsert to SQLite.

Card format
-----------
Each ``.md`` file must have this exact structure (the loader uses regex, not a
full Markdown parser, so the field names and bold-asterisk syntax are required)::

    # Concept Name

    **Topic:** <must match a TOPIC_COLOURS key exactly>
    **Tags:** tag1, tag2, tag3
    **Author:** <model name or "Unknown">

    ---

    ## Definition
    ...

Card ID
-------
Derived from the file path by stripping the ``cards/`` prefix and ``.md`` suffix::

    cards/derivatives/black-scholes-equation.md  →  derivatives/black-scholes-equation

Change detection
----------------
Each card's ``file_mtime`` is stored in the database.  On startup, files whose
mtime matches the stored value are skipped; only changed or new files are
re-parsed.  Deleted files are detected by comparing the live file set against
all IDs in the database and removing any that are no longer present.
"""
import datetime
import json
import re
from pathlib import Path
from typing import Any

from flask import Flask
from markdown_it import MarkdownIt

from app.db import delete_card, get_all_card_ids, get_stored_mtime, upsert_card

CARDS_DIR = Path(__file__).parent.parent / "cards"

# Regex patterns for extracting required metadata fields from raw Markdown text.
TITLE_RE  = re.compile(r'^#\s+(.+)$',              re.MULTILINE)
TOPIC_RE  = re.compile(r'^\*\*Topic:\*\*\s*(.+)$', re.MULTILINE)
TAGS_RE   = re.compile(r'^\*\*Tags:\*\*\s*(.+)$',  re.MULTILINE)
AUTHOR_RE = re.compile(r'^\*\*Author:\*\*\s*(.+)$', re.MULTILINE)

# Strips all metadata lines from the raw text before passing it to the Markdown renderer
# so that field labels like "**Topic:** Calculus" do not appear in the rendered HTML.
_METADATA_RE = re.compile(r'^\*\*(?:Topic|Tags|Created|Author):\*\*\s*.+$', re.MULTILINE)

# Matches both display math ($$...$$) and inline math ($...$), non-greedy.
# Used to locate LaTeX regions for notation/key-term extraction and for math protection.
_MATH_RE = re.compile(r'(\$\$[\s\S]*?\$\$|\$(?!\s)[^$\n]+?\$)')

# Shared Markdown-it instance with table support enabled.
_md = MarkdownIt().enable("table")

# Matches simple LaTeX command names, e.g. \sigma, \mathbb (without argument).
_LATEX_CMD_RE = re.compile(r'\\([a-zA-Z]+)')

# Matches compound LaTeX constructs whose argument matters for lookup, e.g.
# \mathbb{E}, \mathcal{F}, \text{Var}, \operatorname{Cov}.
_LATEX_CONSTRUCT_RE = re.compile(r'\\(mathbb|mathcal|text|operatorname)\{([^}]+)\}')

# Sentinel used to temporarily replace underscores inside math blocks so that
# markdown-it does not interpret them as emphasis markers.
_MATH_UNDERSCORE_PLACEHOLDER = "⟦USCORE⟧"


def extract_key_terms(raw_text: str, key_terms_dict: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Find plain-text variable names that appear inside LaTeX math blocks.

    Scans only the math regions of *raw_text* (not prose) to avoid false
    positives.  Each variable name in *key_terms_dict* is matched as a whole
    token: it must not be preceded by a backslash or a letter (which would
    indicate it is part of a LaTeX command or a longer identifier) and must
    not be followed by a letter.

    Example matches in ``dS = \\mu S\\,dt + \\sigma S\\,dW``:
    - ``dS`` matches (preceded by nothing, followed by space)
    - ``S``  matches (preceded by space after ``\\mu``, followed by ``\\,``)
    - ``dW`` matches; standalone ``W`` does *not* (preceded by ``d``, a letter)

    Parameters
    ----------
    raw_text
        The full raw Markdown source of a card, including LaTeX.
    key_terms_dict
        Mapping of variable name → ``{symbol, meaning}`` from ``key-terms.json``.

    Returns
    -------
    list[dict]
        Matched entries, each augmented with a ``"key"`` field, sorted by key name.
    """
    math_source = " ".join(m.group(0) for m in _MATH_RE.finditer(raw_text))
    if not math_source:
        return []

    found: set[str] = set()
    for term in key_terms_dict:
        pattern = r"(?<![\\a-zA-Z])" + re.escape(term) + r"(?![a-zA-Z])"
        if re.search(pattern, math_source):
            found.add(term)

    return sorted(
        [{**key_terms_dict[k], "key": k} for k in found],
        key=lambda e: e["key"],
    )


def extract_notation(raw_text: str, notation_dict: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Find LaTeX commands from *notation_dict* that appear anywhere in *raw_text*.

    Two passes are made:
    1. Compound constructs (e.g. ``\\mathbb{E}``, ``\\text{Var}``) are matched
       first because their argument is part of the key.
    2. Simple commands (e.g. ``\\sigma``, ``\\Phi``) are matched next.

    Parameters
    ----------
    raw_text
        The full raw Markdown source of a card.
    notation_dict
        Mapping of LaTeX key → ``{symbol, meaning}`` from ``notation.json``.

    Returns
    -------
    list[dict]
        Matched entries, each augmented with a ``"key"`` field, sorted by meaning.
    """
    found: set[str] = set()

    for m in _LATEX_CONSTRUCT_RE.finditer(raw_text):
        key = f"\\{m.group(1)}{{{m.group(2)}}}"
        if key in notation_dict:
            found.add(key)

    for m in _LATEX_CMD_RE.finditer(raw_text):
        key = f"\\{m.group(1)}"
        if key in notation_dict:
            found.add(key)

    return sorted(
        [{**notation_dict[k], "key": k} for k in found],
        key=lambda e: e["meaning"],
    )


def _protect_math(text: str) -> str:
    """
    Escape LaTeX math blocks so that markdown-it does not corrupt their content.

    markdown-it applies two transformations that break LaTeX:
    1. It strips some backslash sequences (e.g. ``\\!`` → ``!``).
    2. It treats underscores as emphasis markers, turning ``x_i`` into
       ``x<em>i</em>``.

    This function pre-processes math blocks by:
    - Doubling every backslash so that markdown-it's escaping leaves one intact.
    - Replacing ``_`` with a Unicode placeholder that markdown-it ignores.

    ``_restore_math`` must be called on the rendered HTML to undo both changes.
    """
    def _escape(m: re.Match) -> str:
        s = m.group(0).replace("\\", "\\\\")
        s = s.replace("_", _MATH_UNDERSCORE_PLACEHOLDER)
        return s
    return _MATH_RE.sub(_escape, text)


def _restore_math(html: str) -> str:
    """
    Restore underscore placeholders in rendered HTML after markdown-it processing.

    Counterpart to ``_protect_math``; called on the HTML string returned by
    ``markdown_it.render()``.
    """
    return html.replace(_MATH_UNDERSCORE_PLACEHOLDER, "_")


def _parse_card(
    path: Path,
    notation_dict: dict[str, Any] | None = None,
    key_terms_dict: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Parse a single card ``.md`` file and return a database-ready dict.

    Raises ``ValueError`` loudly if any required metadata field is missing,
    so malformed cards are caught immediately at startup rather than silently
    producing incomplete records.

    Parameters
    ----------
    path
        Absolute path to the ``.md`` file.
    notation_dict
        Optional mapping from ``notation.json``; if provided, LaTeX commands
        found in the card are stored in the ``notation`` field.
    key_terms_dict
        Optional mapping from ``key-terms.json``; if provided, variable names
        found in the card's math blocks are stored in the ``key_terms`` field.

    Returns
    -------
    dict
        All columns needed for ``upsert_card()``.
    """
    text = path.read_text(encoding="utf-8")

    def _require(pattern: re.Pattern[str], field: str) -> str:
        """Extract the first capture group or raise ValueError with a helpful message."""
        m = pattern.search(text)
        if not m:
            raise ValueError(f"Missing '{field}' in {path}")
        return m.group(1).strip()

    card_id = path.relative_to(CARDS_DIR.parent / "cards").with_suffix("").as_posix()
    name    = _require(TITLE_RE, "title (#)")
    topic   = _require(TOPIC_RE, "**Topic:**")
    tags    = _require(TAGS_RE,  "**Tags:**")

    # Normalise tags: strip whitespace around each comma-separated value.
    tags = ",".join(t.strip() for t in tags.split(","))

    # Derive the creation date from the file's modification time so that the
    # /recent page reflects actual changes rather than an optional metadata field.
    created_date = datetime.datetime.fromtimestamp(
        path.stat().st_mtime
    ).isoformat(sep=" ", timespec="seconds")

    m_author = AUTHOR_RE.search(text)
    author = m_author.group(1).strip() if m_author else "Unknown"

    # Strip metadata lines before rendering so they do not appear in the HTML.
    rendered_text = _METADATA_RE.sub("", text, count=4).strip()
    html_content  = _restore_math(_md.render(_protect_math(rendered_text)))

    notation  = extract_notation(text, notation_dict)   if notation_dict   else []
    key_terms = extract_key_terms(text, key_terms_dict) if key_terms_dict  else []

    return {
        "id":           card_id,
        "name":         name,
        "topic":        topic,
        "tags":         tags,
        "created_date": created_date,
        "author":       author,
        "html_content": html_content,
        "notation":     json.dumps(notation),
        "key_terms":    json.dumps(key_terms),
        "file_mtime":   path.stat().st_mtime,
    }


def load_all_cards(
    app: Flask | None = None,
    notation_dict: dict[str, Any] | None = None,
    key_terms_dict: dict[str, Any] | None = None,
) -> int:
    """
    Synchronise the database with the ``cards/**/*.md`` files on disk.

    For each file:
    - If its ``file_mtime`` matches the stored value, it is skipped (no change).
    - If it is new or modified, it is parsed and upserted.

    After processing all files, any card whose ``.md`` file no longer exists is
    deleted from the database.

    Parameters
    ----------
    app
        Flask application instance for logging; if ``None``, prints to stdout.
    notation_dict
        LaTeX symbol definitions from ``notation.json``, passed to the parser.
    key_terms_dict
        Variable name definitions from ``key-terms.json``, passed to the parser.

    Returns
    -------
    int
        Total number of card files found on disk (not just those reloaded).
    """
    paths  = sorted(CARDS_DIR.rglob("*.md"))
    loaded = 0

    for path in paths:
        card_id       = path.relative_to(CARDS_DIR.parent / "cards").with_suffix("").as_posix()
        current_mtime = path.stat().st_mtime
        stored_mtime  = get_stored_mtime(card_id)

        if stored_mtime is not None and abs(current_mtime - stored_mtime) < 0.001:
            continue  # file unchanged — skip expensive re-parse

        card = _parse_card(path, notation_dict, key_terms_dict)  # raises ValueError on bad card
        upsert_card(card)
        loaded += 1

    # Remove database rows for cards whose source files have been deleted.
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
