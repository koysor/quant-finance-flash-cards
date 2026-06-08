# Accumulator

**Topic:** Derivatives
**Tags:** accumulator, structured product, knock-out, path-dependent, daily settlement, leveraged downside
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

An **accumulator** is a structured product in which the buyer agrees to purchase a fixed number of shares each business day at a discounted forward price $K$, but the contract knocks out permanently if the share price rises above a barrier $H > K$. The buyer gains from the daily discount yet bears unlimited downside if the stock falls sharply — a profile that earned the product the nickname "I kill you later" during the 2008 crisis.

## Key Formula

Each day $t$ that the contract is live (i.e. $S_t \leq H$), the buyer receives a daily settlement:

$$\text{P\&L}_t = n \,(S_t - K)$$

where $n$ is the daily share quantity and $K < S_t$ in normal conditions. The contract terminates on the first day $\tau$ such that $S_\tau > H$. Total P&L over the product's life is:

$$\text{Total} = n \sum_{t=1}^{\tau} (S_t - K)$$

There is no floor: if $S_t \ll K$, the buyer still purchases at $K$, accumulating losses proportional to $K - S_t$ for every remaining day.

## Example

An accumulator on a stock: $K = \$90$ (10 % discount), $H = \$110$ (knock-out barrier), $n = 1{,}000$ shares/day, 6-month term (≈ 130 days).

- Day 1–60: stock trades at \$95–\$105 → buyer gains \$5–\$15 per share daily
- Day 61: stock jumps to \$112 > \$110 → contract knocks out; buyer keeps gains to date
- Alternative scenario: stock falls to \$60 → buyer pays \$90 for shares worth \$60, losing \$30 per share × 1,000 = \$30,000 per day for the remaining days

## Remember

Accumulators are widely sold in private banking in Asia as a yield-enhancement overlay on equity holdings. Because the knock-out triggers only on the upside, the buyer forfeits participation in strong rallies whilst retaining full exposure to severe declines — a short-volatility, short-skew position. Pricing requires Monte Carlo simulation over the full daily path to evaluate the expected knock-out time and daily settlement cash flows.
