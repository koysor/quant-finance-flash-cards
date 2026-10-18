# Forming a Differential Equation from a General Solution

**Topic:** Calculus
**Tags:** ODE, general solution, arbitrary constants, elimination, verification
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Forming a differential equation is the reverse of solving one: given a family of curves with $n$ arbitrary constants, find the $n$th-order differential equation that every member of the family satisfies. The method is to differentiate $n$ times and eliminate the constants.

## Key Formula

$$n \text{ arbitrary constants} \;\Longrightarrow\; n\text{th-order differential equation, containing no constants}$$

The count of constants predicts the order. The result must contain none of the original constants.

## Example

Find the equation satisfied by $y = Ae^{2x} + Be^{-3x}$. Two constants, so expect second order.

$$y' = 2Ae^{2x} - 3Be^{-3x}, \qquad y'' = 4Ae^{2x} + 9Be^{-3x}$$

Form $y'' + y' - 6y$: the $A$ terms give $(4 + 2 - 6)Ae^{2x} = 0$ and the $B$ terms give $(9 - 3 - 6)Be^{-3x} = 0$. Hence

$$y'' + y' - 6y = 0$$

## Remember

This is the skill behind checking that a proposed price function really satisfies the model's PDE. For example, $V = S$ (a share itself) has $V_t = 0$, $V_S = 1$, $V_{SS} = 0$, so the Black-Scholes equation gives $0 + 0 + rS - rS = 0$: the stock is a valid price. A candidate that fails this substitution is not an arbitrage-free price.
