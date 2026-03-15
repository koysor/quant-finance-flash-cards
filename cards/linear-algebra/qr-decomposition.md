# QR Decomposition

**Topic:** Linear Algebra
**Tags:** qr decomposition, orthogonal matrix, regression, numerical stability, least squares
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

**QR decomposition** factorises a matrix $A$ into the product of an orthogonal matrix $Q$ and an upper triangular matrix $R$: $A = QR$. It is the numerically preferred method for solving least-squares problems and computing eigenvalues, offering greater stability than forming the normal equations $A^\top A$ directly.

## Key Formula

$$A = QR$$

where $Q \in \mathbb{R}^{m \times m}$ satisfies $Q^\top Q = I$ and $R \in \mathbb{R}^{m \times n}$ is upper triangular.

For the least-squares problem $\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|^2$, substituting $A = QR$ and using $Q^\top Q = I$ gives:

$$R\mathbf{x} = Q^\top \mathbf{b}$$

This is a triangular system solved by back substitution — no matrix inversion required. The QR decomposition can be computed via Gram-Schmidt orthogonalisation or Householder reflections.

## Example

Decompose $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}$ using Gram-Schmidt.

Columns: $\mathbf{a}_1 = \begin{pmatrix}1\\0\\1\end{pmatrix}$, $\mathbf{a}_2 = \begin{pmatrix}1\\1\\0\end{pmatrix}$.

$\mathbf{q}_1 = \dfrac{\mathbf{a}_1}{\|\mathbf{a}_1\|} = \dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\1\end{pmatrix}$

Project and subtract: $\mathbf{a}_2 - (\mathbf{a}_2 \cdot \mathbf{q}_1)\mathbf{q}_1 = \begin{pmatrix}1\\1\\0\end{pmatrix} - \frac{1}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\1\end{pmatrix} = \begin{pmatrix}1/2\\1\\-1/2\end{pmatrix}$, then normalise to get $\mathbf{q}_2$.

The entries $r_{ij} = \mathbf{q}_i \cdot \mathbf{a}_j$ fill $R$.

## Remember

In linear factor model estimation, OLS solves the normal equations $(X^\top X)\hat{\boldsymbol{\beta}} = X^\top \mathbf{y}$. Squaring the condition number: if $X$ has condition number $\kappa$, then $X^\top X$ has condition number $\kappa^2$, amplifying numerical errors. Using QR decomposition to solve $R\hat{\boldsymbol{\beta}} = Q^\top \mathbf{y}$ directly avoids this squaring and gives substantially more accurate factor loadings when predictors are nearly collinear — as is common with correlated risk factors such as value and quality.
