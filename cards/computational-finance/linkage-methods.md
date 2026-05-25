# Linkage Methods

**Topic:** Computational Finance
**Tags:** linkage methods, hierarchical clustering, ward linkage, single linkage, complete linkage, correlation
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Linkage methods** define how the distance between two clusters is computed from the pairwise distances of their constituent observations. The choice of linkage determines the shape and interpretability of the resulting dendrogram — different methods have different tendencies to produce compact, balanced, or chained clusters.

## Key Formula

Let clusters $A$ and $B$ contain points with pairwise distances $d(a, b)$:

| Linkage | Formula | Behaviour |
|---|---|---|
| Single | $\min_{a \in A,\, b \in B} d(a, b)$ | Sensitive to outliers; creates chains |
| Complete | $\max_{a \in A,\, b \in B} d(a, b)$ | Creates compact, equal-sized clusters |
| Average (UPGMA) | $\frac{1}{\lvert A\rvert\lvert B\rvert}\sum_{a \in A}\sum_{b \in B} d(a, b)$ | Compromise; robust |
| **Ward's** | $\Delta J = J_{A \cup B} - J_A - J_B$ | Minimises within-cluster variance increase |

**Ward's linkage** is typically preferred in finance because it produces balanced clusters of comparable size — reflecting the assumption that securities are drawn from a moderate number of approximately equal-sized risk factor groups.

## Example

Five assets with correlation matrix. Applying Ward's vs Single linkage to distance matrix $d_{ij} = 1 - |\rho_{ij}|$:

- **Ward's**: Merges assets 1 & 2 (correlation 0.85), then 3 & 4 (0.78), producing two tight groups before a late merge — clean sector structure.
- **Single linkage**: Chains assets sequentially, with asset 5 joining the growing cluster last — not useful for portfolio diversification.

## Remember

Ward's linkage dominates in financial applications because it builds compact, balanced clusters that map naturally to risk factor groups — sectors, regions, or style exposures. Single linkage produces "chaining" where one outlier stock can bridge otherwise unrelated clusters, creating misleading dendrograms. In Hierarchical Risk Parity (HRP), Ward's linkage on the correlation distance matrix is the standard first step, ensuring the resulting dendrogram reflects genuine co-movement structure rather than spurious connections through bridging assets.
