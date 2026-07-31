# PCHIP Interpolation

**Topic:** Computational Finance
**Tags:** interpolation, monotone spline, hermite, shape-preserving, volatility surface, python
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

**PCHIP** (Piecewise Cubic Hermite Interpolating Polynomial) is a shape-preserving cubic interpolator: unlike a natural cubic spline, it never overshoots the data — where the input values rise, the interpolated curve only rises, with no spurious wiggles between knots. It achieves this by defining each cubic segment from the values *and* the slopes at its endpoints (a Hermite segment), where the endpoint slopes are estimated from the secants (straight lines) joining neighbouring data points rather than from a global smoothness condition.

## Key Formula

Each segment between nodes $x_i$ and $x_{i+1}$ is a Hermite cubic determined by four pieces of data — $f_i, f_{i+1}$ and the slopes $d_i, d_{i+1}$:

$$H_i(x) = f_i\,h_{00}(t) + h\,d_i\,h_{10}(t) + f_{i+1}\,h_{01}(t) + h\,d_{i+1}\,h_{11}(t), \qquad t = \frac{x - x_i}{h}$$

where $h = x_{i+1} - x_i$ and $h_{00}, h_{10}, h_{01}, h_{11}$ are the standard Hermite basis polynomials. The slope $d_i$ is chosen from the secant slopes $S_{i-1} = \frac{f_i - f_{i-1}}{x_i - x_{i-1}}$ and $S_i = \frac{f_{i+1}-f_i}{x_{i+1}-x_i}$: if $S_{i-1}$ and $S_i$ have opposite signs (a local extremum), $d_i = 0$; otherwise $d_i$ is a weighted harmonic mean of $S_{i-1}$ and $S_i$ — the rule that guarantees monotonicity is preserved. The result is $C^1$ (continuous first derivative), one order less smooth than a natural spline's $C^2$, in exchange for the no-overshoot guarantee.

## Example

Total variance quoted at three expiries: $w(1M) = 0.0060$, $w(3M) = 0.0135$, $w(6M) = 0.0140$ — a slice where the calendar slope flattens sharply between 3M and 6M. A natural cubic spline, forced to match curvature across the flattening, can overshoot and dip *below* $0.0135$ between 3M and 6M, silently creating a calendar arbitrage violation. PCHIP instead detects the flattening secant slopes and damps the interpolated slope towards zero there, producing a curve that stays non-decreasing throughout — available directly as `scipy.interpolate.PchipInterpolator(expiries, w_values)`.

## Remember

PCHIP is the standard choice for interpolating total variance in expiry precisely because a local volatility pipeline cannot afford an interpolation artefact to reintroduce the calendar arbitrage that was just repaired. Its $C^1$ smoothness is exactly enough for the $\partial_T w$ that Dupire's formula needs, while its shape-preserving slope rule means the interpolant itself can never manufacture a violation between quoted nodes — a natural spline, chasing $C^2$ smoothness, offers no such guarantee. The trade-off to remember: PCHIP sacrifices one order of smoothness (no continuous second derivative) for a robustness property that matters far more when the very next step is a no-arbitrage check.
