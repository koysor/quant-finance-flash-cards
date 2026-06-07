# Quasi-Monte Carlo

**Topic:** Computational Finance
**Tags:** quasi-monte carlo, low discrepancy, sobol sequence, variance reduction, option pricing, numerical integration
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Quasi-Monte Carlo (QMC)** replaces the pseudo-random samples used in standard Monte Carlo simulation with **low-discrepancy sequences** — deterministic point sets designed to cover the integration domain more uniformly than random samples. Because the points fill space more evenly, QMC achieves a convergence rate of $O((\log N)^d / N)$ compared to the $O(1/\sqrt{N})$ of standard Monte Carlo, delivering the same accuracy with fewer paths in low-to-moderate dimensions.

## Key Formula

**Standard Monte Carlo** error (random samples, $N$ paths, $d$ dimensions):

$$\text{error} \propto \frac{1}{\sqrt{N}}$$

**Quasi-Monte Carlo** error (Sobol or Halton sequence, $N$ points):

$$\text{error} \propto \frac{(\log N)^d}{N}$$

For $d = 5$ dimensions and $N = 10{,}000$ paths, QMC error is roughly $10\times$ smaller than MC error at the same path count. The advantage shrinks as $d$ grows — QMC is most beneficial for $d \lesssim 20$ effective dimensions.

A **Sobol sequence** in 1D fills $[0,1]$ by successively halving intervals, so the first four points are $\{0.5,\, 0.25,\, 0.75,\, 0.125\}$ — never clustering.

## Example

Pricing a 5-asset basket call (payoff = $\max(\bar{S}_T - K, 0)$) with $N = 4{,}096$ paths:

| Method | Paths | Price estimate | Std error |
|---|---|---|---|
| Monte Carlo | 4,096 | £8.43 | ±£0.18 |
| Quasi-Monte Carlo (Sobol) | 4,096 | £8.47 | ±£0.02 |
| Monte Carlo | 65,536 | £8.45 | ±£0.05 |

QMC with 4,096 paths matches the accuracy of MC with 65,536 paths — a 16× reduction in computation for this 5-dimensional problem. The true price (binomial benchmark) is £8.46.

## Remember

QMC is the first optimisation to apply when a Monte Carlo pricer is too slow: it costs nothing in implementation complexity — just replace `numpy.random.uniform` with a Sobol generator — and typically cuts the required path count by one to two orders of magnitude for low-dimensional products such as European baskets, Asian options, and spread options. The catch is **effective dimension**: a 30-step path-dependent option has $d = 30$ dimensions, and standard Sobol sequences lose their uniformity advantage in high dimensions. Practitioners address this with **Brownian bridge construction** or **principal component analysis** of the covariance matrix, which concentrates most of the variance into the first few dimensions so QMC retains its edge. Regulatory Monte Carlo (e.g., CVA under SA-CVA) often specifies pseudo-random sampling for reproducibility and auditability, so QMC is used internally for speed but the regulatory submission uses standard MC with a fixed seed.
