# Binomial Coefficients

**Topic:** Calculus
**Tags:** binomial coefficients, combinations, combinatorics, choose, factorial, pascal's triangle
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **binomial coefficient** $\binom{n}{k}$ (read "$n$ choose $k$") counts the number of ways to select $k$ items from $n$ distinct items without regard to order. It is the coefficient of $a^{n-k}b^k$ in the expansion of $(a+b)^n$ and appears throughout probability, combinatorics, and finance.

## Key Formula

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

**Key properties:**

$$\binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{1} = \binom{n}{n-1} = n$$

$$\binom{n}{k} = \binom{n}{n-k} \quad \text{(symmetry)}$$

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k} \quad \text{(Pascal's identity)}$$

$$\sum_{k=0}^{n}\binom{n}{k} = 2^n \quad \text{(sum of row } n \text{ of Pascal's triangle)}$$

## Example

A portfolio manager must choose 4 stocks from a shortlist of 10. The number of distinct portfolios is:

$$\binom{10}{4} = \frac{10!}{4!\,6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$$

If order mattered (e.g. ranked by conviction), the count would be $10 \times 9 \times 8 \times 7 = 5040$ — binomial coefficients are the ordered count divided by $k!$ to remove ordering.

## Remember

Binomial coefficients are the **weights in the binomial distribution** and the **path counts in the binomial option pricing tree**. In the CRR tree, exactly $\binom{n}{k}$ paths out of $2^n$ total paths lead to the node with $k$ up-moves after $n$ steps. Multiplied by the risk-neutral probability $p^k(1-p)^{n-k}$ and summed over all nodes where the option pays off, these coefficients produce the option price — a weighted sum with binomial coefficients as the combinatorial weights. The binomial distribution $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$ is the direct probability statement of the same counting argument.
