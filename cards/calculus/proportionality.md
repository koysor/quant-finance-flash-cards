# Proportionality

**Topic:** Calculus
**Tags:** proportionality, direct proportion, inverse proportion, constant of proportionality, power law
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Direct proportion:** $y \propto x$ means $y = kx$ for some constant $k > 0$ — doubling $x$ doubles $y$. **Inverse proportion:** $y \propto 1/x$ means $y = k/x$ — doubling $x$ halves $y$. More generally, $y \propto x^n$ (power law) means $y = kx^n$. The **constant of proportionality** $k$ is found from a known data point. Proportionality relationships are identified by the straight line through the origin when the appropriate quantities are plotted.

## Key Formula

**Direct proportion:** $y = kx \implies k = y/x = \text{constant}$

**Inverse proportion:** $y = k/x \implies xy = k = \text{constant}$

**Power law:** $y = kx^n \implies \ln y = \ln k + n \ln x$ (linear on log-log axes)

**Finding $k$:** substitute one known $(x_0, y_0)$ pair to obtain $k = y_0/x_0^n$.

**Ratio method:** $\dfrac{y_2}{y_1} = \left(\dfrac{x_2}{x_1}\right)^n$

## Example

Transaction cost is directly proportional to the square root of order size: $C \propto \sqrt{Q}$ (the square-root market impact model).

If a £10,000 trade costs £50, find the cost for a £40,000 trade.

$$k = \frac{50}{\sqrt{10{,}000}} = \frac{50}{100} = 0.5$$

$$C = 0.5\sqrt{40{,}000} = 0.5 \times 200 = £100$$

Doubling order size increases cost by factor $\sqrt{2} \approx 1.41$, not 2 — the key insight of **square-root market impact**.

## Remember

Power-law proportionality ($y \propto x^n$) appears throughout quantitative finance. The **square-root rule** for market impact ($C \propto \sqrt{Q}$) determines optimal trade scheduling in execution algorithms. **Volatility scales with the square root of time** ($\sigma_T \propto \sqrt{T}$, the $n=1/2$ power law), so the 10-day VaR is $\sqrt{10}$ times the 1-day VaR under i.i.d. returns. The **Pareto distribution** is a power law relating tail probability to loss size ($P(X>x) \propto x^{-\alpha}$). In each case, fitting the proportionality constant $k$ from observed data allows prediction at new points — the core use of proportionality in financial calibration.
