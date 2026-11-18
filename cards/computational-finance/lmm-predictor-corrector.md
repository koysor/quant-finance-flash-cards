# Predictor–Corrector Drift in the LMM

**Topic:** Computational Finance
**Tags:** libor market model, predictor-corrector, monte carlo, drift, discretisation, log-euler
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

In a LIBOR market model the drift of each forward rate depends on the forward rates themselves, which change during a time step. A plain log-Euler step freezes the drift at its start-of-step value, which biases long steps. The predictor–corrector scheme first takes a trial step with the frozen drift (predictor), recomputes the drift at the predicted forwards, and then repeats the step with the average of the two drifts and the same random numbers (corrector).

## Key Formula

With drift $\mu_i(F)$, volatility $\sigma_i$ and standard Normal draw $Z_i$ over a step $\Delta t$:

$$\ln\hat{F}_i = \ln F_i(t) + \Big(\mu_i\big(F(t)\big) - \tfrac{1}{2}\sigma_i^2\Big)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i \qquad \text{(predictor)}$$

$$\ln F_i(t + \Delta t) = \ln F_i(t) + \Big(\tfrac{1}{2}\big[\mu_i(F(t)) + \mu_i(\hat{F})\big] - \tfrac{1}{2}\sigma_i^2\Big)\Delta t + \sigma_i\sqrt{\Delta t}\,Z_i \qquad \text{(corrector)}$$

Under the spot measure, for example, $\mu_i(F) = \sigma_i \sum_{j} \dfrac{\delta_j\,\rho_{ij}\,\sigma_j\,F_j}{1 + \delta_j F_j}$.

## Example

One forward with $F_0 = 5\%$, $\sigma = 20\%$, accrual $\delta = 0.5$, a single one-year step and $Z = 1$, with drift $\mu(F) = \sigma^2\delta F/(1 + \delta F)$:

- start drift $\mu(F_0) = 0.04 \times 0.5 \times 0.05 / 1.025 = 0.000976$
- predictor $\hat{F} = 0.05\,e^{0.000976 - 0.02 + 0.2} = 5.9919\%$
- drift at the prediction $\mu(\hat{F}) = 0.001164$; average $0.001070$
- corrector $F_1 = 0.05\,e^{0.001070 - 0.02 + 0.2} = 5.9925\%$

The correction is small for one forward, but it compounds across dozens of forwards and long steps.

## Remember

Predictor–corrector lets an LMM Monte Carlo jump straight to each payment date in one or a few long steps instead of many short ones, which is what makes pricing long-dated, path-dependent rate products (Bermudan swaptions, callable range accruals) affordable. Simple averaging of the drift is the same idea as Heun's method for ODEs, and it removes most of the bias of frozen-drift Euler for little extra cost.
