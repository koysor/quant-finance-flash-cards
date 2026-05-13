# Embedding Quality Metrics

**Topic:** Computational Finance
**Tags:** embedding quality, cpd, knn preservation, t-sne, umap, dimensionality reduction
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Embedding quality metrics** quantify how faithfully a low-dimensional map (produced by t-SNE, UMAP, or an autoencoder) preserves the structure of the original high-dimensional data. Two complementary measures are used: **CPD** (Correlation-based Pairwise Distance) for global structure, and **KNN preservation** for local neighbourhood structure.

## Key Formula

**CPD (global)** — Spearman rank correlation between all pairwise distances:

$$\text{CPD} = \rho_s\!\left(\{d^{\text{high}}_{ij}\},\; \{d^{\text{low}}_{ij}\}\right) \in [-1, 1]$$

High CPD ($\approx 1$): the overall distance ordering is preserved — far-apart points in high-D remain far apart in 2-D.

**KNN preservation (local)** — fraction of each point's $k$ nearest neighbours that remain nearest neighbours in the embedding:

$$\text{KNN}(k) = \frac{1}{N}\sum_{i=1}^{N} \frac{|\mathcal{N}_k^{\text{high}}(i) \cap \mathcal{N}_k^{\text{low}}(i)|}{k} \in [0, 1]$$

High KNN: local clusters are intact. $\text{KNN}(k) = 1$ means every point's $k$ neighbours are identical in both spaces.

## Example

Comparing t-SNE vs UMAP on 10 years of daily macro factor scores (5 features, 2,520 observations). $k=10$:

| Method | CPD | KNN(10) |
|---|---|---|
| t-SNE (perplexity 30) | 0.61 | 0.78 |
| UMAP (n_neighbors 15) | 0.74 | 0.72 |

t-SNE preserves local clusters better (higher KNN); UMAP preserves global structure better (higher CPD). Choice depends on whether regime classification (local) or regime ordering (global) matters more.

## Remember

CPD and KNN preservation answer the question a quantitative analyst must ask before using any embedding for production: "Is my 2-D regime map actually showing me what the data looks like, or is it a visual artefact?" In financial applications, KNN preservation is the critical metric for regime detection (you need local clusters to be intact) whilst CPD matters for tasks like stress testing (you need to know which historical periods are genuinely far from the current regime). These metrics also guide hyperparameter selection — scanning perplexity or n_neighbors and choosing the value that maximises the relevant metric on the validation period.
