# Exponential-Affine Ansatz

**Topic:** Fixed Income
**Tags:** exponential-affine, ansatz, bond pricing, ODE, Vasicek, affine model, analytical solution
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **exponential-affine ansatz** is the trial solution $V(r,t) = e^{A(t) - rB(t)}$ substituted into the fixed-income pricing PDE for one-factor models. When the risk-neutral drift is linear in $r$ and the variance is affine in $r$, this substitution eliminates the partial derivatives in $r$ and reduces the PDE to a **pair of ordinary differential equations** (ODEs) for the scalar functions $A(t)$ and $B(t)$.

## Key Formula

Substitute $V = e^{A(t) - rB(t)}$ into the pricing PDE. Dividing by $V$ and collecting powers of $r$:

$$\underbrace{\dot{A} + \tfrac{1}{2}\beta B^2 - \eta B}_{\text{coefficient of }r^0} + r\underbrace{\left(-\dot{B} + \gamma B - 1\right)}_{\text{coefficient of }r^1} = 0$$

Since this must hold for all $r$, both brackets are zero simultaneously:

$$\dot{B} = \gamma B - 1, \qquad A(T) = 0,\; B(T) = 0$$
$$\dot{A} = \eta B - \tfrac{1}{2}\beta B^2, \qquad A(T) = 0$$

The factor $B(t)$ measures the bond price's sensitivity to the spot rate $r$ (duration-like); $A(t)$ captures the convexity/mean-reversion adjustment.

## Example

For Vasicek with $\gamma = 0.4$, $\eta = 0.02$, $\beta = 0.0001$, the ODE for $B$ has the closed-form solution $B(\tau) = (1 - e^{-0.4\tau})/0.4$ where $\tau = T - t$. At $\tau = 5$ years: $B(5) = (1 - e^{-2})/0.4 = 2.162$. The bond price decreases by 2.162 × (basis point change in $r$) per basis point — this is the $r$-dollar duration.

## Remember

The exponential-affine ansatz is the trick that makes Vasicek, CIR, and Hull–White analytically tractable. The reduction from a PDE (two variables, $r$ and $t$) to ODEs (one variable, $t$) is only possible when the risk-neutral drift is **linear** in $r$ and the diffusion coefficient squared is **affine** in $r$. These two conditions define the entire affine term structure class.
