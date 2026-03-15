# Gram-Schmidt Orthogonalisation

**Topic:** Linear Algebra
**Tags:** orthogonalisation, basis vectors, inner product, PCA, factor models, numerical stability
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

Gram-Schmidt orthogonalisation is an algorithm that converts a set of linearly independent vectors into an **orthonormal basis** — a set of vectors that are mutually perpendicular and each have unit length. It works by iteratively projecting each new vector onto the subspace already spanned and subtracting off that component, leaving only the part orthogonal to all previous basis vectors.

## Key Formula

Given vectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$, the orthonormal basis $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$ is built as follows:

**Step 1 — normalise the first vector:**

$$\mathbf{e}_1 = \frac{\mathbf{v}_1}{\|\mathbf{v}_1\|}$$

**Step $k$ — subtract projections onto all previous basis vectors, then normalise:**

$$\mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{e}_j)\,\mathbf{e}_j, \qquad \mathbf{e}_k = \frac{\mathbf{u}_k}{\|\mathbf{u}_k\|}$$

The scalar $\mathbf{v}_k \cdot \mathbf{e}_j$ is the projection coefficient — the amount of $\mathbf{v}_k$ lying along the already-established direction $\mathbf{e}_j$.

## Example

Orthogonalise $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and $\mathbf{v}_2 = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$.

**Step 1:** $\mathbf{e}_1 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$

**Step 2:** Compute the projection of $\mathbf{v}_2$ onto $\mathbf{e}_1$:

$$\mathbf{v}_2 \cdot \mathbf{e}_1 = 2 \cdot \tfrac{1}{\sqrt{2}} + 0 \cdot \tfrac{1}{\sqrt{2}} = \sqrt{2}$$

Subtract: $\mathbf{u}_2 = \begin{pmatrix} 2 \\ 0 \end{pmatrix} - \sqrt{2} \cdot \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Normalise: $\mathbf{e}_2 = \dfrac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$

Check orthogonality: $\mathbf{e}_1 \cdot \mathbf{e}_2 = \tfrac{1}{2} - \tfrac{1}{2} = 0$ ✓

## Remember

In factor model construction, Gram-Schmidt orthogonalisation builds **uncorrelated risk factors** from a set of correlated raw factors (e.g. value, momentum, quality). Because the resulting basis vectors are orthogonal, each factor captures a distinct, non-overlapping source of return — this eliminates multicollinearity and makes attribution unambiguous. The procedure also underpins QR decomposition, which is used in regression and in the QR algorithm for computing eigenvalues of large covariance matrices, directly connecting to PCA-based risk modelling.
