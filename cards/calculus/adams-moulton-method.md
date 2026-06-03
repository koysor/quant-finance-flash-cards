# Adams-Moulton Method

**Topic:** Calculus
**Tags:** adams-moulton, implicit corrector, predictor-corrector, numerical ode, stability, error estimation
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Adams-Moulton methods are implicit multi-step ODE solvers that use the next function value as a corrector step after an Adams-Bashforth predictor, achieving higher accuracy and better stability than the explicit predictor alone with only one extra function evaluation per step.

## Key Formula

**AM4** (4-step corrector, global error $O(h^5)$):

$$y_{n+1} = y_n + \frac{h}{720}\bigl(251f_{n+1} + 646f_n - 264f_{n-1} + 106f_{n-2} - 19f_{n-3}\bigr)$$

In the **Adams-Bashforth-Moulton (ABM) predictor-corrector** scheme:

1. **Predict** $\tilde{y}_{n+1}$ using AB4 (1 function evaluation)
2. **Evaluate** $\tilde{f}_{n+1} = f(t_{n+1}, \tilde{y}_{n+1})$
3. **Correct** using AM4 with $\tilde{f}_{n+1}$ in place of $f_{n+1}$ (1 more evaluation)

The local error estimate is free: $\lvert y_{n+1}^{\text{AM}} - \tilde{y}_{n+1}^{\text{AB}} \rvert \approx C h^5$ — enabling automatic step-size control without extra evaluations.

## Example

ABM applied to the CIR Riccati ODE $\dot{B} = 1 - 0.5B - 0.02B^2$ with $h = 0.1$ over 100 steps. After 4 RK4 start-up steps (16 evaluations): each subsequent ABM step costs 2 evaluations, giving total $16 + 96 \times 2 = 208$. Global error: $\sim 10^{-5}$ versus $\sim 10^{-4}$ for RK4 at 400 evaluations. ABM achieves 10× better accuracy at 52% of the function evaluation cost.

## Remember

The ABM predictor-corrector provides a free local error estimate at every step: the discrepancy between the AB4 prediction and the AM4 correction measures the integration error without any extra function evaluations. In ATSM calibration, where the Riccati ODE changes curvature near short maturities (high $\kappa$) but flattens at long ones, adaptive step-size control using this built-in error estimate automatically concentrates evaluations where the ODE is hardest — further reducing total computation versus fixed-step RK4.
