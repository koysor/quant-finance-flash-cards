# Radial Basis Function (RBF) Kernel

**Topic:** Computational Finance
**Tags:** rbf kernel, gaussian kernel, svm, bandwidth, kernel trick, classification
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Radial Basis Function (RBF) kernel** (also called the Gaussian kernel) measures the similarity between two points as a decreasing function of their squared Euclidean distance. It implicitly maps data into an infinite-dimensional feature space, making it the default kernel for SVMs applied to non-linearly-separable financial data.

## Key Formula

$$k(\mathbf{x}, \mathbf{y}) = \exp\!\left(-\frac{\|\mathbf{x} - \mathbf{y}\|^2}{2\sigma^2}\right)$$

The bandwidth parameter $\sigma > 0$ controls the radius of influence of each training point:

| $\sigma$ small | $\sigma$ large |
|---|---|
| Kernel decays quickly with distance | Kernel decays slowly |
| Complex, localised decision boundary | Smooth, simple boundary |
| Risk of overfitting | Risk of underfitting |

The RBF kernel satisfies Mercer's condition for all $\sigma > 0$, guaranteeing a valid feature map $\phi$ such that $k(\mathbf{x}, \mathbf{y}) = \langle \phi(\mathbf{x}), \phi(\mathbf{y}) \rangle$ in an infinite-dimensional Hilbert space.

## Example

Two loan applicants: $\mathbf{x} = (60, 0.25)$ (income £60k, DTI 0.25) and $\mathbf{y} = (62, 0.28)$. With $\sigma = 5$:

$$k(\mathbf{x}, \mathbf{y}) = \exp\!\left(-\frac{(60{-}62)^2 + (0.25{-}0.28)^2}{50}\right) = \exp(-0.0802) \approx 0.923$$

A known defaulter at $(28, 0.85)$ has $k(\mathbf{x}, \text{defaulter}) \approx \exp(-1088/50) \approx 0$ — essentially zero influence on classifying $\mathbf{x}$.

## Remember

The RBF kernel is the default choice when applying SVMs to financial classification (credit scoring, regime detection, fraud detection) because it makes no assumption about the functional form of the decision boundary. The pair $(\sigma, C)$ — bandwidth and regularisation — are tuned jointly via cross-validation. Intuitively, $\sigma$ determines how far a borrower's "region of influence" extends in feature space: a small $\sigma$ means only very similar applicants matter for a prediction; a large $\sigma$ means even quite different applicants pull the classification.
