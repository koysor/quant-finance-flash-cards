# Akima Spline

**Topic:** Computational Finance
**Tags:** interpolation, spline, outlier-robust, volatility surface, python, curve fitting
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **Akima spline** (Akima, 1970) is a piecewise cubic interpolator whose slope rule uses only nearby data points and is explicitly designed to resist being distorted by a single outlier or abrupt local change — avoiding the wide, unphysical wiggles that ordinary global cubic splines produce near sharp jumps in the data. Like PCHIP it is a local, $C^1$ method, but its slope construction differs: rather than a monotonicity-preserving secant blend, it is a weighted average of the four surrounding secant slopes, with weights chosen to shrug off inconsistent neighbours.

## Key Formula

At node $x_i$, the Akima slope $d_i$ is a weighted average of the two secants either side, using weights built from the *second* differences of the secants:

$$d_i = \frac{w_1\,S_{i-1} + w_2\,S_i}{w_1 + w_2}, \qquad w_1 = |S_{i+1} - S_i|, \quad w_2 = |S_{i-1} - S_{i-2}|$$

where $S_i = \frac{f_{i+1} - f_i}{x_{i+1} - x_i}$ are the local secant slopes. When neighbouring secants agree (smooth, consistent data), the weights are similar and $d_i$ is close to a simple average; when one side is erratic, its weight collapses towards zero and that side is effectively ignored, isolating the fitted slope from the outlier.

## Example

An implied volatility smile has strikes with a single noisy quote: IVs of $19\%, 18\%, 24\%, 17.5\%, 17\%$ at five neighbouring strikes, where $24\%$ is a stale, illiquid print (a clear outlier relative to its neighbours). A standard cubic spline, enforcing global second-derivative continuity, lets that one bad point drag the curve into an unrealistic bulge across several strikes either side. Akima's locally weighted slope construction largely contains the distortion to the immediate vicinity of the bad point, leaving the rest of the smile close to its well-behaved shape — available as `scipy.interpolate.Akima1DInterpolator(strikes, ivs)`.

## Remember

Reach for the Akima spline when the data itself is the problem, not the interpolation method: thin, illiquid strikes near the wings of a smile routinely produce one-off noisy quotes, and a global spline propagates that noise across the whole curve while Akima's purely local slope rule contains it. It is a complementary tool to PCHIP interpolation rather than a replacement — PCHIP's priority is guaranteeing monotonicity (essential for the calendar-arbitrage-sensitive $T$ direction of a total variance surface), while Akima's priority is outlier robustness (useful across the strike direction of a single noisy smile slice). A rigorous local volatility pipeline typically uses both, matched to the axis and the failure mode each is guarding against.
