# Ergodic Theorem

**Topic:** Stochastic Processes
**Tags:** ergodicity, stationary process, time average, ensemble average, Monte Carlo, law of large numbers
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

For an ergodic stationary process, the time average of any integrable function of the process converges almost surely to its expectation under the stationary distribution as the observation period grows without bound. In plain terms: one long path and many independent realisations give the same statistical information.

## Key Formula

$$\frac{1}{T} \int_0^T f(X_t)\, dt \xrightarrow{a.s.} \mathbb{E}_\pi[f(X)] \quad \text{as } T \to \infty$$

where $\pi$ is the stationary distribution of $X$. The discrete version for a time series $(X_1, X_2, \ldots, X_n)$ is:

$$\frac{1}{n} \sum_{k=1}^n f(X_k) \xrightarrow{a.s.} \mathbb{E}_\pi[f(X)]$$

Ergodicity requires irreducibility (the process can reach any state) and positive recurrence (it returns to any state in finite expected time).

## Example

Consider an Ornstein–Uhlenbeck short-rate process $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ with $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$. Simulate a single path for $T = 200$ years and compute the running mean. By the ergodic theorem, the sample mean $\frac{1}{T}\int_0^T r_t\,dt$ converges to $\theta = 4\%$ — the same answer you would obtain by averaging over thousands of independent paths at a single time.

## Remember

Historical volatility estimation implicitly assumes ergodicity: computing $\hat{\sigma}^2 = \frac{1}{n}\sum_{k=1}^n (\log S_{k} - \log S_{k-1})^2$ from one historical price path is only valid if the return process is ergodic. When markets undergo structural breaks or regime shifts, the process is non-ergodic and past data can systematically misrepresent future behaviour — a key source of model risk in risk management.
