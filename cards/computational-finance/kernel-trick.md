# Kernel Trick

**Topic:** Computational Finance
**Tags:** kernel trick, svm, rbf kernel, feature space, non-linear, inner product
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **kernel trick** allows a machine learning algorithm to operate in a high-dimensional (or infinite-dimensional) feature space without ever explicitly computing the coordinates in that space, by replacing dot products $\mathbf{x}_i^\top \mathbf{x}_j$ with a **kernel function** $k(\mathbf{x}_i, \mathbf{x}_j)$ that computes the inner product implicitly. This makes non-linear classification tractable at the cost of a linear model.

## Key Formula

A kernel function $k: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}$ must satisfy Mercer's condition (be symmetric and positive semi-definite), guaranteeing it corresponds to a valid inner product in some feature space $\phi(\mathbf{x})$:

$$k(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^\top \phi(\mathbf{x}_j)$$

**Common kernels:**

$$\text{Linear:} \quad k(\mathbf{x}_i, \mathbf{x}_j) = \mathbf{x}_i^\top \mathbf{x}_j$$

$$\text{Polynomial (degree }d\text{):} \quad k(\mathbf{x}_i, \mathbf{x}_j) = \left(\mathbf{x}_i^\top \mathbf{x}_j + c\right)^d$$

$$\text{RBF (Gaussian):} \quad k(\mathbf{x}_i, \mathbf{x}_j) = \exp\!\left(-\frac{\|\mathbf{x}_i - \mathbf{x}_j\|^2}{2\sigma^2}\right)$$

The RBF kernel implicitly maps to an **infinite-dimensional** feature space.

## Example

A fraud detection model has two features: transaction amount $x_1$ and time-since-last-transaction $x_2$. Fraudulent and legitimate transactions form two interlocking crescents — not linearly separable.

With a polynomial kernel ($d = 2$, $c = 1$):

$$k(\mathbf{x}_i, \mathbf{x}_j) = (x_{i1}x_{j1} + x_{i2}x_{j2} + 1)^2$$

This implicitly maps each point to 6 dimensions: $(x_1^2,\; x_2^2,\; \sqrt{2}x_1x_2,\; \sqrt{2}x_1,\; \sqrt{2}x_2,\; 1)$. In this 6-dimensional space the classes become linearly separable, and the SVM finds the optimal hyperplane — without ever computing the 6-dimensional coordinates explicitly.

## Remember

The kernel trick is why SVMs can classify non-linearly-separable financial data (credit risk, option payoff patterns, regime detection) without the explosion in computation that explicit feature engineering would require. The **RBF kernel** is the default choice in quantitative finance: its single hyperparameter $\sigma$ (the bandwidth) controls the smoothness of the decision boundary, tuned via cross-validation alongside $C$. The key intuition is that the similarity measure $k(\mathbf{x}_i, \mathbf{x}_j)$ tells the model "how alike are these two data points?" — a natural concept for comparing borrower profiles or market states.
