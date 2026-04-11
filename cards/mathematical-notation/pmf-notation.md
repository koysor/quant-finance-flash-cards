# Probability Mass Function Notation

**Topic:** Mathematical Notation
**Tags:** notation, PMF, discrete distribution, probability mass, support
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **probability mass function (PMF)** gives the probability that a discrete random variable takes each specific value. The notation parallels PDF notation for continuous variables but applies to countable outcomes.

| Symbol | Read as | Meaning |
|---|---|---|
| $p_X(k)$ | "PMF of X at k" | $P(X = k)$ — the probability $X$ equals $k$ |
| $p(k)$ | "p of k" | Shorthand when the random variable is clear from context |
| $P(X = k)$ | "probability X equals k" | Explicit event notation, equivalent to $p_X(k)$ |
| $p_i$ | "p sub i" | PMF value at the $i$-th support point |
| $\text{supp}(X)$ | "support of X" | The set of values $k$ where $p_X(k) > 0$ |

## Key Formula

**PMF properties:**

$$p_X(k) \geq 0 \quad \text{for all } k, \qquad \sum_{k \in \text{supp}(X)} p_X(k) = 1$$

**Expectation from PMF:**

$$E[X] = \sum_{k} k \cdot p_X(k)$$

**PMF vs PDF:**

| | PMF $p_X(k)$ | PDF $f_X(x)$ |
|---|---|---|
| Random variable | Discrete | Continuous |
| Values | Probabilities: $P(X=k) \in [0,1]$ | Density: $f_X(x) \geq 0$, can exceed 1 |
| Sum/Integral | $\sum_k p_X(k) = 1$ | $\int f_X(x)\,dx = 1$ |
| Point probability | $P(X = k) = p_X(k)$ | $P(X = x) = 0$ for any single $x$ |

## Example

Binomial($n=3$, $p=0.5$): $p_X(k) = \binom{3}{k}(0.5)^3$ for $k \in \{0, 1, 2, 3\}$.

$p_X(0) = 1/8$, $p_X(1) = 3/8$, $p_X(2) = 3/8$, $p_X(3) = 1/8$. Sum: $8/8 = 1 \checkmark$

In a binomial option pricing tree with $n=3$ steps, $p_X(k)$ is the probability the stock reaches the $k$-th price node at expiry.

## Remember

The key difference from PDF notation: for a discrete RV, $p_X(k) = P(X = k)$ is an actual probability (between 0 and 1), whereas for a continuous RV, $f_X(x)\,dx$ is a probability for an infinitesimal interval and $f_X(x)$ itself can exceed 1. Mixing up PMF and PDF — treating a density as a probability — is a common error when reading statistical formulas in finance.
