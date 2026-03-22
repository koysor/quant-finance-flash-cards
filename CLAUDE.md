# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

Uses [uv](https://docs.astral.sh/uv/) for dependency management. Python 3.12.

```bash
uv sync               # create/update the virtual environment
uv add <pkg>          # add a runtime dependency
uv add --dev <pkg>    # add a dev dependency
uv run python run.py  # start the dev server at http://127.0.0.1:5000
```

## Testing

There are no automated tests. The application is pure CRUD with no business logic to protect. The only meaningful logic is the regex metadata parsing in `loader.py`; a malformed card raises `ValueError` at startup, so failures are immediate and visible.

Verify changes by starting the server and checking:
1. The card appears on the index page under the correct topic
2. The card detail page renders correctly, including maths
3. `/graph` shows the card as a node

## Architecture

Flask web application that reads Markdown flash cards from `cards/` and stores them in a SQLite graph database (`graph.db`, gitignored). Cards are nodes; user-defined relationships are directed edges.

**Sources of truth:**
- `cards/**/*.md` — card content (committed)
- `edges.json` — relationships between cards: label + plain-English description (committed)
- `resources.json` — per-card learning resources (websites, videos), keyed by card ID (committed)
- `graph.db` — derived cache of cards+edges; gitignored; fully regenerable by deleting and restarting

**Startup sequence** (`app/__init__.py` → `create_app()`):
1. `init_db()` — idempotent DDL (creates `cards` and `edges` tables if absent)
2. Load `notation.json` → `app.config["NOTATION"]` (LaTeX symbol definitions)
3. Load `key-terms.json` → `app.config["KEY_TERMS"]` (plain variable definitions, e.g. `dW`, `S`)
4. `load_all_cards(notation_dict, key_terms_dict)` — scans `cards/**/*.md`, skips unchanged files (mtime check), upserts changed ones, removes stale cards whose files no longer exist
5. `load_edges_from_file()` — clears the `edges` table and repopulates from `edges.json`
6. Load `resources.json` → `app.config["RESOURCES"]` (per-card website/video links)
7. Blueprint registered, context processor attached (CSRF token, topic colours, search data, stats)

**Edge mutations:** removing a link via the card detail sidebar writes to `graph.db` first, then calls `save_edges_to_file()` to keep `edges.json` in sync. Commit `edges.json` after changes. Adding edges is done by editing `edges.json` directly and restarting.

**`edges.json` format:** a JSON array of objects with `source`, `target` (card IDs), `label` (short relationship type like "foundation of"), and `description` (plain-English explanation of the relationship).

**`resources.json` format:** a JSON object keyed by card ID, each value containing `websites` and/or `videos` arrays of `{title, url}` objects. Loaded into `app.config["RESOURCES"]` at startup and displayed on card detail pages.

**Card ID scheme:** strip `cards/` prefix and `.md` suffix, keep the `/` separator.
`cards/derivatives/black-scholes-equation.md` → `derivatives/black-scholes-equation`
Flask routes use `<path:card_id>` to allow the `/` in URLs.

**Topic colour identity** is the single source of truth in `routes.py::TOPIC_COLOURS`. Adding a new topic requires adding an entry there; the colour cascades to card tiles, card content headings, graph nodes, and badges — all via the CSS custom property `--tc` set inline.

**Context processor** (`app/__init__.py`) injects into every template:
- `topic_colour(topic)` — returns hex colour from `TOPIC_COLOURS`
- `search_data_json` — JSON array of all cards for client-side search
- `site_stats` — `card_count`, `topic_count`, `edge_count`
- `csrf_token` — session-based token for POST form protection

**Frontend:** no build step. KaTeX (maths) and vis.js (graph) loaded from CDN. Theme (dark/light) and wide mode in `localStorage`, applied via `data-theme` / `data-wide` on `<html>` before paint. Visited cards tracked client-side in `localStorage`.

## Routes

| Method | URL | Handler |
|---|---|---|
| GET | `/` | Card grid, tag filter strip, `?tag=` / `?topic=` filtering |
| GET | `/tag/<tag>` | Dedicated tag page showing all cards with that tag |
| GET | `/card/<path:card_id>` | Card content + prerequisites + see-also + sidebar |
| POST | `/card/<path:card_id>/remove-link` | Delete edge (CSRF-protected), redirect back |
| GET | `/graph` | vis.js network — path finding, topic filtering, edge weights |
| GET | `/formulas` | All Key Formula sections aggregated by topic |
| GET | `/recent` | Reverse-chronological card list, grouped by date (unlisted) |
| GET | `/random` | Redirect to a random card (JS version prefers unvisited) |

## Card Authoring

Each card is a single `.md` file in `cards/<topic>/`. The loader uses regex (not a Markdown parser) to extract metadata, so the exact format is required:

```markdown
# Concept Name

**Topic:** <must match a key in TOPIC_COLOURS exactly>
**Tags:** tag1, tag2, tag3
**Author:** <model name or "Unknown">

---

## Definition

## Key Formula

## Example

## Remember
```

**Content rules:**
- British English throughout (e.g. "normalised", "behaviour", "recognise")
- `$$...$$` for display maths, `$...$` for inline — passed through to KaTeX by the browser
- The **Remember** section must connect the maths to a quantitative finance application
- One concept per card, no padding
- Do **not** add a `**Level:**` field — it is not a recognised metadata field

## URL Validation Hook

`scripts/validate_urls.py` checks every URL in `resources.json` using async HEAD requests (GET fallback on 405). It runs automatically:

- **Claude Code:** `PreToolUse` hook in `.claude/settings.json` fires on `git commit` when `resources.json` is staged
- **Git:** pre-commit hook in `.git/hooks/` (not committed — run `bash scripts/install_hooks.sh` after cloning)

Run manually: `uv run python scripts/validate_urls.py --force`

## Topic Directories

| Directory | Topic name | Scope |
|---|---|---|
| `cards/banking-regulation/` | `Banking Regulation` | FRTB, IRRBB, LCR, NSFR, Basel capital rules |
| `cards/calculus/` | `Calculus` | Differentiation, integration, Taylor series |
| `cards/derivatives/` | `Derivatives` | Options, futures, Greeks, pricing |
| `cards/financial-maths/` | `Financial Mathematics` | TVM, compounding, NPV, leverage, execution |
| `cards/fixed-income/` | `Fixed Income` | Bonds, yield curves, duration, DV01, credit spreads |
| `cards/linear-algebra/` | `Linear Algebra` | Matrices, vectors, eigenvalues |
| `cards/mathematical-notation/` | `Mathematical Notation` | Sigma, pi, set, and logical notation conventions |
| `cards/portfolio-theory/` | `Portfolio Theory & Asset Pricing` | CAPM, factor models, performance ratios |
| `cards/probability/` | `Probability` | Distributions, expectation, Bayes |
| `cards/risk/` | `Risk` | VaR, CVaR, Monte Carlo, stress testing |
| `cards/short-selling/` | `Short Selling` | Short mechanics, securities lending, regulation |
| `cards/statistics/` | `Statistics` | Descriptive stats, regression, hypothesis testing |
| `cards/stochastic-processes/` | `Stochastic Processes` | Brownian motion, GBM, Itô's lemma |
| `cards/volatility/` | `Volatility` | Implied/realised vol, VIX, vol surface, smile |
