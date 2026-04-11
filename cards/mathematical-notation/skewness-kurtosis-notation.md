# Skewness and Kurtosis Notation

**Topic:** Mathematical Notation
**Tags:** notation, skewness, kurtosis, higher moments, fat tails, non-normality
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Skewness** and **kurtosis** are the standardised 3rd and 4th moments of a distribution. Their notation appears throughout quantitative finance wherever models go beyond the normal distribution.

| Symbol | Read as | Definition | Normal value |
|---|---|---|---|
| $\gamma_1$ or $\text{Skew}(X)$ | "skewness" or "gamma one" | $E\!\left[\left(\frac{X-\mu}{\sigma}\right)^3\right] = \mu_3/\sigma^3$ | 0 |
| $\gamma_2$ or $\text{Kurt}(X)$ | "kurtosis" or "gamma two" | $E\!\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] = \mu_4/\sigma^4$ | 3 |
| $\kappa$ or $\gamma_2 - 3$ | "excess kurtosis" | Kurtosis minus 3 (relative to normal) | 0 |
| $\mu_3$ | "third central moment" | $E[(X-\mu)^3]$ | 0 |
| $\mu_4$ | "fourth central moment" | $E[(X-\mu)^4]$ | $3\sigma^4$ |

## Key Formula

$$\gamma_1 = \frac{\mu_3}{\sigma^3} = \frac{E[(X-\mu)^3]}{\left(E[(X-\mu)^2]\right)^{3/2}}$$

$$\gamma_2 = \frac{\mu_4}{\sigma^4} = \frac{E[(X-\mu)^4]}{\left(E[(X-\mu)^2]\right)^{2}}$$

| $\gamma_1 < 0$ | Negative skew | Long left tail — large losses more likely than large gains |
|---|---|---|
| $\gamma_1 > 0$ | Positive skew | Long right tail — large gains more likely than large losses |
| $\gamma_2 - 3 > 0$ | Excess kurtosis (leptokurtic) | Fatter tails than normal — more extreme outcomes |
| $\gamma_2 - 3 < 0$ | Platykurtic | Thinner tails than normal |

## Example

A Student's $t$ distribution with $\nu$ degrees of freedom has $\gamma_1 = 0$ (symmetric) and excess kurtosis $\gamma_2 - 3 = 6/(\nu - 4)$ for $\nu > 4$. At $\nu = 5$: excess kurtosis $= 6$. Equity log-return samples typically show $\gamma_1 \approx -0.3$ to $-1$ and excess kurtosis $\approx 2$ to $10$.

## Remember

The Jarque-Bera test for normality tests the joint hypothesis $\gamma_1 = 0$ and $\gamma_2 = 3$ using the statistic $JB = \frac{n}{6}\left(\gamma_1^2 + \frac{(\gamma_2-3)^2}{4}\right) \overset{d}{\to} \chi^2_2$. Excess kurtosis $> 0$ (fat tails) means VaR estimated from a normal distribution underestimates true tail risk — the core motivation for using Student's $t$ or EVT-based models instead.
