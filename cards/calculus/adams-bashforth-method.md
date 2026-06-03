# Adams-Bashforth Method

**Topic:** Calculus
**Tags:** adams-bashforth, multistep method, numerical ode, explicit solver, predictor, efficiency
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Adams-Bashforth methods are explicit multi-step ODE solvers that fit a polynomial through the last $p$ function evaluations and extrapolate it one step forward, achieving the same high-order accuracy as Runge-Kutta while requiring only one new function evaluation per step after start-up.

## Key Formula

The $p$-step Adams-Bashforth method takes the form:

$$y_{n+1} = y_n + h \sum_{k=0}^{p-1} b_k\, f(t_{n-k},\, y_{n-k})$$

The two most common variants are:

**AB2** (2-step, global error $O(h^2)$):
$$y_{n+1} = y_n + \tfrac{h}{2}(3f_n - f_{n-1})$$

**AB4** (4-step, global error $O(h^4)$):
$$y_{n+1} = y_n + \tfrac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

AB4 matches RK4's $O(h^4)$ accuracy but uses **1 function evaluation per step** (versus 4 for RK4) once the first 4 steps have been seeded with a single-step method.

## Example

Integrating the Vasicek bond ODE $\dot{B} = 1 - 0.2B$ from $\tau = 0$ to $\tau = 10$ with $h = 0.1$. Four RK4 start-up steps require $4 \times 4 = 16$ evaluations. The remaining 96 AB4 steps require 96 evaluations. Total: 112 evaluations. Pure RK4 over the same 100 steps requires $100 \times 4 = 400$ evaluations — AB4 gives the same accuracy at 28% of the computational cost.

## Remember

When calibrating a multi-factor term structure model, the Riccati ODE must be integrated once per maturity bucket for every trial parameter set — potentially thousands of integrations per calibration run. Switching from RK4 to AB4 reduces function evaluations by 75% per integration, which can shrink a 4-minute swaption calibration to under 1 minute without any loss of accuracy. The efficiency gain is largest when the ODE right-hand side is expensive to evaluate, as in multi-dimensional square-root or affine-diffusion processes.
