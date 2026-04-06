# Permutations

**Topic:** Probability
**Tags:** combinatorics, counting, probability, arrangements, factorial
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A permutation is an ordered arrangement of $r$ objects chosen from $n$ distinct objects. The order in which the objects are selected matters — swapping two items produces a different permutation.

## Key Formula

The number of ways to arrange $r$ objects from $n$ distinct objects is:

$${}^nP_r = \frac{n!}{(n - r)!}$$

where $n!$ (n factorial) is the product $n \times (n-1) \times \cdots \times 2 \times 1$, and $0! = 1$ by convention.

The special case $r = n$ gives:

$${}^nP_n = n!$$

which counts all orderings of the full set.

## Example

A portfolio manager is ranking her top 3 stock picks from a shortlist of 8 candidates for an ordered presentation to a client (1st, 2nd, and 3rd choice).

The number of ordered arrangements is:

$${}^8P_3 = \frac{8!}{(8 - 3)!} = \frac{8!}{5!} = 8 \times 7 \times 6 = 336$$

There are 336 distinct ordered rankings she could present.

## Remember

Permutations appear in probability calculations where **order matters** — for example, computing the probability that a specific sequence of price moves occurs, or counting the number of ways to rank assets in a stress test scenario. The binomial coefficient $\binom{n}{k}$ used in the binomial distribution divides out the ordering factor: $\binom{n}{k} = \frac{{}^nP_k}{k!}$, recovering combinations when order is irrelevant.
