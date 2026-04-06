# Sine

**Topic:** Calculus
**Tags:** sine, sin, trigonometry, periodic, Fourier, wave, oscillation
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **sine function** $\sin(\theta)$ is defined as the $y$-coordinate of the point on the unit circle at angle $\theta$ from the positive $x$-axis. It is a periodic, odd function with period $2\pi$, range $[-1, 1]$, and $\sin(0) = 0$.

## Key Formula

$$\sin(\theta) = \frac{\text{opposite}}{\text{hypotenuse}} \quad \text{(right triangle)}, \qquad \sin(\theta) = \text{Im}(e^{i\theta}) \quad \text{(unit circle)}$$

**Derivative and integral:**

$$\frac{d}{d\theta}\sin(\theta) = \cos(\theta), \qquad \int \sin(\theta)\, d\theta = -\cos(\theta) + C$$

**Key values:** $\sin(0) = 0$, $\sin(\pi/6) = \tfrac{1}{2}$, $\sin(\pi/4) = \tfrac{1}{\sqrt{2}}$, $\sin(\pi/2) = 1$, $\sin(\pi) = 0$

**Taylor series:**

$$\sin(\theta) = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}$$

**Odd function:** $\sin(-\theta) = -\sin(\theta)$

**Euler representation:**

$$\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

## Example

The imaginary part of the characteristic function of a standard normal $Z \sim \mathcal{N}(0,1)$:

$$\varphi_Z(u) = e^{-u^2/2} = \cos(0) + i\sin(0) \cdot e^{-u^2/2}$$

Since the normal distribution is symmetric (even), the imaginary part $E[\sin(uZ)] = 0$ for all $u$ — the sine component vanishes because $\sin$ is odd and the normal PDF is even. Only the cosine (real) part survives.

## Remember

$\sin$ is the **imaginary part** of $e^{i\theta}$ via Euler's formula. In characteristic function pricing, $E[\sin(uX)]$ is the imaginary part of the characteristic function $\varphi_X(u)$. For symmetric distributions, this imaginary part is identically zero — since $\sin(-x) = -\sin(x)$, the positive and negative contributions cancel. This simplification halves the numerical work in Fourier inversion: only the real (cosine) part of $\varphi_X(u)$ needs to be integrated.
