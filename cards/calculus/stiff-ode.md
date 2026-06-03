# Stiff ODE

**Topic:** Calculus
**Tags:** stiff ode, implicit method, numerical stability, mean reversion, multi-timescale, step size
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

A stiff ODE contains solution components that decay at vastly different rates; explicit solvers are forced to use a step size governed by the fastest component, making implicit methods necessary for efficient integration when the fastest timescale is much shorter than the timescale of interest.

## Key Formula

The canonical stiffness test is $\dot{y} = \lambda y$ with $\text{Re}(\lambda) \ll 0$. The explicit Euler stability condition requires:

$$h \leq \frac{2}{|\lambda|}$$

For a fast mode with $\lambda = -1000$, this demands $h \leq 0.002$ even if the solution of interest evolves on a timescale of $\sim 1$. The **stiffness ratio** $S = |\lambda_{\text{fast}}| / |\lambda_{\text{slow}}|$ measures the severity: explicit methods need $S \times$ more steps than accuracy alone requires.

The implicit Euler method $y_{n+1} = y_n/(1 - h\lambda)$ is **unconditionally A-stable** — convergent for any $h > 0$ regardless of $|\lambda|$. Adams-Moulton (AM4) and backward differentiation formula (BDF) methods extend this stability to high-order accuracy.

## Example

Two-factor Hull-White (G2++) with $a = 0.01$ (slow level factor) and $b = 2.0$ (fast short-rate factor): stiffness ratio $S = 200$. Explicit RK4 integration of the Riccati system requires $h \leq 0.001$ for stability of the fast component — 10,000 steps to reach $\tau = 10$. The implicit AM4 scheme integrates stably at $h = 0.1$ in 100 steps, achieving the same accuracy 100× faster.

## Remember

When a multi-factor term structure model "blows up" numerically or demands absurdly small step sizes during calibration, the root cause is almost always stiffness: the model has factors with very different mean-reversion speeds (e.g. a fast 3-month factor at $\kappa = 5$ and a slow level factor at $\kappa = 0.05$, giving $S = 100$). Reducing the step size treats the symptom; switching to an unconditionally stable implicit solver (Adams-Moulton, BDF) fixes the cause and is the standard approach in production term structure calibration libraries.
