# GEMINI.md

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
- **Cache:** `graph.db` (Gitignored SQLite database, rebuilt on startup)

## Building and Running

The project uses `uv` for dependency management.

### Setup
```bash
uv sync                      # Create/update virtual environment
```

### Running the App
```bash
uv run python run.py         # Starts server at http://127.0.0.1:5000
```

On first run or restart, the app scans `cards/`, parses metadata, and populates `graph.db`. Card changes are picked up on server restart.

### Utilities
- **URL Validation:** `uv run python scripts/validate_urls.py --force` (Checks links in `resources.json`)
- **README Stats:** `uv run python scripts/update_readme_stats.py` (Updates card and edge counts in README)

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

- **British English:** Use British spelling (e.g., "normalised", "behaviour").
- **Maths:** Use `$...$` for inline and `$$...$$` for display maths (KaTeX).
- **Topic Identity:** Topics must match keys in `app/routes.py::TOPIC_COLOURS`.

### Database and Loading
- **Card IDs:** Derived from file paths (e.g., `derivatives/black-scholes-equation`).
- **Loader:** `app/loader.py` performs incremental reloads based on file `st_mtime`.
- **Edges:** Mutations (removing links) are written back to `edges.json`. Adding edges is currently manual via `edges.json`.

### Frontend
- **No Build Step:** All CSS is in `app/static/style.css`. Third-party JS/CSS is loaded from CDNs.
- **Theme:** Dark/Light theme is client-side only (localStorage).
- **Search:** Fuzzy search is client-side using a JSON blob injected via context processor.
