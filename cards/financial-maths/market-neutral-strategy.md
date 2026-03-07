# Market Neutral Strategy

**Topic:** Financial Mathematics
**Tags:** market neutral, beta, hedging, long-short, alpha, portfolio construction
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A market neutral strategy constructs a portfolio with zero (or near-zero) exposure to broad market movements by balancing long and short positions so that the portfolio beta is zero. Returns depend entirely on security selection (alpha), not on market direction.

## Key Formula

The **portfolio beta** must equal zero:

$$\beta_p = \sum_{i \in \text{long}} w_i \beta_i + \sum_{j \in \text{short}} w_j \beta_j = 0$$

where $w_i > 0$ for long positions and $w_j < 0$ for short positions.

The **portfolio return** is then pure alpha:

$$R_p = \alpha_p + \underbrace{\beta_p \cdot R_m}_{= \, 0} + \varepsilon_p = \alpha_p + \varepsilon_p$$

To achieve dollar neutrality as well, the total long exposure equals total short exposure:

$$\sum_{i \in \text{long}} |w_i| = \sum_{j \in \text{short}} |w_j|$$

## Example

A fund holds £5 million long in stock $A$ ($\beta_A = 1.3$) and £5 million short in stock $B$ ($\beta_B = 0.8$).

$$\beta_p = \frac{5}{10} \times 1.3 + \frac{-5}{10} \times 0.8 = 0.65 - 0.40 = 0.25$$

The portfolio is not yet market neutral. To achieve $\beta_p = 0$, the fund adjusts the short to £8.125 million in $B$:

$$\beta_p = \frac{5}{13.125} \times 1.3 + \frac{-8.125}{13.125} \times 0.8 = 0.495 - 0.495 = 0$$

Now the portfolio is insulated from market moves and returns depend only on whether $A$ outperforms $B$ on a risk-adjusted basis.

## Remember

Market neutral strategies are central to quantitative hedge funds because they isolate alpha from beta. The key insight is that **beta is free** — any investor can get market exposure through an index fund — so the value a quant fund adds comes from security selection. By hedging out beta, the strategy's Sharpe ratio reflects pure stock-picking skill. However, neutrality is never perfect: beta estimates are noisy, they shift over time, and during market crises, correlations spike towards 1, temporarily breaking the hedge. Successful market neutral funds therefore rebalance frequently and stress-test their beta exposure under extreme scenarios.
