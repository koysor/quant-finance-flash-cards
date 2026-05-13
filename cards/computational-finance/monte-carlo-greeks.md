# Monte Carlo Greeks

**Topic:** Computational Finance
**Tags:** python, monte carlo, greeks, pathwise, likelihood ratio, sensitivities, hedging
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Monte Carlo Greeks are methods for computing option price sensitivities (delta, vega, gamma, etc.) from simulation without re-pricing the option at shifted parameters. Two main approaches exist: the **pathwise method** (differentiates the payoff through the simulation paths) and the **likelihood ratio method** (differentiates the probability density instead of the path).

## Key Formula

**Pathwise (infinitesimal perturbation analysis):**

$$\Delta = \frac{\partial C}{\partial S_0} = \mathbb{E}^{\mathbb{Q}}\!\left[\frac{\partial}{\partial S_0} \text{payoff}(S_T)\right] = \mathbb{E}^{\mathbb{Q}}\!\left[\mathbb{1}_{S_T > K} \cdot \frac{S_T}{S_0}\right]$$

Valid when the payoff is differentiable (European, Asian). Implemented in code:

```python
# Pathwise delta for a European call
ST = S0 * np.exp((r - 0.5*sig**2)*T + sig*np.sqrt(T)*Z)  # Z ~ N(0,1)
delta = np.mean((ST > K) * ST / S0) * np.exp(-r * T)
```

**Likelihood ratio (score function):**

$$\Delta = \mathbb{E}^{\mathbb{Q}}\!\left[\text{payoff}(S_T) \cdot \frac{\partial \ln p(S_T; S_0)}{\partial S_0}\right]$$

Valid for **any** payoff including discontinuous ones (digital options, barriers):

```python
score = (np.log(ST / S0) - (r - 0.5*sig**2)*T) / (sig**2 * T * S0)
delta_lr = np.exp(-r * T) * np.mean(payoff * score)
```

## Example

Price a digital call (payoff = £1 if $S_T > 100$) with $S_0 = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ yr. The pathwise method fails — the payoff is a step function with zero derivative almost everywhere. The likelihood ratio method gives:

```python
Z  = np.random.randn(100_000)
ST = 100 * np.exp((0.05 - 0.02)*1 + 0.20*Z)
payoff = (ST > 100).astype(float)
score  = (np.log(ST/100) - 0.03) / (0.04 * 100)
delta  = np.exp(-0.05) * np.mean(payoff * score)  # ≈ 0.043
```

## Remember

Finite-difference Greeks (re-pricing at $S_0 \pm \varepsilon$) require two full simulations per Greek and suffer from numerical noise at small $\varepsilon$. Pathwise and likelihood ratio methods compute all Greeks from a **single simulation run**, dramatically reducing cost for high-dimensional products (basket options, path-dependent exotics) where re-running the simulation is expensive. The choice between them hinges on payoff differentiability: pathwise for smooth payoffs, likelihood ratio for digital or barrier payoffs.
