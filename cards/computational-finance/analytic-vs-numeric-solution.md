# Analytic vs Numeric Solution

**Topic:** Computational Finance
**Tags:** analytic solution, numerical methods, closed-form, monte carlo, accuracy, option pricing
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

An **analytic (closed-form) solution** expresses the answer as a single formula evaluated in finite steps, with no approximation error. A **numerical solution** approximates the answer by iterative or simulation-based computation, trading exactness for generality — it can tackle problems where no closed-form formula exists.

## Key Formula

**Black-Scholes analytic call price** (exact, evaluated once):

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

**Monte Carlo numeric estimate** (approximate, improves with sample size $N$):

$$\hat{C} = e^{-rT} \frac{1}{N} \sum_{i=1}^{N} \max(S_T^{(i)} - K,\, 0)$$

Standard error of the Monte Carlo estimate scales as:

$$\text{SE} = \frac{\hat{\sigma}_{\text{payoff}}}{\sqrt{N}}$$

so quadrupling $N$ halves the error — a $1/\sqrt{N}$ convergence rate.

## Example

Price a European call with $S_0 = £100$, $K = £100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year:

| Method | Price | Time | Error |
|---|---|---|---|
| Black-Scholes (analytic) | £10.45 | < 1 ms | exact |
| Monte Carlo, $N = 1{,}000$ | £10.63 | ~10 ms | ±£1.20 |
| Monte Carlo, $N = 1{,}000{,}000$ | £10.46 | ~1 s | ±£0.04 |

For this simple payoff, the analytic formula is faster by several orders of magnitude and exact. Monte Carlo matches only at very large $N$.

## Remember

The choice between analytic and numeric methods is one of the most important decisions in quantitative finance. Analytic solutions (Black-Scholes, put-call parity, bond pricing) are preferred wherever they exist because they are instant, exact, and differentiable — you can compute Greeks analytically at no extra cost. Numerical methods (Monte Carlo, finite-difference PDE solvers, binomial trees) become essential for path-dependent exotics, American options, and multi-asset products where no closed form exists. In practice, quants use analytic solutions to validate and benchmark their numerical engines before deploying them on harder problems.
