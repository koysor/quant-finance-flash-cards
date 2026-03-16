---
name: update-docs
description: Recount cards and edges, then update README.md stats line and per-topic table
allowed-tools: Read, Edit, Bash, Glob
---

Update all documentation statistics to reflect the current state of the card library.

## Step 1 — Collect counts

Run the existing stats script to update the header line:

```bash
uv run python scripts/update_readme_stats.py
```

Then count cards per topic manually:

```bash
for dir in cards/*/; do
  topic=$(basename "$dir")
  count=$(find "$dir" -name "*.md" | wc -l | tr -d ' ')
  echo "$topic: $count"
done
```

Also count total edges:
```bash
python3 -c "import json; print(len(json.load(open('edges.json'))))"
```

## Step 2 — Update the per-topic table in README.md

Read README.md and update the Topics table so each row reflects the current card count. Only change the number — do not alter the Scope column text unless it is clearly wrong for the topic.

The table rows follow this pattern:
```
| Topic Name | <count> | Scope description |
```

Update every row whose count differs from the actual directory count.

## Step 3 — Update CONTRIBUTING.md skills list

Read CONTRIBUTING.md. If the "Using Claude Code Skills" section does not list all currently available skills (check `.claude/skills/*/SKILL.md` for the full list), add the missing ones. Do not remove or reword existing entries unless they are factually wrong.

## Step 4 — Report

Print a one-line summary:
```
Updated README.md: <N> cards · <T> topics · <E> edges
Per-topic changes: <list any rows that changed>
```
