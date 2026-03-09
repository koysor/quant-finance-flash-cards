"""
SQLite persistence layer for the flash card graph store.

Schema
------
cards
    One row per Markdown file.  ``id`` is the card's URL path segment, e.g.
    ``stochastic-processes/brownian-motion``.  ``html_content`` is pre-rendered
    HTML stored at load time so page renders require no Markdown processing.
    ``notation`` and ``key_terms`` are JSON arrays of symbol/meaning objects
    extracted from the card's LaTeX at load time.  ``file_mtime`` is used to
    skip re-parsing cards whose source files have not changed since the last run.

edges
    Directed relationships between cards, loaded from ``edges.json``.
    ``source_id`` → ``target_id`` with a short ``label`` and a plain-English
    ``description``.  The edges table is fully replaced on each startup from
    the committed ``edges.json`` file, which is the canonical source of truth.

Both tables are created idempotently; ``init_db`` also runs ``ALTER TABLE``
migrations for columns added after the initial schema was deployed.
"""
import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH    = Path(__file__).parent.parent / "graph.db"
EDGES_PATH = Path(__file__).parent.parent / "edges.json"

DDL = """
CREATE TABLE IF NOT EXISTS cards (
    id           TEXT PRIMARY KEY,
    name         TEXT NOT NULL,
    topic        TEXT NOT NULL,
    tags         TEXT NOT NULL,
    html_content TEXT NOT NULL,
        created_date TEXT NOT NULL DEFAULT '',
        author       TEXT NOT NULL DEFAULT '',
            file_mtime   REAL NOT NULL
        );
CREATE TABLE IF NOT EXISTS edges (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id   TEXT NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    target_id   TEXT NOT NULL REFERENCES cards(id) ON DELETE CASCADE,
    label       TEXT NOT NULL DEFAULT '',
    description TEXT NOT NULL DEFAULT '',
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_id);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_id);
"""


def get_db() -> sqlite3.Connection:
    """
    Open and return a new SQLite connection to ``graph.db``.

    ``row_factory`` is set to ``sqlite3.Row`` so columns can be accessed by name.
    Foreign key enforcement is enabled for every connection.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """
    Create the database schema and run any pending column migrations.

    Safe to call on every startup — all DDL statements use ``IF NOT EXISTS``.
    Migrations use ``ALTER TABLE ... ADD COLUMN`` wrapped in a try/except so
    they silently succeed if the column already exists.
    """
    with get_db() as conn:
        conn.executescript(DDL)
        # Edges table: add description column introduced after initial release.
        try:
            conn.execute("ALTER TABLE edges ADD COLUMN description TEXT NOT NULL DEFAULT ''")
        except sqlite3.OperationalError:
            pass  # column already exists

        # Cards table: add columns introduced after the initial schema.
        for col in (
            "created_date TEXT NOT NULL DEFAULT ''",
            "author TEXT NOT NULL DEFAULT ''",
            "notation TEXT NOT NULL DEFAULT '[]'",
            "key_terms TEXT NOT NULL DEFAULT '[]'",
        ):
            try:
                conn.execute(f"ALTER TABLE cards ADD COLUMN {col}")
            except sqlite3.OperationalError:
                pass  # column already exists


# ---------------------------------------------------------------------------
# Card queries
# ---------------------------------------------------------------------------

def upsert_card(card: dict[str, Any]) -> None:
    """
    Insert a card row or update it in place if the ID already exists.

    All fields are replaced on conflict so that editing a card's source file and
    restarting the server immediately reflects the change.

    Parameters
    ----------
    card
        Dict with keys matching the ``cards`` column names as returned by
        ``loader._parse_card()``.
    """
    sql = """
    INSERT INTO cards (id, name, topic, tags, html_content, created_date, author, notation, key_terms, file_mtime)
    VALUES (:id, :name, :topic, :tags, :html_content, :created_date, :author, :notation, :key_terms, :file_mtime)
    ON CONFLICT(id) DO UPDATE SET
        name         = excluded.name,
        topic        = excluded.topic,
        tags         = excluded.tags,
        html_content = excluded.html_content,
        created_date = excluded.created_date,
        author       = excluded.author,
        notation     = excluded.notation,
        key_terms    = excluded.key_terms,
        file_mtime   = excluded.file_mtime
    """
    with get_db() as conn:
        conn.execute(sql, card)


def get_stored_mtime(card_id: str) -> float | None:
    """
    Return the ``file_mtime`` stored for *card_id*, or ``None`` if not in the DB.

    Used by the loader to decide whether a card file needs to be re-parsed.
    """
    with get_db() as conn:
        row = conn.execute(
            "SELECT file_mtime FROM cards WHERE id = ?", (card_id,)
        ).fetchone()
    return row["file_mtime"] if row else None


def get_all_card_ids() -> set[str]:
    """Return the set of every card ID currently stored in the database."""
    with get_db() as conn:
        return {r[0] for r in conn.execute("SELECT id FROM cards").fetchall()}


def delete_card(card_id: str) -> None:
    """
    Permanently delete a card from the database.

    Called by the loader when a ``.md`` source file has been removed from disk
    so that stale entries do not linger in the cache.
    """
    with get_db() as conn:
        conn.execute("DELETE FROM cards WHERE id = ?", (card_id,))


def get_all_cards() -> list[sqlite3.Row]:
    """
    Return a lightweight summary of every card, ordered by topic then name.

    Columns: ``id``, ``name``, ``topic``, ``tags``.
    Used for the index page, search data, and the context processor.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags FROM cards ORDER BY topic, name"
        ).fetchall()


def get_all_cards_with_content() -> list[sqlite3.Row]:
    """
    Return every card including ``html_content``, ordered by topic then name.

    Used by the /formulas aggregation page, which needs to extract the
    Key Formula section from the pre-rendered HTML of every card.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags, html_content FROM cards ORDER BY topic, name"
        ).fetchall()


def get_card(card_id: str) -> sqlite3.Row | None:
    """
    Return all columns for a single card, or ``None`` if not found.

    Parameters
    ----------
    card_id
        Full card ID, e.g. ``stochastic-processes/brownian-motion``.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT * FROM cards WHERE id = ?", (card_id,)
        ).fetchone()


def get_topic_cards(topic: str) -> list[sqlite3.Row]:
    """
    Return all cards in *topic*, ordered alphabetically by name.

    Columns: ``id``, ``name``.  Used to build prev/next navigation on the
    card detail page.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name FROM cards WHERE topic = ? ORDER BY name", (topic,)
        ).fetchall()


def get_all_cards_by_date() -> list[sqlite3.Row]:
    """
    Return all cards ordered by ``created_date`` descending, then name ascending.

    Columns: ``id``, ``name``, ``topic``, ``tags``, ``created_date``, ``author``.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags, created_date, author"
            " FROM cards ORDER BY created_date DESC, name ASC"
        ).fetchall()


def get_cards_by_date_range(
    start_date: str | None = None,
    end_date: str | None = None,
    order: str = "ASC",
) -> list[sqlite3.Row]:
    """
    Return cards whose ``created_date`` falls within an optional date range.

    Parameters
    ----------
    start_date
        Inclusive lower bound as a string (``YYYY-MM-DD`` or ``YYYY-MM-DD HH:MM:SS``).
    end_date
        Inclusive upper bound in the same format.
    order
        ``"ASC"`` or ``"DESC"`` — applied to ``created_date``.

    Columns returned: ``id``, ``name``, ``topic``, ``tags``, ``created_date``, ``author``.
    """
    query = "SELECT id, name, topic, tags, created_date, author FROM cards WHERE 1=1"
    params = []

    if start_date:
        query += " AND created_date >= ?"
        params.append(start_date)
    if end_date:
        query += " AND created_date <= ?"
        params.append(end_date)

    query += f" ORDER BY created_date {order}, name ASC"

    with get_db() as conn:
        return conn.execute(query, params).fetchall()


def find_cards_by_slug(slug: str) -> list[sqlite3.Row]:
    """
    Return every card whose ID ends with ``/<slug>``.

    Used for cross-topic slug resolution when a requested URL is not found
    verbatim in the database.  The caller redirects (1 match) or renders a
    disambiguation page (2+ matches).

    Parameters
    ----------
    slug
        The final path segment of a card ID, e.g. ``sharpe-ratio``.

    Columns returned: ``id``, ``name``, ``topic``.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic FROM cards WHERE id LIKE ?", (f"%/{slug}",)
        ).fetchall()


def get_random_card() -> sqlite3.Row | None:
    """
    Return a single randomly selected card row, or ``None`` if the table is empty.

    Columns: ``id``.  The caller redirects to the full card URL.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id FROM cards ORDER BY RANDOM() LIMIT 1"
        ).fetchone()


def get_cards_by_tag(tag: str) -> list[sqlite3.Row]:
    """
    Return all cards that include *tag* in their comma-separated tags field.

    The query pads the tags column with commas on both sides so that a partial
    tag name (e.g. ``"risk"``) cannot accidentally match a longer tag
    (e.g. ``"systematic-risk"``).

    Columns: ``id``, ``name``, ``topic``, ``tags``.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags FROM cards"
            " WHERE ',' || tags || ',' LIKE ? ORDER BY topic, name",
            (f"%,{tag.strip()},%",),
        ).fetchall()


# ---------------------------------------------------------------------------
# Edge queries
# ---------------------------------------------------------------------------

def get_outgoing(card_id: str) -> list[sqlite3.Row]:
    """
    Return all edges where *card_id* is the source (i.e. "this card links to…").

    Joins to ``cards`` to include the target card's name and topic, which the
    template uses to colour the link dot correctly.

    Columns: ``id``, ``target_id``, ``label``, ``description``, ``target_name``,
    ``target_topic``.
    """
    with get_db() as conn:
        return conn.execute(
            """SELECT e.id, e.target_id, e.label, e.description,
                      c.name AS target_name, c.topic AS target_topic
               FROM edges e JOIN cards c ON c.id = e.target_id
               WHERE e.source_id = ?""",
            (card_id,),
        ).fetchall()


def get_incoming(card_id: str) -> list[sqlite3.Row]:
    """
    Return all edges where *card_id* is the target (i.e. "linked from…").

    Joins to ``cards`` to include the source card's name and topic.

    Columns: ``id``, ``source_id``, ``label``, ``description``, ``source_name``,
    ``source_topic``.
    """
    with get_db() as conn:
        return conn.execute(
            """SELECT e.id, e.source_id, e.label, e.description,
                      c.name AS source_name, c.topic AS source_topic
               FROM edges e JOIN cards c ON c.id = e.source_id
               WHERE e.target_id = ?""",
            (card_id,),
        ).fetchall()


def delete_edge(edge_id: int) -> None:
    """
    Delete a single edge by its integer primary key.

    Called by the ``remove_link`` route after a user clicks the × button in the
    sidebar.  The caller is responsible for persisting the change to
    ``edges.json`` via ``save_edges_to_file()``.
    """
    with get_db() as conn:
        conn.execute("DELETE FROM edges WHERE id = ?", (edge_id,))


def load_edges_from_file() -> None:
    """
    Replace the entire edges table with the contents of ``edges.json``.

    ``edges.json`` is the committed source of truth for relationships.  This
    function is called on every startup so that any manual edits to the file
    (the primary way of adding new edges) are reflected immediately.
    """
    if not EDGES_PATH.exists():
        return
    data = json.loads(EDGES_PATH.read_text(encoding="utf-8"))
    with get_db() as conn:
        conn.execute("DELETE FROM edges")
        conn.executemany(
            "INSERT INTO edges (source_id, target_id, label, description)"
            " VALUES (?, ?, ?, ?)",
            [
                (e["source"], e["target"], e.get("label", ""), e.get("description", ""))
                for e in data
            ],
        )


def save_edges_to_file() -> None:
    """
    Write the current edges table back to ``edges.json``.

    Called after any in-app edge mutation (currently only ``remove_link``) so
    that the committed file stays in sync with the database.  Rows are written
    in ``source_id``, ``target_id`` order to produce a stable diff.
    """
    with get_db() as conn:
        rows = conn.execute(
            "SELECT source_id, target_id, label, description"
            " FROM edges ORDER BY source_id, target_id"
        ).fetchall()
    data = [
        {
            "source":      r["source_id"],
            "target":      r["target_id"],
            "label":       r["label"],
            "description": r["description"],
        }
        for r in rows
    ]
    EDGES_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def get_all_edges() -> list[sqlite3.Row]:
    """
    Return every edge row.

    Columns: ``source_id``, ``target_id``, ``label``, ``description``.
    Used by the graph view to build the vis.js edge dataset.
    """
    with get_db() as conn:
        return conn.execute(
            "SELECT source_id, target_id, label, description FROM edges"
        ).fetchall()


def get_site_stats() -> dict[str, int]:
    """
    Return aggregate counts for display in the site header.

    Returns
    -------
    dict
        ``{"card_count": int, "topic_count": int, "edge_count": int}``
    """
    with get_db() as conn:
        card_count  = conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
        topic_count = conn.execute("SELECT COUNT(DISTINCT topic) FROM cards").fetchone()[0]
        edge_count  = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    return {"card_count": card_count, "topic_count": topic_count, "edge_count": edge_count}
