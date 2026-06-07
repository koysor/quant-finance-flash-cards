# Annualised Return

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** annualised return, cagr, geometric mean, compounding, performance measurement
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The annualised return (also called compound annualised growth rate, CAGR) is the constant rate of return that, if applied each year, would grow an investment from its starting value to its ending value over the measurement period. It accounts for compounding and gives a single comparable figure regardless of how long a track record is.

## Key Formula

$$R_{\text{ann}} = \left(\frac{V_T}{V_0}\right)^{1/T} - 1$$

where $V_0$ is the initial value, $V_T$ is the final value, and $T$ is the number of years.

From periodic returns $r_1, r_2, \ldots, r_n$ measured over $\delta t$ years each:

$$R_{\text{ann}} = \left(\prod_{i=1}^{n}(1 + r_i)\right)^{1/T} - 1$$

where $T = n \cdot \delta t$ is the total period in years (e.g. 252 trading days $= 1$ year, so $\delta t = 1/252$).

## Example

A portfolio starts at \$100 and grows to \$161 over five years.

$$R_{\text{ann}} = \left(\frac{161}{100}\right)^{1/5} - 1 = (1.61)^{0.2} - 1 \approx 0.10 = 10\%$$

The same 61% total gain expressed as a simple average of annual returns might give a misleading figure if individual years varied widely (e.g. +40%, −10%, +20%, −5%, +16%). The geometric mean captures the path-dependence that the arithmetic mean ignores.

## Remember

Annualised return is the numerator in the Calmar ratio, the Sharpe ratio (when using annualised inputs), and most other risk-adjusted metrics. Using arithmetic mean returns instead of geometric mean overstates performance when volatility is high — the gap between the two is approximately $\tfrac{1}{2}\sigma^2$ (the variance drag), which is why high-volatility strategies must clear a higher hurdle to deliver the same compounded wealth growth.

