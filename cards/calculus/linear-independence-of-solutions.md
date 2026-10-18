# Linear Independence and the Structure of ODE Solutions

**Topic:** Calculus
**Tags:** ODE, linear independence, Wronskian, superposition, general solution, complementary function
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

For a **linear homogeneous** ODE, any linear combination of solutions is again a solution (superposition). An $n$th-order linear equation has exactly $n$ **linearly independent** solutions $y_1, \dots, y_n$, and its general solution is their combination. This is why the complementary function plus a particular integral is the *complete* solution, not merely *a* solution.

## Key Formula

$$y = c_1 y_1 + c_2 y_2 + \cdots + c_n y_n \qquad\text{with Wronskian}\qquad W = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} \neq 0$$

A non-zero Wronskian confirms that two solutions are independent.

## Example

For $y'' - y = 0$ take $y_1 = e^{x}$ and $y_2 = e^{-x}$:

$$W = \begin{vmatrix} e^{x} & e^{-x} \\ e^{x} & -e^{-x} \end{vmatrix} = -1 - 1 = -2 \neq 0$$

They are independent, so $y = Ae^{x} + Be^{-x}$ is the general solution. By contrast $e^{2x}$ and $3e^{2x}$ are dependent: they span only one dimension, not two.

## Remember

Superposition is what lets you build a solution to a pricing PDE from simpler pieces, and it is the same idea as a portfolio being the sum of its positions. The fact that a non-homogeneous equation's solution is $y_c + y_p$ rests on it.
