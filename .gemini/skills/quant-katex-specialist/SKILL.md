---
name: quant-katex-specialist
description: Master the project's LaTeX and KaTeX formatting conventions for mathematical formulas. Use when writing or debugging maths in .md files.
---

# Quant KaTeX Specialist

This skill ensures mathematical formulas are formatted for high-quality client-side rendering with KaTeX, maintaining consistency across all flash cards.

## Core Conventions

### 1. LaTeX Notation (`notation.json`)
Check `notation.json` for standardized symbols. Use these verbatim:
- `\mathbb{E}` for expected value.
- `\sigma` for volatility.
- `\mu` for drift.
- `\Sigma` for the covariance matrix.
- `dW_t` for a Wiener increment.

### 2. Formatting Rules
- **Display Maths**: Use `$$...$$` with a leading/trailing newline.
- **Inline Maths**: Use `$S_t$` for variables in sentences. No spaces between `$` and the content (e.g., ` $ S_t $ ` is wrong).
- **Subscripts**: `S_t`, `\sigma^2`, `\text{VaR}_{0.99}`.
- **Vectors/Matrices**: Use `\mathbf{w}` for vectors and uppercase bold `\mathbf{M}` for matrices if standard notation is used.

### 3. Common Escaping Pitfalls
In Markdown, `\` is an escape character. While `app/loader.py` has a `_protect_math` function to handle this, it's safer to:
- Double check if complex LaTeX constructs (like `\begin{pmatrix}...`) render correctly.
- Use `\text{...}` for descriptive subscripts like $V_{\text{call}}$.

### 4. KaTeX Tooltips
The frontend maps LaTeX commands to tooltips using `notation.json`. Ensure that any new symbols are added to `notation.json` so they become interactive in the UI.

## Workflow
1. **Review**: Identify all LaTeX blocks in a card.
2. **Standardise**: Match symbols to the existing `notation.json` schema.
3. **Verify**: Ensure inline/display formatting is correct.
4. **Extend**: Propose additions to `notation.json` for new symbols introduced by the card.
