# Spectral Clustering

**Topic:** Machine Learning
**Tags:** spectral clustering, graph laplacian, eigenvectors, asset clustering, k-means, dimensionality reduction
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Spectral clustering embeds assets into a low-dimensional space using the eigenvectors of the graph Laplacian built from pairwise distances, then applies K-means to that embedding to find clusters with arbitrary shapes that correlation distance alone cannot reveal.

## Key Formula

From distance matrix $D$, build a similarity matrix $W_{ij} = \exp(-d_{ij}^2 / \sigma^2)$ with $W_{ii} = 0$. Let $\text{Deg}_{ii} = \sum_j W_{ij}$. The normalised graph Laplacian is:

$$L_{\text{sym}} = I - \text{Deg}^{-1/2}\, W\, \text{Deg}^{-1/2}$$

Compute the $k$ eigenvectors $\mathbf{u}_1, \ldots, \mathbf{u}_k$ of $L_{\text{sym}}$ corresponding to its $k$ smallest eigenvalues. Stack them as columns to form $U \in \mathbb{R}^{N \times k}$; each row $U_i$ is the spectral embedding of asset $i$. Run K-means on $\{U_i\}$ to assign assets to $k$ clusters.

## Example

Twenty assets split into two latent groups (energy and technology), but within each group assets are in two sub-clusters connected by a single bridge asset. Hierarchical clustering on raw correlation distances merges groups sequentially, placing the bridge asset inconsistently. Spectral clustering with $k = 2$ and the second eigenvector of $L_{\text{sym}}$ cleanly separates the two groups because the Laplacian eigenvectors encode global connectivity, not just local pairwise distances.

## Remember

Hierarchical clustering finds clusters shaped like nested branches on a dendrogram; if the true asset groupings are "ring-like" or connected by correlations that span many hops in the network, hierarchical methods will fail. Spectral clustering is the method of choice when the asset graph has bottleneck structures — for example, commodity markets where seasonal clusters are connected by cross-commodity arbitrage links that span the groups.
