# Vectors

**Topic:** Calculus
**Tags:** vector, magnitude, direction, unit vector, dot product, position vector, addition
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **vector** is a quantity with both magnitude and direction, written as a column $\mathbf{v} = \begin{pmatrix}a\\b\\c\end{pmatrix}$ or using component notation $a\mathbf{i} + b\mathbf{j} + c\mathbf{k}$. Vectors are added component-wise and scaled by multiplying each component by a scalar.

## Key Formula

**Magnitude:** $|\mathbf{v}| = \sqrt{a^2 + b^2 + c^2}$

**Unit vector:** $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{|\mathbf{v}|}$

**Addition:** $\mathbf{u} + \mathbf{v} = \begin{pmatrix}u_1 + v_1\\u_2 + v_2\\u_3 + v_3\end{pmatrix}$

**Dot product:** $\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3 = |\mathbf{u}||\mathbf{v}|\cos\theta$

**Angle between vectors:** $\cos\theta = \dfrac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}||\mathbf{v}|}$

## Example

Let $\mathbf{u} = \begin{pmatrix}3\\4\end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix}1\\2\end{pmatrix}$.

$|\mathbf{u}| = 5$, $|\mathbf{v}| = \sqrt{5}$, $\mathbf{u} \cdot \mathbf{v} = 3 + 8 = 11$.

Angle: $\cos\theta = \frac{11}{5\sqrt{5}} \approx 0.984$, so $\theta \approx 10.3°$.

## Remember

Vectors are the language of **multi-asset portfolio analysis**. A portfolio is a weight vector $\mathbf{w} = (w_1, \ldots, w_n)^\top$ and expected returns are a vector $\boldsymbol{\mu}$; the portfolio return is the dot product $\boldsymbol{\mu} \cdot \mathbf{w}$. Portfolio variance is $\mathbf{w}^\top \Sigma \mathbf{w}$ — a quadratic form in the weight vector. The **correlation** between two assets is the cosine of the angle between their return vectors, directly connecting the vector dot product formula to the financial concept of correlation and diversification.
