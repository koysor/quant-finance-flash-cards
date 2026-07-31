# Semimartingale

**Topic:** Stochastic Processes
**Tags:** semimartingale, local martingale, finite variation, stochastic integration, ito calculus, decomposition
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

A **semimartingale** is a stochastic process $X$ that can be decomposed as $X = M + A$, where $M$ is a local martingale and $A$ is a process of locally finite variation (i.e. its paths have bounded total variation on every compact interval). Semimartingales are precisely the class of processes for which the Itô stochastic integral is well-defined, making them the natural domain of stochastic calculus.

## Key Formula

The canonical decomposition is:

$$X_t = X_0 + M_t + A_t$$

where $M_0 = A_0 = 0$, $M$ is a local martingale, and $A$ has paths of finite variation. For a continuous semimartingale driven by Brownian motion, this takes the familiar SDE form:

$$dX_t = \underbrace{\sigma_t\,dW_t}_{\text{martingale part}} + \underbrace{\mu_t\,dt}_{\text{finite-variation part}}$$

Itô's lemma for a smooth function $f$ applied to a continuous semimartingale $X$ gives:

$$df(X_t) = f'(X_t)\,dX_t + \tfrac{1}{2}f''(X_t)\,d[X,X]_t$$

## Example

Consider the Vasicek short-rate model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$. Here $r_t$ is a semimartingale with:
- **Martingale part:** $M_t = \sigma W_t$ (Brownian integral, zero-drift)
- **Finite-variation part:** $A_t = \int_0^t \kappa(\theta - r_s)\,ds$ (Riemann integral of the mean-reversion drift)

With $\kappa = 0.5$, $\theta = 0.03$, $\sigma = 0.01$, $r_0 = 0.02$: over one year the drift contributes $\approx 0.5 \times 0.01 \times 1 = 0.005$ in expectation, while the martingale part adds random noise with standard deviation $0.01$.

## Remember

The semimartingale framework matters in quantitative finance because it is the minimal structure required for a price process to admit a consistent no-arbitrage theory. The fundamental theorem of asset pricing (in its modern form due to Delbaen and Schachermayer) states that a price process is locally arbitrage-free if and only if it is a semimartingale under some equivalent probability measure. Processes that are not semimartingales — such as fractional Brownian motion with Hurst exponent $H \ne \frac{1}{2}$ — allow arbitrage when used naively as price models, which is why rough volatility models require special non-standard integration theories.
