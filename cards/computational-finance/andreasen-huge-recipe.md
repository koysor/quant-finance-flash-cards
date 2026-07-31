# Andreasen-Huge Recipe

**Topic:** Computational Finance
**Tags:** local volatility, dupire formula, calibration, interpolation, call prices, finite differences
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **Andreasen-Huge recipe** (2011) is a production-grade route to local volatility that interpolates option **prices** directly, rather than implied volatility or total variance, and then takes simple finite differences of the price grid to feed Dupire's formula. It sidesteps the fragility of differentiating volatility-space interpolants by working in a space — call prices, convex in strike and linear in $\sqrt{T}$ between expiries — where the required shape constraints are simpler to enforce.

## Key Formula

Local variance directly from the call-price surface $C(K,T)$:

$$\sigma_{\text{LV}}^2(K,T) = \frac{\partial_T C + (r_T - q_T)\,K\,\partial_K C + q_T\,C}{\tfrac{1}{2}\,K^2\,\partial_{KK} C}$$

On a non-uniform strike grid, the curvature term uses the three-point formula for unevenly spaced nodes:

$$\partial_{KK} C \approx \frac{C_{j+1} - 2C_j + C_{j-1}}{(K_j - K_{j-1})(K_{j+1} - K_j)}$$

where $r_T, q_T$ are the risk-free rate and dividend yield for expiry $T$, and $\partial_T C$, $\partial_K C$, $\partial_{KK} C$ are the calendar slope, strike slope and strike curvature of the call-price surface respectively.

## Example

At $K = 4{,}500$, $T = 0.5$, a call price grid gives $C = 210.4$, $\partial_T C = 85.0$, $\partial_K C = -0.42$, $\partial_{KK} C = 0.00095$, with $r = 4\%$, $q = 1.5\%$.

$$\sigma_{\text{LV}}^2 = \frac{85.0 + 0.025 \times 4500 \times (-0.42) + 0.015 \times 210.4}{0.5 \times 4500^2 \times 0.00095} = \frac{85.0 - 47.25 + 3.16}{9{,}618.75} \approx 0.00420$$

$$\sigma_{\text{LV}} \approx \sqrt{0.00420} \approx 6.5\% \text{ per year}$$

The same inputs, if instead differentiated in total-variance space via Gatheral's $w(T,y)$ form, would give an equivalent answer — the two routes should agree on the admissible region of the grid, which is a standard cross-check.

## Remember

The recipe's real contribution is a *workflow*, not a new formula: build a smooth call-price surface (even one reconstructed from a well-behaved total-variance grid), require it to be convex in strike and increasing appropriately in $\sqrt{T}$, then take plain finite differences — no vol-space Jacobians, no risk of dividing by a near-zero implied-vol-space denominator from a poorly conditioned interpolant. Running both the price-space (Andreasen-Huge) and total-variance-space Dupire forms on the same data and checking they agree on the trustworthy central band of the surface is exactly the kind of self-validating design a rigorous local volatility pipeline is expected to demonstrate.
