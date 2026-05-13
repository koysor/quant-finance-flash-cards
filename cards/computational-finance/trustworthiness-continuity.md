# Trustworthiness and Continuity

**Topic:** Computational Finance
**Tags:** trustworthiness, continuity, embedding quality, t-sne, umap, nearest neighbours, dimensionality reduction
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Trustworthiness** and **continuity** are complementary embedding quality metrics that give a more complete picture than KNN preservation alone. Trustworthiness penalises **false neighbours** — points that appear close in the 2-D embedding but are far apart in high-D. Continuity penalises **missing neighbours** — points that are genuinely close in high-D but pulled apart in the embedding. Both lie in $[0, 1]$; values above $0.90$ indicate a high-quality embedding.

## Key Formula

Let $r(i,j)$ = rank of point $j$ in the high-D neighbourhood of $i$, and $\hat{r}(i,j)$ = rank in the low-D embedding.

**Trustworthiness** (penalises false low-D neighbours):

$$T(k) = 1 - \frac{2}{nk(2n-3k-1)} \sum_{i=1}^{n} \sum_{j \in \mathcal{U}_k(i)} \bigl(r(i,j) - k\bigr)$$

where $\mathcal{U}_k(i)$ = $k$-nearest neighbours of $i$ in the embedding that are **not** in the top $k$ in high-D.

**Continuity** (penalises missing high-D neighbours):

$$C(k) = 1 - \frac{2}{nk(2n-3k-1)} \sum_{i=1}^{n} \sum_{j \in \mathcal{V}_k(i)} \bigl(\hat{r}(i,j) - k\bigr)$$

where $\mathcal{V}_k(i)$ = $k$-nearest neighbours of $i$ in high-D that are **not** in the top $k$ in the embedding.

## Example

t-SNE applied to 500 equity factor vectors, $k = 10$:

| Metric | Score | Interpretation |
|---|---|---|
| $T(10)$ | 0.94 | 94% of low-D neighbours are genuine high-D neighbours |
| $C(10)$ | 0.87 | 87% of true high-D neighbours appear in the embedding |

High trustworthiness but lower continuity indicates **cluster fragmentation**: true neighbours are sometimes split across visually distinct groups. For regime classification by $k$-NN lookup, the 2-D map is reliable (false-neighbour rate is low). For discovering *all* similar historical episodes, 13% of genuine analogues will be missed — requiring a search over a wider neighbourhood radius.

## Remember

Trustworthiness and continuity diagnose different failure modes. A low-trustworthiness embedding creates phantom relationships in a regime map — the current market state appears close to a historical episode it does not actually resemble, leading to a wrong regime classification. A low-continuity embedding fragments true regimes — a 2008 crisis cluster may appear as three separate blobs, causing the algorithm to miss that today's conditions resemble episodes from all three. In quant finance, **use trustworthiness as the gate for $k$-NN inference tasks** (regime identification, nearest-neighbour stress test selection) and **continuity as the gate for cluster analysis** (regime definition, anomaly region mapping). Both should be reported alongside CPD and KNN preservation as part of a complete embedding validation framework.
