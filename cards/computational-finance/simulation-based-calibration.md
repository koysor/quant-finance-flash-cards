# Simulation-Based Calibration

**Topic:** Computational Finance
**Tags:** calibration, monte carlo, parameter estimation, stochastic model, simulation, optimisation
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Simulation-based calibration fits a parametric stochastic model to market data by repeatedly running Monte Carlo simulations at candidate parameter values and choosing the parameters that minimise the discrepancy between simulated and observed statistics.

## Key Formula

The calibration problem is an optimisation over model parameters $\theta$:

$$\theta^* = \arg\min_{\theta} \sum_{i=1}^{N} w_i \bigl(f_i^{\text{sim}}(\theta) - f_i^{\text{market}}\bigr)^2$$

where $f_i^{\text{market}}$ are observed market statistics (option prices, implied volatilities, moments) and $f_i^{\text{sim}}(\theta)$ are their counterparts estimated from $M$ simulated paths. Each evaluation of $f_i^{\text{sim}}(\theta)$ requires running $M$ Monte Carlo paths:

$$f_i^{\text{sim}}(\theta) \approx \frac{1}{M}\sum_{j=1}^{M} g_i\!\left(S^{(j)}(\theta)\right)$$

## Example

Calibrating a Heston model to 30 vanilla option prices: for each trial $(\kappa, \theta_v, \xi, \rho, v_0)$, 50,000 paths are simulated and option prices extracted. Gradient-free optimisers (Nelder-Mead or Bayesian optimisation) navigate the 5-dimensional parameter space. Starting from a sensible initial guess, the calibration converges in ~200 evaluations, each taking 0.5 seconds — a total of 100 seconds versus 3 hours for a naïve grid search.

## Remember

Simulation-based calibration is the method of choice when no closed-form pricing formula exists for the target model (e.g. stochastic local volatility, rough volatility). The cost is computational: each loss evaluation requires thousands of simulation paths, so efficiency hinges on fast Monte Carlo engines or surrogate models (such as neural-network calibration) that replace the simulation with a pre-trained approximation for online calibration.
