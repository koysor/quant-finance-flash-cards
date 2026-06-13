# Smooth Pasting Condition

**Topic:** Derivatives
**Tags:** smooth pasting, free boundary, american option, delta, no-arbitrage, value matching
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **smooth pasting condition** (also called the **high-contact condition**) requires that the derivative of the option value with respect to the underlying is continuous across the free exercise boundary $S^*(t)$. It is not an arbitrary assumption — it is a consequence of no-arbitrage: a kink in the value function at the boundary would allow a risk-free profit from a position that straddles the boundary.

## Key Formula

At the free boundary $S^*(t)$, two conditions must hold simultaneously:

$$\underbrace{V(S^*,\, t) = h(S^*,\, t)}_{\text{value matching}} \qquad \underbrace{\left.\frac{\partial V}{\partial S}\right|_{S^{*+}} = \left.\frac{\partial h}{\partial S}\right|_{S^{*-}}}_{\text{smooth pasting}}$$

For an **American put** with payoff $h(S) = K - S$, this gives $\partial h/\partial S = -1$, so:

$$\left.\frac{\partial V}{\partial S}\right|_{S^*(t)^+} = -1$$

The put delta equals $-1$ exactly at the boundary. Just inside the continuation region ($S$ slightly above $S^*$), the delta is greater than $-1$ (less negative), confirming the boundary is crossed smoothly.

## Example

American put: $K = 100$, $r = 5\%$, $\sigma = 25\%$, $\tau = 6$ months to expiry. The free boundary lies at $S^* \approx \pounds80$.

| Spot $S$ | Region | Option value $V$ | Delta $\partial V/\partial S$ |
|----------|--------|-------------------|-------------------------------|
| £78 | Exercise | £22.00 | $-1.0$ (payoff slope) |
| £80 | Boundary | £20.00 | $-1.0$ (smooth pasting) |
| £82 | Continuation | £19.15 | $-0.91$ (Black-Scholes PDE) |
| £90 | Continuation | £13.20 | $-0.68$ |

Delta transitions smoothly through $-1$ at the boundary — there is no jump.

## Remember

Smooth pasting is the condition that makes the free-boundary problem well-posed: value matching alone leaves one equation short of pinning down both $V$ and $S^*$, so smooth pasting provides the second equation. The no-arbitrage proof is the intuition: if a kink existed (delta jumped at $S^*$), an investor could earn a risk-free profit by buying and selling an infinitesimal straddle centred at $S^*$. In practice, smooth pasting is implemented numerically by finding the price node where the PDE solution and the payoff function are tangent — if the grid is too coarse, the boundary is mislocated and the option delta just inside the continuation region diverges from $-1$, a diagnostic that experienced quants use to verify that the exercise boundary is correctly resolved.
