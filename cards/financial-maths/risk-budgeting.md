# Risk Budgeting

**Topic:** Financial Mathematics
**Tags:** risk budgeting, risk contribution, portfolio construction, risk allocation, diversification
**Author:** Claude Opus 4.6

---

## Definition

Risk budgeting is a portfolio construction framework that allocates a total risk budget across assets or strategies according to their expected contribution to portfolio risk. Unlike risk parity (which demands equal risk contributions), risk budgeting allows deliberate tilts — assigning larger risk budgets to assets with higher expected risk-adjusted returns. The portfolio is then optimised so that each asset's marginal risk contribution matches its assigned budget.

## Key Formula

The **risk contribution** of asset $i$ to total portfolio volatility is:

$$\text{RC}_i = w_i \cdot \frac{\partial \sigma_p}{\partial w_i} = w_i \cdot \frac{(\Sigma \mathbf{w})_i}{\sigma_p}$$

The risk budget constraint requires:

$$\text{RC}_i = b_i \cdot \sigma_p$$

where $b_i$ is the target risk budget fraction for asset $i$, with $\sum_i b_i = 1$.

Risk parity is the special case where $b_i = \frac{1}{n}$ for all $i$.

## Example

A three-asset portfolio has target risk budgets of 50% equities, 30% bonds, and 20% commodities. If the portfolio volatility is 10%:

$$\text{RC}_{\text{equities}} = 0.50 \times 10\% = 5.0\%$$
$$\text{RC}_{\text{bonds}} = 0.30 \times 10\% = 3.0\%$$
$$\text{RC}_{\text{commodities}} = 0.20 \times 10\% = 2.0\%$$

The optimiser finds weights $\mathbf{w}$ such that these contributions are achieved. Because equities are more volatile, their capital weight will be lower than 50% — perhaps 25% — while bonds might receive 55% of capital to produce their 30% risk share.

## Remember

Risk budgeting bridges the gap between traditional mean-variance optimisation (which is notoriously sensitive to expected return inputs) and risk parity (which ignores expected returns entirely). By expressing portfolio decisions in risk units rather than capital units, it forces investment committees to answer the question: "How much of our risk are we willing to allocate to this view?" This framing is used by sovereign wealth funds, pension funds, and multi-strategy hedge funds to ensure that no single bet dominates the portfolio's overall risk profile.
