# Constant-Mix Strategy

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** constant-mix, rebalancing, contrarian, volatility harvesting, mean-reversion, portfolio strategy
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A constant-mix strategy maintains **fixed target weights** in each asset class by rebalancing whenever the portfolio drifts. When an asset rises it is sold to restore its target share; when it falls it is bought. This is mechanically contrarian — it buys dips and sells rallies — and produces a **concave payoff profile**: it outperforms buy-and-hold in oscillating markets and underperforms in strongly trending markets.

## Key Formula

Target weights $w^* = (w_1^*, \ldots, w_n^*)$ are held constant by rebalancing. After price moves the portfolio drifts to $\tilde{w}$; the rebalancing trade restores $\tilde{w} \to w^*$.

The **rebalancing bonus** (excess compound return vs. the weighted average of constituent compound returns) is positive when assets are volatile and imperfectly correlated:

$$g_p \geq \sum_i w_i^*\, g_i$$

where $g_p$ is the compound (geometric mean) return of the rebalanced portfolio and $g_i$ is the compound return of asset $i$ held in isolation. The bonus is approximately:

$$g_p - \sum_i w_i^* g_i \approx \frac{1}{2}\!\left(\sum_i w_i^* \sigma_i^2 - \sigma_p^2\right) > 0$$

This excess equals half the **diversification variance** — the variance eliminated by holding uncorrelated assets together.

## Example

60/40 stock-bond portfolio. Stocks (£600) rise 20% to £720; bonds (£400) stay flat. Portfolio drifts to 64/36. Constant-mix sells £37.5 of stocks and buys £37.5 of bonds to restore 60/40.

Stocks then fall 16.7% (back to their original level): £720 − £37.5 = £682.5 × 0.833 = £568.6. Bonds = £437.5.  
Constant-mix portfolio: £568.6 + £437.5 = £1,006.1 (return +0.6%).  
Buy-and-hold: £600 × 1.00 + £400 = £1,000 (return 0%).

By selling high and buying low across the oscillation, constant-mix added 0.6% despite stocks ending flat.

## Remember

Constant-mix is the **default policy of most pension funds and multi-asset passive funds** — calendar-based or threshold-based rebalancing to a 60/40 or 70/30 target. Its rebalancing bonus is sometimes called **volatility harvesting** because higher volatility (with low correlation) increases the bonus: the strategy mechanically profits from the spread between the arithmetic and geometric mean return. This is why diversified portfolios across low-correlation assets (equities + bonds + commodities) show larger rebalancing bonuses than concentrated single-asset portfolios, providing a mathematical argument for broad diversification beyond just risk reduction.
