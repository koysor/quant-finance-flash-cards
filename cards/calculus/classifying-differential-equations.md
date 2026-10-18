# Classifying Differential Equations

**Topic:** Calculus
**Tags:** ODE, order, linear, homogeneous, classification, PDE
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Classifying a differential equation means naming its **order** (the highest derivative present), whether it is **linear** (the unknown function and its derivatives appear only to the first power and are never multiplied together), whether it is **homogeneous** (no term free of the unknown), and whether it is an **ODE** (one independent variable) or a **PDE** (several). The classification decides which solution method applies.

## Key Formula

The general linear ODE of order $n$ is

$$a_n(x)\,y^{(n)} + \cdots + a_1(x)\,y' + a_0(x)\,y = g(x)$$

It is **homogeneous** when $g(x) = 0$ and has **constant coefficients** when every $a_i$ is a constant.

## Example

| Equation | Order | Linear? |
|---|---|---|
| $y'' + 3y' + 2y = e^x$ | 2 | Yes, constant coefficients, non-homogeneous |
| $y' = x^2 y$ | 1 | Yes ($y$ appears to the first power) |
| $y' = y^2$ | 1 | **No** (the $y^2$ term) |
| $(y')^2 = x + y$ | 1 | No (derivative squared) |
| $x^2 y'' - 2xy' + 2y = 4x^3$ | 2 | Yes, variable coefficients |

The Black-Scholes equation $V_t + \tfrac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$ is second order, linear, with variable coefficients, and is a **PDE** because $V$ depends on both $S$ and $t$.

## Remember

Classify first, solve second. Linearity is what makes the Black-Scholes PDE tractable: solutions can be superposed, so a portfolio of options is priced by adding the prices of its parts. Applying an integrating factor to a non-linear equation such as $y' = y^2$ is the commonest wasted half-hour.
