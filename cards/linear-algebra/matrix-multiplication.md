# Matrix Multiplication

**Topic:** Linear Algebra
**Level:** A Level Mathematics
**Tags:** linear algebra, matrices, portfolio theory

---

## Definition

The product of an (m × n) matrix A and an (n × p) matrix B is an (m × p) matrix C, where each element is the **dot product** of a row of A with a column of B.

The number of **columns** of A must equal the number of **rows** of B.

## Key Formula

$$C_{ij} = \sum_{k=1}^{n} A_{ik} \, B_{kj}$$

**Properties:**
- Generally **not commutative**: AB ≠ BA
- Associative: A(BC) = (AB)C
- Distributive: A(B + C) = AB + AC
- Transpose: (AB)ᵀ = BᵀAᵀ

## Example

$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

$$AB = \begin{pmatrix} 1(5)+2(7) & 1(6)+2(8) \\ 3(5)+4(7) & 3(6)+4(8) \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

## Remember

In finance, matrices appear in:
- **Covariance matrices** (Σ): a symmetric matrix encoding variances and covariances of asset returns.
- **Portfolio variance**: σ²_p = **w**ᵀ Σ **w**, where **w** is the vector of portfolio weights.
- **Principal Component Analysis (PCA)**: decomposing the covariance matrix to find the main drivers of risk.
- **Linear regression**: the ordinary least squares solution is β̂ = (XᵀX)⁻¹ Xᵀy.
