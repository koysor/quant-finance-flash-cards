# Backward Difference Approximation

**Topic:** Calculus
**Tags:** numerical methods, finite differences, differentiation, approximation, truncation error
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **backward difference approximation** estimates the derivative of a function at a point by using the function value at that point and the value one step *behind* it. It is a first-order finite difference scheme: accurate to order $O(h)$, meaning the error shrinks linearly as the step size $h$ decreases. Unlike the central difference (which requires values on both sides), it only needs values at $x$ and $x - h$, making it suitable when only past information is available.

## Key Formula

$$f'(x) \approx \frac{f(x) - f(x - h)}{h}$$

The truncation error comes from the Taylor series:

$$f(x - h) = f(x) - h f'(x) + \frac{h^2}{2} f''(x) - \cdots$$

Rearranging gives the exact relationship:

$$f'(x) = \frac{f(x) - f(x - h)}{h} + \frac{h}{2} f''(x) + O(h^2)$$

so the leading error term is $\frac{h}{2} f''(x)$, confirming $O(h)$ accuracy.

## Example

Estimate $f'(2)$ for $f(x) = x^3$ using $h = 0.1$.

$$f(2) = 8, \qquad f(1.9) = 6.859$$

$$f'(2) \approx \frac{8 - 6.859}{0.1} = \frac{1.141}{0.1} = 11.41$$

The exact answer is $f'(2) = 3 \times 4 = 12$. The error is $0.59$, or about $4.9\%$.

For comparison, the forward difference with the same $h$ gives $\frac{f(2.1) - f(2)}{0.1} = \frac{9.261 - 8}{0.1} = 12.61$, an error of $5.1\%$. Central difference gives $\frac{9.261 - 6.859}{0.2} = 12.01$, an error of only $0.08\%$.

## Remember

In the implicit (backward) finite difference scheme for option pricing, the Black-Scholes PDE is discretised using a backward difference in time: $\frac{\partial V}{\partial t} \approx \frac{V_i^n - V_i^{n-1}}{\Delta t}$. This makes the scheme **unconditionally stable** — unlike the explicit (forward difference) scheme, it does not impose a stability condition on the ratio $\Delta t / (\Delta S)^2$, allowing larger time steps and faster computation when pricing American options or solving the full PDE grid.
