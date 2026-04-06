# Rotational Symmetry

**Topic:** Calculus
**Tags:** rotational symmetry, symmetry, odd function, normal distribution, isotropic, Brownian motion
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function or shape has **rotational symmetry** of order $n$ if it maps to itself under rotation by $\frac{360°}{n}$ about a fixed point. In one dimension, a function is symmetric under a 180° rotation about the origin if and only if it is an **odd function**: $f(-x) = -f(x)$. In higher dimensions, a distribution or process is **rotationally symmetric** (or **isotropic**) if it is invariant under any rotation about the origin.

## Key Formula

**180° rotational symmetry about the origin (1D):**

$$f(-x) = -f(x) \iff f \text{ is odd}$$

**Rotation matrix** in $\mathbb{R}^2$ by angle $\theta$:

$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad R_\theta^\top R_\theta = I$$

A distribution $p(\mathbf{x})$ on $\mathbb{R}^n$ is **rotationally symmetric** if:

$$p(R\mathbf{x}) = p(\mathbf{x}) \quad \text{for all orthogonal } R$$

This holds if and only if $p(\mathbf{x})$ depends only on $\|\mathbf{x}\|$ — the distribution's density is constant on spheres.

## Example

The standard bivariate normal $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, I)$ has density:

$$p(x_1, x_2) = \frac{1}{2\pi} e^{-(x_1^2 + x_2^2)/2} = \frac{1}{2\pi} e^{-\|\mathbf{x}\|^2/2}$$

Since this depends only on $\|\mathbf{x}\|^2 = x_1^2 + x_2^2$, it is rotationally symmetric — the probability of a draw depends only on its distance from the origin, not its direction. Rotating the axes by any angle $\theta$ leaves the distribution unchanged.

By contrast, $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \Sigma)$ with $\Sigma \neq I$ is not rotationally symmetric — it is elongated along the principal eigenvectors of $\Sigma$.

## Remember

Rotational symmetry is broken whenever assets have unequal volatilities or non-zero correlations — the joint return distribution is an ellipse, not a circle. PCA restores a form of rotational symmetry by rotating to the eigenvector basis where the covariance matrix becomes diagonal (equal-variance components are then isotropic). Recognising whether a model is rotationally symmetric matters in multi-asset Monte Carlo: if the covariance matrix is a scalar multiple of the identity ($\Sigma = \sigma^2 I$), you can draw isotropic random vectors directly; otherwise you must apply a Cholesky or spectral transformation to introduce the correct correlations.
