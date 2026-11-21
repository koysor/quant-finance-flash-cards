# Contributing

## Using Claude Code Skills

If you are using Claude Code to contribute, the following skills automate card creation and maintenance:

### Creating content
- **`generate-card`**: `generate card: "[Concept Name]"` — Writes the card file, finds related cards, appends edges to `edges.json`, and adds learning resources to `resources.json`.
- **`generate-edges`**: `generate edges: "[card-id]"` — Finds and appends concept relationship edges for a card that has few or no connections.
- **`add-resources`**: `add resources: "[topic]"` — Populates `resources.json` entries (websites + videos) for cards that have none. Omit the argument to process all missing cards.

### Reviewing quality
- **`validate-card`**: `validate card: "[card-id]"` — Checks structure, metadata, British English spelling, and finance relevance for a single card.
- **`bulk-validate`**: `bulk validate: "[topic]"` — Runs validation checks across an entire topic directory (or all cards if no argument given) and produces a summary report.
- **`review-card`**: `review card: "[card-id]"` — Content-quality review: suggests improvements to Definition, Example, and Remember sections.
- **`review-edges`**: `/review-edges` — Audits `edges.json` for broken references, missing descriptions, and quality issues.
- **`find-duplicates`**: `/find-duplicates` — Scans the library for cards with significant concept overlap and recommends merges or clarifications.

### Maintenance
- **`update-docs`**: `/update-docs` — Recounts cards and edges, updates the README.md stats line and per-topic table, and syncs the skills list in this file.
- **`gap-analysis`**: `/gap-analysis` — Identifies orphaned cards, topic connectivity gaps, and concepts referenced across cards that lack their own card.
- **`validate-links`**: `/validate-links` — Validates all URLs in `resources.json` and offers to fix or remove broken links.

---

## Adding a flash card

Create a single `.md` file in `cards/<topic>/`. The filename becomes part of the card's permanent ID, so use a short lowercase hyphenated slug (e.g. `black-scholes-equation.md`).

### Required format

Every card needs the title, the metadata fields and all four sections, in this exact order:

```markdown
# Concept Name

**Topic:** Derivatives
**Tags:** tag1, tag2, tag3
**Created:** YYYY-MM-DD
**Author:** <Your Name or AI model>

---

## Definition

## Key Formula

## Example

## Remember
```

### Metadata rules

The loader requires `# Title`, `**Topic:**` and `**Tags:**`. `**Created:**` and `**Author:**` are optional to the loader, but include both on new cards. Do not add a `**Level:**` field; it is not a recognised field.

**`**Topic:**`** must exactly match one of the keys in `TOPIC_COLOURS` in `app/routes.py`:

| Value | Colour | Directory |
|---|---|---|
| `Banking Regulation` | purple | `cards/banking-regulation/` |
| `Calculus` | amber | `cards/calculus/` |
| `Computational Finance` | lime | `cards/computational-finance/` |
| `Derivatives` | blue | `cards/derivatives/` |
| `Financial Mathematics` | emerald | `cards/financial-maths/` |
| `Fixed Income` | teal-dark | `cards/fixed-income/` |
| `Linear Algebra` | violet | `cards/linear-algebra/` |
| `Machine Learning` | green | `cards/machine-learning/` |
| `Mathematical Notation` | orange | `cards/mathematical-notation/` |
| `Portfolio Theory & Asset Pricing` | teal | `cards/portfolio-theory/` |
| `Probability` | rose | `cards/probability/` |
| `Risk` | red | `cards/risk/` |
| `Short Selling` | pink | `cards/short-selling/` |
| `Statistics` | cyan | `cards/statistics/` |
| `Stochastic Processes` | indigo | `cards/stochastic-processes/` |
| `Volatility` | fuchsia | `cards/volatility/` |

A topic that is not in `TOPIC_COLOURS` (a typo, say) stops the app at startup with `ValueError: Unknown topic`. To add a genuinely new topic, see [Adding a new topic](#adding-a-new-topic).

**`**Tags:**`** is a comma-separated list of tags, e.g. `options, Greeks, delta, gamma`. Each tag gets a `/tag/<tag>` page and appears in the tag strip on the index page.

**`**Created:**`** is the date the card was written, as `YYYY-MM-DD`. It orders the `/recent` page. Without it the loader falls back to the file's modification time, which changes whenever the file is checked out or edited, so always set it on new cards.

### Section content rules

**Accessibility** — while the subject matter can be advanced, the explanation should remain accessible to a student of A Level mathematics age. Avoid unnecessary jargon and explain technical terms where possible.

**Definition** — one or two sentences. State precisely what the concept is.

**Key Formula** — the central equation(s), using LaTeX delimiters:
- Display maths: `$$...$$` on its own line
- Inline maths: `$...$`

These are passed through to KaTeX in the browser — do not use MathJax or image-based maths.

**Example** — a short worked numerical example. Prefer concrete numbers over abstract symbols.

**Remember** — the key insight. This section must explicitly connect the mathematics to a quantitative finance application. Do not leave it as a pure maths summary.

### Language

Use **British English** throughout: *normalised*, *behaviour*, *recognise*, *colour*, *modelled*, *practise* (verb).

### Tone and length

Cards are intentionally bite-sized — one concept per card, no padding. If you find yourself writing more than a screen's worth of content, split into two cards.

---

## Adding concept relationships

Edit `edges.json` in the project root and restart the server. Each entry is a JSON object with four fields:

```json
{
  "source": "probability/normal-distribution",
  "target": "risk/value-at-risk",
  "label": "used in",
  "description": "The normal distribution underpins the parametric VaR calculation."
}
```

- **`source`** / **`target`** — card IDs (file path minus `cards/` prefix and `.md` suffix)
- **`label`** — short relationship tag, e.g. *derived via*, *used in*, *parameterised by*
- **`description`** — plain-English sentence explaining why the cards are linked; shown in the "See Also" section on the card detail page

With `ALLOW_EDGE_EDIT=1` set, edges can also be removed at runtime from the card detail page sidebar, which writes the change back to `edges.json`. Commit `edges.json` afterwards. Entries whose card IDs do not exist are skipped with a warning at startup.

---

## Adding a new topic

1. Add an entry to `TOPIC_COLOURS` in `app/routes.py` first (cards with an unknown topic stop startup):
   ```python
   "New Topic": "#hexcolour",
   ```
2. Create the directory: `cards/<new-topic>/`
3. Add at least one card
4. Restart the server
5. Add the topic to the topic tables in `README.md`, `CLAUDE.md`, `GEMINI.md` and this file

The colour cascades automatically to card tiles, the graph, content headings, and badges. The topic also gets `/topic/<slug>` and `/quiz/<slug>` pages, which the static build picks up without further changes.

---

## Verifying your changes

Run `uv run pytest` for the automated tests, then start the server and check:

```bash
FLASK_DEBUG=1 uv run python run.py
```

(In PowerShell: `$env:FLASK_DEBUG=1; uv run python run.py`. `bash launch_app.sh` or `launch_app.bat` does the same.)

1. Your card appears on the index page under the correct topic
2. The card detail page renders correctly, including maths
3. `http://127.0.0.1:5000/graph` shows the card as a node

The live site is a static build. CI runs it on every pull request and fails on any broken link. To run it yourself (Linux or WSL only, because some tag names are not valid Windows file names):

```bash
uv run python scripts/build_static.py --prefix /flashcards --out dist
```
