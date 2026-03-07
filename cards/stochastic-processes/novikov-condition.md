# Novikov Condition

**Topic:** Stochastic Processes
**Tags:** martingale, exponential, girsanov, measure change, integrability
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Novikov condition** is a sufficient condition guaranteeing that an exponential local martingale is a true martingale. It ensures that the process $\theta(t)$ used in a change of measure does not grow too fast, so that the resulting Radon–Nikodým derivative is well-behaved and defines a proper probability measure.

## Key Formula

A process $\theta(t)$ satisfies the Novikov condition if:

$$E\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty$$

When satisfied, the exponential martingale:

$$M_t^{\theta} = \exp\!\left(-\int_0^t \theta_s\,dX_s - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)$$

is a **true martingale** with $E[M_t^{\theta}] = 1$.

## Example

For the Black–Scholes model with constant market price of risk $\theta = (\mu - r)/\sigma$:

$$\frac{1}{2}\int_0^T \theta^2\,ds = \frac{(\mu - r)^2}{2\sigma^2}\,T$$

This is finite for any finite $T$, so $\exp\!\left(\frac{(\mu - r)^2}{2\sigma^2}\,T\right) < \infty$ and the Novikov condition holds trivially. Girsanov's theorem applies.

## Remember

The Novikov condition is the technical safeguard that validates Girsanov's theorem and hence risk-neutral pricing. Without it, the exponential process used to define the risk-neutral measure might only be a local martingale — meaning $E[M_t^{\theta}]$ could be less than 1, and $\mathbb{Q}$ would not be a proper probability measure. In standard models with deterministic or bounded market prices of risk, the condition is easily satisfied. It becomes a genuine concern in models with stochastic volatility or explosive drift, where the market price of risk can grow without bound and the change of measure may fail.
