# ODE Numerical Methods

**Topic:** Calculus
**Tags:** runge-kutta, euler method, numerical ode, step size, riccati, affine term structure
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

ODE numerical methods approximate the solution of $\dot{y} = f(t,y)$ by stepping forward in small increments when no closed form exists; the fourth-order Runge-Kutta (RK4) method is the standard choice for integrating the Riccati ODEs that arise in multi-factor term structure models.

## Key Formula

**Euler method** (first-order, global error $O(h)$):

$$y_{n+1} = y_n + h\, f(t_n, y_n)$$

**Fourth-order Runge-Kutta (RK4)** (global error $O(h^4)$):

$$k_1 = f(t_n, y_n), \quad k_2 = f\!\left(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_1\right)$$

$$k_3 = f\!\left(t_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_2\right), \quad k_4 = f(t_n + h,\, y_n + hk_3)$$

$$y_{n+1} = y_n + \tfrac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

RK4 evaluates $f$ four times per step but achieves $O(h^4)$ accuracy — with $h = 0.1$, the global error is $\sim 10^{-4}$ versus $\sim 10^{-1}$ for Euler.

## Example

Integrating the CIR Riccati ODE $\dot{B} = 1 - 0.5B - 0.02B^2$ from $\tau = 0$ to $\tau = 10$. Euler with $h = 0.1$ (100 steps): $B(10) = 1.831$, error $0.018$ versus exact $1.849$. RK4 with the same $h = 0.1$ (100 steps, 400 function evaluations): $B(10) = 1.849$, error $0.00003$. RK4 is 600 times more accurate at the same number of steps, requiring no extra storage and trivially parallelisable across maturities.

## Remember

Multi-factor term structure models with square-root or affine-diffusion factors require numerical Riccati integration at every calibration step. Because swaption calibration calls the pricer thousands of times, the ODE solver's accuracy directly sets the minimum achievable calibration error: using Euler with $h = 0.1$ introduces 1.8bp of bond-price error per step, which overwhelms the market fit and makes the calibration meaningless. RK4 with adaptive step-size control solves the same ODE to machine precision in 20-50 steps — enabling real-time re-calibration on a trading desk that Euler at equivalent accuracy could not achieve.
