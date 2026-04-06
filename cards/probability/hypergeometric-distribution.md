# Hypergeometric Distribution

**Topic:** Probability
**Tags:** hypergeometric, sampling without replacement, finite population, credit pool
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **hypergeometric distribution** models the number of successes in $n$ draws taken **without replacement** from a finite population of size $N$ containing $K$ successes. Unlike the binomial (which assumes independent draws with replacement), the hypergeometric accounts for the fact that each draw changes the composition of the remaining pool.

## Key Formula

**PMF:**

$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n+K-N) \leq k \leq \min(n,K)$$

**Mean and variance:**

$$\mathbb{E}[X] = n\frac{K}{N}, \qquad \text{Var}(X) = n\frac{K}{N}\cdot\frac{N-K}{N}\cdot\frac{N-n}{N-1}$$

**Finite population correction factor (FPC):** $\sqrt{\dfrac{N-n}{N-1}}$ — the factor by which the hypergeometric standard deviation is smaller than the binomial.

**Binomial limit:** when $N \gg n$, hypergeometric $\approx B(n, K/N)$ since the FPC $\approx 1$.

## Example

A credit pool contains 100 bonds, 10 of which are below investment grade. A reviewer samples 20 bonds without replacement. Find the probability of selecting exactly 3 sub-investment-grade bonds.

$$P(X=3) = \frac{\binom{10}{3}\binom{90}{17}}{\binom{100}{20}} \approx 0.196, \quad \mathbb{E}[X] = 20 \times \frac{10}{100} = 2$$

## Remember

The hypergeometric distribution is relevant in **credit portfolio sampling** and **regulatory review processes** — when an auditor samples $n$ loans from a finite pool to estimate the fraction that are non-compliant, the correct model is hypergeometric, not binomial. The FPC shows that larger samples from small populations are more efficient than the binomial would suggest: sampling 50% of a 100-loan portfolio gives you far more information than sampling 50 loans from an infinite population. In practice, the binomial approximation is used when the population is large relative to the sample, which covers most quant finance applications.
