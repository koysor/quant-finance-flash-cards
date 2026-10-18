# Euler (Equidimensional) Equations

**Topic:** Calculus
**Tags:** ODE, Euler equation, variable coefficients, indicial equation, Black-Scholes, perpetual option
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

An **Euler equation** is a linear ODE with variable coefficients in which each derivative $y^{(k)}$ carries the matching power $x^k$. The trial solution is $y = x^m$ (not $e^{mx}$), which turns the equation into a quadratic **indicial equation** in $m$.

## Key Formula

$$x^2 y'' + a\,x\,y' + b\,y = 0 \;\longrightarrow\; m(m - 1) + am + b = 0$$

| Indicial roots | General solution |
|---|---|
| Real and distinct, $m_1 \neq m_2$ | $Ax^{m_1} + Bx^{m_2}$ |
| Repeated, $m$ | $x^{m}\,(A + B\ln x)$ |
| Complex, $\alpha \pm i\beta$ | $x^{\alpha}\bigl(A\cos(\beta\ln x) + B\sin(\beta\ln x)\bigr)$ |

## Example

Solve $x^2 y'' - 4xy' + 6y = 0$. The indicial equation is $m(m - 1) - 4m + 6 = m^2 - 5m + 6 = 0$, so $m = 2$ or $3$ and

$$y = Ax^2 + Bx^3$$

## Remember

The Black-Scholes equation has exactly this structure in $S$: $\tfrac{1}{2}\sigma^2 S^2 V_{SS}$ is an $S^2$ times a second derivative and $rSV_S$ is an $S$ times a first derivative. For the perpetual American option, with no time dependence, $V = S^m$ gives $\tfrac{1}{2}\sigma^2 m(m - 1) + rm - r = 0$, which is why the price has a power-law form in $S$.
