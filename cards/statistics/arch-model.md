# ARCH Model

**Topic:** Statistics
**Tags:** ARCH, conditional variance, volatility clustering, time series, Engle
**Author:** Claude Opus 4.6

---

## Definition

The **Autoregressive Conditional Heteroskedasticity (ARCH)** model, introduced by Robert Engle in 1982, was the first model to formally capture time-varying volatility in financial returns. It expresses today's conditional variance as a function of past squared return shocks, formalising the observation that large returns — of either sign — tend to be followed by more large returns.

## Key Formula

**ARCH($q$) model:**

$$r_t = \mu + \varepsilon_t, \qquad \varepsilon_t = \sigma_t z_t, \qquad z_t \sim \mathcal{N}(0, 1)$$

$$\sigma_t^2 = \omega + \alpha_1 \varepsilon_{t-1}^2 + \alpha_2 \varepsilon_{t-2}^2 + \cdots + \alpha_q \varepsilon_{t-q}^2 = \omega + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2$$

where $\omega > 0$, $\alpha_i \geq 0$, and $\sum \alpha_i < 1$ for stationarity.

**ARCH(1)** — the simplest case:

$$\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2$$

## Example

An ARCH(1) model with $\omega = 0.00005$ and $\alpha = 0.30$. Yesterday's return shock was $\varepsilon_{t-1} = -0.04$ (a 4% drop).

$$\sigma_t^2 = 0.00005 + 0.30 \times (-0.04)^2 = 0.00005 + 0.00048 = 0.00053$$

$$\sigma_t = \sqrt{0.00053} \approx 2.30\%$$

If the previous day had been calm ($\varepsilon_{t-1} = 0.005$):

$$\sigma_t^2 = 0.00005 + 0.30 \times 0.000025 = 0.0000575, \quad \sigma_t \approx 0.76\%$$

The large shock triples the volatility forecast — this is volatility clustering in action.

## Example

Long-run variance: $\bar{\sigma}^2 = \omega / (1 - \alpha) = 0.00005 / 0.70 = 0.0000714$, so long-run daily vol $\approx 0.85\%$.

## Remember

ARCH was a breakthrough that earned Engle the 2003 Nobel Prize in Economics. Before ARCH, financial models treated volatility as constant — an assumption clearly violated by the data. The practical limitation of ARCH is that capturing persistent volatility clustering requires many lagged terms (high $q$), making estimation cumbersome. GARCH(1,1) solved this by adding the lagged variance term $\beta \sigma_{t-1}^2$, which parsimoniously captures the long memory that ARCH needs many parameters to achieve. ARCH remains important as the conceptual foundation: every modern conditional volatility model — GARCH, EGARCH, GJR-GARCH — is a descendant of Engle's original idea.
