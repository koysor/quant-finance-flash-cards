# Finite Difference Methods

**Topic:** Derivatives
**Tags:** finite differences, numerical methods, PDE, option pricing, grid methods, Black-Scholes
**Author:** Claude Opus 4.6

---

## Definition

**Finite difference methods** (FDM) are numerical techniques for solving partial differential equations (PDEs) by replacing continuous derivatives with discrete approximations on a grid. In quantitative finance, they are primarily used to solve the Black-Scholes PDE and its generalisations when no closed-form solution exists — for example, when pricing American options or options with path-dependent features.

## Key Formula

The core idea is to approximate a derivative using nearby grid values. For a function $V(S, t)$ on a grid with spacing $\Delta S$, the three standard approximations of the first derivative are:

**Forward difference:**

$$\frac{\partial V}{\partial S} \approx \frac{V_{i+1} - V_i}{\Delta S}$$

**Backward difference:**

$$\frac{\partial V}{\partial S} \approx \frac{V_i - V_{i-1}}{\Delta S}$$

**Central difference (most accurate):**

$$\frac{\partial V}{\partial S} \approx \frac{V_{i+1} - V_{i-1}}{2\,\Delta S}$$

The second derivative, needed for the $\frac{\partial^2 V}{\partial S^2}$ term in the Black-Scholes PDE, is approximated by:

$$\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1} - 2V_i + V_{i-1}}{(\Delta S)^2}$$

## Example

Price a European put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$ year. Set up a grid with $\Delta S = 5$ (asset prices from 0 to 200) and $\Delta t = 0.01$ (100 time steps).

At expiry, the boundary condition gives $V_i = \max(100 - S_i,\; 0)$ for each grid point $S_i$. Working backwards one time step using the explicit scheme, the interior node at $S = 100$ updates as:

$$V_{100}^{n} = V_{100}^{n+1} + \Delta t \left[\tfrac{1}{2}\sigma^2 S^2 \frac{V_{101} - 2V_{100} + V_{99}}{(\Delta S)^2} + rS\frac{V_{101} - V_{99}}{2\,\Delta S} - rV_{100}\right]$$

Substituting the payoff values at expiry and iterating backwards through all time steps produces the option price at $t = 0$.

## Remember

Finite difference methods turn a continuous PDE into a system of equations on a grid, solved step-by-step backwards from expiry. They are the standard numerical tool when the Black-Scholes PDE cannot be solved analytically — particularly for American options, where the early exercise boundary must be found as part of the solution. Unlike Monte Carlo (which simulates forward paths), FDM works backwards from the terminal condition, making it naturally suited to problems with early exercise or free boundaries.
