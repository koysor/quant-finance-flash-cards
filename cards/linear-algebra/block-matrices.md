# Block Matrices

**Topic:** Linear Algebra
**Tags:** linear algebra, matrices, block matrix, partitioned matrix, covariance matrix, portfolio optimisation
**Author:** Claude Opus 4.6

---

## Definition

A **block matrix** (or partitioned matrix) is a matrix divided into rectangular sub-matrices called **blocks** by horizontal and vertical partitions. Block multiplication follows the same rules as scalar matrix multiplication, provided the block dimensions are compatible. The **block diagonal** matrix is a special case where all off-diagonal blocks are zero.

## Key Formula

For a $2 \times 2$ block partition:

$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} E & F \\ G & H \end{pmatrix} = \begin{pmatrix} AE + BG & AF + BH \\ CE + DG & CF + DH \end{pmatrix}$$

where each product (e.g. $AE$) is a matrix multiplication of compatible blocks.

Determinant of a block diagonal matrix:

$$\det\begin{pmatrix} A & 0 \\ 0 & D \end{pmatrix} = \det(A)\,\det(D)$$

**Schur complement:** if $A$ is invertible, the Schur complement of $A$ in the full matrix is $S = D - CA^{-1}B$, and

$$\det\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \det(A)\,\det(S)$$

## Example

Let $M = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{pmatrix}$, partitioned as $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $C = \begin{pmatrix} 0 & 0 \end{pmatrix}$, $D = (4)$.

Since $C = 0$, this is block triangular. The determinant is:

$$\det(M) = \det(A)\,\det(D) = (2 \times 3 - 0 \times 0)(4) = 6 \times 4 = 24$$

## Remember

Multi-asset covariance matrices are naturally block-structured: assets within the same class (equities, bonds, commodities) are correlated with each other but often weakly correlated across classes. A **block-diagonal approximation** sets cross-class covariances to zero, dramatically reducing the number of parameters to estimate and speeding up portfolio optimisation. The **Schur complement** appears when computing conditional covariances — for example, the covariance of equity returns conditional on bond returns is exactly $\Sigma_{EE} - \Sigma_{EB}\,\Sigma_{BB}^{-1}\,\Sigma_{BE}$, which is the Schur complement of the bond block in the full covariance matrix.
