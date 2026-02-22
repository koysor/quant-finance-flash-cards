# Quantitative Finance Flash Cards

Bite-sized revision flash cards for Quantitative Finance exams and interviews, pitched at **A Level mathematics** standard. Each card covers one concept — definition, key formula, worked example, and its finance application.

31 cards · 8 topics · 37 concept connections

## Running the app

```bash
uv sync                      # install dependencies
uv run python run.py         # http://127.0.0.1:5000
```

On first run the app scans `cards/` and loads `edges.json`, building `graph.db` automatically. Adding or editing a card takes effect on the next server restart.

## Topics

| Topic | Cards |
|---|---|
| Probability | Normal Distribution, Lognormal Distribution, Expected Value, Bayes' Theorem |
| Statistics | Variance & Std Dev, Correlation, Statistical Properties of Returns, Scaling Mean with Time, Square-Root Rule, Estimating Parameters |
| Calculus | Differentiation Rules, Taylor Series |
| Linear Algebra | Matrix Multiplication |
| Financial Mathematics | Time Value of Money, Return on Investment |
| Derivatives | Put-Call Parity, Option Greeks, Black-Scholes Equation, Risk-Neutral Pricing, Implied Volatility, Delta Hedging |
| Stochastic Processes | Brownian Motion, Geometric Brownian Motion, Itô's Lemma, Drift & Volatility, Discrete Random Walk, SDE, Growth vs Volatility Timescales |
| Risk | Value at Risk (VaR), Monte Carlo Simulation, Model Limitations |

## Features

- **Card library** — browse all cards grouped by topic, filter by tag or topic
- **Tag pages** — dedicated `/tag/<tag>` pages listing all cards for a given tag
- **Prerequisites & See Also** — incoming edges shown as prerequisites above card content; outgoing edges shown as "See Also" below
- **Knowledge graph** — interactive force-directed network with topic filtering, shortest-path highlighting between any two nodes, and edge weights based on shared tags
- **Spotlight search** — press `/` for fuzzy search across all cards by name or tag
- **Keyboard navigation** — `←`/`→` for prev/next card in topic, `j`/`k` for card list, `r` for random, `g` for graph, `?` for shortcuts
- **Dark / Light theme** — persisted across sessions
- **Concept links** — directed relationships between cards with plain-English descriptions, stored in `edges.json`
- **Visited tracking** — cards you have read are marked in the browser

## Stack

| Layer | Technology |
|---|---|
| Server | Python 3.12, Flask 3 |
| Database | SQLite (via `sqlite3` stdlib) |
| Maths rendering | KaTeX 0.16.9 (client-side, CDN) |
| Graph visualisation | vis-network 9.1.9 (CDN) |
| Fonts | Sora · Inter · JetBrains Mono (Google Fonts) |
| Package management | uv |

No npm, no build step, no Docker.

## Project layout

```
cards/          Markdown source files — card content source of truth
edges.json      Concept relationships — edge source of truth
app/            Flask application package
  __init__.py   Application factory (create_app)
  db.py         SQLite schema and all query functions
  loader.py     Scans cards/, parses metadata, upserts to DB
  routes.py     All routes + topic colour map
  templates/    Jinja2 templates
  static/       CSS and favicon
run.py          Development server entry point
graph.db        Runtime only — gitignored, fully regenerable
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for a full explanation of how the layers fit together.

## Note

The flash cards in this repository are generated with [Claude Opus](https://www.anthropic.com/claude) for learning and revision purposes. While care has been taken to ensure accuracy, they should be used as study aids alongside primary course materials, not as a sole reference.

## Adding a card

Create a `.md` file in the appropriate `cards/<topic>/` directory and restart the server. See [CONTRIBUTING.md](CONTRIBUTING.md) for the required format and content rules.
