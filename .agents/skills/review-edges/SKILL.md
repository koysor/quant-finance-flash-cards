---
name: review-edges
description: Check edges.json for broken references, missing descriptions, and quality
allowed-tools: Read, Glob
---

Review `edges.json` for issues:

1. **Broken references** — read all card files via `cards/**/*.md` glob and check that every `source` and `target` in `edges.json` matches a real card ID (file path minus `cards/` prefix and `.md` suffix)
2. **Missing descriptions** — flag any edge with an empty or missing `description` field (every edge should have a plain-English sentence explaining the relationship)
3. **Missing labels** — flag any edge with an empty `label` field
4. **Duplicate edges** — flag any (source, target) pair that appears more than once
5. **Orphaned cards** — list any cards that have zero edges (neither source nor target in any edge) as candidates for new connections
6. **Description quality** — flag descriptions that are too vague (e.g. just "related to") or that don't explain *why* the concepts are linked

Report results as a summary with counts, then list specific issues.
