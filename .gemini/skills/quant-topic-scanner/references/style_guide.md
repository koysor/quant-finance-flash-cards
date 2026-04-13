# Flash Card Style Guide

All flash cards MUST follow this structure and tone:

## Tone and Target Audience
- **Target Audience:** A Level maths standard student.
- **Tone:** Clear, succinct, and educational.
- **Language:** British English (e.g., "normalised", "behaviour").
- **Mathematics:** Use LaTeX for all mathematical notation. Use `$...$` for inline and `$$...$$` for block equations.

## Structure

```markdown
# [Topic Name]

## [What is it? / Description]
A brief, clear explanation of the concept. Focus on the intuition and basic definition.

## Formula
[LaTeX formula block]
[Explanation of variables]

## Key Points
- Bullets covering important properties, constraints, or interpretations.
- Use a table if it helps explain different scenarios (e.g., long vs short).

## Example
A simple, concrete numerical or conceptual example to illustrate the concept.

---
> **Remember:** A one-sentence takeaway or critical rule-of-thumb.
```

## Examples

### Return on Investment
# Return on Investment

## What is it?
The **relative** change in the value of an asset over a period — not the absolute profit in pounds.

## Formula

$$R = \frac{\Delta S + \text{cashflows}}{S_0}$$

Where:
- $S_0$ = starting price
- $\Delta S$ = change in price
- cashflows = dividends, coupons, etc.

## Key Point
Using **returns** (not raw prices) lets you compare assets of completely different scales — a £5 stock vs a £500 stock on equal footing.

## Discrete-step version

$$R_i = \frac{S_{i+1} - S_i}{S_i}$$

This is the return from day $i$ to day $i+1$.

---
> **Remember:** Return is always expressed as a fraction (or percentage), not a cash amount.

### Portfolio Weights
# Portfolio Weights

## What are they?

**Portfolio weights** express each asset's share of total portfolio value. They are the fundamental language of portfolio construction — every allocation decision comes down to choosing weights.

## Formula

$$w_i = \frac{\text{Market Value of Asset } i}{\text{Total Market Value of Portfolio}}$$

## Budget Constraint

Weights must sum to 1 (the full portfolio is allocated):

$$\sum_{i=1}^{N} w_i = 1 \qquad \text{or in matrix form:} \quad \mathbf{w}^T \mathbf{1}_N = 1$$

## Key Points

| Situation | Weight | Interpretation |
|---|---|---|
| $w_i > 0$ | Long position | Own the asset |
| $w_i < 0$ | Short position | Borrow and sell |
| $w_i > 1$ | Leveraged long | Borrowed to buy more |
| $w_i = 0$ | Not held | Asset excluded |

## Example

A portfolio worth £100k holds £60k in equity and £40k in bonds:

$$w_{\text{equity}} = 0.6, \quad w_{\text{bonds}} = 0.4, \quad w_{\text{equity}} + w_{\text{bonds}} = 1 \checkmark$$

---

> **Remember:** Weights sum to 1 — that single constraint is the budget equation. Short positions and leverage are allowed; they just shift weights outside [0, 1].
