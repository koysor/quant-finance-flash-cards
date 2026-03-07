# Convergence Notation

**Topic:** Mathematical Notation
**Tags:** notation, convergence, distribution, probability, asymptotic
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Convergence notation** distinguishes the different ways in which a sequence of random variables can approach a limit. Each arrow type encodes a different strength of convergence, from weakest (in distribution) to strongest (almost sure).

| Symbol | Read as | Meaning |
|---|---|---|
| $X_n \xrightarrow{d} X$ | "converges in distribution" | CDFs converge: $F_{X_n}(x) \to F_X(x)$ at continuity points |
| $X_n \xrightarrow{p} X$ | "converges in probability" | $P(\|X_n - X\| > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| $X_n \xrightarrow{a.s.} X$ | "converges almost surely" | $P(\lim_{n\to\infty} X_n = X) = 1$ |
| $X_n \xrightarrow{L^2} X$ | "converges in $L^2$" / "in mean square" | $E[(X_n - X)^2] \to 0$ |
| $X \sim N(\mu, \sigma^2)$ | "$X$ is distributed as" | $X$ follows a normal distribution with mean $\mu$, variance $\sigma^2$ |
| $X \approx Y$ | "$X$ is approximately equal to $Y$" | Numerical approximation (not a formal mode) |

## Key Formula

**Central Limit Theorem** (convergence in distribution):

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty$$

**Law of Large Numbers** (convergence in probability / almost surely):

$$\bar{X}_n \xrightarrow{p} \mu \quad \text{as } n \to \infty$$

**Implication hierarchy:**

$$\xrightarrow{a.s.} \;\Rightarrow\; \xrightarrow{p} \;\Rightarrow\; \xrightarrow{d}$$

$$\xrightarrow{L^2} \;\Rightarrow\; \xrightarrow{p} \;\Rightarrow\; \xrightarrow{d}$$

## Example

A Monte Carlo simulation estimates $E[e^{-rT}\max(S_T - K, 0)]$ using $n$ paths. The sample mean $\bar{V}_n$ satisfies:

- $\bar{V}_n \xrightarrow{a.s.} V$ (strong law of large numbers — the estimate converges path by path)
- $\sqrt{n}(\bar{V}_n - V)/s \xrightarrow{d} N(0, 1)$ (CLT — the error is approximately normal for large $n$)

With $n = 10{,}000$ paths and $s = £2.50$: the 95% confidence interval has half-width $1.96 \times 2.50 / \sqrt{10000} = £0.049$.

## Remember

The type of convergence arrow tells you how reliable a limit result is. In Monte Carlo pricing, $\xrightarrow{a.s.}$ guarantees the estimator will eventually be correct for any single simulation run, while $\xrightarrow{d}$ gives the distribution of the error for confidence intervals. The distinction matters when validating numerical methods: convergence in distribution (the weakest form) is sufficient for the CLT to justify confidence intervals, but convergence in probability is needed for consistent estimators, and almost-sure convergence is required to guarantee that a single long simulation will produce the right answer.
