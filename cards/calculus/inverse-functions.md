# Inverse Functions

**Topic:** Calculus
**Tags:** inverse function, bijection, domain, range, one-to-one, quantile, function composition
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **inverse function** $f^{-1}$ of $f$ reverses the mapping: if $f(a) = b$ then $f^{-1}(b) = a$. An inverse exists if and only if $f$ is **one-to-one** (each output comes from exactly one input). The domain of $f^{-1}$ is the range of $f$, and vice versa.

## Key Formula

$$f(f^{-1}(x)) = x \quad \text{and} \quad f^{-1}(f(x)) = x$$

**To find $f^{-1}$:** write $y = f(x)$, rearrange for $x$, then replace $x$ with $f^{-1}(y)$.

**Derivative of inverse function:**

$$\frac{d}{dx}f^{-1}(x) = \frac{1}{f'(f^{-1}(x))}$$

## Example

Find the inverse of $f(x) = 2x + 3$.

Write $y = 2x + 3$, rearrange: $x = \frac{y - 3}{2}$.

So $f^{-1}(y) = \frac{y - 3}{2}$, or equivalently $f^{-1}(x) = \frac{x - 3}{2}$.

Check: $f(f^{-1}(x)) = 2 \cdot \frac{x-3}{2} + 3 = x$. ✓

## Remember

The **quantile function** $\Phi^{-1}$ is the inverse of the standard normal CDF $\Phi$, and it appears explicitly in the Black-Scholes formula: $d_1$ and $d_2$ are the inputs to $\Phi$, and VaR at confidence level $\alpha$ is computed as $\mu + \sigma\Phi^{-1}(\alpha)$. Risk managers who express loss thresholds in probability terms and then convert to cash amounts are applying $\Phi^{-1}$ — the inverse function — to move between the probability domain and the profit-and-loss domain.
