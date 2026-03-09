# Linear Transformations

**Topic:** Linear Algebra
**Tags:** linear transformation, matrix, rotation, scaling, change of basis
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **linear transformation** $T: \mathbb{R}^n \to \mathbb{R}^m$ is a function that preserves vector addition and scalar multiplication: $T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$. Every linear transformation can be represented by matrix multiplication $T(\mathbf{x}) = A\mathbf{x}$, where $A$ is an $m \times n$ matrix whose columns are the images of the standard basis vectors.

## Key Formula

The two **linearity conditions** that define a linear transformation are:

$$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \qquad \text{(additivity)}$$

$$T(\alpha\mathbf{u}) = \alpha T(\mathbf{u}) \qquad \text{(homogeneity)}$$

Every linear transformation has a unique **matrix representation**:

$$T(\mathbf{x}) = A\mathbf{x}$$

Common $2 \times 2$ transformation matrices include:

**Scaling** by factors $s_x$ and $s_y$:

$$S = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$$

**Rotation** by angle $\theta$ anticlockwise:

$$R = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

**Reflection** in the $x$-axis:

$$F = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

## Example

A portfolio holds two assets with weights $\mathbf{w} = \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix}$. A risk manager applies a scaling transformation that doubles the exposure to Asset 1 and halves the exposure to Asset 2:

$$S = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$$

The transformed weight vector is:

$$S\mathbf{w} = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix} \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix} = \begin{pmatrix} 1.2 \\ 0.2 \end{pmatrix}$$

The transformation scales each component independently — Asset 1's weight moves from 0.6 to 1.2, and Asset 2's weight moves from 0.4 to 0.2.

## Remember

Every matrix operation in finance is a linear transformation. Multiplying a return vector by a weight vector ($\mathbf{w}^\top \mathbf{r}$) is a linear transformation from asset space to portfolio space. The Cholesky factor $L$ transforms independent random draws into correlated ones ($\mathbf{z}_{\text{corr}} = L\mathbf{z}$). Change of basis via eigenvectors transforms correlated asset returns into uncorrelated principal components. Understanding that matrices **are** transformations — not just arrays of numbers — is the geometric insight that makes portfolio theory, factor models, and risk decomposition intuitive.
