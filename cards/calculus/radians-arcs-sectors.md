# Radians, Arcs, and Sectors

**Topic:** Calculus
**Tags:** radians, arc length, sector area, angle, circle, angular frequency, Fourier
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **radian** is the angle subtended at the centre of a circle by an arc whose length equals the radius. There are $2\pi$ radians in a full turn ($360°$). For a circle of radius $r$, the arc length $s$ and sector area $A$ subtended by angle $\theta$ (in radians) are given by simple formulae.

## Key Formula

**Conversion:** $\theta \text{ (rad)} = \theta° \times \frac{\pi}{180}$

**Arc length:** $s = r\theta$

**Sector area:** $A = \tfrac{1}{2}r^2\theta$

**Key values:**

| Degrees | $30°$ | $45°$ | $60°$ | $90°$ | $180°$ | $360°$ |
|---|---|---|---|---|---|---|
| Radians | $\pi/6$ | $\pi/4$ | $\pi/3$ | $\pi/2$ | $\pi$ | $2\pi$ |

## Example

A sector has radius $r = 8$ cm and angle $\theta = \pi/6$ rad.

Arc length: $s = 8 \times \frac{\pi}{6} = \frac{4\pi}{3} \approx 4.19$ cm.

Sector area: $A = \frac{1}{2}(8^2)\frac{\pi}{6} = \frac{32\pi}{6} = \frac{16\pi}{3} \approx 16.76$ cm².

## Remember

Radians are mandatory in calculus because the derivative formula $\frac{d}{dx}\sin(x) = \cos(x)$ holds only when $x$ is measured in radians. In quantitative finance, **Fourier transforms** use **angular frequency** $\omega$ measured in radians per unit time — the characteristic function $\varphi(\omega) = E[e^{i\omega X}]$ integrates over $\omega \in \mathbb{R}$ in radians. The arc-length formula $s = r\theta$ also underpins the small-angle approximation ($\sin\theta \approx \theta$) used to linearise bond duration formulas and option Greeks near the money.
