# Initial and Boundary Value Problems

**Topic:** Calculus
**Tags:** ODE, initial value problem, boundary value problem, terminal condition, general solution
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The general solution of an ODE contains arbitrary constants; extra conditions pin them down. In an **initial value problem** (IVP) all conditions are given at one point, so the problem is solved forward from there. In a **boundary value problem** (BVP) the conditions are given at two different points. A **terminal value problem** specifies the conditions at the end and is solved backwards.

## Key Formula

$$\text{IVP: } y(a),\; y'(a) \text{ given} \qquad\qquad \text{BVP: } y(a),\; y(b) \text{ given}$$

An IVP typically has exactly one solution. A BVP may have none, one, or infinitely many.

## Example

IVP: $y'' = 6x$ with $y(0) = 1$ and $y'(0) = 2$. Integrating twice gives $y = x^3 + c_1 x + c_2$; the conditions give $c_1 = 2$ and $c_2 = 1$, so $y = x^3 + 2x + 1$.

BVP: $y'' + y = 0$ has general solution $y = A\cos x + B\sin x$. With $y(0) = 0$ and $y(\pi) = 0$, $A = 0$ and $B$ is free: infinitely many solutions. With $y(0) = 0$ and $y(\pi) = 1$ there is no solution.

## Remember

A European option is a terminal value problem: the data is the payoff at expiry, $V(S, T) = \max(S - K, 0)$ for a call, together with boundary conditions as $S \to 0$ and $S \to \infty$. You solve backwards from $T$ to today. The payoff and boundary behaviour, not the PDE itself, are what distinguish a call from a put.
