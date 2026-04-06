# Pascal's Triangle

**Topic:** Calculus
**Tags:** pascal's triangle, binomial coefficients, combinatorics, binomial expansion, binomial tree
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Pascal's triangle** is a triangular array in which each entry equals the sum of the two entries directly above it. Row $n$ (starting from row 0) lists the binomial coefficients $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$, giving the coefficients of the expansion of $(a + b)^n$.

## Key Formula

**Pascal's identity** (the construction rule):

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

**First six rows:**

$$\begin{array}{ccccccccccc}
n=0: & & & & & 1 & & & & \\
n=1: & & & & 1 & & 1 & & & \\
n=2: & & & 1 & & 2 & & 1 & & \\
n=3: & & 1 & & 3 & & 3 & & 1 \\
n=4: & 1 & & 4 & & 6 & & 4 & & 1
\end{array}$$

Row $n$ sums to $2^n$; the triangle is symmetric ($\binom{n}{k} = \binom{n}{n-k}$).

## Example

Read the coefficients of $(a + b)^4$ directly from row 4: $1, 4, 6, 4, 1$.

$$(a+b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4$$

No multiplication needed — the triangle gives all coefficients instantly.

## Remember

Pascal's triangle is the **state-counting structure of the binomial option pricing tree**. After $n$ steps of a binomial tree with up-factor $u$ and down-factor $d$, the number of paths reaching state $k$ (exactly $k$ up-moves) is $\binom{n}{k}$ — the entry in row $n$, column $k$ of Pascal's triangle. The risk-neutral option price is:

$$C = e^{-rn\delta t}\sum_{k=0}^{n}\binom{n}{k}p^k(1-p)^{n-k}\max(S_0 u^k d^{n-k} - K,\, 0)$$

Every binomial tree calculation implicitly uses Pascal's triangle to count how many paths lead to each terminal stock price.
