# Infinite Series

**Topic:** Calculus
**Tags:** infinite series, convergence, divergence, ratio test, partial sums, power series
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

An **infinite series** $\sum_{n=1}^\infty a_n$ is the limit of its partial sums $S_N = \sum_{n=1}^N a_n$. The series **converges** if $\lim_{N\to\infty} S_N$ exists and is finite; otherwise it **diverges**.

## Key Formula

**Ratio test:** for $L = \lim_{n\to\infty} |a_{n+1}/a_n|$:

$$L < 1 \implies \text{converges absolutely}, \qquad L > 1 \implies \text{diverges}, \qquad L = 1 \implies \text{inconclusive}$$

**$p$-series:** $\displaystyle\sum_{n=1}^\infty \frac{1}{n^p}$ converges iff $p > 1$.

**Absolute convergence:** if $\sum |a_n|$ converges, then $\sum a_n$ converges (but not vice versa).

**Geometric:** $\displaystyle\sum_{n=0}^\infty r^n = \frac{1}{1-r}$ for $|r| < 1$.

## Example

Does $\sum_{n=1}^\infty \frac{n}{2^n}$ converge?

Ratio test: $L = \lim_{n\to\infty} \frac{(n+1)/2^{n+1}}{n/2^n} = \lim_{n\to\infty} \frac{n+1}{2n} = \frac{1}{2} < 1$.

The series converges. (Its sum is 2, by differentiating the geometric series.)

## Remember

Convergence of infinite series is the rigorous basis for **Taylor series pricing models** and **characteristic function representations**. In Lewis's Fourier option pricing, the option price is expressed as an integral over a contour, which numerically becomes an infinite sum; that sum converges because the characteristic function $\varphi(\omega)$ decays to zero as $|\omega| \to \infty$ for distributions with finite moments — the analytic counterpart of the ratio test. Knowing when a series converges tells a quant when a pricing algorithm will produce a finite, meaningful answer and when it will blow up.
