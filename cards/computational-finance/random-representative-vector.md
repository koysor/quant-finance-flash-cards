# Random Representative Vector

**Topic:** Computational Finance
**Tags:** initialisation, som, competitive learning, weight vector, random initialisation, clustering
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **random representative vector** is a prototype vector that has been randomly initialised before competitive learning begins. In Self-Organizing Maps and k-means, each node (or cluster centre) starts as a random vector in the feature space; training then moves these random starting points towards meaningful representatives of the data they eventually model.

## Key Formula

**Uniform random initialisation** — draw each component independently from the data range:

$$w_{kj} \sim \mathcal{U}(\min_i x_{ij},\; \max_i x_{ij}), \quad k = 1,\ldots,K,\quad j = 1,\ldots,d$$

**Random data-point initialisation** (Forgy method) — sample $K$ observations without replacement:

$$\mathbf{w}_k = \mathbf{x}_{i_k}, \quad i_1, \ldots, i_K \sim \text{Uniform}\{1, \ldots, N\} \text{ without replacement}$$

**k-means++ seeding** — choose each new centroid with probability proportional to squared distance from the nearest existing centroid:

$$P(\mathbf{x}_i \text{ is next centre}) = \frac{\|\mathbf{x}_i - \mathbf{w}_{\text{nearest}}\|^2}{\sum_j \|\mathbf{x}_j - \mathbf{w}_{\text{nearest}}\|^2}$$

k-means++ spreads initial centroids across the data, reducing the chance of poor local-minimum convergence by a factor of $O(\log K)$ in theory.

## Example

A $4 \times 4$ SOM is trained on daily market states (yield, spread, VIX, FX — all normalised). With fully random initialisation, runs 1–5 produce regime maps that look different from each other — some runs miss the "crisis" regime entirely by initialising no nodes near the high-VIX region. With k-means++ seeding, all five runs produce qualitatively similar maps. The within-cluster inertia is 23% lower on average with k-means++ seeding than with pure random initialisation.

## Remember

In quantitative finance, poor initialisation of SOM or k-means weight vectors is a **practical production risk**: if the random starting vectors cluster in a low-volatility region of the data, the algorithm may converge to a map that lumps together distinct crisis and near-crisis regimes. Risk teams mitigate this by:

1. Running the algorithm multiple times with different random seeds and choosing the solution with the lowest inertia (best total within-cluster distance)
2. Using **k-means++ seeding**, which guarantees the initial random representatives are spread across the feature space, dramatically reducing sensitivity to the random start
3. Using **PCA-based initialisation** for SOMs — placing the initial weight vectors along the first two principal components of the data, which directly embeds prior knowledge of the main variance directions (e.g., risk-on/risk-off and duration exposure)

The principle generalises: any model with random initialisation is only as good as its escape from poor starting conditions.
