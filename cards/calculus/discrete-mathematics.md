# Discrete Mathematics

**Topic:** Calculus
**Tags:** discrete, counting, combinatorics, sequences, finite structures
**Author:** Claude Sonnet 4.6

---

## Definition

Discrete mathematics is the branch of mathematics concerned with structures that can be counted or enumerated — integers, finite sets, sequences, graphs, and combinatorics — as opposed to continuous quantities such as real numbers or smooth functions.

## Key Formula

The number of ways to choose $r$ items from $n$ without regard to order (a binomial coefficient):

$$\binom{n}{r} = \frac{n!}{r!\,(n-r)!}$$

A recurrence relation (discrete analogue of a differential equation) links successive terms:

$$a_{n+1} = f(a_n, a_{n-1}, \ldots)$$

## Example

A 2-step binomial tree for an option has $n = 2$ periods. The number of distinct paths from root to leaf is $2^2 = 4$. The number of paths reaching the up-up node is $\binom{2}{2} = 1$; the number reaching the up-down node is $\binom{2}{1} = 2$. These counts are used to weight payoffs in the risk-neutral binomial pricing formula.

## Remember

Discrete mathematics is the foundation of lattice models in derivatives pricing. The Cox–Ross–Rubinstein binomial tree, Monte Carlo simulation with discrete time steps, and bond amortisation schedules (difference equations) are all built on counting, integer arithmetic, and recurrence relations. Every continuous-time finance model ultimately has a discrete approximation used in numerical implementation.
