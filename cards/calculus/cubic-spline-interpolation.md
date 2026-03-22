# Cubic Spline Interpolation

**Topic:** Calculus
**Level:** A Level Mathematics
**Tags:** cubic spline, interpolation, yield curve, curve construction, smoothness
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Cubic spline interpolation fits a piecewise cubic polynomial through a set of data points such that the resulting curve is continuous and has continuous first and second derivatives at every knot (data point). Between each pair of adjacent knots, a separate cubic polynomial $S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$ is fitted, subject to smoothness constraints. In quantitative finance, cubic splines are the standard method for constructing yield curves, volatility surfaces, and forward rate curves from discrete market quotes.

## Key Formula

For $n+1$ data points $(x_0, y_0), \ldots, (x_n, y_n)$, there are $n$ cubic pieces, each with 4 coefficients (4$n$ unknowns). The constraints are:

- **Interpolation:** $S_i(x_i) = y_i$ and $S_i(x_{i+1}) = y_{i+1}$ ($2n$ equations)
- **First derivative continuity:** $S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})$ ($n-1$ equations)
- **Second derivative continuity:** $S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})$ ($n-1$ equations)

Total: $4n - 2$ equations. The remaining 2 degrees of freedom are fixed by boundary conditions, most commonly **natural spline** ($S_0''(x_0) = S_{n-1}''(x_n) = 0$) or **clamped spline** (specified endpoint slopes).

## Example

A yield curve has three observed rates:

| Tenor (years) | Rate |
|--------------|------|
| 1 | 4.00% |
| 5 | 4.80% |
| 10 | 5.20% |

A natural cubic spline fits two cubic pieces. The spline passes exactly through all three points while ensuring the curve and its first two derivatives are continuous at the 5-year knot. Interpolating at $t = 3$ years:

$$S_1(3) = 4.00 + 0.28(3-1) + 0(3-1)^2 - 0.0125(3-1)^3$$
$$= 4.00 + 0.56 + 0 - 0.10 = 4.46\%$$

The spline gives a smooth rate of 4.46% at 3 years, avoiding the kinks that linear interpolation would produce.

## Remember

Cubic spline interpolation is one of the first things a quant developer implements when joining a fixed income or derivatives desk. Every interest rate curve, credit spread curve, and volatility surface is constructed by interpolating between observed market quotes, and the choice of interpolation method directly affects pricing and hedging. Cubic splines are preferred over linear interpolation because smooth forward rates prevent artificial hedging signals, and over higher-order polynomials because they avoid Runge's phenomenon (oscillation between knots). Production curve engines use monotone-preserving or tension splines to ensure forward rates remain positive — a constraint that standard natural splines do not guarantee.
