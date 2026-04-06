# Binomial Expansion

**Topic:** Calculus
**Tags:** binomial theorem, series expansion, approximation, combinatorics, taylor series
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **binomial expansion** expresses $(a + b)^n$ as an explicit sum of terms, each involving a binomial coefficient and powers of $a$ and $b$. For a positive integer $n$ the series is finite; for a non-integer or negative exponent the expansion becomes an infinite power series valid within a radius of convergence.

## Key Formula

**Exact expansion** (integer $n \geq 0$):

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
\qquad \text{where} \quad \binom{n}{k} = \frac{n!}{k!\,(n-k)!}
$$

**Generalised binomial series** (any real or complex $\alpha$, $|x| < 1$):

$$(1 + x)^\alpha = \sum_{k=0}^{\infty} \binom{\alpha}{k} x^k, \qquad \binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$$

**First-order approximation** (small $x$):

$$(1 + x)^\alpha \approx 1 + \alpha x$$

## Example

Approximate $(1 + 0.02)^{0.5}$ — the square root of a number close to 1, as arises in CRR binomial-tree up-factor calculations.

Using the first-order approximation with $\alpha = 0.5$ and $x = 0.02$:

$$(1.02)^{0.5} \approx 1 + 0.5 \times 0.02 = 1.01$$

The exact value is $1.00995\ldots$, so the error is about $0.005\%$ — entirely acceptable for a first-order correction.

Second-order correction: $1 + 0.5(0.02) + \tfrac{0.5 \times (-0.5)}{2}(0.02)^2 = 1.01 - 0.00005 = 1.00995$, matching the true value to five decimal places.

## Remember

The first-order binomial approximation $(1 + x)^\alpha \approx 1 + \alpha x$ is the workhorse behind the **Cox-Ross-Rubinstein (CRR) binomial tree**: the up and down factors $u = e^{\sigma\sqrt{\delta t}}$ and $d = e^{-\sigma\sqrt{\delta t}}$ are themselves first-order binomial approximations of $e^{\sigma\sqrt{\delta t}} \approx 1 + \sigma\sqrt{\delta t}$. Every time a quant linearises a small-move expression in $\sigma\sqrt{\delta t}$, they are applying the binomial expansion.
