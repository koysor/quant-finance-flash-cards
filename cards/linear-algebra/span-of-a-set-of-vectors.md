# Span of a Set of Vectors

**Topic:** Linear Algebra
**Tags:** span, linear combinations, subspace, column space, reachable payoffs, replication
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **span** of a set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ is the set of all possible linear combinations of those vectors. It is the smallest subspace that contains every vector in the set.

## Key Formula

$$\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_n) = \left\{ c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n \;\middle|\; c_i \in \mathbb{R} \right\}$$

The span is always a **subspace** of the ambient vector space: it contains the zero vector (set all $c_i = 0$), and is closed under addition and scalar multiplication.

The **dimension** of the span equals the number of linearly independent vectors in the set — any redundant vectors do not enlarge the span.

## Example

Consider two asset return vectors over three months: $\mathbf{r}_1 = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ and $\mathbf{r}_2 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$.

Any portfolio combining these two assets produces a return vector in their span. For weights $c_1 = 0.6$ and $c_2 = 0.4$:

$$0.6\begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} + 0.4\begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = \begin{pmatrix} 1.6 \\ -0.6 \\ 1.4 \end{pmatrix}$$

This portfolio return lies in $\text{span}(\mathbf{r}_1, \mathbf{r}_2)$ — a plane through the origin in $\mathbb{R}^3$. Any return vector not on this plane is **unreachable** with just these two assets.

## Remember

In derivatives pricing, the span of a set of traded instruments defines exactly which payoffs can be **replicated**. A market is complete when the payoff vectors of the available instruments span the entire state space — every contingent claim can be expressed as a linear combination. If a desired payoff lies outside the span, it cannot be perfectly hedged, and residual risk remains. Checking whether a target payoff belongs to the span of your hedging instruments is the first step in any replication argument.
