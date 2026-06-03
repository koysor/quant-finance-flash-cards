# Riccati ODE

**Topic:** Calculus
**Tags:** riccati ode, ordinary differential equation, affine term structure, optimal control, nonlinear ode
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Riccati ODE is a first-order nonlinear ordinary differential equation of the form $\dot{y} = a(t) + b(t)y + c(t)y^2$; it arises in affine term structure models (determining bond price factor loadings) and in optimal control (determining feedback gain matrices), and has a closed-form solution when $c(t) = 0$.

## Key Formula

In affine term structure models, the bond price $P(t,T) = e^{A(\tau) - B(\tau)r_t}$ requires solving a Riccati ODE for $B(\tau)$ (with $\tau = T - t$):

$$\frac{dB}{d\tau} = 1 - \kappa B - \tfrac{1}{2}\sigma^2 B^2, \qquad B(0) = 0$$

When $\sigma = 0$ (Gaussian/Vasicek-type), the $B^2$ term vanishes and the linear ODE solves analytically:

$$B(\tau) = \frac{1 - e^{-\kappa\tau}}{\kappa}$$

For the CIR square-root model ($\sigma \neq 0$), the full nonlinear Riccati equation must be solved; a closed form exists but involves hyperbolic functions. Multi-factor models generally require numerical ODE integration.

## Example

Vasicek model with $\kappa = 0.20$: $B(2) = (1 - e^{-0.4})/0.20 = 1.65$. This means a 1% rise in the short rate increases the 2-year bond yield by $B(2)/2 = 0.825\%$ — 82.5bp — and reduces the bond price by approximately $1.65 \times 0.01 = 1.65\%$. Computing this takes microseconds once $\kappa$ is known, versus simulating thousands of Monte Carlo paths for models without a Riccati solution.

## Remember

The Riccati ODE is the mathematical gatekeeper of affine term structure model speed. Gaussian models (Vasicek, Hull-White, two-factor G2++) have $c = 0$, so $B(\tau)$ is a simple exponential formula that evaluates instantly — this is why these models are the workhorses of interest rate trading desks. Square-root models (CIR, multi-factor square-root) introduce a $B^2$ term that requires numerical integration at every calibration step, making them significantly slower to fit to market data. Choosing between model richness and calibration speed ultimately comes down to whether the Riccati ODE has a closed form.
