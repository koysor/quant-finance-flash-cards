# Itô Isometry

**Topic:** Stochastic Processes
**Tags:** stochastic integral, variance, brownian motion, expectation, quadratic variation
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Itô isometry** converts the expected value of a squared Itô integral into an ordinary (Lebesgue) integral. Since Itô integrals have zero mean, their variance equals $E[I^2]$, so the isometry is the primary tool for computing variances of stochastic integrals.

## Key Formula

$$E\!\left[\left(\int_0^T f(t)\,dX_t\right)^{\!2}\right] = E\!\left[\int_0^T f(t)^2\,dt\right]$$

| Left side | Right side |
|---|---|
| Expected square of a stochastic integral | Ordinary integral of the squared integrand |

If $f$ is deterministic, the right side simplifies to $\int_0^T f(t)^2\,dt$.

## Example

Compute the variance of $I = \int_0^T t\,dX_t$ where $X_t$ is standard Brownian motion.

Since $E[I] = 0$ (Itô integral), $\text{Var}(I) = E[I^2]$. By the Itô isometry with $f(t) = t$:

$$\text{Var}(I) = \int_0^T t^2\,dt = \frac{T^3}{3}$$

For $T = 1$: $\text{Var}(I) = 1/3 \approx 0.333$.

## Remember

The Itô isometry is essential for quantifying hedging error and portfolio variance in continuous-time finance. When a trader's hedging strategy involves a stochastic integral $\int_0^T \Delta_t \sigma S_t\,dW_t$, the variance of the hedging P&L is computed via the isometry as $\int_0^T E[\Delta_t^2 \sigma^2 S_t^2]\,dt$. This transforms a difficult stochastic calculation into a tractable deterministic integral, enabling quants to evaluate how much risk remains in a dynamically hedged portfolio — particularly when hedging is discrete rather than continuous.
