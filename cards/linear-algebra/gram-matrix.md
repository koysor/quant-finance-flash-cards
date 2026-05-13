# Gram Matrix

**Topic:** Linear Algebra
**Tags:** gram matrix, kernel methods, positive semi-definite, covariance matrix, inner product, svm
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gram matrix** of a set of vectors $\{\mathbf{x}_1, \ldots, \mathbf{x}_N\}$ is the $N \times N$ symmetric matrix of all pairwise inner products. In kernel machine learning, it encodes every pairwise similarity in the dataset; algorithms then operate entirely on this matrix rather than the raw feature vectors.

## Key Formula

**Linear kernel (explicit features):**

$$G_{ij} = \langle \mathbf{x}_i, \mathbf{x}_j \rangle = \mathbf{x}_i^\top \mathbf{x}_j \qquad \Rightarrow \qquad \mathbf{G} = \mathbf{X}\mathbf{X}^\top$$

**General kernel:**

$$K_{ij} = k(\mathbf{x}_i, \mathbf{x}_j)$$

By Mercer's theorem, a kernel produces a valid Gram matrix if and only if $\mathbf{K} \succeq 0$ (positive semi-definite) for every choice of data points. The Gram matrix is always symmetric, and its diagonal entries are $k(\mathbf{x}_i, \mathbf{x}_i) = \|\phi(\mathbf{x}_i)\|^2 \geq 0$.

## Example

Three borrowers with features $\mathbf{x}_1 = (1, 0)$, $\mathbf{x}_2 = (0, 1)$, $\mathbf{x}_3 = (1, 1)$:

$$\mathbf{G} = \mathbf{X}\mathbf{X}^\top = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$

The SVM dual optimisation problem depends only on $\mathbf{G}$, not the individual $\mathbf{x}_i$. When features lie in thousands of dimensions (e.g. text data for news sentiment), storing the $N \times N$ kernel matrix is far cheaper than the full $N \times d$ feature matrix.

## Remember

In quantitative finance, the sample covariance matrix $\hat{\Sigma} = \frac{1}{T-1}\mathbf{R}^\top\mathbf{R}$ (where $\mathbf{R}$ is the de-meaned returns matrix) is a scaled Gram matrix of return time series. Both share the same positive semi-definiteness property — the mathematical guarantee that portfolio variance $\mathbf{w}^\top\hat{\Sigma}\mathbf{w} \geq 0$ mirrors the kernel guarantee that the SVM dual has a unique solution. Checking whether a candidate kernel produces a valid (PSD) Gram matrix is therefore the financial equivalent of checking whether an estimated covariance matrix is a legitimate risk model.
