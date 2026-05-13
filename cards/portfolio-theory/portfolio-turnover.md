# Portfolio Turnover

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** portfolio turnover, rebalancing, transaction costs, active management, trading
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

Portfolio turnover measures how much of a portfolio's holdings are replaced over a given period, expressed as a fraction of total portfolio value. High turnover means frequent trading, which amplifies transaction costs and can erode net returns even when the underlying strategy has genuine alpha.

## Key Formula

$$\text{Turnover} = \frac{\sum_{i} \max(\Delta w_i^+, 0)}{1} = \frac{1}{2} \sum_{i} |\Delta w_i|$$

where $\Delta w_i = w_i^{\text{new}} - w_i^{\text{old}}$ is the change in weight for asset $i$. The factor of $\frac{1}{2}$ avoids double-counting buys and sells. Annualised turnover scales by the number of rebalancing periods per year:

$$\text{Annual Turnover} = \text{Turnover per period} \times \text{Periods per year}$$

## Example

A portfolio holds three assets with weights $[0.5, 0.3, 0.2]$. After rebalancing, the new weights are $[0.4, 0.4, 0.2]$.

Weight changes: $[-0.1, +0.1, 0.0]$.

$$\text{Turnover} = \frac{1}{2}(0.1 + 0.1 + 0) = 0.10 = 10\%$$

If the portfolio rebalances monthly, annual turnover is $10\% \times 12 = 120\%$. At a one-way transaction cost of 20 bps, annual cost drag is $120\% \times 20\text{ bps} = 24\text{ bps}$.

## Remember

Turnover is the bridge between a strategy's gross alpha and its net alpha. A momentum strategy might generate 3% gross alpha per year, but at 300% annual turnover and 20 bps per-trade costs, the drag is $300\% \times 20\text{ bps} = 60\text{ bps}$ — still profitable, but a fund with 400% turnover would wipe out the edge entirely. Index funds deliberately minimise turnover (often below 5% per year), while high-frequency strategies may exceed 10,000% — each percentage point of turnover must be justified by the incremental alpha it harvests.
