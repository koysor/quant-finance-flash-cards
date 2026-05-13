# Local Outlier Factor

**Topic:** Computational Finance
**Tags:** local outlier factor, lof, density-based anomaly detection, nearest neighbours, outlier score, unsupervised learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Local Outlier Factor (LOF)** is a density-based anomaly detection algorithm that scores each observation by comparing its local density to the densities of its $k$ nearest neighbours. An observation in a sparse neighbourhood surrounded by denser clusters receives a high LOF score — it is locally anomalous relative to its context, even if it would not be flagged by a global threshold. This local perspective is essential in financial data, where different market regimes have different "normal" densities.

## Key Formula

**Reachability distance** (smoothed distance to neighbour $o$):

$$\text{reach-dist}_k(p, o) = \max\!\left(k\text{-dist}(o),\; d(p, o)\right)$$

**Local reachability density** of point $p$:

$$\text{lrd}_k(p) = \frac{1}{\displaystyle\frac{1}{|\mathcal{N}_k(p)|}\sum_{o \in \mathcal{N}_k(p)} \text{reach-dist}_k(p, o)}$$

**Local Outlier Factor:**

$$\text{LOF}_k(p) = \frac{\displaystyle\frac{1}{|\mathcal{N}_k(p)|}\sum_{o \in \mathcal{N}_k(p)} \text{lrd}_k(o)}{\text{lrd}_k(p)}$$

$\text{LOF}_k(p) \approx 1$: normal (similar density to neighbours). $\text{LOF}_k(p) \gg 1$: anomalous (much lower density than neighbours).

## Example

LOF ($k = 20$) applied to 10 years of daily equity factor scores (5 features). Two types of anomaly detected:

| Observation | LOF score | Nature |
|---|---|---|
| Normal trading day | $1.02$ | In-distribution |
| Isolated single-day spike | $4.7$ | Global outlier — far from all clusters |
| Day on crisis cluster boundary | $2.3$ | Local outlier — denser neighbours in calm regime |
| GFC core crisis day | $1.1$ | In-distribution within crisis cluster |

The GFC core days score as normal because LOF measures local density — deep within the crisis cluster they are surrounded by similar observations. A global threshold (as used by isolation forest) would flag them; LOF correctly identifies them as within-regime observations.

## Remember

LOF's key advantage over isolation forest in financial applications is **regime awareness**: it does not flag all crisis-period observations as anomalous just because crisis data is globally rare — instead it identifies observations that are unusual *relative to their local regime context*. This matters for intraday surveillance where the question is not "is this a crisis?" but "is this trade anomalous given today's market conditions?" The practical limitation is that LOF does not support out-of-sample scoring without recomputation — every new observation requires updating the $k$-NN graph, making real-time use expensive. For production systems, approximate nearest-neighbour libraries (FAISS, Annoy) reduce the per-observation cost sufficiently for end-of-day batch scoring of intraday trades.
