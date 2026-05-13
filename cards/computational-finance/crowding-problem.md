# Crowding Problem

**Topic:** Computational Finance
**Tags:** crowding problem, dimensionality reduction, t-sne, t-distribution, curse of dimensionality, visualisation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **crowding problem** is a fundamental obstacle in dimensionality reduction: when projecting from high-dimensional space to 2-D, there is insufficient geometric room to faithfully represent all inter-point distances. Points that are moderately separated in high-D collapse together in 2-D, producing a featureless blob that obscures genuine cluster structure.

## Key Formula

The root cause is the volume scaling of high-dimensional balls. In $d$ dimensions, the volume of a shell at distance $r$ grows as $r^{d-1}$:

$$\text{Vol}(\text{shell at } r) \propto r^{d-1} \, \delta r$$

As $d \to \infty$, almost all volume lies near the surface — pairwise distances concentrate around a single value, making all points approximately equidistant.

**t-SNE's solution**: use a Student-$t$ distribution (heavy tails) in low-D instead of Gaussian, so that a moderate distance in high-D maps to a large distance in 2-D:

$$q_{ij}^{\text{Gaussian}} = \frac{e^{-\|\mathbf{y}_i - \mathbf{y}_j\|^2 / 2\sigma^2}}{\sum} \quad \to \quad q_{ij}^{t} = \frac{(1+\|\mathbf{y}_i-\mathbf{y}_j\|^2)^{-1}}{\sum}$$

The heavier tail allows the 2-D map to use more space, pushing clusters apart.

## Example

100 points drawn uniformly from a 50-dimensional unit hypersphere. Pairwise distance histogram: mean $\approx \sqrt{50}$, standard deviation $\approx 1.0$ — all points are almost equidistant. PCA projection to 2-D: blob with no discernible structure. t-SNE: even though all high-D distances are similar, the $t$-distribution allows the algorithm to exaggerate small relative differences, revealing the otherwise invisible local neighbourhood structure.

## Remember

The crowding problem explains why linear methods (PCA) fail to reveal cluster structure in high-dimensional financial factor spaces, and why t-SNE's $t$-distribution choice is not arbitrary — it is a mathematically motivated correction for the volume concentration of high-dimensional spaces. In practice, this means a t-SNE plot of equity factor loadings will show visually well-separated clusters even when the raw pairwise distances in 50-D are nearly all identical, because the heavy tail is doing the geometric work of creating separation. The trade-off is that inter-cluster distances in the 2-D map are not interpretable — only intra-cluster distances (local neighbourhoods) are meaningful.
