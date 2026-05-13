# Mercer's Theorem

**Topic:** Computational Finance
**Tags:** mercer's theorem, kernel methods, positive semi-definite, gram matrix, svm, kernel trick
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Mercer's theorem** provides the validity condition for kernel functions: a symmetric function $k(\mathbf{x}, \mathbf{y})$ corresponds to a valid inner product in some feature space if and only if the **Gram matrix** formed from any finite set of points is positive semi-definite. This guarantees that $k(\mathbf{x}, \mathbf{y}) = \langle \phi(\mathbf{x}), \phi(\mathbf{y}) \rangle$ for some feature map $\phi$.

## Key Formula

For any finite set $\{\mathbf{x}_1, \ldots, \mathbf{x}_N\}$, the $N \times N$ **Gram matrix** $\mathbf{K}$ must satisfy:

$$K_{ij} = k(\mathbf{x}_i, \mathbf{x}_j) \qquad \text{and} \qquad \mathbf{K} \succeq 0$$

Common kernels satisfying Mercer's condition:

$$\text{Polynomial: } k(\mathbf{x}, \mathbf{y}) = (\mathbf{x}^\top \mathbf{y} + c)^d$$

$$\text{RBF (Gaussian): } k(\mathbf{x}, \mathbf{y}) = \exp\!\left(-\frac{\|\mathbf{x} - \mathbf{y}\|^2}{2\sigma^2}\right)$$

## Example

Three borrowers described by 2 features (income, debt ratio): $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$. Using the RBF kernel with $\sigma = 1$, compute the $3 \times 3$ Gram matrix. Mercer's theorem guarantees all eigenvalues of this matrix are non-negative, so the SVM convex optimisation problem is well-posed. A made-up function like $k(\mathbf{x},\mathbf{y}) = \cos(\|\mathbf{x}-\mathbf{y}\|)$ may not be PSD — the Gram matrix test would catch this before wasting compute on a non-convex training run.

## Remember

In financial machine learning, choosing a kernel is not just a modelling choice — it is a mathematical commitment. Mercer's theorem is the guarantee that the SVM's quadratic programming problem remains convex and has a unique global solution. When practitioners build custom kernels for financial time series (e.g., kernels that weight recent observations more heavily), they must verify the PSD condition; otherwise the optimiser may diverge or produce a suboptimal classifier.
