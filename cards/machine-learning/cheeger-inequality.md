# Cheeger Inequality

**Topic:** Machine Learning
**Tags:** cheeger inequality, graph partitioning, spectral graph theory, normalised cut, algebraic connectivity, fiedler
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Cheeger inequality bounds the minimum normalised cut cost of a graph between half the Fiedler value and its square root, providing the theoretical guarantee that spectral clustering using the Fiedler vector finds a near-optimal asset partition.

## Key Formula

The **Cheeger constant** (minimum normalised cut) for a graph $G = (V, E)$ is:

$$h(G) = \min_{S \subset V} \frac{\lvert\{(i,j)\in E : i\in S,\, j\notin S\}\rvert}{\min(\lvert S\rvert,\, \lvert V\setminus S\rvert)}$$

The Cheeger inequality relates $h(G)$ to the Fiedler value $\lambda_2$ of the normalised Laplacian:

$$\frac{\lambda_2}{2} \leq h(G) \leq \sqrt{2\lambda_2}$$

The **lower bound** guarantees that any partition must remove at least $\lambda_2/2$ of the normalised edge weight. The **upper bound** guarantees the Fiedler vector partition achieves cut cost at most $\sqrt{2\lambda_2}$ — within $O(\sqrt{1/\lambda_2})$ of optimal.

## Example

Asset graph with $\lambda_2 = 0.04$: Cheeger bounds give $0.02 \leq h(G) \leq 0.283$. The Fiedler vector partition achieves $h = 0.07$, against an optimal $h = 0.06$ from exhaustive search. The spectral method finds a partition within 17% of optimal. For 200 assets, exhaustive search over $2^{199}$ possible bisections is impossible; spectral clustering achieves near-optimal quality in $O(N^2)$ time by exploiting the Fiedler vector.

## Remember

The Cheeger inequality transforms spectral clustering from a plausible heuristic into a provably good algorithm. In portfolio construction, the cluster partition determines how capital is allocated across groups of correlated assets in HRP and NCO — a poor partition leads to concentrated risk. The Cheeger bound guarantees the Fiedler vector partition minimises cross-cluster correlation leakage to within a factor of $O(\sqrt{\lambda_2})$ of the best possible partition, making spectral methods the theoretically sound choice over ad-hoc groupings by sector or market-cap.
