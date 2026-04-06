# Trigonometric Equations

**Topic:** Calculus
**Tags:** trigonometry, equations, general solution, principal value, CAST diagram, periodicity
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **trigonometric equation** is an equation involving sin, cos, or tan that is solved by finding all angles satisfying it over a given range. Because trig functions are periodic, there are infinitely many solutions; the **general solution** captures them all using integer multiples of the period.

## Key Formula

**General solutions** (all solutions in $\mathbb{R}$):

$$\sin\theta = k \implies \theta = \arcsin(k) + 2n\pi \;\text{ or }\; \theta = \pi - \arcsin(k) + 2n\pi, \quad n \in \mathbb{Z}$$

$$\cos\theta = k \implies \theta = \pm\arccos(k) + 2n\pi, \quad n \in \mathbb{Z}$$

$$\tan\theta = k \implies \theta = \arctan(k) + n\pi, \quad n \in \mathbb{Z}$$

**CAST rule:** identifies which quadrants give positive values — All (I), Sine (II), Tan (III), Cos (IV).

## Example

Solve $2\sin x = \sqrt{3}$ for $0 \leq x \leq 2\pi$.

$$\sin x = \frac{\sqrt{3}}{2} \implies x = \arcsin\!\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{3}$$

Second solution (sin is also positive in quadrant II): $x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$.

Solutions: $x = \pi/3$ and $x = 2\pi/3$.

## Remember

Trigonometric equations arise in **interest rate models** when working with oscillatory term structures or seasonal adjustments. More directly, calibrating implied volatility surfaces requires solving transcendental equations — equations where the unknown appears inside a non-linear function — using exactly the same iteration strategy (bracket-and-bisect, or Newton-Raphson) that solves trigonometric equations. The general solution structure — periodically spaced roots — is also the reason option pricing under Heston's model uses a principal value convention for the complex square root, analogous to choosing the correct CAST quadrant.
