# Information Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** information ratio, tracking error, active management, benchmark, performance attribution
**Author:** Claude Opus 4.6

---

## Definition

The information ratio (IR) measures the risk-adjusted return of an active portfolio relative to its benchmark. It divides the average excess return over the benchmark (active return) by the tracking error (the volatility of that excess return). A higher IR indicates more consistent outperformance per unit of active risk taken.

## Key Formula

$$\text{IR} = \frac{\bar{R}_p - \bar{R}_b}{\sigma(R_p - R_b)} = \frac{\bar{\alpha}}{\text{TE}}$$

where $\bar{R}_p$ is the mean portfolio return, $\bar{R}_b$ is the mean benchmark return, and $\text{TE} = \sigma(R_p - R_b)$ is the tracking error.

The information ratio is related to the Sharpe ratio by:

$$\text{IR} = \text{SR}_p - \text{SR}_b \quad \text{(approximately, for small active bets)}$$

## Example

A fund manager outperforms the FTSE 100 by an average of 2.4% per annum over five years. The monthly active returns have an annualised standard deviation (tracking error) of 4%:

$$\text{IR} = \frac{0.024}{0.04} = 0.60$$

An IR of 0.60 is considered good. For context:
- IR $> 0.5$: strong active manager
- IR $\approx 0.2\text{--}0.3$: typical active manager
- IR $< 0$: underperforming the benchmark

## Remember

The information ratio is to relative return what the Sharpe ratio is to absolute return — it answers whether the active risk a manager takes is rewarded with consistent outperformance. Institutional investors use the IR to decide whether to allocate capital to an active manager or simply buy a cheap index tracker. A manager with high alpha but erratic tracking error may have a lower IR than a steady, modest outperformer, which is why consistency matters as much as magnitude in professional fund management.
