# Milstein Method

**Topic:** Stochastic Processes
**Tags:** Milstein, SDE, simulation, discretisation, numerical methods, strong convergence
**Created:** 2026-03-15
**Author:** Claude Opus 4.6

---

## Definition

The **Milstein method** is a numerical scheme for simulating stochastic differential equations that improves on the Euler-Maruyama method by adding a correction term involving the derivative of the diffusion coefficient. This extra term captures the effect of the diffusion's curvature and raises the strong convergence order from $O(\sqrt{\delta t})$ to $O(\delta t)$.

## Key Formula

For the general SDE $dS = a(S, t) \, dt + b(S, t) \, dW$, the Milstein discretisation is:

$$S_{i+1} = S_i + a(S_i, t_i) \, \delta t + b(S_i, t_i) \, \Delta W_i + \tfrac{1}{2} \, b(S_i, t_i) \, b'(S_i, t_i) \left(\Delta W_i^2 - \delta t\right)$$

where $\Delta W_i = \phi \sqrt{\delta t}$ with $\phi \sim \mathcal{N}(0,1)$, and $b'(S, t) = \frac{\partial b}{\partial S}$.

For GBM ($a = \mu S$, $b = \sigma S$, so $b' = \sigma$):

$$S_{i+1} = S_i \left[1 + \mu \, \delta t + \sigma \, \Delta W_i + \tfrac{1}{2} \sigma^2 \left(\Delta W_i^2 - \delta t\right)\right]$$

The correction term $\tfrac{1}{2} \sigma^2 (\Delta W_i^2 - \delta t)$ is exactly what distinguishes Milstein from Euler-Maruyama.

## Example

Simulate one step of GBM with $S_0 = 100$, $\mu = 0.05$, $\sigma = 0.20$, $\delta t = 0.01$, and $\phi = 0.73$:

$$\Delta W = 0.73 \times \sqrt{0.01} = 0.073$$

Euler-Maruyama part:

$$100(1 + 0.05 \times 0.01 + 0.20 \times 0.073) = 100 \times 1.0151 = 101.51$$

Milstein correction:

$$\tfrac{1}{2} \times 0.20^2 \times (0.073^2 - 0.01) = 0.02 \times (0.005329 - 0.01) = 0.02 \times (-0.004671) = -0.00009342$$

$$S_1 = 100 \times (1.0151 - 0.00009342) = \textbf{101.50}$$

The correction is small here, but over thousands of paths it systematically reduces the bias in path-dependent payoff estimates.

## Remember

The Milstein method matters most when the diffusion coefficient depends on the state variable (i.e. $b'(S) \neq 0$), which is the case for GBM and most interest rate models. For models with additive noise ($b' = 0$), such as the Vasicek model, the correction term vanishes and Milstein reduces to Euler-Maruyama. In practice, the improved strong convergence means Monte Carlo simulations of barrier options, lookbacks, and other path-dependent derivatives converge with fewer time steps, saving significant computation time.
