# Newton-Raphson Method

**Topic:** Calculus
**Level:** A Level Mathematics
**Tags:** newton-raphson, root finding, iteration, implied volatility, numerical methods
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The Newton-Raphson method is an iterative root-finding algorithm that uses the function value and its derivative at a current estimate to produce a better estimate. Starting from an initial guess $x_0$, each iteration follows the tangent line to the x-axis, converging quadratically to a root of $f(x) = 0$. In quantitative finance it is the standard algorithm for computing implied volatility — inverting the Black-Scholes formula to find the volatility that matches an observed option price.

## Key Formula

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

For **implied volatility**, the function to solve is:

$$f(\sigma) = C_{\text{BS}}(\sigma) - C_{\text{market}} = 0$$

where the derivative is vega:

$$f'(\sigma) = \frac{\partial C_{\text{BS}}}{\partial \sigma} = S \sqrt{T} \, \phi(d_1)$$

So the iteration becomes:

$$\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{\text{vega}(\sigma_n)}$$

## Example

An option trades at £5.20. Using Black-Scholes with $S = £100$, $K = £100$, $T = 0.25$, $r = 5\%$, starting guess $\sigma_0 = 0.30$:

| Iteration | $\sigma_n$ | $C_{\text{BS}}(\sigma_n)$ | Vega | $\sigma_{n+1}$ |
|-----------|-----------|-------------------------|------|----------------|
| 0 | 0.3000 | £5.46 | 19.88 | $0.30 - \frac{5.46 - 5.20}{19.88} = 0.2869$ |
| 1 | 0.2869 | £5.21 | 19.89 | $0.2869 - \frac{5.21 - 5.20}{19.89} = 0.2864$ |
| 2 | 0.2864 | £5.200 | — | Converged |

The implied volatility is 28.64%, found in just 2 iterations.

## Remember

Newton-Raphson is the workhorse of derivatives pricing libraries. Every time a quant dev displays an implied volatility surface, the method runs thousands of times — once per strike and expiry. Its quadratic convergence (errors roughly square each iteration) makes it extremely fast, but it can fail if vega is near zero (deep in/out-of-the-money options) or the initial guess is poor. Production implementations use safeguards: Brent's method as a fallback, rational approximations (Jäckel 2015) for the initial guess, and bounds checking. Understanding Newton-Raphson is essential because it generalises to calibrating any model parameter — fitting Heston parameters, solving for break-even rates, or inverting any monotonic pricing function.
