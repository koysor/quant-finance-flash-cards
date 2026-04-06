# Tangent

**Topic:** Calculus
**Tags:** tangent, tan, trigonometry, asymptote, gradient, slope
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **tangent function** $\tan(\theta) = \sin(\theta)/\cos(\theta)$ is the ratio of the opposite to adjacent sides in a right-angled triangle. It is periodic with period $\pi$, odd, and undefined wherever $\cos(\theta) = 0$ — it has vertical asymptotes at $\theta = \pm\pi/2, \pm 3\pi/2, \ldots$ Its range is all of $\mathbb{R}$.

## Key Formula

$$\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} = \frac{\text{opposite}}{\text{adjacent}}$$

**Derivative:**

$$\frac{d}{d\theta}\tan(\theta) = \sec^2(\theta) = 1 + \tan^2(\theta)$$

**Key values:** $\tan(0) = 0$, $\tan(\pi/6) = 1/\sqrt{3}$, $\tan(\pi/4) = 1$, $\tan(\pi/3) = \sqrt{3}$, $\tan(\pi/2)$ undefined

**Odd function:** $\tan(-\theta) = -\tan(\theta)$

**Vertical asymptotes** at $\theta = \frac{\pi}{2} + n\pi$ for $n \in \mathbb{Z}$.

**Tangent line** to a curve $y = f(x)$ at $x = a$:

$$y = f(a) + f'(a)(x - a)$$

The slope $f'(a)$ is the value of the tangent function only in the geometric sense — the derivative gives the gradient angle $\alpha$ where $\tan(\alpha) = f'(a)$.

## Example

In a rotation matrix, the angle $\theta$ by which a portfolio's risk factor axes are rotated satisfies:

$$\tan(\theta) = \frac{\sigma_{12}}{\sigma_1^2 - \sigma_2^2}$$

for the principal axis angle of a 2-asset covariance ellipse (related to eigenvalue decomposition). With $\sigma_1^2 = 0.04$, $\sigma_2^2 = 0.01$, $\sigma_{12} = 0.015$:

$$\tan(\theta) = \frac{0.015}{0.03} = 0.5 \implies \theta = \arctan(0.5) \approx 26.6°$$

## Remember

The tangent function's geometric meaning — slope of the line from the origin to a point on the unit circle — connects directly to the concept of the **gradient** or **derivative** of a curve. The delta of an option is the slope (tangent) of the price curve at the current spot — $\Delta = \tan(\alpha)$ where $\alpha$ is the angle the price curve makes with the horizontal. The vertical asymptotes of $\tan$ at $\pm\pi/2$ are a concrete example of a function that is continuous on an open interval but unbounded — an important contrast with the bounded behaviour of $\sin$ and $\cos$.
