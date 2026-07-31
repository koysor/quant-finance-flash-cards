# GEMINI.md

> This file contains Gemini-specific instructions. An equivalent file for Claude Code exists as `CLAUDE.md`. Both cover the same project but are tailored to their respective AI assistants.

This file provides context and instructions for the **Quantitative Finance Flash Cards** project.

## Project Overview

A Flask-based web application that manages revision flash cards for Quantitative Finance. The project is designed with a "source of truth in the filesystem" architecture, where card content and relationships are stored in Markdown and JSON files, while a SQLite database acts as a disposable, regenerable cache.

### Agent Skills
The project includes specialized Gemini skills to automate workflows:
- **`quant-card-generator`**: Creates new cards, edges, and resources (equivalent to `generate-card`).
- **`quant-card-validator`**: Validates card structure, metadata, British English, and finance relevance.
- **`quant-graph-architect`**: Manages concept dependencies and link descriptions in `edges.json`.
- **`quant-katex-specialist`**: Ensures consistent LaTeX formatting using `notation.json`.
- **`quant-resource-manager`**: Manages external links in `resources.json` and updates project statistics.

### Core Technologies
- **Backend:** Python 3.12, Flask 3, SQLite (standard library)
- **Frontend:** Jinja2 templates, Vanilla CSS (CSS custom properties), KaTeX (maths rendering), vis-network (graph visualisation)
- **Package Management:** [uv](https://docs.astral.sh/uv/)
- **Parsing:** `markdown-it-py` for content, regex for metadata.

### Architecture
- **Content:** `cards/**/*.md` (Card body and metadata)
- **Relationships:** `edges.json` (Directed edges between cards)
- **Resources:** `resources.json` (External links per card)
- **Notation:** `notation.json` (LaTeX symbol definitions)
- **Key Terms:** `key-terms.json` (Plain-text equation variable definitions, e.g. `dW`, `S`)
- **Cache:** `graph.db` (Gitignored SQLite database, rebuilt on startup)

### Startup Sequence
`app/__init__.py` → `create_app()` performs, in order:
1. `init_db()` — idempotent DDL for the `cards` and `edges` tables
2. Load `notation.json` → `app.config["NOTATION"]`
3. Load `key-terms.json` → `app.config["KEY_TERMS"]`
4. `load_all_cards(...)` — scans `cards/**/*.md`, skips unchanged files by `st_mtime`, upserts changed ones, removes cards whose files no longer exist
5. `load_edges_from_file()` — clears the `edges` table and repopulates from `edges.json`
6. Load `resources.json` → `app.config["RESOURCES"]`
7. Register the blueprint and attach the context processor (CSRF token, topic colours, search data, site stats)

## Building and Running

The project uses `uv` for dependency management.

### Setup
```bash
uv sync                      # Create/update virtual environment
```

### Running the App
```bash
FLASK_DEBUG=1 uv run python run.py    # Starts server at http://127.0.0.1:5000
```

**`FLASK_DEBUG=1` is required for local development.** `create_app()` raises `RuntimeError` unless either `SECRET_KEY` is set in the environment or debug mode is on. If the server is launched in the background without it, the process dies immediately and the traceback is easily lost — always confirm the server is actually serving before assuming a restart succeeded.

Startup rebuilds `graph.db` by parsing every card, which takes upwards of twenty seconds for a collection of this size. Poll for a response rather than waiting a fixed couple of seconds:

```bash
for i in $(seq 1 30); do
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:5000/card/<card-id>")
  [ "$code" = "200" ] && break
  sleep 2
done
```

Card changes are picked up on server restart. Delete `graph.db` first to force a full rebuild. To stop a running instance, kill it **by port** (`lsof -ti tcp:5000 | xargs -r kill`) rather than with `pkill -f "run.py"` — that pattern also matches the shell issuing the command whenever the same command line contains the launch string, killing the caller instead of the server.

### Utilities
- **URL Validation:** `uv run python scripts/validate_urls.py --force` (Checks links in `resources.json`)
- **README Stats:** `uv run python scripts/update_readme_stats.py` (Updates card and edge counts in README)
- **Install Git Hooks:** `bash scripts/install_hooks.sh` (Installs the pre-commit URL validator; the hook itself is not committed, so run this after cloning)

URL validation runs automatically on `git commit` when `resources.json` is staged, and **blocks the commit** if any link fails. Some well-known hosts reject automated requests outright (Real Python returns 403 to every user agent) while others rate-limit intermittently under concurrency — a failure on retry-friendly hosts such as Wikipedia or BIS is usually transient, but a hard 403 means the link must be replaced.

## Routes

| Method | URL | Purpose |
|---|---|---|
| GET | `/` | Card grid, tag filter strip, `?tag=` / `?topic=` filtering |
| GET | `/tag/<tag>` | All cards carrying one tag |
| GET | `/card/<path:card_id>` | Card content, prerequisites, see-also, sidebar |
| POST | `/card/<path:card_id>/remove-link` | Delete an edge (CSRF-protected) |
| GET | `/graph` | vis.js network — path finding, topic filtering, edge weights |
| GET | `/formulas` | All Key Formula sections aggregated by topic |
| GET | `/recent` | Reverse-chronological card list grouped by date (unlisted) |
| GET | `/random` | Redirect to a random card |

## Testing

There are no automated test suites. Verification is manual:
1. Start the server and ensure it doesn't fail with `ValueError` (triggered by malformed cards).
2. Verify new cards appear on the index page under the correct topic.
3. Check the card detail page for correct HTML/KaTeX rendering.
4. Verify the node appears correctly in the `/graph` view.

## Development Conventions

### Card Authoring
Cards are stored in `cards/<topic>/<slug>.md`. They MUST follow a strict format for metadata parsing (regex-based):

```markdown
# Concept Name

**Topic:** <Topic Name>
**Tags:** tag1, tag2
**Created:** YYYY-MM-DD
**Author:** <Name/Model>

---

## Definition
...
## Key Formula
...
## Example
...
## Remember (Finance application)
...
```

- **Required fields:** `**Topic:**`, `**Tags:**` and `**Author:**` are extracted by regex; a card missing any of them raises `ValueError` at startup. `**Created:**` is conventional but not parsed — it is stripped from the rendered output, and `/recent` sorts by the file's modification time instead.
- **British English:** Use British spelling (e.g., "normalised", "behaviour").
- **Maths:** Use `$...$` for inline and `$$...$$` for display maths (KaTeX).
- **Topic Identity:** Topics must match keys in `app/routes.py::TOPIC_COLOURS`.
- **Do not** add a `**Level:**` field — it is not a recognised metadata field.

### LaTeX Pitfalls
- **Inside Markdown tables:** a bare `|` within `$...$` is misread as a column separator. Use `\lvert` and `\rvert` for absolute value (e.g. `$\lvert x\rvert$`) and `\middle\vert` for conditional-expectation bars. Never place a `\begin{...}` environment (cases, aligned, matrix, …) inside inline `$...$` in a table cell — Markdown treats the `\\` line break as an escaped backslash. Move such formulas into a `$$...$$` block outside the table.
- **Currency in prose:** escape dollar signs as `\$` (e.g. `\$6 bn`). A bare `$` can be read by KaTeX as the opening of inline maths, especially when other `$...$` appears later in the same card.

### Topics and Directories

Topics (16):

| Directory | Topic name |
|---|---|
| `cards/banking-regulation/` | `Banking Regulation` |
| `cards/calculus/` | `Calculus` |
| `cards/computational-finance/` | `Computational Finance` |
| `cards/derivatives/` | `Derivatives` |
| `cards/financial-maths/` | `Financial Mathematics` |
| `cards/fixed-income/` | `Fixed Income` |
| `cards/linear-algebra/` | `Linear Algebra` |
| `cards/machine-learning/` | `Machine Learning` |
| `cards/mathematical-notation/` | `Mathematical Notation` |
| `cards/portfolio-theory/` | `Portfolio Theory & Asset Pricing` |
| `cards/probability/` | `Probability` |
| `cards/risk/` | `Risk` |
| `cards/short-selling/` | `Short Selling` |
| `cards/statistics/` | `Statistics` |
| `cards/stochastic-processes/` | `Stochastic Processes` |
| `cards/volatility/` | `Volatility` |

Adding a topic requires a new entry in `TOPIC_COLOURS`; the colour cascades to card tiles, content headings, graph nodes and badges through the CSS custom property `--tc`.

### Database and Loading
- **Card IDs:** Derived from file paths (e.g., `derivatives/black-scholes-equation`).
- **Loader:** `app/loader.py` performs incremental reloads based on file `st_mtime`.
- **Edges:** Mutations (removing links) are written back to `edges.json`. Adding edges is currently manual via `edges.json`.
- **Edge integrity:** Both `source` and `target` must be existing card IDs. Orphaned edges are skipped silently at load time, so a typo produces a missing link rather than an error — verify IDs when editing `edges.json` by hand, and never commit `edges.json` without the cards it references.

### Frontend
- **No Build Step:** All CSS is in `app/static/style.css`. Third-party JS/CSS is loaded from CDNs.
- **Theme:** Dark/Light theme is client-side only (`localStorage`, `data-theme` on `<html>`).
- **Wide Mode:** Removes `max-width` constraints for full-viewport layouts (`localStorage`, `data-wide` on `<html>`). Toggle via the expand button in the navbar or the `w` keyboard shortcut.
- **Search:** Fuzzy search is client-side using a JSON blob injected via context processor.
- **Notation & Key Terms:** LaTeX symbols and plain-text variables used in each card are extracted at load time and displayed in the card sidebar, sourced from `notation.json` and `key-terms.json`.
