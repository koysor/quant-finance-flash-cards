# Copilot instructions

## Build, test, and lint

Python dependencies are managed with `uv` (Python 3.14).

```bash
uv sync
uv run pytest
uv run pytest tests/test_routes.py
uv run pytest tests/test_routes.py::test_name
uv run ruff check .
FLASK_DEBUG=1 uv run python run.py
```

Use the relevant test file or pytest node ID for a focused run. Local startup
requires `FLASK_DEBUG=1` unless `SECRET_KEY` is set; in PowerShell, use
`$env:FLASK_DEBUG=1; uv run python run.py`. Startup scans the card library;
allow it to finish and treat malformed-card errors as failures.

In CI, `code-quality.yml` runs only Ruff. Pytest runs in the `test` job of
`deploy-ec2.yml`, on pull requests as well as pushes; the deploy step itself is
skipped on pull requests.

## Architecture and sources of truth

This is a Flask/Jinja application with no frontend build step. `app/__init__.py`
is the application factory, `app/routes.py` owns routes and topic colours,
`app/loader.py` parses and loads cards, and `app/db.py` contains SQLite access.
Templates and CSS are under `app/templates/` and `app/static/`; KaTeX and
vis-network are loaded from CDNs.

- `cards/**/*.md` is the source of card content; `edges.json`,
  `resources.json`, `notation.json`, and `key-terms.json` are other committed
  content sources.
- `graph.db` is a gitignored, disposable SQLite cache rebuilt from those files
  at startup. Do not treat it as the content source or commit it.
- Card IDs come from the relative path under `cards/`, including the topic
  directory (for example, `derivatives/black-scholes-equation`). Moving a card
  changes its ID and can break edges/resources that refer to it.
- Production is served behind a URL prefix. Build template links with Flask's
  `url_for`, not root-relative paths.

## Content and implementation conventions

- A card lives at `cards/<topic>/<slug>.md`. The loader requires a `# Title`,
  `Topic`, and `Tags`. `Author` (defaults to "Unknown") and `Created` (falls
  back to the file's modification time) are optional to the loader, but include
  both on new cards. Follow them with `Definition`, `Key Formula`, `Example`,
  and `Remember` sections. The loader extracts metadata by exact-format
  patterns; a missing required field or a topic not in
  `app/routes.py::TOPIC_COLOURS` prevents startup.
- Keep cards concise, use British English, and connect the `Remember` section
  to quantitative finance. Use `$...$` and `$$...$$` for KaTeX.
- In Markdown table cells, avoid raw `|` in LaTeX and avoid multiline LaTeX
  environments; use `\lvert`/`\rvert` or move display maths outside the table.
  Escape currency dollar signs as `\$`.
- Add concept relationships to `edges.json` with valid card IDs, a short label,
  and a plain-English description. Add per-card learning links to
  `resources.json`; `uv run python scripts/validate_urls.py --force` validates
  them. `TOPIC_COLOURS` is the single source for each topic's UI/graph colour.
- Tests use temporary copies of the database and edge file; preserve that
  isolation when adding fixtures or tests.
