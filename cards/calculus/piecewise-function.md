# Piecewise Function

**Topic:** Calculus
**Tags:** piecewise function, discontinuity, payoff, option, step function, modulus
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **piecewise function** is defined by different expressions on different parts of its domain. Each piece applies over a specified interval, and the function's behaviour can change abruptly at the **breakpoints** between pieces. A piecewise function may be continuous (the pieces join smoothly) or discontinuous (there is a jump at a breakpoint).

## Key Formula

**General form:**

$$f(x) = \begin{cases} f_1(x) & x < a \\ f_2(x) & a \leq x < b \\ f_3(x) & x \geq b \end{cases}$$

**Modulus function** as a piecewise function:

$$|x| = \begin{cases} x & x \geq 0 \\ -x & x < 0 \end{cases}$$

**Call option payoff** at expiry — the most important piecewise function in derivatives:

$$C_T = \max(S_T - K,\, 0) = \begin{cases} S_T - K & S_T > K \\ 0 & S_T \leq K \end{cases}$$

Differentiation must be applied piece-by-piece; the derivative may not exist at breakpoints.

## Example

A structured product pays:

$$V(S_T) = \begin{cases} 0 & S_T < 80 \\ S_T - 80 & 80 \leq S_T < 120 \\ 40 & S_T \geq 120 \end{cases}$$

This is a capped call (bull spread): participation in upside between 80 and 120, floored at zero below 80, and capped at 40 above 120. Each piece is linear, but the overall payoff is a piecewise linear function with kinks at $S_T = 80$ and $S_T = 120$.

The delta is:

$$\Delta = \frac{dV}{dS_T} = \begin{cases} 0 & S_T < 80 \\ 1 & 80 \leq S_T < 120 \\ 0 & S_T \geq 120 \end{cases}$$

## Remember

Every vanilla option payoff is piecewise: zero below the strike, linear above it. This single kink at the strike makes the payoff non-differentiable at $S_T = K$, which is why the Black-Scholes PDE is solved in the smooth region $S \neq K$ and the payoff is applied as a **boundary condition** rather than differentiated directly. Piecewise linear payoffs (digitals, barriers, spreads) require special handling in finite-difference solvers — the kink must be aligned with a grid node to avoid oscillation errors in the computed Greeks.
