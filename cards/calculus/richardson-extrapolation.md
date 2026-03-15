# Richardson Extrapolation

**Topic:** Calculus
**Tags:** numerical methods, extrapolation, convergence, error reduction, approximation
**Created:** 2026-03-15
**Author:** Claude Opus 4.6

---

## Definition

**Richardson extrapolation** is a technique for improving the accuracy of a numerical approximation whose error has a known power-law dependence on the step size. By computing the same quantity at two different step sizes and forming a weighted combination, the leading error term cancels, yielding a result that converges at a higher order than either estimate alone.

## Key Formula

Suppose an approximation $A(h)$ of the true value $A^*$ satisfies:

$$A(h) = A^* + c \, h^p + O(h^{p+1})$$

where $c$ is an unknown constant and $p$ is the known order of the error. Computing $A(h)$ and $A(h/2)$ and eliminating the $c \, h^p$ term gives the improved estimate:

$$A^* \approx \frac{2^p \, A(h/2) - A(h)}{2^p - 1}$$

For a second-order method ($p = 2$) this simplifies to:

$$A^* \approx \frac{4 \, A(h/2) - A(h)}{3}$$

## Example

Estimate $f'(1)$ for $f(x) = x^3$ using the central difference formula $A(h) = \frac{f(1+h) - f(1-h)}{2h}$, which has error $O(h^2)$ (so $p = 2$).

With $h = 0.1$: $A(0.1) = \frac{1.1^3 - 0.9^3}{0.2} = \frac{1.331 - 0.729}{0.2} = 3.0100$

With $h = 0.05$: $A(0.05) = \frac{1.05^3 - 0.95^3}{0.1} = \frac{1.157625 - 0.857375}{0.1} = 3.0025$

Applying Richardson extrapolation:

$$A^* \approx \frac{4 \times 3.0025 - 3.0100}{3} = \frac{12.0100 - 3.0100}{3} = \frac{9.0000}{3} = \textbf{3.0000}$$

The exact answer is $f'(1) = 3x^2\big|_{x=1} = 3$. Extrapolation recovers it exactly here because the higher-order error terms also vanish for a cubic polynomial.

## Remember

Richardson extrapolation is a practical tool for squeezing more accuracy out of existing numerical schemes without redesigning them. In quantitative finance, it is applied to finite-difference grids for PDE-based option pricing (e.g. Black-Scholes) — running the solver on a coarse and a fine grid and combining the results can deliver fourth-order accuracy from a second-order scheme, dramatically reducing the grid size needed for reliable Greeks and exotic option prices. It is also used to accelerate convergence of Monte Carlo estimates of sensitivities computed via bump-and-revalue.
