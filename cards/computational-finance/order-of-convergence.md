# Order of Convergence

**Topic:** Computational Finance
**Tags:** convergence rate, grid refinement, discretisation error, model validation, pde pricing, numerical accuracy
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

The order of convergence $p$ is the power of the step size at which a numerical scheme's error vanishes as the grid is refined. Measuring $p$ empirically — by repricing the same instrument on successively finer grids — is how a quant proves that a pricing error is discretisation noise rather than a bug or a modelling failure.

## Key Formula

The error of a scheme with step size $h$ behaves asymptotically as

$$\varepsilon(h) = \lvert V_h - V_{\text{exact}}\rvert \approx C h^{p}$$

Halving the step and taking the ratio eliminates the unknown constant $C$:

$$p \approx \log_2\!\left(\frac{\varepsilon(2h)}{\varepsilon(h)}\right)$$

When no exact value exists, use three successive grids and the differences between them:

$$p \approx \log_2\!\left(\frac{V_{4h} - V_{2h}}{V_{2h} - V_{h}}\right)$$

Expected orders: explicit and fully implicit time-stepping $p = 1$, Crank-Nicolson $p = 2$, centred spatial differences $p = 2$, Monte Carlo $p = \tfrac{1}{2}$ in the number of paths.

## Example

Reprice a European call by Crank-Nicolson against its Black-Scholes value of \$10.4506, halving both $\Delta S$ and $\Delta t$ each time:

| Steps | Price | Error | Ratio |
|---|---|---|---|
| 50 | 10.4102 | 0.0404 | — |
| 100 | 10.4404 | 0.0102 | 3.96 |
| 200 | 10.4480 | 0.0026 | 3.92 |
| 400 | 10.4499 | 0.0007 | 3.71 |

$$p \approx \log_2(3.96) = 1.99$$

The error falls by a factor of four each refinement, confirming the expected second order. Had the ratio come out near 2 instead of 4, that would point to a first-order defect — most often a boundary condition or a payoff kink left unsmoothed.

## Remember

A convergence table is the single most persuasive piece of evidence in a numerical pricing report, and it is diagnostic rather than decorative. If the measured order falls short of the theoretical one, the scheme is being held back by its weakest component — an $O(h)$ one-sided boundary stencil, a discontinuous payoff, or an early-exercise constraint — and refining further wastes computation. In a local volatility study the table serves a specific purpose: once repricing errors are shown to converge at the expected rate, any residual mismatch between the model's vanilla prices and the market quotes must be attributed to the surface fit and regularisation, not to the PDE solver. Note also that the ratio only holds in the asymptotic regime; on very coarse grids, or once round-off dominates on very fine ones, the estimate for $p$ degrades.
