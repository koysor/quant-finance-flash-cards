# Cosine

**Topic:** Calculus
**Tags:** cosine, cos, trigonometry, periodic, Fourier, characteristic function, even function
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **cosine function** $\cos(\theta)$ is defined as the $x$-coordinate of the point on the unit circle at angle $\theta$ from the positive $x$-axis. It is a periodic, even function with period $2\pi$, range $[-1, 1]$, and $\cos(0) = 1$.

## Key Formula

$$\cos(\theta) = \frac{\text{adjacent}}{\text{hypotenuse}} \quad \text{(right triangle)}, \qquad \cos(\theta) = \text{Re}(e^{i\theta}) \quad \text{(unit circle)}$$

**Derivative and integral:**

$$\frac{d}{d\theta}\cos(\theta) = -\sin(\theta), \qquad \int \cos(\theta)\, d\theta = \sin(\theta) + C$$

**Key values:** $\cos(0) = 1$, $\cos(\pi/3) = \tfrac{1}{2}$, $\cos(\pi/4) = \tfrac{1}{\sqrt{2}}$, $\cos(\pi/2) = 0$, $\cos(\pi) = -1$

**Taylor series:**

$$\cos(\theta) = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n \theta^{2n}}{(2n)!}$$

**Even function:** $\cos(-\theta) = \cos(\theta)$

**Euler representation:**

$$\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$$

## Example

For a symmetric distribution (e.g. standard normal $Z$), the characteristic function is purely real:

$$\varphi_Z(u) = E[e^{iuZ}] = E[\cos(uZ)] + i\,E[\sin(uZ)] = E[\cos(uZ)]$$

since $E[\sin(uZ)] = 0$ by symmetry. For $Z \sim \mathcal{N}(0,1)$:

$$\varphi_Z(u) = e^{-u^2/2}$$

This is the cosine transform of the normal PDF — a purely real, even function of $u$, reflecting the symmetry of the distribution. The characteristic function of any symmetric distribution is always a real-valued even function.

## Remember

$\cos$ is the **real part** of $e^{i\theta}$ via Euler's formula. In characteristic function pricing, $E[\cos(uX)]$ is the real part of $\varphi_X(u)$. Because $\cos$ is even — $\cos(-\theta) = \cos(\theta)$ — it contributes the symmetric component of the distribution. Cosine dominates for symmetric distributions (where the imaginary part vanishes), but for skewed distributions (e.g. the Heston model's log-price), both $\cos$ and $\sin$ components are non-zero and the full complex characteristic function must be used.
