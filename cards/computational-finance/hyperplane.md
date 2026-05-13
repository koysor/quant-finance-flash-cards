# Hyperplane

**Topic:** Computational Finance
**Tags:** hyperplane, linear algebra, decision boundary, svm, classification, high-dimensional
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **hyperplane** in $\mathbb{R}^n$ is a flat affine subspace of dimension $n-1$ defined by a single linear equation. In machine learning it acts as the **decision boundary** that separates two classes: points on one side belong to one class, points on the other side to the other.

## Key Formula

The hyperplane equation:

$$\mathbf{w}^\top \mathbf{x} + b = 0$$

where $\mathbf{w} \in \mathbb{R}^n$ is the normal vector (perpendicular to the hyperplane) and $b \in \mathbb{R}$ is the bias (offset from the origin).

The signed distance from a point $\mathbf{x}_i$ to the hyperplane:

$$d_i = \frac{\mathbf{w}^\top \mathbf{x}_i + b}{\|\mathbf{w}\|}$$

Points with $d_i > 0$ lie on the positive side; points with $d_i < 0$ on the negative side.

## Example

In $\mathbb{R}^2$ (two features), a hyperplane is a line: $w_1 x_1 + w_2 x_2 + b = 0$.

A credit classifier with features $x_1 =$ debt-to-income ratio and $x_2 =$ credit score, and hyperplane $-0.8 x_1 + 0.6 x_2 - 1.2 = 0$:

- Borrower A: $x_1 = 0.3, x_2 = 720$ → $-0.8(0.3) + 0.6(720) - 1.2 = 430.4 > 0$ → predict **no default**
- Borrower B: $x_1 = 0.9, x_2 = 580$ → $-0.8(0.9) + 0.6(580) - 1.2 = 345.6 > 0$ — with real-world weights, this flips; scaling matters.

In $\mathbb{R}^{100}$ (100 features), the hyperplane is a 99-dimensional subspace — impossible to visualise, but the arithmetic is identical.

## Remember

Hyperplanes are the building block of SVMs, logistic regression, and linear discriminant analysis — all of which define a decision boundary as a hyperplane. In credit scoring and fraud detection, the question "which side of the hyperplane does this borrower fall on?" is literally how the classifier produces a prediction. The normal vector $\mathbf{w}$ encodes the relative importance of each feature: a large $|w_j|$ means feature $j$ strongly influences the classification decision.
