# Back Substitution

**Topic:** Linear Algebra
**Tags:** back substitution, triangular systems, linear systems, numerical methods, direct solvers
**Author:** Claude Opus 4.6

---

## Definition

**Back substitution** is the algorithm for solving an upper triangular system $U\mathbf{x} = \mathbf{c}$ by working from the last equation upward. Because each row introduces exactly one new unknown, the system unravels in $O(n^2)$ operations — far cheaper than the $O(n^3)$ forward elimination that produced the triangular form.

## Key Formula

Given an $n \times n$ upper triangular matrix $U$ with non-zero diagonal entries, the solution components are computed from bottom to top:

$$x_n = \frac{c_n}{u_{nn}}$$

$$x_k = \frac{1}{u_{kk}}\!\left(c_k - \sum_{j=k+1}^{n} u_{kj}\, x_j\right), \quad k = n-1,\, n-2,\, \dots,\, 1$$

Each $x_k$ depends only on values $x_{k+1}, \dots, x_n$ that have already been found, so no further elimination is needed.

## Example

Solve the upper triangular system:

$$\begin{pmatrix} 3 & 1 & -2 \\ 0 & 2 & 4 \\ 0 & 0 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \\ 15 \end{pmatrix}$$

**Row 3:** $x_3 = \dfrac{15}{5} = 3$

**Row 2:** $x_2 = \dfrac{10 - 4(3)}{2} = \dfrac{-2}{2} = -1$

**Row 1:** $x_1 = \dfrac{7 - 1(-1) - (-2)(3)}{3} = \dfrac{7 + 1 + 6}{3} = \dfrac{14}{3}$

Solution: $\mathbf{x} = \begin{pmatrix} 14/3 \\ -1 \\ 3 \end{pmatrix}$.

## Remember

In production quantitative finance systems, back substitution is the fast final step that runs thousands of times while the expensive factorisation runs only once. When a risk engine reprices a portfolio under many stress scenarios, the coefficient matrix $A$ stays the same — only the right-hand side $\mathbf{b}$ changes with each scenario. The bank factorises $A = LU$ once at $O(n^3)$ cost, then solves each scenario by forward substitution on $L$ and back substitution on $U$, each costing only $O(n^2)$. This separation of the cubic factorisation from the quadratic solves is what makes real-time scenario analysis computationally feasible.
