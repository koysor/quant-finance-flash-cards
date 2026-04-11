# Order Statistics Notation

**Topic:** Mathematical Notation
**Tags:** notation, order statistics, minimum, maximum, quantile, median
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Order statistics** are the values of a sample rearranged from smallest to largest. The notation $X_{(k)}$ denotes the $k$-th smallest value in a sample of $n$ observations.

| Symbol | Read as | Meaning |
|---|---|---|
| $X_{(1)}$ | "first order statistic" | Minimum: $\min(X_1, \ldots, X_n)$ |
| $X_{(k)}$ | "k-th order statistic" | The $k$-th smallest value in the sample |
| $X_{(n)}$ | "n-th order statistic" | Maximum: $\max(X_1, \ldots, X_n)$ |
| $X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$ | "ordered sample" | The full sorted sequence |
| $X_{((n+1)/2)}$ | "sample median" | Middle value (for odd $n$); average of two middle values for even $n$ |
| $Q(\alpha)$ or $X_{(\lceil n\alpha \rceil)}$ | "sample $\alpha$-quantile" | Empirical quantile at probability level $\alpha$ |

## Key Formula

**PDF of the $k$-th order statistic** (for i.i.d. sample from $F$, $f$):

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1}[1-F(x)]^{n-k} f(x)$$

**Special cases:**

$$f_{X_{(1)}}(x) = n[1-F(x)]^{n-1}f(x) \qquad \text{(minimum)}$$

$$f_{X_{(n)}}(x) = n[F(x)]^{n-1}f(x) \qquad \text{(maximum)}$$

## Example

For a sample of $n = 100$ daily losses, $X_{(95)}$ is the 95th-largest loss — the empirical 95% quantile, used as the historical VaR estimate. $X_{(100)}$ is the maximum observed loss. The spacing between $X_{(95)}$ and $X_{(100)}$ reflects the tail beyond VaR, which CVaR averages.

## Remember

Order statistics are the foundation of non-parametric risk measurement: historical simulation VaR is simply an order statistic of the loss distribution. The notation $X_{(k)}$ (round brackets, not square) distinguishes the ordered sample from the original sequence $X_k$ (square or no brackets). In extreme value theory, the distribution of $X_{(n)}$ as $n \to \infty$ — the maximum — converges to a GEV distribution, underpinning stress-testing frameworks.
