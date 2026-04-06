# Generalised Extreme Value Distribution

**Topic:** Probability
**Tags:** GEV, extreme value theory, block maxima, Gumbel, Fréchet, Weibull, tail risk
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Generalised Extreme Value (GEV) distribution** is the limiting distribution of **block maxima** (e.g. the maximum loss in each year), as established by the Fisher–Tippett–Gnedenko theorem. It unifies three extreme value distributions: **Gumbel** ($\xi = 0$, light tails), **Fréchet** ($\xi > 0$, heavy tails), and **Weibull** ($\xi < 0$, bounded upper tail). The shape parameter $\xi$ is the key quantity — financial returns typically have $\xi > 0$.

## Key Formula

**CDF:**

$$F(x;\mu,\sigma,\xi) = \exp\!\left\{-\left[1 + \xi\left(\frac{x-\mu}{\sigma}\right)\right]^{-1/\xi}\right\}, \quad 1 + \xi\left(\frac{x-\mu}{\sigma}\right) > 0$$

For $\xi = 0$ (Gumbel): $F(x) = \exp\{-e^{-(x-\mu)/\sigma}\}$.

**Return level** $x_T$ (the level exceeded on average once every $T$ blocks):

$$x_T = \mu - \frac{\sigma}{\xi}\left[1 - (-\ln(1-1/T))^{-\xi}\right]$$

**Block maxima approach:** divide data into $n$ blocks (e.g. years), take the maximum of each, fit GEV to the $n$ maxima.

## Example

Annual maximum daily loss for a trading desk over 20 years. Fitted GEV: $\hat{\mu} = 3\%$, $\hat{\sigma} = 1\%$, $\hat{\xi} = 0.3$ (Fréchet, heavy tail).

**100-year return level** (1-in-100 annual maximum loss):

$$x_{100} = 3 - \frac{1}{0.3}\left[1 - (-\ln 0.99)^{-0.3}\right] \approx 3 + 5.2 = 8.2\%$$

This extreme daily loss (8.2%) informs stress testing capital buffers.

## Remember

GEV modelling is the foundation of **stress testing and scenario analysis** in banking. The **1-in-200 year stress** required under Solvency II and ICAAP is a return level calculated directly from the GEV distribution fitted to historical extreme losses. The choice of $\xi > 0$ (Fréchet) vs $\xi = 0$ (Gumbel) is critical: Fréchet tails decay as a power law, implying that extreme losses can be arbitrarily large, while Gumbel tails decay exponentially. For equity returns, empirical evidence strongly supports Fréchet — the normal distribution ($\xi < 0$) systematically **underestimates tail risk**, which contributed to the failure of many pre-2008 risk models.
