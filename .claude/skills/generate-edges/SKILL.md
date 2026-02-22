---
name: generate-edges
description: Generate concept relationship edges for a card that has few or no connections
allowed-tools: Read, Edit, Glob
---

Generate edges for: $ARGUMENTS

If no argument is given, find all cards with zero or one edges and generate edges for each.

## Step 1 — Identify the target card(s)

If a card path or ID is given (e.g. `cards/risk/value-at-risk.md` or `risk/value-at-risk`), use that card. Otherwise, read `edges.json` and glob `cards/**/*.md` to find all cards that appear as neither source nor target in any edge (orphaned), or appear in only one edge. Process each of these.

## Step 2 — Read context

For each target card, read its full `.md` file to understand the concept, topic, tags, and formulae. Then scan the other cards (read their `# Title`, `**Topic:**`, and `**Tags:**` lines) to find 2-4 cards that are conceptually related.

Also read `edges.json` to understand existing edges and avoid duplicates.

## Step 3 — Generate edges

For each related card, create a directed edge. Pick whichever direction makes conceptual sense. Each edge needs:

- **`source`** / **`target`** — card IDs (e.g. `derivatives/black-scholes-equation`)
- **`label`** — short relationship tag (2-3 words), e.g. *derived via*, *used in*, *parameterised by*, *extends*, *constrains*, *feeds into*, *motivates*, *generalises*
- **`description`** — one plain-English sentence explaining *why* these concepts are linked in quantitative finance

Quality bar for descriptions (match the tone and specificity of existing edges in `edges.json`):
- Good: "Parametric VaR assumes returns are normally distributed, so the 1% loss quantile is simply the mean minus a fixed multiple of the standard deviation."
- Bad: "These concepts are related." / "Used in finance." / "See also."

Do NOT create an edge if:
- The (source, target) pair already exists in `edges.json`
- The relationship is trivial or forced
- You cannot write a specific, informative description

## Step 4 — Write edges

Append the new edges to `edges.json`, keeping the array sorted by `source` then `target`. Preserve the existing formatting (2-space indent, trailing newline).

## Step 5 — Summary

Report a table of new edges: source → target, label, description. If processing multiple cards, group by card.
