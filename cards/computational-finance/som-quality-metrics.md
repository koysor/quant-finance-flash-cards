# SOM Quality Metrics

**Topic:** Computational Finance
**Tags:** som quality, quantisation error, topographic error, self-organising maps, validation, regime detection
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**SOM quality metrics** measure how well a trained Self-Organising Map represents both the data distribution and its topological structure. The two standard metrics are **Quantisation Error (QE)**, which measures representational fidelity, and **Topographic Error (TE)**, which measures topology preservation.

## Key Formula

**Quantisation Error** — mean distance from each data point to its Best Matching Unit (BMU):

$$\text{QE} = \frac{1}{N} \sum_{i=1}^{N} \|\mathbf{x}_i - \mathbf{w}_{\text{BMU}(i)}\|$$

**Topographic Error** — fraction of data points whose second-best BMU is not a grid neighbour of the BMU:

$$\text{TE} = \frac{1}{N} \sum_{i=1}^{N} \mathbf{1}\!\left[\text{BMU}_2(\mathbf{x}_i) \notin \mathcal{N}\!\left(\text{BMU}_1(\mathbf{x}_i)\right)\right]$$

A perfectly topology-preserving SOM has TE $= 0$. A smaller grid reduces QE but increases TE (overfitting); a larger grid reduces TE but increases QE if the data manifold is simpler than the grid.

## Example

A $6 \times 6$ SOM trained on daily macro factor scores (30 years, 5 features). QE $= 0.18$ (mean distance to closest node), TE $= 0.08$ (8% of observations "jump" non-adjacently on the grid). Increasing to $10 \times 10$: QE drops to $0.12$ but TE rises to $0.15$ — the grid is too large and nearby regimes are being split across distant nodes. Optimal grid: $8 \times 8$ (QE $= 0.14$, TE $= 0.06$).

## Remember

In financial regime detection, a low Topographic Error is the priority metric: a SOM where similar market conditions (e.g. two slightly different risk-off states) map to non-adjacent nodes cannot be used to trace smooth regime transitions over time. Practitioners accept a slightly higher QE in exchange for TE $< 0.05$ to ensure the SOM's 2-D visualisation faithfully represents the continuity of market state transitions — allowing a regime path (the sequence of BMUs over time) to be read as a coherent narrative of the market cycle.
