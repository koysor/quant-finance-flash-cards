# Column Vector

**Topic:** Linear Algebra
**Tags:** column vector, n×1 matrix, portfolio weights, returns, matrix multiplication
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **column vector** is a matrix with a single column — an $n \times 1$ array of numbers written vertically. It is the default representation of a vector in linear algebra. In quantitative finance, portfolio weights, asset returns, factor exposures, and risk sensitivities are all stored as column vectors.

## Key Formula

$$\mathbf{w} = \begin{pmatrix} w_1 \\ w_2 \\ \vdots \\ w_n \end{pmatrix} \quad (n \times 1)$$

**Matrix times column vector** (produces a column vector):

$$A\mathbf{w} = \mathbf{b} \quad (m \times n)(n \times 1) = (m \times 1)$$

**Outer product** (column times row, produces a matrix):

$$\mathbf{u}\mathbf{v}^\top = \begin{pmatrix}u_1 v_1 & \cdots & u_1 v_n \\ \vdots & & \vdots \\ u_n v_1 & \cdots & u_n v_n\end{pmatrix} \quad (n \times 1)(1 \times n) = (n \times n)$$

**Full constraint:** portfolio weights satisfy $\mathbf{1}^\top \mathbf{w} = 1$ (the all-ones row vector dotted with the weight column vector sums to 1).

## Example

A covariance matrix $\Sigma$ and weight vector $\mathbf{w}$ for two assets:

$$\Sigma = \begin{pmatrix}0.04 & 0.01\\0.01 & 0.02\end{pmatrix}, \qquad \mathbf{w} = \begin{pmatrix}0.6\\0.4\end{pmatrix}$$

First compute $\Sigma\mathbf{w}$ (matrix times column vector):

$$\Sigma\mathbf{w} = \begin{pmatrix}0.04(0.6)+0.01(0.4)\\0.01(0.6)+0.02(0.4)\end{pmatrix} = \begin{pmatrix}0.028\\0.014\end{pmatrix}$$

Then $\sigma_P^2 = \mathbf{w}^\top(\Sigma\mathbf{w}) = 0.6(0.028) + 0.4(0.014) = 0.0168 + 0.0056 = 0.0224$.

## Remember

The column vector is the **atomic unit of quantitative portfolio analysis**. The weight vector $\mathbf{w}$ is always an $n \times 1$ column; the returns vector $\mathbf{r}$ is $n \times 1$; the vector of expected returns $\boldsymbol{\mu}$ is $n \times 1$. The full Markowitz optimisation can be written compactly as: maximise $\boldsymbol{\mu}^\top\mathbf{w} - \frac{\lambda}{2}\mathbf{w}^\top\Sigma\mathbf{w}$ subject to $\mathbf{1}^\top\mathbf{w} = 1$ — three column vectors and one matrix, with transposes to produce scalars. Understanding which dimension a vector has prevents the most common linear algebra errors in financial computing.
