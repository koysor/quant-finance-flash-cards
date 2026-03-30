# Augmented Matrix

**Topic:** Linear Algebra
**Tags:** augmented matrix, linear systems, gaussian elimination, row reduction, calibration
**Author:** Claude Opus 4.6

---

## Definition

An **augmented matrix** is formed by appending the constant vector $\mathbf{b}$ to the coefficient matrix $A$ of a linear system $A\mathbf{x} = \mathbf{b}$, written $[A \mid \mathbf{b}]$. It packages the entire system into a single matrix so that row operations applied to find the solution act on both the coefficients and the constants simultaneously.

## Key Formula

For a system of $m$ equations in $n$ unknowns, the augmented matrix is the $m \times (n+1)$ matrix:

$$[A \mid \mathbf{b}] = \left[\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array}\right]$$

The system is **consistent** (has at least one solution) if and only if:

$$\text{rank}(A) = \text{rank}([A \mid \mathbf{b}])$$

## Example

A risk manager calibrates two hedge ratios $h_1, h_2$ from the system:

$$3h_1 + 2h_2 = 8, \quad h_1 + 4h_2 = 9$$

Form the augmented matrix and row-reduce:

$$\left[\begin{array}{cc|c} 3 & 2 & 8 \\ 1 & 4 & 9 \end{array}\right] \xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{cc|c} 1 & 4 & 9 \\ 3 & 2 & 8 \end{array}\right] \xrightarrow{R_2 - 3R_1} \left[\begin{array}{cc|c} 1 & 4 & 9 \\ 0 & -10 & -19 \end{array}\right]$$

Back substitution gives $h_2 = 1.9$ and $h_1 = 9 - 4(1.9) = 1.4$.

## Remember

The augmented matrix is the standard bookkeeping device for solving linear systems by hand or by algorithm. In quantitative finance, every calibration problem — fitting discount factors to bond prices, solving for implied forward rates, or finding portfolio weights that match target factor exposures — begins by writing down $A\mathbf{x} = \mathbf{b}$ and forming $[A \mid \mathbf{b}]$. Comparing $\text{rank}(A)$ with $\text{rank}([A \mid \mathbf{b}])$ is the quickest way to diagnose whether the calibration problem is solvable, underdetermined, or inconsistent — before any numerical work begins.
