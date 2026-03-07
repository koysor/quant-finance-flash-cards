---
name: quant-card-generator
description: Generate a new quantitative finance flash card, including its content, graph edges, and learning resources. Use when a new concept needs to be added to the project.
---

# Quant Card Generator

This skill automates the creation of a new flash card, ensuring it follows all project conventions and is properly integrated into the knowledge graph and resources.

## Workflow

### Step 1: Research & Topic Selection
- Check `cards/**/*.md` to ensure the concept doesn't already exist.
- Read `app/routes.py` to confirm the `TOPIC_COLOURS` keys.
- Choose the most appropriate topic for the new concept.

### Step 2: Write the Card
Create the card at `cards/<topic-slug>/<concept-slug>.md` using the standard format:
- **British English** (e.g., *normalised*, *behaviour*, *colour*).
- **A Level standard** mathematics (rigorous but accessible).
- **Sections**: `# Title`, `**Topic:**`, `**Tags:**`, `**Author:**`, `---`, `## Definition`, `## Key Formula`, `## Example`, `## Remember`.
- **The "Remember" Test**: Ensure the `## Remember` section explicitly connects the maths to a quantitative finance application.

### Step 3: Map Graph Edges
- Read `edges.json`.
- Identify 2-4 related cards.
- Add new directed edges with high-quality labels and descriptions.
- **Label Examples**: `extends`, `prices`, `requires`, `approximates`.
- **Maintain sorting**: Sort `edges.json` by `source` then `target`.

### Step 4: Add Learning Resources
- Read `resources.json`.
- Add 2 high-quality websites and 2 YouTube videos for the new card.
- **Trusted Sources**: Khan Academy, Investopedia, 3Blue1Brown, Paul's Online Math Notes.
- **Maintain sorting**: Sort `resources.json` by card ID.

### Step 5: Refresh the Cache
- Delete the disposable `graph.db`.
- Restart the Flask server to trigger a reload:
  ```bash
  pkill -f "python run.py" 2>/dev/null; rm -f graph.db; uv run python run.py &
  ```
- Verify the new card's page is live (e.g., using `curl -I http://127.0.0.1:5000/card/<card_id>`).

### Step 6: Summary & Next Steps
- Report the created card path and the new edges.
- Suggest 3-5 related concepts for future cards.

## Integration
This skill works best when combined with:
- **`quant-card-validator`**: To double-check the final Markdown.
- **`quant-katex-specialist`**: To refine complex formulas.
- **`quant-resource-manager`**: To update the final project statistics.
