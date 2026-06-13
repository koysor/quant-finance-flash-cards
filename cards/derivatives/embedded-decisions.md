# Embedded Decisions

**Topic:** Derivatives
**Tags:** embedded decisions, early exercise, free boundary, linear complementarity, optimal stopping, american option
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An **embedded decision** is a contractual right for one party to take a specific action — exercise, call, convert, prepay — at specified times during a financial contract's life. The party holding the decision right acts optimally, which converts the standard pricing PDE into a **free boundary problem**: the boundary between "act now" and "wait" is itself unknown and must be found as part of the solution.

## Key Formula

An embedded decision transforms the Black-Scholes PDE into a **linear complementarity problem**. For a holder's optimal decision with payoff $h(S, t)$:

$$\min\!\bigl(\mathcal{L}V,\;\; V - h\bigr) = 0$$

where $\mathcal{L}V = \dfrac{\partial V}{\partial t} + \dfrac{1}{2}\sigma^2 S^2 \dfrac{\partial^2 V}{\partial S^2} + rS\dfrac{\partial V}{\partial S} - rV$.

This states: either the PDE holds (holder waits, option alive), or the option equals its payoff (holder has exercised). Both cannot fail simultaneously. The free boundary $S^*(t)$ is located by the **smooth-pasting conditions**:

$$V(S^*(t),\, t) = h(S^*(t),\, t), \qquad \left.\frac{\partial V}{\partial S}\right|_{S^*(t)} = \left.\frac{\partial h}{\partial S}\right|_{S^*(t)}$$

## Example

A Bermudan swaption has exercise dates at $t_1 = 1$, $t_2 = 2$, $t_3 = 3$ years. At each date the holder compares:

- **Exercise value**: present value of the swap entered now (e.g. £3.2m if rates are currently 5% against a strike of 3.5%)
- **Continuation value**: the value of the right to exercise at $t_2$ and $t_3$, computed by backward induction (e.g. £3.8m)

At $t_1$ the holder does not exercise because £3.8m > £3.2m. At $t_2$, with rates now at 5.5%, the exercise value rises to £5.1m and the continuation value (only one date left) is £4.7m — so the holder exercises. This sequential backward computation is the exact structure of the embedded decision problem.

## Remember

Embedded decisions appear throughout financial markets: American options (holder's exercise right), callable bonds (issuer's refinancing right), mortgage-backed securities (homeowner's prepayment right), and Bermudan swaptions (the dominant exotic in rates). The computational cost of handling embedded decisions is the main reason these products require numerical methods — backward induction on a tree or finite-difference grid, or the Longstaff-Schwartz Monte Carlo algorithm. Getting the exercise boundary wrong introduces systematic mispricing: a too-early boundary overstates the option value, while a too-late boundary understates it, and the error feeds directly into hedge ratios and risk limits reported to senior management.
