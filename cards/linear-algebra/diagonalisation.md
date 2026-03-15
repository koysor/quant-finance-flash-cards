# Diagonalisation

**Topic:** Linear Algebra
**Tags:** diagonalisation, eigendecomposition, matrix powers, Markov chains, covariance matrix
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

A square matrix $A$ is **diagonalisable** if it can be written as $A = P\Lambda P^{-1}$, where $\Lambda$ is a diagonal matrix of eigenvalues and $P$ is the matrix of corresponding eigenvectors. This expresses $A$ in a basis where its action is simply scaling along each eigenvector direction.

## Key Formula

$$A = P\Lambda P^{-1}, \quad \Lambda = \begin{pmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{pmatrix}$$

A matrix is diagonalisable if and only if it has $n$ linearly independent eigenvectors. The power formula follows immediately:

$$A^k = P\Lambda^k P^{-1}, \quad \Lambda^k = \begin{pmatrix} \lambda_1^k & & \\ & \ddots & \\ & & \lambda_n^k \end{pmatrix}$$

For symmetric matrices (e.g. covariance matrices), $P$ is orthogonal so $P^{-1} = P^\top$, and diagonalisation becomes the **spectral decomposition**: $A = P\Lambda P^\top$.

## Example

Let $A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$. Eigenvalues: $\lambda_1 = 3$, $\lambda_2 = 2$. Eigenvectors: $\mathbf{p}_1 = \begin{pmatrix}1\\0\end{pmatrix}$, $\mathbf{p}_2 = \begin{pmatrix}1\\-1\end{pmatrix}$.

$$P = \begin{pmatrix}1&1\\0&-1\end{pmatrix}, \quad \Lambda = \begin{pmatrix}3&0\\0&2\end{pmatrix}$$

Then $A^{10} = P\begin{pmatrix}3^{10}&0\\0&2^{10}\end{pmatrix}P^{-1}$ — computed instantly rather than by ten matrix multiplications.

## Remember

Diagonalisation makes computing matrix powers tractable, which is essential for discrete-time credit models. A credit rating transition matrix $T$ (where $T_{ij}$ is the probability of migrating from rating $i$ to rating $j$ in one period) is diagonalisable; $T^k = P\Lambda^k P^{-1}$ gives the $k$-period transition probabilities in closed form. The dominant eigenvalue of $T$ determines the long-run stationary distribution of credit ratings — a key input to expected credit loss calculations under IFRS 9.
