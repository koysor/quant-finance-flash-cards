# Law and Distribution Notation

**Topic:** Mathematical Notation
**Tags:** distribution, law, convergence, notation, probability, asymptotic theory
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

**Law notation** specifies how a random variable is distributed or how sequences of random variables behave as sample size grows. These symbols are ubiquitous in statistical finance: asserting that log-returns are normally distributed, proving that a sample mean converges to a true mean, or stating that an estimator is consistent.

| Symbol | Read as | Meaning |
|---|---|---|
| $X \sim \mathcal{N}(\mu, \sigma^2)$ | "X is distributed as normal" | $X$ has a normal distribution with mean $\mu$, variance $\sigma^2$ |
| $\mathcal{L}(X)$ | "law of X" | The probability distribution of $X$; same as the distribution of $X$ |
| $X \overset{d}{=} Y$ | "X equals Y in distribution" | $X$ and $Y$ have the same distribution (need not be equal as r.v.s) |
| $X_n \overset{d}{\to} X$ | "converges in distribution" | CDFs converge: $F_{X_n}(x) \to F_X(x)$ — also written $X_n \Rightarrow X$ |
| $X_n \overset{p}{\to} X$ | "converges in probability" | $P(\lvert X_n - X\rvert > \varepsilon) \to 0$ for all $\varepsilon > 0$ |
| $X_n \overset{a.s.}{\to} X$ | "converges almost surely" | $P(\lim_{n\to\infty} X_n = X) = 1$ — the strongest mode |

## Key Formula

**Central limit theorem** in law notation:

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \overset{d}{\to} \mathcal{N}(0,1) \quad \text{as } n \to \infty$$

**Hierarchy of convergence** (each implies the one below):

$$\overset{a.s.}{\to} \implies \overset{p}{\to} \implies \overset{d}{\to}$$

## Example

Daily log-returns $r_1, \ldots, r_n$ are assumed i.i.d. with $r_i \sim \mathcal{N}(0.0003, \, 0.01^2)$. This says each return is drawn independently from the same normal distribution. If instead returns have fat tails, we might write $r_i \sim t_\nu$ (Student's $t$ with $\nu$ degrees of freedom). The CLT then tells us: even if $r_i \sim t_\nu$, the monthly average $\bar{r}_n \overset{d}{\to} \mathcal{N}(\mu, \sigma^2/n)$ as $n \to \infty$ — justifying normal approximations for aggregated returns.

## Remember

The distinction between $\overset{d}{=}$ (same distribution) and $=$ (same random variable) matters in derivatives. Two different stocks can each follow $\mathcal{N}(0, \sigma^2)$ increments — they are equal in distribution — but are not the same Brownian motion. Convergence in distribution ($\overset{d}{\to}$) is the weakest mode and is sufficient for the CLT and for justifying asymptotic confidence intervals in risk model backtesting. Convergence almost surely ($\overset{a.s.}{\to}$) is required for the strong law of large numbers, which underpins Monte Carlo convergence proofs.
