---
name: gap-analysis
description: Analyse the knowledge graph for orphaned cards, weak topic links, and missing concept cards
allowed-tools: Read, Glob, Grep, Bash
---

Analyse the flash card library and knowledge graph to identify gaps and suggest improvements.

## Step 1 — Load data

Read `edges.json` to build a set of all card IDs that appear as source or target. Glob `cards/**/*.md` to get the full card list and their topics.

## Step 2 — Find orphaned and underconnected cards

Classify each card:
- **Orphaned** — appears in neither source nor target in any edge
- **Weakly connected** — appears in exactly one edge (either as source or target)

Report these grouped by topic, with a count per topic.

## Step 3 — Find cross-topic connectivity gaps

For each pair of topics, count how many edges cross between them. Report topic pairs with zero cross-topic edges — these represent knowledge silos where the graph provides no navigation path between topics.

## Step 4 — Find referenced concepts without cards

Scan every `cards/**/*.md` file. Extract:
- Bold terms: `**term**`
- Capitalised noun phrases in the Definition and Remember sections that look like named concepts (e.g. "Black-Scholes", "Itô's Lemma", "Jensen's Inequality")

Cross-reference against the full card list. Flag any concept mentioned 3 or more times across different cards but lacking its own card. Deduplicate and rank by mention count.

## Step 5 — Report

Output three sections:

### Orphaned / Weakly Connected Cards
Table: card ID | topic | edge count

### Topic Connectivity Matrix
Table or list of topic pairs with zero cross-topic edges.

### Suggested New Cards
Ranked list of concepts referenced across cards but missing their own card, with mention count and the cards that reference them.

Keep the analysis concise — flag the top issues, not an exhaustive dump.
