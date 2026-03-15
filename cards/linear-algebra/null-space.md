# Null Space

**Topic:** Linear Algebra
**Tags:** null space, kernel, linear systems, rank, portfolio optimisation, redundancy
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **null space** (or **kernel**) of a matrix $A$ is the set of all vectors $\mathbf{x}$ that satisfy $A\mathbf{x} = \mathbf{0}$. It is always a subspace, and its dimension — the **nullity** — measures how many degrees of freedom exist in the solution set of any system $A\mathbf{x} = \mathbf{b}$.

## Key Formula

$$\text{null}(A) = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$$

By the **rank-nullity theorem**:

$$\text{rank}(A) + \text{nullity}(A) = n$$

where $n$ is the number of columns. If $A\mathbf{x} = \mathbf{b}$ has a particular solution $\mathbf{x}_0$, the **general solution** is:

$$\mathbf{x} = \mathbf{x}_0 + \mathbf{x}_n, \quad \mathbf{x}_n \in \text{null}(A)$$

The null space is trivial ($\{\mathbf{0}\}$) if and only if $A$ has full column rank — i.e., $A$ is invertible when square.

## Example

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$. Row reduction gives $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{pmatrix}$, so $\text{rank}(A) = 1$ and nullity $= 3 - 1 = 2$.

The null space is all $\mathbf{x}$ with $x_1 = -2x_2 - 3x_3$:

$$\text{null}(A) = \text{span}\!\left\{\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix},\ \begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix}\right\}$$

## Remember

In mean-variance portfolio optimisation, the null space of the constraint matrix determines the set of **unconstrained portfolio directions** — movements in weight space that satisfy all constraints but affect return and risk. If the covariance matrix $\Sigma$ has a non-trivial null space (i.e., is singular), portfolios exist with zero measured risk, which is an artefact of perfectly correlated assets or redundant positions. Regularisation techniques such as eigenvalue clipping and ridge regression work precisely by shrinking or eliminating these null-space directions.
