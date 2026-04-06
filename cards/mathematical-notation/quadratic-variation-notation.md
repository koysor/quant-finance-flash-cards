# Quadratic Variation Notation

**Topic:** Mathematical Notation
**Tags:** notation, quadratic variation, covariation, bracket notation, Ito calculus, Brownian motion
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

**Quadratic variation** measures the total accumulated squared fluctuation of a stochastic process. The bracket notation is standard:

| Symbol | Read as | Meaning |
|---|---|---|
| $[X]_t$ or $\langle X \rangle_t$ | "quadratic variation of $X$ up to $t$" | $\lim \sum (X_{t_{i+1}} - X_{t_i})^2$ over partitions |
| $[X, Y]_t$ or $\langle X, Y \rangle_t$ | "quadratic covariation of $X$ and $Y$" | $\lim \sum (X_{t_{i+1}} - X_{t_i})(Y_{t_{i+1}} - Y_{t_i})$ |
| $[W]_t = t$ | "quadratic variation of Brownian motion" | The defining property $dW_t^2 = dt$ |
| $(dW_t)^2 = dt$ | Itô multiplication rule | Informal shorthand for the quadratic variation result |

The **angle bracket** $\langle X \rangle_t$ denotes the **predictable** quadratic variation (compensator), while the **square bracket** $[X]_t$ denotes the **realised** quadratic variation. In continuous processes (like Brownian motion) they coincide.

## Key Formula

**Brownian motion quadratic variation:**

$$[W, W]_t = t$$

**Itô's lemma** (using bracket notation):

$$df(X_t) = f'(X_t)\,dX_t + \tfrac{1}{2}f''(X_t)\,d[X]_t$$

**Realised variance** estimator (discrete approximation):

$$\text{RV}_T = \sum_{i=1}^{n} (r_{t_i})^2 \approx [X]_T, \qquad r_{t_i} = \ln S_{t_i} - \ln S_{t_{i-1}}$$

## Example

For a GBM $S_t$ with $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, the log-price $X_t = \ln S_t$ has quadratic variation:

$$[X]_t = \sigma^2 t$$

This is estimated in practice by **realised variance** — summing squared log returns over fine time intervals. As the sampling frequency increases, the realised variance converges to the true $\sigma^2 t$, forming the basis of volatility estimation from high-frequency data without needing a parametric model.

## Remember

The identity $[W]_t = t$ is the single most important property of Brownian motion in finance. It is the reason why Itô's lemma requires a second-order term that does not appear in ordinary calculus — the $\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}$ term in the Black-Scholes PDE comes directly from this quadratic variation. **Variance swaps** are contracts that pay the difference between realised variance $[X]_T$ and a fixed strike — the bracket notation maps directly to the product specification, making it the canonical instrument for trading volatility as a quantity in its own right.
