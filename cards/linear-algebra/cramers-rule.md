# Cramer's Rule

**Topic:** Linear Algebra
**Tags:** determinant, linear systems, hedging, replication, closed-form
**Author:** Claude Opus 4.6

---

## Definition

Cramer's Rule is a determinant-based method for solving a system of $n$ linear equations in $n$ unknowns. Each unknown is expressed as the ratio of two determinants: the numerator replaces the corresponding column of the coefficient matrix with the constant vector, and the denominator is the determinant of the original coefficient matrix. The rule applies only when the system has a unique solution, i.e. when $\det(A) \neq 0$.

## Key Formula

For a system $A\mathbf{x} = \mathbf{b}$ where $A$ is an $n \times n$ matrix with $\det(A) \neq 0$, each unknown $x_i$ is given by:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

where $A_i$ is the matrix formed by replacing the $i$-th column of $A$ with $\mathbf{b}$.

For a $2 \times 2$ system:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} e \\ f \end{pmatrix}$$

$$x_1 = \frac{ed - bf}{ad - bc}, \quad x_2 = \frac{af - ce}{ad - bc}$$

## Example

A trader holds a portfolio and needs to hedge using two instruments. The hedge ratios $h_1$ and $h_2$ satisfy:

$$3h_1 + 2h_2 = 8$$
$$h_1 + 4h_2 = 10$$

The coefficient matrix determinant is $\det(A) = (3)(4) - (2)(1) = 10$.

Applying Cramer's Rule:

$$h_1 = \frac{(8)(4) - (2)(10)}{10} = \frac{32 - 20}{10} = 1.2$$

$$h_2 = \frac{(3)(10) - (8)(1)}{10} = \frac{30 - 8}{10} = 2.2$$

The trader should hold 1.2 units of the first instrument and 2.2 units of the second.

## Remember

Cramer's Rule gives a closed-form solution for small linear systems, making it particularly useful in quantitative finance for $2 \times 2$ and $3 \times 3$ hedging and replication problems where you need explicit expressions for hedge ratios or portfolio weights. For larger systems it is computationally expensive ($O(n!)$ via cofactor expansion), so LU decomposition or Gaussian elimination is preferred. However, the closed-form nature of Cramer's Rule makes it valuable for deriving analytical results — for instance, expressing option replication weights directly in terms of market parameters.
