# Similar Matrices

**Topic:** Linear Algebra
**Tags:** similarity, eigenvalues, change of basis, diagonalisation, covariance matrix
**Author:** Claude Opus 4.6

---

## Definition

Two square matrices $A$ and $B$ are **similar** if there exists an invertible matrix $P$ such that $B = P^{-1}AP$. Similar matrices represent the same linear transformation expressed in different bases. They share all basis-independent properties: eigenvalues, determinant, trace, rank, and characteristic polynomial.

## Key Formula

$$B = P^{-1}AP$$

If $A$ and $B$ are similar then:

$$\det(B) = \det(A), \quad \operatorname{tr}(B) = \operatorname{tr}(A), \quad \operatorname{rank}(B) = \operatorname{rank}(A)$$

$$\det(B - \lambda I) = \det(A - \lambda I) \quad \text{(same characteristic polynomial and eigenvalues)}$$

Diagonalisation is the special case where $B = \Lambda$ is diagonal: $A = P\Lambda P^{-1}$ means $A$ is similar to the diagonal matrix of its eigenvalues.

## Example

Let $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$, so $P^{-1} = \frac{1}{3}\begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$.

$$B = P^{-1}AP = \frac{1}{3}\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}1&1\\1&-2\end{pmatrix} = \begin{pmatrix}5&0\\0&2\end{pmatrix}$$

Both $A$ and $B$ have eigenvalues $5$ and $2$, trace $7$, and determinant $10$. The matrix $B$ is diagonal, confirming that $A$ is diagonalisable.

## Remember

Diagonalisation is precisely the statement that a matrix is similar to the diagonal matrix of its eigenvalues: $\Sigma = Q\Lambda Q^\top$. When you decompose a covariance matrix this way in Principal Component Analysis, you are finding the basis (eigenvectors in $Q$) in which the covariance matrix becomes diagonal — meaning the risk factors are uncorrelated. Similarity guarantees that the total variance ($\operatorname{tr}(\Sigma) = \sum \lambda_i$) and the generalised variance ($\det(\Sigma) = \prod \lambda_i$) are preserved regardless of which basis you choose.
