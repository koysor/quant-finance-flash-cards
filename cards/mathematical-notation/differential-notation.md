# Differential Notation

**Topic:** Mathematical Notation
**Tags:** notation, differential, delta, calculus, stochastic
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Differential notation** uses variations of the letter "d" to express different kinds of change. The three symbols $\Delta$, $\delta$, and $d$ represent progressively smaller changes, while the distinction between $d$ and $\partial$ signals whether one or many variables are involved.

| Symbol | Read as | Meaning |
|---|---|---|
| $\Delta x$ | "delta $x$" | Finite change in $x$ (any size) |
| $\delta x$ | "delta $x$" (small) | Small but finite change; used in variational calculus |
| $dx$ | "$dx$" | Infinitesimal change in $x$; limit as $\Delta x \to 0$ |
| $df$ | "total differential" | Full change in $f$: $df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$ |
| $\partial f$ | "partial of $f$" | Change in $f$ due to one variable only |
| $dW_t$ | "$dW_t$" | Brownian increment; $dW_t \sim N(0, dt)$ |

## Key Formula

**Total differential** of $f(x, y)$:

$$df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy$$

**Itô differential** of $f(S, t)$ where $dS = \mu S\,dt + \sigma S\,dW$:

$$df = \left(\frac{\partial f}{\partial t} + \mu S\frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 f}{\partial S^2}\right)dt + \sigma S\frac{\partial f}{\partial S}\,dW$$

The extra $\frac{1}{2}\sigma^2 S^2 f_{SS}$ term arises because $(dW)^2 = dt \neq 0$.

## Example

A stock price changes from £100 to £102: $\Delta S = £2$.

In the Black–Scholes framework, the infinitesimal version is:

$$dS = \mu S\,dt + \sigma S\,dW_t$$

For $\mu = 0.08$, $\sigma = 0.20$, $S = 100$, over $dt = 1/252$:

- Expected $dt$ component: $0.08 \times 100 \times (1/252) = £0.032$
- Random $dW$ component: $0.20 \times 100 \times \sqrt{1/252} \approx £1.26$ per standard deviation

## Remember

The notation $d$ versus $\Delta$ signals whether you are working in continuous or discrete time — and this distinction matters enormously in finance. A $\Delta$-hedged portfolio rebalances at finite intervals and carries hedging error; the Black–Scholes argument uses $d$ (continuous rebalancing) to eliminate risk entirely. When you see $dW_t$ rather than $dt$, it indicates a stochastic (random) source of change — and the multiplication rule $dW \cdot dW = dt$ is the reason Itô calculus differs from ordinary calculus. Confusing $d$ and $\partial$ is a common error: $df$ includes contributions from all variables, while $\partial f / \partial S$ isolates one.
