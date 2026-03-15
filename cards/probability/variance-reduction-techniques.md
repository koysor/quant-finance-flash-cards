# Variance Reduction Techniques

**Topic:** Probability
**Tags:** variance reduction, Monte Carlo, antithetic variates, control variates, simulation, efficiency
**Created:** 2026-03-15
**Author:** Claude Opus 4.6

---

## Definition

**Variance reduction techniques** are methods that lower the statistical error of a Monte Carlo estimate without increasing the number of simulated paths. By exploiting known structure in the problem — symmetry, correlations, or analytical results — these techniques produce tighter confidence intervals for the same computational budget. The most widely used methods are **antithetic variates**, **control variates**, and **importance sampling**.

## Key Formula

**Standard Monte Carlo estimator** for $\theta = E[f(X)]$:

$$\hat{\theta} = \frac{1}{N} \sum_{i=1}^{N} f(X_i), \qquad \operatorname{Var}(\hat{\theta}) = \frac{\sigma^2}{N}$$

**Antithetic variates:** pair each draw $Z_i$ with $-Z_i$ (exploiting symmetry of $N(0,1)$):

$$\hat{\theta}_{\text{AV}} = \frac{1}{N} \sum_{i=1}^{N} \frac{f(Z_i) + f(-Z_i)}{2}$$

$$\operatorname{Var}(\hat{\theta}_{\text{AV}}) = \frac{1}{N} \cdot \frac{\operatorname{Var}(f(Z)) + \operatorname{Cov}(f(Z), f(-Z))}{2}$$

When $f$ is monotonic (as most payoff functions are), $\operatorname{Cov}(f(Z), f(-Z)) < 0$, so variance falls — often by more than half.

**Control variates:** if $Y$ has known mean $E[Y] = \mu_Y$ and is correlated with $f(X)$:

$$\hat{\theta}_{\text{CV}} = \hat{\theta} - c\,(\bar{Y} - \mu_Y)$$

The optimal coefficient is $c^* = \operatorname{Cov}(f(X), Y) / \operatorname{Var}(Y)$, reducing variance by a factor of $1 - \rho^2$ where $\rho$ is the correlation between $f(X)$ and $Y$.

## Example

Price a European call ($K = 100$, $S_0 = 100$, $\sigma = 0.20$, $r = 0.05$, $T = 1$) using 10,000 paths. The crude Monte Carlo estimate has a standard error of £0.32.

**Antithetic variates:** for each $Z_i$, compute payoffs for both $Z_i$ and $-Z_i$, then average. The negative correlation between the paired payoffs reduces the standard error to £0.18 — a 44% reduction at no extra simulation cost.

**Control variates:** use the terminal stock price $S_T$ as a control (its risk-neutral mean $E[S_T] = S_0 e^{rT} = 105.13$ is known analytically). Regress the payoffs on $S_T$, subtract the correction, and the standard error drops to £0.09 — a 72% reduction.

## Remember

In production Monte Carlo engines, variance reduction is not optional — it is essential. Pricing an exotic derivative to two-decimal-place accuracy might require 10 million crude paths but only 500,000 with control variates, cutting computation time by 95%. Antithetic variates are trivially easy to implement (just negate the random draws), while control variates require identifying a correlated quantity with a known expectation — the discounted stock price or the Black-Scholes price of a simpler option are standard choices. The $1/\sqrt{N}$ convergence rate of Monte Carlo cannot be improved, but variance reduction effectively multiplies $N$ by a large factor for free.
