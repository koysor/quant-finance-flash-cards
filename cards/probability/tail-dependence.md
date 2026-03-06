# Tail Dependence

**Topic:** Probability
**Tags:** tail dependence, copulas, extreme events, credit risk, joint distribution
**Author:** Claude Opus 4.6

---

## Definition

**Tail dependence** measures the probability that two variables simultaneously take extreme values. The **lower tail dependence coefficient** $\lambda_L$ quantifies the probability that one variable is in its extreme left tail given that the other is also in its extreme left tail. Similarly, **upper tail dependence** $\lambda_U$ measures joint extreme right-tail events. A distribution with $\lambda_L > 0$ exhibits lower tail dependence — crashes tend to happen together.

## Key Formula

**Lower tail dependence coefficient:**

$$\lambda_L = \lim_{u \to 0^+} P\!\left(X \leq F_X^{-1}(u) \mid Y \leq F_Y^{-1}(u)\right)$$

**Upper tail dependence coefficient:**

$$\lambda_U = \lim_{u \to 1^-} P\!\left(X > F_X^{-1}(u) \mid Y > F_Y^{-1}(u)\right)$$

**Key results by copula family:**

| Copula | $\lambda_L$ | $\lambda_U$ |
|--------|------------|------------|
| Gaussian | 0 | 0 |
| Student-$t$ ($\nu$ d.f.) | $2 t_{\nu+1}\!\left(-\sqrt{(\nu+1)(1-\rho)/(1+\rho)}\right) > 0$ | same |
| Clayton ($\theta > 0$) | $2^{-1/\theta} > 0$ | 0 |
| Gumbel ($\theta > 1$) | 0 | $2 - 2^{1/\theta} > 0$ |

## Example

Two stocks modelled with a Student-$t$ copula with $\nu = 4$ degrees of freedom and $\rho = 0.5$:

$$\lambda_L = 2 \, t_5\!\left(-\sqrt{\frac{5 \times 0.5}{1.5}}\right) = 2 \, t_5(-1.291) \approx 2 \times 0.127 = 0.254$$

There is a 25.4% probability that stock B is in its worst 0.1% of outcomes given that stock A is also in its worst 0.1%.

Under a Gaussian copula with the same $\rho = 0.5$: $\lambda_L = 0$ — the model says joint crashes are asymptotically impossible, regardless of the correlation.

## Remember

Tail dependence is the mathematical quantity that separates adequate risk models from dangerous ones. During the 2008 financial crisis, assets that appeared moderately correlated under normal conditions exhibited near-perfect co-movement in the crash — precisely the behaviour that non-zero tail dependence captures. The Gaussian copula's $\lambda_L = 0$ was a key reason CDO risk models failed catastrophically: they could not generate the simultaneous defaults that actually occurred. Any risk model for portfolio VaR, credit portfolio losses, or systemic risk assessment must account for tail dependence, typically by using Student-$t$ or Clayton copulas instead of the Gaussian.
