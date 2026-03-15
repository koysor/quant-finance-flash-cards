# Natural Numbers

**Topic:** Mathematical Notation
**Tags:** notation, number sets, counting, indices, sequences
**Author:** Claude Sonnet 4.6

---

## Definition

The **natural numbers**, denoted $\mathbb{N}$, are the positive counting integers $\{1, 2, 3, \ldots\}$. Some conventions include zero, writing $\mathbb{N}_0 = \{0, 1, 2, 3, \ldots\}$, though in most finance contexts $\mathbb{N} = \{1, 2, 3, \ldots\}$ is used.

They are the smallest number set and sit at the base of the hierarchy:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

## Key Formula

**Membership and indexing:**

$$i \in \mathbb{N} \implies i \in \{1, 2, 3, \ldots\}$$

**Summation over $n$ terms** (index runs through $\mathbb{N}$):

$$\sum_{i=1}^{n} x_i \quad \text{where } i \in \mathbb{N},\; n \in \mathbb{N}$$

**Sequence definition:** a sequence is a function $a : \mathbb{N} \to \mathbb{R}$, written $(a_n)_{n \in \mathbb{N}}$.

## Example

A portfolio has $n = 5$ assets. The weights are $w_1, w_2, w_3, w_4, w_5$ where the index $i \in \{1, 2, 3, 4, 5\} \subset \mathbb{N}$.

The total portfolio weight sums to one:

$$\sum_{i=1}^{5} w_i = 1$$

Here, $5 \in \mathbb{N}$ is the number of assets and each index $i \in \mathbb{N}$ labels a distinct position. Extending to $n$ assets is natural because $n$ itself must be a counting number.

## Remember

Natural numbers appear constantly in quantitative finance as **indices and counts**: the number of time steps $N$ in a binomial tree, the number of assets $n$ in a portfolio, or the tenor $T$ measured in whole periods. When a formula requires $n \in \mathbb{N}$, it means the quantity must be a positive integer — using a non-integer (e.g. $n = 2.5$ time steps) would be undefined. Recognising this constraint prevents specification errors in discretised models such as the binomial option pricing tree or Monte Carlo path simulators.
