#!/usr/bin/env python3
"""Update the stats line in README.md to reflect current card/edge counts."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CARDS_DIR = ROOT / "cards"
EDGES_FILE = ROOT / "edges.json"

STATS_RE = re.compile(r"^\d+ cards · \d+ topics · \d+ concept connections$", re.MULTILINE)


def main() -> None:
    cards = list(CARDS_DIR.rglob("*.md"))
    topics = {p.parent.name for p in cards}
    edges = json.loads(EDGES_FILE.read_text(encoding="utf-8")) if EDGES_FILE.exists() else []

    new_line = f"{len(cards)} cards · {len(topics)} topics · {len(edges)} concept connections"

    text = README.read_text(encoding="utf-8")
    if not STATS_RE.search(text):
        print("WARNING: stats line not found in README.md — skipping")
        return

    updated = STATS_RE.sub(new_line, text)
    if updated == text:
        print(f"README stats already up to date: {new_line}")
        return

    README.write_text(updated, encoding="utf-8")
    print(f"README stats updated: {new_line}")


if __name__ == "__main__":
    main()
