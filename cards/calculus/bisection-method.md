# Bisection Method

**Topic:** Calculus
**Tags:** bisection, root finding, implied volatility, intermediate value theorem, numerical method
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **bisection method** is a root-finding algorithm that repeatedly halves an interval $[a, b]$ containing a root of a continuous function $f$, eliminating the half that does not contain the root. It is guaranteed to converge whenever $f(a)$ and $f(b)$ have opposite signs, making it the most robust — if slowest — root-finding method. Each iteration halves the error, giving linear convergence.

## Key Formula

Given $f(a) \cdot f(b) < 0$ (sign change guarantees a root by the Intermediate Value Theorem):

$$c = \frac{a + b}{2}$$

Then update: if $f(c) \cdot f(a) < 0$, set $b \leftarrow c$; otherwise set $a \leftarrow c$. Repeat.

After $n$ iterations, the error is bounded by:

$$|c_n - x^*| \leq \frac{b - a}{2^n}$$

To achieve tolerance $\varepsilon$, the number of iterations required is:

$$n \geq \log_2\!\left(\frac{b - a}{\varepsilon}\right)$$

## Example

Solve for **implied volatility** $\sigma^*$ of a call option priced at $C^{\text{mkt}} = \$10.50$, with $S = K = \$100$, $r = 5\%$, $T = 1$ year. Define $f(\sigma) = C^{\text{BS}}(\sigma) - 10.50$.

| Iteration | $a$ | $b$ | $c$ | $f(c)$ |
|-----------|-----|-----|-----|--------|
| 1 | 0.00 | 1.00 | 0.500 | +15.82 |
| 2 | 0.00 | 0.50 | 0.250 | +5.05 |
| 3 | 0.00 | 0.25 | 0.125 | +0.40 |
| 4 | 0.00 | 0.125 | 0.063 | −4.02 |
| 5 | 0.063 | 0.125 | 0.094 | −1.86 |

After ~20 iterations, $\sigma^* \approx 0.199$ (19.9% implied vol). Each iteration halves the interval; tolerance $10^{-6}$ requires $\log_2(1/10^{-6}) \approx 20$ steps.

## Remember

Bisection is the **fallback method for implied volatility inversion** on trading desks. Newton-Raphson (which uses vega as the derivative) is faster — converging in 3–5 iterations — but can diverge if the initial guess is poor or vega is near zero (deep in- or out-of-the-money options). Bisection never diverges: as long as you bracket the root with an initial interval (e.g. $\sigma \in [10^{-6}, 5]$), it will find the implied vol to any precision in at most 23 iterations ($\log_2(5/10^{-6}) \approx 23$). Robust production systems often use a hybrid: bisection to get close, then Newton-Raphson for the final few digits.
