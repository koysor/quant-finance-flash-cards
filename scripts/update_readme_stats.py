#!/usr/bin/env python3
"""Update the stats line and per-topic card counts in README.md."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CARDS_DIR = ROOT / "cards"
EDGES_FILE = ROOT / "edges.json"

TOPIC_RE = re.compile(r"^\*\*Topic:\*\*\s*(.+)$", re.MULTILINE)
ROW_RE = re.compile(r"^\| ([^|]+?) \| \d+ \| ", re.MULTILINE)

STATS_RE = re.compile(r"^\d+ cards · \d+ topics · \d+ concept connections$", re.MULTILINE)


def main() -> None:
    cards = list(CARDS_DIR.rglob("*.md"))
    topics = {p.parent.name for p in cards}
    edges = json.loads(EDGES_FILE.read_text(encoding="utf-8")) if EDGES_FILE.exists() else []

    new_line = f"{len(cards)} cards · {len(topics)} topics · {len(edges)} concept connections"

    counts: dict[str, int] = {}
    for p in cards:
        m = TOPIC_RE.search(p.read_text(encoding="utf-8"))
        if m:
            counts[m.group(1).strip()] = counts.get(m.group(1).strip(), 0) + 1

    text = README.read_text(encoding="utf-8")
    listed = set(ROW_RE.findall(text))
    for topic in sorted(set(counts) - listed):
        print(f"WARNING: topic '{topic}' has cards but no row in the README topic table")
    text = ROW_RE.sub(
        lambda m: f"| {m.group(1)} | {counts[m.group(1)]} | " if m.group(1) in counts else m.group(0),
        text,
    )
    if not STATS_RE.search(text):
        print("WARNING: stats line not found in README.md — skipping")
        return

    updated = STATS_RE.sub(new_line, text)
    if updated == README.read_text(encoding="utf-8"):
        print(f"README stats already up to date: {new_line}")
        return

    README.write_text(updated, encoding="utf-8")
    print(f"README stats updated: {new_line}")


if __name__ == "__main__":
    main()
