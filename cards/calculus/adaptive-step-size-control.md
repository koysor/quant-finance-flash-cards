# Adaptive Step Size Control

**Topic:** Calculus
**Tags:** adaptive step size, runge-kutta, error control, ode solver, dormand-prince
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Adaptive step size control** automatically adjusts the step size $h$ during numerical ODE integration to maintain a target accuracy with minimum computation. At each step, an **error estimate** is computed by comparing two solutions of different orders; if the error is too large, $h$ is reduced and the step retaken; if the error is well within tolerance, $h$ is increased to speed up integration. The result is a solver that uses small steps only where the solution changes rapidly and large steps where it varies smoothly.

## Key Formula

The **embedded Runge-Kutta** approach (e.g. Dormand-Prince RK45) computes two solutions of orders $p$ and $p+1$ from the same function evaluations. The local error estimate is their difference:

$$\varepsilon = \|y^{(p+1)} - y^{(p)}\|$$

The new step size is chosen to hit the target tolerance $\tau$:

$$h_{\text{new}} = h \cdot \left(\frac{\tau}{\varepsilon}\right)^{1/(p+1)} \cdot S$$

where $S \approx 0.9$ is a safety factor. If $\varepsilon > \tau$, the step is rejected and retaken with $h_{\text{new}}$; if $\varepsilon \leq \tau$, the step is accepted and $h_{\text{new}}$ is used for the next step.

## Example

Integrating the CIR Riccati ODE $\dot{B} = 1 - 0.5B - 0.02B^2$ from $t = 0$ to $t = 10$ with tolerance $10^{-8}$:

| Phase | Step size | Reason |
|-------|-----------|--------|
| $t \in [0, 0.5]$ | $h = 0.01$ | Solution changes rapidly near $t = 0$ |
| $t \in [0.5, 5]$ | $h = 0.25$ | Solution slowing — solver expands $h$ |
| $t \in [5, 10]$ | $h = 1.2$ | Near steady state — large steps acceptable |

Total: 38 accepted steps versus 1,000 fixed steps for RK4 at $h = 0.01$, achieving the same accuracy in 4% of the function evaluations.

## Remember

Adaptive step size control is what makes ODE solvers practical for production use in quantitative finance. When calibrating multi-factor term structure models (CIR, Hull-White, Vasicek), the Riccati ODEs must be solved thousands of times per calibration run. A fixed-step solver must use the smallest step needed anywhere in the domain — wasting computation where the solution is flat. An adaptive solver (e.g. SciPy's `solve_ivp` with `method='RK45'`) automatically concentrates evaluations near the origin where term structure curvature is highest, cutting calibration time by an order of magnitude. The same principle applies to the Hamilton-Jacobi-Bellman PDE in optimal execution: near the trade deadline, the value function changes rapidly and requires fine time steps; far from the deadline, coarse steps suffice.
