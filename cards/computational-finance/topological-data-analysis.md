# Topological Data Analysis

**Topic:** Computational Finance
**Tags:** topological data analysis, tda, persistent homology, betti numbers, manifold, regime detection
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Topological data analysis (TDA)** studies the shape of data by tracking which connected components, loops, and voids persist as a distance threshold is varied. Unlike t-SNE or UMAP, TDA produces **coordinate-free, scale-invariant summaries** of data topology — it detects structural features that survive across multiple scales, which is precisely the structure that matters for regime detection and crisis identification in financial markets.

## Key Formula

**Persistent homology** — build a sequence of simplicial complexes (Vietoris–Rips filtration) by growing balls of radius $\varepsilon$ around each point:

$$\emptyset = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_n$$

For each topological feature (connected component, loop, void) track its **birth** $b_i$ and **death** $d_i$ as $\varepsilon$ increases:

$$\text{Persistence} = d_i - b_i$$

Features with high persistence are genuine topological structure; short-lived features are noise.

**Betti numbers** count features at dimension $p$:
- $\beta_0$: number of connected components (clusters)
- $\beta_1$: number of independent loops
- $\beta_2$: number of voids

Results are visualised as a **persistence diagram** (scatter plot of $(b_i, d_i)$ pairs) or **barcode** (horizontal bars of length $d_i - b_i$).

## Example

TDA applied to 20 years of daily macro factor scores (5 features). The Vietoris–Rips filtration reveals:

- $\beta_0$: 4 persistent connected components — corresponding to expansion, contraction, crisis, and recovery regimes. These match $k$-means with $k = 4$ but are discovered without specifying $k$ in advance.
- $\beta_1$: 1 persistent loop — a cyclic structure connecting crisis → recovery → expansion → contraction → crisis. t-SNE flattens this cycle into an apparent cluster; TDA captures the cyclical topology.

The persistent loop survives across scales $\varepsilon \in [0.3, 1.8]$ — confirming it is genuine market cycle structure, not a noise artefact.

## Remember

TDA's key advantage over t-SNE and UMAP in financial applications is detecting **cyclical regime structure** — the business cycle is genuinely loop-shaped in macro factor space, and embedding-based methods destroy this topology by forcing data into a 2-D scatter plot. TDA captures it without any embedding. The practical limitation is computational cost: the Vietoris–Rips filtration scales $O(N^3)$ in the number of observations, making it impractical for daily data over 20+ years without subsampling. In practice, TDA is used to audit the topology of a training set (confirming that $k$-means or t-SNE cluster counts are consistent with the Betti numbers) rather than as a real-time regime signal — it provides the ground truth topological structure that other methods approximate.
