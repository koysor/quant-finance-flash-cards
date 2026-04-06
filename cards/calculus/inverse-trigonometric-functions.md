# Inverse Trigonometric Functions

**Topic:** Calculus
**Tags:** arcsin, arccos, arctan, inverse trig, principal value, Cauchy distribution, calibration
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **inverse trigonometric functions** are the inverses of sin, cos, and tan on restricted domains where they are one-to-one. The most important is $\arctan(x)$, which maps all of $\mathbb{R}$ to $(-\pi/2, \pi/2)$. These functions recover an angle from a ratio.

## Key Formula

| Function | Domain | Range | Notation |
|---|---|---|---|
| $\arcsin(x)$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ | also $\sin^{-1}(x)$ |
| $\arccos(x)$ | $[-1, 1]$ | $[0, \pi]$ | also $\cos^{-1}(x)$ |
| $\arctan(x)$ | $\mathbb{R}$ | $(-\pi/2, \pi/2)$ | also $\tan^{-1}(x)$ |

**Derivatives:**

$$\frac{d}{dx}\arcsin(x) = \frac{1}{\sqrt{1-x^2}}, \qquad \frac{d}{dx}\arccos(x) = \frac{-1}{\sqrt{1-x^2}}, \qquad \frac{d}{dx}\arctan(x) = \frac{1}{1+x^2}$$

**Key limits:**

$$\lim_{x \to \infty}\arctan(x) = \frac{\pi}{2}, \qquad \lim_{x \to -\infty}\arctan(x) = -\frac{\pi}{2}$$

**Cauchy CDF:**

$$F(x) = \frac{1}{2} + \frac{1}{\pi}\arctan\!\left(\frac{x - \mu}{\gamma}\right)$$

## Example

In rotation-based optimisation, the angle $\theta$ of the principal axis of a 2D covariance ellipse is:

$$\theta = \frac{1}{2}\arctan\!\left(\frac{2\sigma_{12}}{\sigma_1^2 - \sigma_2^2}\right)$$

With $\sigma_1^2 = 0.04$, $\sigma_2^2 = 0.01$, $\sigma_{12} = 0.015$:

$$\theta = \frac{1}{2}\arctan(1.0) = \frac{1}{2} \cdot \frac{\pi}{4} = \frac{\pi}{8} \approx 22.5°$$

This is the angle by which the eigenvector axes of the covariance matrix are rotated from the standard basis — the core geometric step in PCA.

## Remember

$\arctan$ is the most important inverse trig function in quantitative finance because it appears in the **Cauchy distribution CDF** and in **angle computations** for rotation matrices. The Cauchy distribution has no finite mean or variance — it is the canonical example of a fat-tailed distribution where the CLT fails — and its CDF is expressed entirely through $\arctan$. The derivative formula $\frac{d}{dx}\arctan(x) = \frac{1}{1+x^2}$ also appears in Stein's lemma applications and in certain variance-reduction techniques for Monte Carlo integration.
