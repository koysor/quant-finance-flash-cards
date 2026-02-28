# Systems of Linear Equations

**Topic:** Linear Algebra
**Tags:** linear algebra, systems, simultaneous equations, calibration, replication
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

A **system of linear equations** is a set of equations, each linear in the same unknowns, that must all be satisfied simultaneously. In matrix form the system is written $A\mathbf{x} = \mathbf{b}$, where $A$ is the coefficient matrix, $\mathbf{x}$ the vector of unknowns, and $\mathbf{b}$ the vector of constants.

## Key Formula

A system of $n$ equations in $n$ unknowns:

$$A\mathbf{x} = \mathbf{b}$$

has a unique solution when $\det(A) \neq 0$:

$$\mathbf{x} = A^{-1}\mathbf{b}$$

The system may also be solved by **Gaussian elimination** (row reduction) or **Cramer's rule**. When $\det(A) = 0$, the system has either no solution or infinitely many solutions.

## Example

A trader wants to replicate a payoff using two bonds. Bond A pays £1 in year 1 and £1 in year 2. Bond B pays £0 in year 1 and £1 in year 2. The target payoff is £3 in year 1 and £5 in year 2.

$$\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x_A \\ x_B \end{pmatrix} = \begin{pmatrix} 3 \\ 5 \end{pmatrix}$$

From row 1: $x_A = 3$. Substituting into row 2: $3 + x_B = 5$, so $x_B = 2$.

Buy 3 units of Bond A and 2 units of Bond B.

## Remember

Systems of linear equations are the workhorse of quantitative finance calibration. When fitting a yield curve, you solve a system to find discount factors that exactly reprice observed bond prices. When constructing a replicating portfolio, you solve for the holdings that match a target set of cash flows. When calibrating a volatility surface, you solve for model parameters that match market option prices. In each case, the no-arbitrage condition translates directly into a system $A\mathbf{x} = \mathbf{b}$.
