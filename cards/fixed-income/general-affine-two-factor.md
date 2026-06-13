# General Affine Two-Factor Model

**Topic:** Fixed Income
**Tags:** affine model, two-factor, bond pricing, Riccati ODE, exponential-affine, state variables
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The general affine two-factor model uses state variables $(r, l)$ (typically short rate plus a second factor) and requires that the risk-neutral drifts and squared diffusion coefficients are affine in $(r, l)$, so that zero-coupon bond prices take the exponential-affine form.

## Key Formula

$$V(r, l, t) = e^{A(t) - B(t)\,r - C(t)\,l}$$

The three scalar functions satisfy a **system of Riccati ODEs** derived by substituting the ansatz into the two-factor pricing PDE and collecting powers of $r$ and $l$:

$$\dot{B} = f_B(B, C), \qquad \dot{C} = f_C(B, C), \qquad \dot{A} = f_A(B, C)$$

with terminal conditions $A(T) = B(T) = C(T) = 0$.

The yield on a $\tau = T - t$ maturity bond is then:

$$y(\tau) = -\frac{A(t)}{\ \tau} + \frac{B(t)}{\tau}\,r + \frac{C(t)}{\tau}\,l$$

which is affine in the two state variables.

## Example

In the Longstaff–Schwartz model $r = cx + dy$ with independent CIR factors: the three-ODE system reduces to two independent single-factor Riccati ODEs (for $B$ and $C$) because the cross terms vanish under independence, and analytic solutions exist. For correlated Gaussian factors (G2++), the ODEs are linear and also solvable analytically.

## Remember

The three-ODE Riccati system must generally be solved numerically when factors are correlated and non-Gaussian. This is the primary computational cost of two-factor models versus one-factor models. In practice, the G2++ / two-factor Hull–White model is preferred on trading desks because its Gaussian structure makes the ODEs linear and analytically tractable, allowing fast calibration to both the yield curve and the swaption volatility surface.
