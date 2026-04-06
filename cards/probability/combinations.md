# Combinations

**Topic:** Probability
**Tags:** combinatorics, counting, binomial coefficient, permutations, probability
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A combination counts the number of ways to choose $k$ items from a set of $n$ distinct items where **order does not matter**. The result is written $\binom{n}{k}$ (read "n choose k") and is also called the **binomial coefficient**.

## Key Formula

$$\binom{n}{k} = \frac{n!}{k!\,(n - k)!}, \quad 0 \le k \le n$$

where $n! = n \times (n-1) \times \cdots \times 2 \times 1$ is the factorial function and $0! = 1$ by convention.

Key identities:

$$\binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{k} = \binom{n}{n-k}$$

## Example

A portfolio manager wants to select 3 stocks from a shortlist of 8. How many distinct portfolios are possible?

$$\binom{8}{3} = \frac{8!}{3!\,5!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

There are 56 different three-stock portfolios. If instead order mattered (e.g. ranking the top 3), the answer would be $8 \times 7 \times 6 = 336$ permutations — six times larger because each combination corresponds to $3! = 6$ orderings.

## Remember

The binomial coefficient $\binom{n}{k}$ is the direct building block of the **binomial distribution**: the probability mass function $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ counts the number of paths through an $n$-step binomial tree that end with exactly $k$ up-moves. In option pricing, this counting argument underpins the **Cox-Ross-Rubinstein (CRR) binomial model** — the number of favourable paths determines each terminal node's weight in the risk-neutral expected payoff.
