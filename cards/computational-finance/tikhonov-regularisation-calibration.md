# Tikhonov Regularisation in Yield-Curve Calibration

**Topic:** Computational Finance
**Tags:** Tikhonov regularisation, yield curve, ill-conditioning, calibration, inverse problem, smoothing, Ho-Lee, spline, numerical stability
**Created:** 2026-06-14
**Author:** Claude Sonnet 4.6

---

## Definition

The Ho-Lee calibration formula $\eta^*(t) = c^2(t-t^*) - \partial_{tt}\log Z_M$ requires the **second derivative of the log discount factor from noisy market data**. Small bid-ask spreads in bond prices cause large oscillations in $\eta^*(t)$, making the raw formula numerically unstable. Tikhonov regularisation suppresses these oscillations by penalising the roughness of $\eta^*(t)$.

## Key Formula

Replace the exact-fit constraint with a penalised least-squares objective:

$$\min_\eta \;\underbrace{\sum_i\!\bigl(Z_{model}(\eta;\,T_i) - Z_M(T_i)\bigr)^2}_{\text{data fit}} + \lambda\;\underbrace{\int_0^T\!\bigl(\eta'(t)\bigr)^2\,dt}_{\text{roughness penalty}}$$

where $\lambda > 0$ is the **regularisation parameter**:

| $\lambda$ | Effect |
|---|---|
| $\lambda \to 0$ | Exact fit — oscillatory, noise-sensitive $\eta(t)$ |
| $\lambda \to \infty$ | Constant $\eta$ — maximum smoothness, poor fit |

The most common practical implementation fits a **cubic spline** to market discount factors first, then differentiates the smooth spline analytically. This is equivalent to implicit Tikhonov regularisation.

## Example

Ten bond prices observed with 0.5 bp bid-ask noise. Raw finite differences of $\log Z_M$ at monthly resolution give $\eta(t)$ swinging between $-8\%$ and $+6\%$ — economically implausible. Fitting a cubic spline to the same ten prices, then differentiating analytically, gives a smoothly varying $\eta(t) \in [-1\%, 3\%]$ — consistent with observed forward-rate curvature.

## Remember

Calibration is an **ill-posed inverse problem**: differentiating noisy data amplifies errors at a rate proportional to the square of the frequency. Tikhonov regularisation is the standard remedy. In yield-curve work it usually appears as pre-smoothing (Nelson-Siegel fit, cubic spline, or parametric discount curve) before extracting forward rates — never differencing raw market quotes directly.
