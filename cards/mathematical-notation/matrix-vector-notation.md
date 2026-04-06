# Matrix and Vector Notation

**Topic:** Mathematical Notation
**Tags:** notation, matrix, vector, bold, transpose, inverse, linear algebra
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

**Matrix and vector notation** uses typographical conventions to distinguish scalars, vectors, and matrices at a glance. The most common convention in quantitative finance is:

| Symbol | Type | Example |
|---|---|---|
| $x$ (italic) | Scalar | $\sigma = 0.2$, $r = 0.05$ |
| $\mathbf{v}$ (bold lower-case) | Column vector | $\mathbf{w} \in \mathbb{R}^n$ (portfolio weights) |
| $\mathbf{A}$ (bold upper-case) | Matrix | $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times n}$ (covariance matrix) |
| $A_{ij}$ or $a_{ij}$ | Matrix entry | Row $i$, column $j$ |
| $\mathbf{A}^\top$ or $\mathbf{A}^T$ | Transpose | $(A^\top)_{ij} = A_{ji}$ |
| $\mathbf{A}^{-1}$ | Inverse | $\mathbf{A}\mathbf{A}^{-1} = \mathbf{I}$ |

## Key Formula

**Portfolio variance** using matrix notation:

$$\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$$

**OLS estimator:**

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{y}$$

**Transpose of a product:**

$$(\mathbf{A}\mathbf{B})^\top = \mathbf{B}^\top \mathbf{A}^\top$$

**Inverse of a product:**

$$(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$$

## Example

A three-asset portfolio with weight vector $\mathbf{w} = (0.5, 0.3, 0.2)^\top$ and covariance matrix:

$$\boldsymbol{\Sigma} = \begin{pmatrix} 0.04 & 0.01 & 0.00 \\ 0.01 & 0.09 & 0.02 \\ 0.00 & 0.02 & 0.01 \end{pmatrix}$$

Portfolio variance is $\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$. The $^\top$ symbol signals that $\mathbf{w}$ is transposed from a column to a row vector before multiplication, yielding a scalar result.

## Remember

The compact expression $\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$ for portfolio variance is one of the most important formulas in quantitative finance — it simultaneously encodes $n^2$ variance and covariance terms in three symbols. Without matrix notation, Markowitz mean-variance optimisation would be intractable to write, let alone compute. In code, this maps directly to `w.T @ Sigma @ w` in NumPy, making the notation a near-literal translation between mathematics and implementation.
