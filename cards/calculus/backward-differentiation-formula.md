# Backward Differentiation Formula

**Topic:** Calculus
**Tags:** bdf, backward differentiation, stiff ode, implicit method, a-stable, numerical integration
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Backward Differentiation Formula (BDF) methods are implicit multi-step ODE solvers that approximate the derivative using a backward-difference of past solution values, making them unconditionally stable for stiff ODEs and the industry standard in production calibration libraries.

## Key Formula

The $p$-step BDF method approximates $\dot{y}_{n+1}$ using a backward polynomial through the last $p+1$ solution values:

$$\sum_{k=0}^{p} \alpha_k\, y_{n+1-k} = h\, \beta_0\, f(t_{n+1}, y_{n+1})$$

Note $f$ is evaluated only at $t_{n+1}$ — making BDF fully implicit. The three most used variants:

**BDF1** (implicit Euler, global error $O(h)$): $y_{n+1} - y_n = h\, f_{n+1}$

**BDF2** (global error $O(h^2)$): $\tfrac{3}{2}y_{n+1} - 2y_n + \tfrac{1}{2}y_{n-1} = h\, f_{n+1}$

**BDF4** (global error $O(h^4)$): $\tfrac{25}{12}y_{n+1} - 4y_n + 3y_{n-1} - \tfrac{4}{3}y_{n-2} + \tfrac{1}{4}y_{n-3} = h\, f_{n+1}$

BDF methods are **A-stable** up to order 2 and **A($\alpha$)-stable** for orders 3–6; Adams-Moulton loses stability for orders above 2, making BDF the preferred choice for very stiff systems.

## Example

Two-factor Hull-White Riccati system with stiffness ratio $S = 200$. Adams-Moulton AM4 (A-stable only to order 4 for non-stiff systems) shows mild oscillation near $\tau = 0$. BDF4 with the same step size $h = 0.1$ remains perfectly smooth throughout, matching the exact solution to $10^{-6}$ — MATLAB's `ode15s` (BDF) and SciPy's `Radau` solver both default to BDF-family methods for exactly this reason.

## Remember

BDF is the go-to solver when Adams-Bashforth-Moulton shows instability despite using an implicit corrector step — this happens in multi-factor models where very fast mean-reverting factors push stiffness beyond what AM4 can handle stably. Production term structure libraries (QuantLib, OpenGamma) use BDF or its close relative Radau-IIA for Riccati integration precisely because the solvers are unconditionally stable regardless of how extreme the stiffness ratio becomes, allowing analysts to focus on model accuracy rather than numerical stability.
