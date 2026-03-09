# Matrix Norms

**Topic:** Linear Algebra
**Tags:** matrix norms, Frobenius norm, spectral norm, condition number, numerical stability
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **matrix norm** measures the "size" of a matrix, generalising the concept of vector length to rectangular arrays of numbers. The most common are the **Frobenius norm** (square root of the sum of all squared entries), the **spectral norm** (largest singular value, measuring worst-case input amplification), and the **induced $p$-norms** defined by how much the matrix stretches vectors measured in the $\ell^p$ norm.

## Key Formula

**Frobenius norm** (entry-wise):

$$\|A\|_F = \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n} |a_{ij}|^2} = \sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2}$$

**Spectral norm** (operator 2-norm):

$$\|A\|_2 = \sigma_{\max}(A) = \max_{\|\mathbf{x}\|_2=1} \|A\mathbf{x}\|_2$$

where $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r$ are the singular values of $A$.

**Submultiplicativity** — for any compatible matrices $A$ and $B$:

$$\|AB\| \le \|A\| \cdot \|B\|$$

This holds for both the Frobenius and spectral norms and bounds how errors compound through successive linear transformations.

## Example

Let

$$A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$

**Frobenius norm:**

$$\|A\|_F = \sqrt{3^2 + 1^2 + 0^2 + 2^2} = \sqrt{9 + 1 + 0 + 4} = \sqrt{14} \approx 3.742$$

**Spectral norm:** compute $A^T A$:

$$A^T A = \begin{pmatrix} 9 & 3 \\ 3 & 5 \end{pmatrix}$$

The eigenvalues of $A^T A$ are $\lambda_1 = 7 + \sqrt{13} \approx 10.606$ and $\lambda_2 = 7 - \sqrt{13} \approx 3.394$.

$$\|A\|_2 = \sqrt{\lambda_{\max}(A^T A)} = \sqrt{7 + \sqrt{13}} \approx 3.257$$

The spectral norm is always less than or equal to the Frobenius norm: here $3.257 \le 3.742$.

## Remember

Matrix norms quantify how much a matrix amplifies perturbations — the **condition number** $\kappa(A) = \|A\| \cdot \|A^{-1}\|$ directly measures how sensitive portfolio optimisation is to estimation error in the covariance matrix. The **Frobenius norm** is the loss function minimised in Ledoit-Wolf shrinkage estimation, which finds the optimal blend of the sample covariance matrix and a structured target to reduce estimation noise. The **spectral norm** bounds the worst-case amplification of risk factor shocks through a linear model: if $\|A\|_2$ is large, a small perturbation in factor returns can produce an outsized change in portfolio value. Controlling matrix norms is therefore central to building numerically stable quantitative models.
