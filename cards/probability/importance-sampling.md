# Importance Sampling

**Topic:** Probability
**Tags:** importance sampling, variance reduction, likelihood ratio, rare events, monte carlo, tail risk
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Importance sampling** is a variance reduction technique that simulates from a different probability distribution $q$ (the **proposal**) rather than the true distribution $p$, then corrects each sampled value by multiplying by the **likelihood ratio** (or importance weight) $w(x) = p(x)/q(x)$. The estimator remains unbiased while its variance can be dramatically lower — especially for **rare-event** problems where the payoff is concentrated in a thin tail that standard simulation almost never visits.

## Key Formula

The fundamental identity — the expectation under $p$ can be computed by sampling under $q$:

$$\mathbb{E}_p[f(X)] = \mathbb{E}_q\!\left[f(X)\,\frac{p(X)}{q(X)}\right] = \mathbb{E}_q[f(X)\,w(X)]$$

The **importance-sampling Monte Carlo estimator** with $N$ draws $X_1,\ldots,X_N \sim q$:

$$\hat{\theta}_{\text{IS}} = \frac{1}{N}\sum_{i=1}^{N} f(X_i)\,w(X_i), \qquad w(X_i) = \frac{p(X_i)}{q(X_i)}$$

**Optimal proposal:** variance is zero when $q^*(x) \propto \lvert f(x)\rvert\, p(x)$ — concentrate samples where the integrand is largest. In practice $q^*$ is unknown, but choosing $q$ to mimic this shape dramatically reduces variance.

**For GBM under a drift shift** $\mu$ away from the risk-neutral drift $r$:

$$w(S_T) = \exp\!\left(-\theta W_T - \tfrac{1}{2}\theta^2 T\right), \qquad \theta = \frac{\mu - r}{\sigma}$$

where $W_T$ is the simulated Brownian increment — this is the Radon-Nikodym derivative of $\mathbb{Q}$ with respect to the tilted measure.

## Example

Pricing a deep out-of-the-money put: $S_0 = 100$, $K = 60$, $r = 5\%$, $\sigma = 20\%$, $T = 1$. The risk-neutral probability of $S_T < 60$ is approximately 0.3% — in 10,000 crude MC paths, only ~30 paths contribute to the price estimate, giving a noisy result.

**Importance sampling:** shift the drift from $r = 5\%$ to $\mu = -20\%$ (pushing $S_T$ lower), simulate 10,000 paths under the tilted measure, and reweight each payoff by $w(S_T)$:

| Method | Paths | Std error |
|---|---|---|
| Crude MC | 10,000 | ±£0.018 |
| IS (drift $= -20\%$) | 10,000 | ±£0.002 |

IS achieves a 9× reduction in standard error at identical path count — equivalent to running 810,000 crude paths.

## Remember

Importance sampling is the standard technique for pricing **deep out-of-the-money options** and estimating **tail risk measures** such as Conditional VaR at the 99.9% confidence level, where crude Monte Carlo requires millions of paths to observe even a handful of loss events. In credit risk, IS is used to estimate the probability of a large-loss portfolio event by tilting default probabilities toward higher-correlation scenarios. The key practical challenge is choosing the proposal $q$ well: a poor choice (weights $w$ that occasionally become very large) can make IS perform *worse* than crude MC, with the estimator variance dominated by a few enormous weight realisations — a phenomenon called **weight degeneracy**. Practitioners guard against this by monitoring the **effective sample size** $N_{\text{eff}} = (\sum w_i)^2 / \sum w_i^2$; if $N_{\text{eff}} \ll N$, the proposal needs adjustment.
