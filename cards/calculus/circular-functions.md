# Circular Functions

**Topic:** Calculus
**Tags:** circular functions, unit circle, sine, cosine, radians, periodicity, complex exponential
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **circular functions** sin and cos are defined by the coordinates of a point on the **unit circle** (radius 1, centre origin) as the angle $\theta$ is swept anticlockwise from the positive $x$-axis. For a point at angle $\theta$:

$$(\cos\theta,\, \sin\theta) = \text{coordinates on the unit circle}$$

This definition extends trigonometric ratios from right-angled triangles to all real angles $\theta \in \mathbb{R}$, making sin and cos well-defined periodic functions with period $2\pi$.

## Key Formula

**Unit circle identity:**

$$\cos^2\theta + \sin^2\theta = 1$$

This is just the equation of the unit circle $x^2 + y^2 = 1$ evaluated at $(\cos\theta, \sin\theta)$.

**Key values:**

| $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ |
|---|---|---|---|---|---|---|
| $\cos\theta$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$ | $0$ | $-1$ |
| $\sin\theta$ | $0$ | $\frac{1}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ |

**Connection to complex numbers (Euler's formula):**

$$e^{i\theta} = \cos\theta + i\sin\theta \implies \begin{cases} \cos\theta = \text{Re}(e^{i\theta}) \\ \sin\theta = \text{Im}(e^{i\theta}) \end{cases}$$

The unit circle is literally the set $\{e^{i\theta} : \theta \in \mathbb{R}\} \subset \mathbb{C}$.

## Example

The characteristic function of a distribution always has modulus $\leq 1$:

$$|\varphi_X(u)| = |E[e^{iuX}]| \leq E[|e^{iuX}|] = E[1] = 1$$

since $|e^{iuX}| = 1$ for all real $u$ and $X$ — the complex exponential $e^{iuX}$ lives on the unit circle. This is why characteristic functions always exist (their modulus is bounded), unlike moment generating functions which can diverge for fat-tailed distributions.

## Remember

The unit circle provides the geometric reason why $|e^{i\theta}| = 1$ for all real $\theta$ — the complex exponential traces the unit circle, never escaping it. This single fact explains why characteristic functions $\varphi_X(u) = E[e^{iuX}]$ are always well-defined, making them superior to MGFs for fat-tailed distributions like the Student-$t$ or stable distributions used in heavy-tail models. The unit circle also underpins the FFT algorithm — the $N$-th roots of unity $e^{2\pi i k/N}$ are equally-spaced points on the unit circle, and the FFT is essentially a clever way to evaluate sums at these points simultaneously.
