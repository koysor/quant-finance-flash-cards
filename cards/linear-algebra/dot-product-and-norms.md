# Dot Product and Norms

**Topic:** Linear Algebra
**Tags:** linear algebra, vectors, dot product, norms, Cauchy-Schwarz, portfolio theory
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

The **dot product** (or inner product) of two vectors $\mathbf{a}$ and $\mathbf{b}$ in $\mathbb{R}^n$ is a scalar that measures how much the two vectors point in the same direction. The **Euclidean norm** (or magnitude) of a vector is its length, derived from the dot product of the vector with itself.

## Key Formula

**Algebraic dot product:**

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i \, b_i$$

**Geometric interpretation:**

$$\mathbf{a} \cdot \mathbf{b} = \|\mathbf{a}\| \, \|\mathbf{b}\| \cos\theta$$

where $\theta$ is the angle between the two vectors.

**Euclidean norm:**

$$\|\mathbf{x}\| = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{\sum_{i=1}^{n} x_i^2}$$

**Properties:**

- **Linearity:** $\mathbf{a} \cdot (c\,\mathbf{b} + \mathbf{d}) = c\,(\mathbf{a} \cdot \mathbf{b}) + \mathbf{a} \cdot \mathbf{d}$
- **Symmetry:** $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$
- **Positive-definiteness:** $\|\mathbf{a}\|^2 = \mathbf{a} \cdot \mathbf{a} \geq 0$, with equality iff $\mathbf{a} = \mathbf{0}$
- **Cauchy–Schwarz inequality:** $|\mathbf{a} \cdot \mathbf{b}| \leq \|\mathbf{a}\| \, \|\mathbf{b}\|$

## Example

Let $\mathbf{a} = \begin{pmatrix} 1 \\ 3 \\ -2 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 4 \\ -1 \\ 5 \end{pmatrix}$.

**Dot product:**

$$\mathbf{a} \cdot \mathbf{b} = 1(4) + 3(-1) + (-2)(5) = 4 - 3 - 10 = -9$$

**Norms:**

$$\|\mathbf{a}\| = \sqrt{1^2 + 3^2 + (-2)^2} = \sqrt{14} \approx 3.742$$

$$\|\mathbf{b}\| = \sqrt{4^2 + (-1)^2 + 5^2} = \sqrt{42} \approx 6.481$$

**Angle between them:**

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \, \|\mathbf{b}\|} = \frac{-9}{\sqrt{14}\,\sqrt{42}} = \frac{-9}{\sqrt{588}} \approx -0.371$$

$$\theta \approx 111.8°$$

The negative dot product confirms the vectors point in broadly opposite directions.

**Cauchy–Schwarz check:** $|-9| = 9 \leq \sqrt{14}\,\sqrt{42} = \sqrt{588} \approx 24.25$ ✓

## Remember

In portfolio theory, **portfolio variance** is the quadratic form $\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w}$, where $\mathbf{w}$ is the weight vector and $\Sigma$ is the covariance matrix. This is built from dot products: the $(i,j)$ entry of $\Sigma$ is itself a dot-product-like sum $\sum_t r_{i,t}\,r_{j,t}$ over return observations.

**Correlation is a normalised dot product.** If you treat each asset's return series as a vector in $\mathbb{R}^T$, the sample correlation coefficient is:

$$\rho_{ij} = \frac{\mathbf{r}_i \cdot \mathbf{r}_j}{\|\mathbf{r}_i\| \, \|\mathbf{r}_j\|}$$

(after de-meaning). This is exactly $\cos\theta$ — two perfectly correlated assets have $\theta = 0°$, uncorrelated assets are orthogonal ($\theta = 90°$), and negatively correlated assets point in opposite directions. The Cauchy–Schwarz inequality guarantees $-1 \leq \rho \leq 1$.
