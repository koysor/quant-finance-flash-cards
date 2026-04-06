# Weibull Distribution

**Topic:** Probability
**Tags:** Weibull, survival analysis, hazard rate, time to default, reliability, shape parameter
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Weibull distribution** is a flexible continuous distribution on $(0, \infty)$ parameterised by shape $k > 0$ and scale $\lambda > 0$. It generalises the exponential distribution ($k = 1$) to allow **increasing** ($k > 1$), **constant** ($k = 1$), or **decreasing** ($k < 1$) hazard rates over time. This makes it suitable for modelling time-to-event data where the failure rate changes with age — unlike the memoryless exponential.

## Key Formula

**PDF and CDF:**

$$f(t) = \frac{k}{\lambda}\left(\frac{t}{\lambda}\right)^{k-1} e^{-(t/\lambda)^k}, \qquad F(t) = 1 - e^{-(t/\lambda)^k}$$

**Hazard rate:**

$$h(t) = \frac{k}{\lambda}\left(\frac{t}{\lambda}\right)^{k-1}$$

**Mean and variance:**

$$\mathbb{E}[T] = \lambda\,\Gamma\!\left(1 + \frac{1}{k}\right), \qquad \text{Var}(T) = \lambda^2\!\left[\Gamma\!\left(1+\frac{2}{k}\right) - \Gamma\!\left(1+\frac{1}{k}\right)^2\right]$$

## Example

Mortgage defaults: empirical evidence shows default rates increase in the first 3 years then decline — the so-called **seasoning curve**. This is captured by a Weibull with $k \approx 2.5$ (increasing then decreasing hazard from a mixture) fitted to loan survival data.

With $k = 2$, $\lambda = 5$ years: $\mathbb{E}[T] = 5\,\Gamma(1.5) = 5 \times 0.886 = 4.43$ years; hazard increases linearly in $t$ — riskier as the loan ages (up to the peak period).

## Remember

The Weibull distribution is used in **credit risk survival analysis** to model time to default when the hazard rate is not constant. Unlike the constant-hazard exponential, the Weibull can capture **vintage effects** in mortgage and consumer credit: newly originated loans have low early default rates, which rise as poorly underwritten loans self-identify, then fall as remaining loans have proven their quality. The **accelerated failure time (AFT) model** uses Weibull regression to incorporate covariate effects on loan survival, allowing credit analysts to adjust default timing estimates for loan characteristics such as LTV ratio and borrower credit score.
