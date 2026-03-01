"""SQLite schema and query functions for the flash card graph store."""
import json
import sqlite3
from pathlib import Path

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
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    with get_db() as conn:
        conn.executescript(DDL)
        # Migrate existing databases that pre-date the description column
        try:
            conn.execute("ALTER TABLE edges ADD COLUMN description TEXT NOT NULL DEFAULT ''")
        except sqlite3.OperationalError:
            pass  # column already exists
        # Migrate existing databases that pre-date created_date/author columns
        for col in ("created_date TEXT NOT NULL DEFAULT ''", "author TEXT NOT NULL DEFAULT ''"):
            try:
                conn.execute(f"ALTER TABLE cards ADD COLUMN {col}")
            except sqlite3.OperationalError:
                pass  # column already exists


# ---------------------------------------------------------------------------
# Card queries
# ---------------------------------------------------------------------------

def upsert_card(card: dict) -> None:
    sql = """
    INSERT INTO cards (id, name, topic, tags, html_content, created_date, author, file_mtime)
    VALUES (:id, :name, :topic, :tags, :html_content, :created_date, :author, :file_mtime)
    ON CONFLICT(id) DO UPDATE SET
        name         = excluded.name,
        topic        = excluded.topic,
        tags         = excluded.tags,
        html_content = excluded.html_content,
        created_date = excluded.created_date,
        author       = excluded.author,
        file_mtime   = excluded.file_mtime
    """
    with get_db() as conn:
        conn.execute(sql, card)


def get_stored_mtime(card_id: str) -> float | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT file_mtime FROM cards WHERE id = ?", (card_id,)
        ).fetchone()
    return row["file_mtime"] if row else None


def get_all_card_ids() -> set[str]:
    with get_db() as conn:
        return {r[0] for r in conn.execute("SELECT id FROM cards").fetchall()}


def delete_card(card_id: str) -> None:
    with get_db() as conn:
        conn.execute("DELETE FROM cards WHERE id = ?", (card_id,))


def get_all_cards() -> list[sqlite3.Row]:
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags FROM cards ORDER BY topic, name"
        ).fetchall()


def get_all_cards_with_content() -> list[sqlite3.Row]:
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags, html_content FROM cards ORDER BY topic, name"
        ).fetchall()


def get_card(card_id: str) -> sqlite3.Row | None:
    with get_db() as conn:
        return conn.execute(
            "SELECT * FROM cards WHERE id = ?", (card_id,)
        ).fetchone()


def get_topic_cards(topic: str) -> list[sqlite3.Row]:
    """Return all cards in a topic, ordered by name."""
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name FROM cards WHERE topic = ? ORDER BY name", (topic,)
        ).fetchall()


def get_all_cards_by_date() -> list[sqlite3.Row]:
    """Return all cards ordered by created_date descending, then name ascending."""
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags, created_date, author"
            " FROM cards ORDER BY created_date DESC, name ASC"
        ).fetchall()


def get_cards_by_date_range(
    start_date: str | None = None,
    end_date: str | None = None,
    order: str = "ASC"
) -> list[sqlite3.Row]:
    """Return cards within a date range (inclusive), ordered by date."""
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


def get_random_card() -> sqlite3.Row | None:
    with get_db() as conn:
        return conn.execute(
            "SELECT id FROM cards ORDER BY RANDOM() LIMIT 1"
        ).fetchone()


def get_cards_by_tag(tag: str) -> list[sqlite3.Row]:
    with get_db() as conn:
        return conn.execute(
            "SELECT id, name, topic, tags FROM cards WHERE ',' || tags || ',' LIKE ? ORDER BY topic, name",
            (f"%,{tag.strip()},%",)
        ).fetchall()


# ---------------------------------------------------------------------------
# Edge queries
# ---------------------------------------------------------------------------

def get_outgoing(card_id: str) -> list[sqlite3.Row]:
    with get_db() as conn:
        return conn.execute(
            """SELECT e.id, e.target_id, e.label, e.description,
                      c.name AS target_name, c.topic AS target_topic
               FROM edges e JOIN cards c ON c.id = e.target_id
               WHERE e.source_id = ?""",
            (card_id,)
        ).fetchall()


def get_incoming(card_id: str) -> list[sqlite3.Row]:
    with get_db() as conn:
        return conn.execute(
            """SELECT e.id, e.source_id, e.label, e.description,
                      c.name AS source_name, c.topic AS source_topic
               FROM edges e JOIN cards c ON c.id = e.source_id
               WHERE e.target_id = ?""",
            (card_id,)
        ).fetchall()


def delete_edge(edge_id: int) -> None:
    with get_db() as conn:
        conn.execute("DELETE FROM edges WHERE id = ?", (edge_id,))


def load_edges_from_file() -> None:
    """Replace the edges table with the contents of edges.json (source of truth)."""
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
    """Write the current edges table to edges.json (call after any mutation)."""
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
    with get_db() as conn:
        return conn.execute(
            "SELECT source_id, target_id, label, description FROM edges"
        ).fetchall()


def get_site_stats() -> dict:
    with get_db() as conn:
        card_count  = conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
        topic_count = conn.execute("SELECT COUNT(DISTINCT topic) FROM cards").fetchone()[0]
        edge_count  = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    return {"card_count": card_count, "topic_count": topic_count, "edge_count": edge_count}
