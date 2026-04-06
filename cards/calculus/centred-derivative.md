# Centred Derivative

**Topic:** Calculus
**Tags:** numerical differentiation, finite difference, approximation, error analysis, calculus
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **centred derivative** (or central difference approximation) estimates the derivative of a function at a point by averaging the slopes of a forward step and a backward step of equal size. Symmetry about the evaluation point causes first-order errors to cancel, giving second-order accuracy — twice the precision of one-sided differences for the same step size.

## Key Formula

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$

The truncation error is $O(h^2)$, derived from the Taylor series:

$$f(x+h) = f(x) + h f'(x) + \tfrac{h^2}{2} f''(x) + \tfrac{h^3}{6} f'''(x) + \cdots$$
$$f(x-h) = f(x) - h f'(x) + \tfrac{h^2}{2} f''(x) - \tfrac{h^3}{6} f'''(x) + \cdots$$

Subtracting and dividing by $2h$ cancels all even-order terms:

$$\frac{f(x+h) - f(x-h)}{2h} = f'(x) + \frac{h^2}{6} f'''(x) + O(h^4)$$

The second-order approximation for the second derivative is:

$$f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2}$$

## Example

Estimate $f'(1)$ for $f(x) = x^3$ with $h = 0.1$:

$$\frac{f(1.1) - f(0.9)}{2 \times 0.1} = \frac{1.331 - 0.729}{0.2} = \frac{0.602}{0.2} = 3.01$$

The exact answer is $f'(1) = 3x^2\big|_{x=1} = 3$. The error is $0.01 = O(h^2)$.

Compare with the forward difference: $\frac{f(1.1) - f(1)}{0.1} = \frac{0.331}{0.1} = 3.31$ — an error of $0.31 = O(h)$, thirty times larger for the same step size.

## Remember

The centred derivative is the standard method for computing option Greeks numerically. When a pricing function has no closed-form derivative — for example, a barrier option priced by Monte Carlo or a PDE solver — a quant bumps the input up and down by $h$ and applies the central difference formula. The $O(h^2)$ error means halving the bump size reduces the approximation error by a factor of four, whereas a one-sided bump only reduces it by two. The practical choice of $h$ balances this truncation error against floating-point cancellation noise: too large a bump inflates truncation error; too small a bump loses significant digits when nearly equal numbers are subtracted.
