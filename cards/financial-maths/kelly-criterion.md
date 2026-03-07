# Kelly Criterion

**Topic:** Financial Mathematics
**Tags:** kelly criterion, optimal sizing, leverage, expected growth, risk management
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The Kelly criterion determines the optimal fraction of capital to wager on a favourable bet (or invest in a risky asset) in order to maximise the long-run geometric growth rate of wealth. Betting more than the Kelly fraction increases risk without improving long-term growth; betting less sacrifices growth for lower volatility.

## Key Formula

For a simple bet with win probability $p$, loss probability $q = 1 - p$, and net odds $b$ (win $b$ for every 1 risked):

$$f^* = \frac{p \cdot b - q}{b} = \frac{p(b + 1) - 1}{b}$$

For a continuous investment with excess return $\mu$ and volatility $\sigma$:

$$f^* = \frac{\mu}{\sigma^2}$$

This is the **leverage ratio** that maximises the expected logarithmic growth rate $g = \mu f - \frac{1}{2}\sigma^2 f^2$.

## Example

A trading strategy has an expected excess return of $\mu = 12\%$ per annum and volatility $\sigma = 20\%$.

$$f^* = \frac{0.12}{0.20^2} = \frac{0.12}{0.04} = 3.0$$

The Kelly-optimal leverage is 3x. At this level the expected growth rate is:

$$g = 0.12 \times 3 - \frac{1}{2} \times 0.04 \times 9 = 0.36 - 0.18 = 0.18 = 18\%$$

Most practitioners use **half-Kelly** ($f = 1.5$) to reduce drawdown risk, sacrificing only 25% of the growth rate while halving the variance.

## Remember

The Kelly criterion is the mathematical bridge between leverage and long-term wealth growth. It shows that there is a precise optimal leverage — go beyond it and the geometric growth rate actually **decreases** despite higher expected arithmetic returns. In quantitative finance, Kelly sizing is used by systematic funds to determine position sizes, and it explains why even strategies with positive expected value can destroy wealth if over-leveraged. The formula $f^* = \mu / \sigma^2$ also reveals that the Sharpe ratio alone does not determine optimal leverage — a high-Sharpe, high-volatility strategy warrants less leverage than a high-Sharpe, low-volatility one.
