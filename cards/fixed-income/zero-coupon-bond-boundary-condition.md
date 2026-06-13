# Zero-Coupon Bond Boundary Condition

**Topic:** Fixed Income
**Tags:** zero-coupon bond, boundary condition, pricing PDE, terminal condition, bond pricing
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **zero-coupon bond boundary condition** is the terminal condition $V(r,T) = 1$ imposed on the fixed-income pricing PDE. It specifies that the bond pays exactly £1 at maturity $T$ regardless of the level of the spot rate, and distinguishes the zero-coupon bond from all other fixed-income instruments whose final conditions differ.

## Key Formula

At maturity $t = T$:

$$V(r, T) = 1 \quad \forall\, r$$

The PDE is solved **backwards** from this terminal condition to $t = 0$.

| Instrument | Final condition at $t = T$ |
|---|---|
| Zero-coupon bond | $V(r,T) = 1$ |
| Coupon bond | $V(r,T) = 1 + \text{final coupon}$ |
| Interest rate cap/floor | $V(r,T) = \max(r - K, 0)$ or $\max(K - r, 0)$ |
| Callable bond | $\min(\text{call price}, V_{\text{non-callable}})$ |

Once $V(r,t)$ is obtained, the **continuously compounded yield to maturity** $Y$ is:

$$Y(r,t;T) = -\frac{\ln V(r,t;T)}{T - t}$$

## Example

Under the Vasicek model the solution with $V(r,T) = 1$ is $V = e^{A(\tau) - B(\tau)r}$ where $\tau = T - t$, $B(\tau) = (1 - e^{-\gamma\tau})/\gamma$, and $A(\tau)$ is a deterministic function of parameters. At $\tau = 0$: $B(0) = 0$, $A(0) = 0$, so $V = e^0 = 1$ — the boundary condition is automatically satisfied.

## Remember

The final condition plays exactly the same role as the payoff function in the Black–Scholes option pricing equation: it pins the solution at maturity and the PDE propagates values backwards through time. The elegant consequence is that one model (one set of parameters $\eta, \gamma, \beta, \lambda$) prices the entire yield curve simultaneously — just solve the same PDE with different maturities $T$.
