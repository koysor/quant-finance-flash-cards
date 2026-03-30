# Homogeneous Systems

**Topic:** Linear Algebra
**Tags:** linear systems, null space, arbitrage, matrix equations, trivial solution
**Author:** Claude Opus 4.6

---

## Definition

A homogeneous system of linear equations is one in which every equation equals zero, written in matrix form as $A\mathbf{x} = \mathbf{0}$. The set of all solutions forms the **null space** of $A$. Every homogeneous system has at least the **trivial solution** $\mathbf{x} = \mathbf{0}$; a non-trivial solution exists if and only if $A$ has rank less than the number of unknowns.

## Key Formula

$$A\mathbf{x} = \mathbf{0}$$

where $A$ is an $m \times n$ matrix, $\mathbf{x} \in \mathbb{R}^n$, and $\mathbf{0} \in \mathbb{R}^m$. The system has a non-trivial solution if and only if

$$\operatorname{rank}(A) < n$$

equivalently, if and only if $\det(A) = 0$ when $A$ is square.

## Example

Consider the system $A\mathbf{x} = \mathbf{0}$ with

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}$$

Row-reducing gives $\begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \end{pmatrix}$, so $\operatorname{rank}(A) = 1 < 3$. The free variables $x_2 = s$ and $x_3 = t$ yield the general solution

$$\mathbf{x} = s\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} -3 \\ 0 \\ 1 \end{pmatrix}$$

The null space is two-dimensional, spanned by these two vectors.

## Remember

In quantitative finance, the no-arbitrage condition can be expressed as a homogeneous system. If columns of a matrix represent payoffs of traded assets in different states, then a portfolio $\mathbf{x}$ satisfying $A\mathbf{x} = \mathbf{0}$ with non-negative cost is an arbitrage opportunity. An arbitrage-free market requires that the only solution to this homogeneous system (subject to cost constraints) is the trivial one — making the existence or absence of non-trivial solutions directly linked to the fundamental theorem of asset pricing.
