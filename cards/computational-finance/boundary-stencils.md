# Boundary Stencils

**Topic:** Computational Finance
**Tags:** finite difference, one-sided stencil, order of accuracy, numerical derivatives, volatility surface, noise amplification
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

A **stencil** is the set of grid points combined to approximate a derivative. Interior points can use a symmetric (centred) stencil, but the first and last points of a grid have no neighbour on one side, so they require a **boundary stencil** — a one-sided formula built from points on the available side only, weighted to preserve the desired order of accuracy.

## Key Formula

Centred second derivative, interior, error $O(h^2)$:

$$f''_i \approx \frac{f_{i-1} - 2f_i + f_{i+1}}{h^2}$$

Wide 5-point centred stencil, error $O(h^4)$:

$$f''_i \approx \frac{-f_{i-2} + 16f_{i-1} - 30f_i + 16f_{i+1} - f_{i+2}}{12h^2}$$

One-sided (forward) second derivative at the left boundary, still $O(h^2)$:

$$f''_0 \approx \frac{2f_0 - 5f_1 + 4f_2 - f_3}{h^2}$$

Naively falling back to the two-point difference $(f_1 - f_0)/h$ at the edge drops the scheme to $O(h)$ there, and the boundary error then pollutes the whole solution.

## Example

A total-variance slice is sampled on a log-moneyness grid with $h = 0.02$ and quote noise of $\varepsilon = 10^{-5}$ in $w$.

The centred second-difference noise is amplified by roughly $4\varepsilon / h^2 = 4 \times 10^{-5} / 0.0004 = 0.1$ — an error of $0.1$ in $\partial_{yy} w$, which is the same order as the curvature itself. Halving the spacing to $h = 0.01$ quadruples the amplification to $0.4$: a *finer* grid gives a *worse* derivative once noise dominates truncation error.

Switching to the 5-point $O(h^4)$ stencil cuts truncation error by a factor of $h^2 \approx 400$ but raises the noise coefficient (weights $1, 16, 30, 16, 1$ over $12h^2$), so it only pays where quotes are liquid and clean.

## Remember

Stencil choice is where a volatility surface pipeline is won or lost. Dupire's formula needs $\partial_T w$, $\partial_y w$ and $\partial_{yy} w$ evaluated across the whole grid, and the wings of an option surface are exactly where quotes are thinnest and one-sided stencils are unavoidable. The working compromise on a desk is to use wide high-order stencils in the liquid near-forward band, drop to 3-point centred formulae in transition regions, and use one-sided stencils only at the outermost strikes — then discard local volatility at any node where the resulting denominator $\partial_{yy}w$ is small or the curvature has gone negative, rather than smoothing the numbers until they look pretty and breaking exact calibration.
