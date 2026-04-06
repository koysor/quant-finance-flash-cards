# Inner Product Notation

**Topic:** Mathematical Notation
**Tags:** notation, inner product, dot product, angle bracket, orthogonality, projection
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **inner product** is a function that takes two vectors and returns a scalar, encoding the geometric relationship between them. Several notations coexist:

| Symbol | Context | Definition (finite-dimensional) |
|---|---|---|
| $\langle \mathbf{u}, \mathbf{v} \rangle$ | Abstract / general | Inner product in any inner product space |
| $\mathbf{u} \cdot \mathbf{v}$ | Euclidean geometry | $\sum_i u_i v_i$ |
| $\mathbf{u}^\top \mathbf{v}$ | Matrix algebra | Row vector times column vector |
| $\langle f, g \rangle = \int f(x) g(x) \, dx$ | Function spaces | $L^2$ inner product of functions |

All three finite-dimensional forms are equivalent: $\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \mathbf{u}^\top \mathbf{v} = \sum_i u_i v_i$.

## Key Formula

**Cosine of angle between vectors:**

$$\cos\theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}$$

**Orthogonality condition:**

$$\langle \mathbf{u}, \mathbf{v} \rangle = 0 \iff \mathbf{u} \perp \mathbf{v}$$

**Projection of $\mathbf{u}$ onto $\mathbf{v}$:**

$$\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\langle \mathbf{v}, \mathbf{v} \rangle} \mathbf{v}$$

**Portfolio return** as inner product:

$$R_p = \mathbf{w}^\top \mathbf{r} = \langle \mathbf{w}, \mathbf{r} \rangle = \sum_{i=1}^n w_i r_i$$

## Example

**Principal Component Analysis (PCA):** the first principal component $\mathbf{v}_1$ is the direction of maximum variance. The projection of a return vector $\mathbf{r}$ onto $\mathbf{v}_1$ is the inner product $\langle \mathbf{r}, \mathbf{v}_1 \rangle = \mathbf{r}^\top \mathbf{v}_1$, giving the first factor score. Orthogonality of principal components — $\langle \mathbf{v}_i, \mathbf{v}_j \rangle = 0$ for $i \neq j$ — ensures factors carry non-redundant risk information.

## Remember

The inner product notation $\mathbf{w}^\top \mathbf{r}$ for portfolio return is ubiquitous in quant finance precisely because it reduces the sum $\sum_i w_i r_i$ to a single symbol. The geometric interpretation — $\langle \mathbf{u}, \mathbf{v} \rangle = \lVert\mathbf{u}\rVert\lVert\mathbf{v}\rVert\cos\theta$ — connects portfolio construction to orthogonality: an **orthogonal portfolio** to a factor $\mathbf{v}_k$ satisfies $\langle \mathbf{w}, \mathbf{v}_k \rangle = 0$, meaning it has zero factor exposure. This is the mathematical basis for factor neutrality in long/short hedge fund strategies.
