# Partition of a Sample Space

**Topic:** Probability
**Tags:** partition, sample space, law of total probability, conditional probability, stress testing, scenario analysis
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

A **partition** of sample space $\Omega$ is a finite or countably infinite collection of events $\{A_1, A_2, \ldots, A_n\}$ satisfying two conditions:

1. **Mutually exclusive:** $A_i \cap A_j = \emptyset$ for all $i \neq j$ — no two events can occur simultaneously.
2. **Exhaustive:** $\bigcup_{i=1}^{n} A_i = \Omega$ — together they cover every possible outcome.

Every outcome in $\Omega$ belongs to exactly one $A_i$. Partitions are the building blocks of conditional reasoning: once you know which $A_i$ occurred, you can update probabilities for any other event $B$.

## Key Formula

The **Law of Total Probability** follows directly from a partition $\{A_1, \ldots, A_n\}$:

$$P(B) = \sum_{i=1}^{n} P(B \mid A_i)\, P(A_i)$$

Each term $P(B \mid A_i)\, P(A_i)$ is the probability that $B$ occurs *and* scenario $A_i$ is the one that materialises. Summing over the exhaustive, exclusive scenarios gives the unconditional probability of $B$.

## Example

Suppose the economy next year falls into one of three states that form a partition of $\Omega$:

| Scenario $A_i$ | $P(A_i)$ | $P(\text{default} \mid A_i)$ |
|---|---|---|
| Recession | 0.20 | 0.12 |
| Stagnation | 0.50 | 0.04 |
| Growth | 0.30 | 0.01 |

$$P(\text{default}) = 0.12 \times 0.20 + 0.04 \times 0.50 + 0.01 \times 0.30 = 0.024 + 0.020 + 0.003 = 0.047$$

The unconditional default probability is 4.7%, a probability-weighted blend across the three macro scenarios.

## Remember

This structure is the mathematical backbone of **IFRS 9 Expected Credit Loss (ECL)** models and **stress testing**. Under IFRS 9, banks must estimate ECL as a probability-weighted average across multiple forward-looking macroeconomic scenarios — exactly the law of total probability applied to a partition of economic futures. The Basel stress-testing framework similarly demands that banks define exhaustive, non-overlapping macro scenarios (adverse, severely adverse, base) and compute losses conditional on each, then aggregate. Getting the partition right — scenarios that are truly mutually exclusive and together span the plausible outcome space — is as much an art as a maths problem.
