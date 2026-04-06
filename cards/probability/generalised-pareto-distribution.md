# Generalised Pareto Distribution

**Topic:** Probability
**Tags:** GPD, extreme value theory, peaks over threshold, tail risk, EVT, shape parameter
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Generalised Pareto Distribution (GPD)** is the limiting distribution of exceedances over a high threshold, as established by the **Pickands–Balkema–de Haan theorem**. It is parameterised by shape $\xi$ (tail index), scale $\sigma > 0$, and threshold $\mu$. The shape parameter determines tail behaviour: $\xi > 0$ gives heavy tails (Pareto-type), $\xi = 0$ gives exponential tails, $\xi < 0$ gives bounded tails.

## Key Formula

**CDF** (for $x \geq 0$):

$$F(x) = 1 - \left(1 + \frac{\xi x}{\sigma}\right)^{-1/\xi} \; (\xi \neq 0), \qquad F(x) = 1 - e^{-x/\sigma} \; (\xi = 0)$$

**Mean excess function** (mean loss above threshold $u$):

$$\mathbb{E}[X - u \mid X > u] = \frac{\sigma + \xi u}{1 - \xi} \; (\xi < 1)$$

**Expected Shortfall** above VaR at level $q$:

$$\text{ES}_q = \frac{\text{VaR}_q}{1-\xi} + \frac{\sigma - \xi\mu}{1-\xi}$$

**Peaks-over-threshold (POT) method:** choose threshold $u$, fit GPD to exceedances $X - u \mid X > u$.

## Example

Daily losses exceeding 2% (the threshold $u$) for an equity portfolio, $n = 60$ exceedances over 10 years. Fitted GPD: $\hat{\xi} = 0.25$, $\hat{\sigma} = 0.8\%$.

$$\text{VaR}_{99\%} = u + \frac{\hat{\sigma}}{\hat{\xi}}\left[(n(1-0.99)/60)^{-\hat{\xi}} - 1\right] \approx 3.8\%$$

$$\text{ES}_{99\%} = \frac{3.8\%}{1-0.25} + \frac{0.8\% - 0.25 \times 2\%}{0.75} \approx 5.7\%$$

## Remember

The GPD is the **workhorse of Extreme Value Theory in quantitative finance**. The POT method is preferred over block maxima (GEV) because it uses all extreme observations above the threshold, not just one per period, giving more efficient tail estimates. Under FRTB, banks using the Internal Models Approach must estimate **Expected Shortfall at 97.5%** — a tail quantity that requires EVT methods like GPD for accurate estimation from limited data. The shape parameter $\hat{\xi} > 0$ for financial returns confirms **fat tails**: losses follow a power law, not an exponential decay.
