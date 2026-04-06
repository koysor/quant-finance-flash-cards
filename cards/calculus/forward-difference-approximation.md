# Forward Difference Approximation

**Topic:** Calculus
**Tags:** numerical methods, finite difference, differentiation, truncation error, approximation
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **forward difference approximation** estimates the derivative of a function at a point $x$ by comparing its value at $x$ and at a nearby point $x + h$. It is the simplest finite difference formula and underpins numerical differentiation wherever analytical derivatives are unavailable. The approximation is **first-order accurate**: halving the step size $h$ halves the error.

## Key Formula

$$f'(x) \approx \frac{f(x + h) - f(x)}{h}$$

The error comes directly from the Taylor series:

$$f(x + h) = f(x) + h f'(x) + \frac{h^2}{2} f''(x) + O(h^3)$$

Rearranging gives the approximation plus its **truncation error**:

$$\frac{f(x + h) - f(x)}{h} = f'(x) + \underbrace{\frac{h}{2} f''(x) + O(h^2)}_{\text{truncation error}} = f'(x) + O(h)$$

The leading error term is proportional to $h$, so the scheme is $O(h)$ — first-order accurate.

## Example

Estimate $f'(1)$ for $f(x) = x^3$ using $h = 0.1$:

$$f'(1) \approx \frac{(1.1)^3 - (1)^3}{0.1} = \frac{1.331 - 1.000}{0.1} = \frac{0.331}{0.1} = 3.31$$

The exact answer is $f'(1) = 3x^2\big|_{x=1} = 3$, so the error is $0.31$ — roughly $\frac{h}{2} f''(1) = \frac{0.1}{2} \times 6 = 0.30$, matching the $O(h)$ prediction.

## Remember

In quantitative finance, the forward difference is used to compute **Greeks by bumping**: Delta is estimated as $\Delta \approx (V(S + h) - V(S)) / h$, where $V$ is the option price and $h$ is a small shift in the underlying price. Because only one extra pricing call is needed (versus two for the central difference), it is cheaper but less accurate. Risk systems that must compute hundreds of sensitivities overnight often use forward differences as a cost–accuracy trade-off, switching to central differences only for the most important Greeks such as Gamma.
