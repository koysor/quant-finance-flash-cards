# Value at Risk (VaR)

**Topic:** Risk
**Tags:** risk, VaR, quantile, loss distribution
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Value at Risk (VaR)** at confidence level α is the maximum loss that will not be exceeded with probability α over a given time horizon.

Equivalently: there is a (1 − α) probability that losses will **exceed** VaR.

Common conventions: 95% VaR (5% chance of exceeding) or 99% VaR (1% chance).

## Key Formula

For a portfolio with normally distributed P&L with mean μ and standard deviation σ:

$$\text{VaR}\_{\alpha} = -(\mu + z\_{\alpha} \sigma)$$

Where z_α is the α-quantile of the standard normal distribution:

| Confidence level | z_α |
|---|---|
| 95% | −1.645 |
| 99% | −2.326 |

(The negative sign converts a left-tail loss to a positive VaR number.)

## Example

A portfolio has daily mean return μ = 0 and daily standard deviation σ = £100,000.

**1-day 99% VaR:**

VaR = −(0 + (−2.326) × 100,000) = **£232,600**

There is a 1% chance of losing more than £232,600 on any given day.

**Scaling to n days** (for independent returns): VaR_n = VaR_1 × √n

## Remember

- VaR tells you **nothing** about the size of losses beyond the threshold (the tail). Two portfolios with the same VaR can have very different worst-case scenarios.
- **CVaR** (Conditional Value at Risk, also called Expected Shortfall) addresses this by measuring the *expected* loss given that losses exceed VaR. CVaR is a **coherent risk measure**; VaR is not.
- VaR was widely used before the 2008 financial crisis, whose severity highlighted the danger of relying solely on VaR for risk management.
