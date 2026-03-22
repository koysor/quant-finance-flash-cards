# Rebalancing

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** rebalancing, asset allocation, portfolio drift, transaction costs, target weights
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Rebalancing is the process of realigning a portfolio's actual asset weights back to their target allocation after market movements cause them to drift. As different assets earn different returns, the portfolio's composition shifts away from the intended risk profile. Rebalancing restores the original allocation by selling assets that have grown above target and buying those that have fallen below. It can be executed on a fixed calendar schedule (e.g. quarterly), at threshold bands (when drift exceeds a tolerance), or continuously using optimisation.

## Key Formula

The **drift** of asset $i$ from its target weight:

$$d_i = w_i^{\text{actual}} - w_i^{\text{target}}$$

where $w_i^{\text{actual}} = \frac{V_i}{\sum_j V_j}$ is the current weight and $w_i^{\text{target}}$ is the strategic allocation.

The **trade required** to rebalance asset $i$:

$$\Delta V_i = (w_i^{\text{target}} - w_i^{\text{actual}}) \times V_{\text{total}}$$

The **rebalancing cost** across all assets:

$$C_{\text{rebal}} = \sum_{i=1}^{n} |\Delta V_i| \times c_i$$

where $c_i$ is the one-way transaction cost (including spread and market impact) for asset $i$.

## Example

A portfolio has a 60/40 target split between equities and bonds. Starting value is £1,000,000. After a year, equities returned 15% and bonds returned 3%:

| Asset | Start | End value | Actual weight | Target |
|-------|-------|-----------|--------------|--------|
| Equities | £600,000 | £690,000 | 64.2% | 60% |
| Bonds | £400,000 | £412,000 | 38.3% | 40% |
| **Total** | | **£1,102,000** | | |

Drift: equities are 4.2% above target. Trade required:

$$\Delta V_{\text{equities}} = (0.60 - 0.642) \times £1{,}102{,}000 = -£46{,}284$$

Sell £46,284 of equities and buy £46,284 of bonds. At a transaction cost of 0.10%:

$$C_{\text{rebal}} = 2 \times £46{,}284 \times 0.001 = £92.57$$

## Remember

Rebalancing is a disciplined, contrarian mechanism — it systematically sells winners and buys losers, capturing a "rebalancing premium" in mean-reverting markets. However, it comes at a cost: transaction expenses and potential tax consequences. In quantitative finance, the optimal rebalancing policy balances the risk-reduction benefit of staying near target weights against the cost of trading. Research shows that threshold-based rebalancing (trade only when drift exceeds a band, typically 3–5%) outperforms rigid calendar rebalancing because it avoids unnecessary trades while still controlling risk. For multi-asset portfolios, rebalancing frequency is one of the most impactful implementation decisions a portfolio manager makes.
