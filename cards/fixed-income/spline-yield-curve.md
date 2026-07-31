# Spline-Based Yield Curve Models

**Topic:** Fixed Income
**Tags:** spline, yield curve, curve fitting, smoothing, discount function, term structure
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

A spline-based yield curve model represents the zero-coupon yield (or discount function) as a piecewise cubic polynomial, joined at fixed **knots** along the maturity axis with continuity enforced on the value, first derivative, and second derivative at each knot.

## Key Formula

The smoothing spline minimises a penalised least-squares objective that trades fitting accuracy against curve roughness:

$$\min_{z(\tau)} \sum_{i=1}^{N} w_i \left[y_i^{\text{obs}} - z(\tau_i)\right]^2 + \lambda \int_0^T \left[z''(\tau)\right]^2 d\tau$$

where $z(\tau)$ is the fitted zero rate at tenor $\tau$, $w_i$ is an instrument weight (typically DV01), $y_i^{\text{obs}}$ is the observed yield, and $\lambda \geq 0$ is the **roughness penalty**. Between adjacent knots $\tau_k$ and $\tau_{k+1}$, the curve is:

$$z(\tau) = a_k + b_k(\tau - \tau_k) + c_k(\tau - \tau_k)^2 + d_k(\tau - \tau_k)^3$$

Continuity of $z$, $z'$, and $z''$ at each knot links the coefficients across segments. A natural cubic spline additionally imposes $z''=0$ at the two endpoints.

## Example

Knots at 0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30 years give a natural cubic spline with 10 free parameters, compared with 4 for Nelson-Siegel. With roughness penalty $\lambda = 0$: the spline passes exactly through every observed yield but may oscillate wildly between sparse tenors. With $\lambda \to \infty$: the penalty dominates and the curve collapses to a straight line through the data. Practitioners choose $\lambda$ via cross-validation or by setting it to match a target root-mean-square pricing error of around 1–2 bp.

## Remember

The UK Debt Management Office uses a smoothing spline on the gilt strip curve, and similar methods underpin the US Treasury par yield curve published by the Federal Reserve. Placing knots at liquid benchmark tenors (2Y, 5Y, 10Y, 30Y) anchors the fitted curve where market information is richest, while the penalty $\lambda$ prevents spurious wiggles in the illiquid intermediate zones used to price off-the-run bonds and liability-matching portfolios.
