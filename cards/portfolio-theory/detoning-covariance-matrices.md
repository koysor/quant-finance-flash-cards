# Detoning Covariance Matrices

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** covariance matrix, market factor, clustering, eigenvalues, portfolio construction, correlation
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Detoning is a post-denoising refinement that removes the dominant market-wide eigenvector from a correlation matrix, exposing the underlying sub-market structure that clustering algorithms need to find meaningful asset groupings.

## Key Formula

After eigendecomposition $C = W\Lambda W^\top$, the market component — captured by the largest eigenvector $\mathbf{w}_1$ — is subtracted:

$$\tilde{C} = C - \lambda_1\, \mathbf{w}_1 \mathbf{w}_1^\top$$

The off-diagonal elements of $\tilde{C}$ now reflect sector and style correlations rather than universal market co-movement. Diagonal entries are rescaled to restore unit variances:

$$\tilde{C}_{ij} \leftarrow \frac{\tilde{C}_{ij}}{\sqrt{\tilde{C}_{ii}\,\tilde{C}_{jj}}}$$

## Example

A correlation matrix of 100 equities has a dominant first eigenvalue $\lambda_1 = 18$, representing broad market exposure. After detoning, residual correlations reflect industry and style factors. Hierarchical clustering on the detoned matrix cleanly separates technology, energy, and financial sectors; the same clustering on the raw matrix produces one large cluster in which every asset correlates with every other because they all share the market factor.

## Remember

Without detoning, clustering algorithms see the market factor dominating all pairwise correlations, making every asset look similar and obscuring sector structure. Removing the market "tone" reveals the sub-market correlations that matter for diversification. This step is particularly important for Nested Cluster Optimisation and Hierarchical Risk Parity, where the quality of the cluster partition determines portfolio stability.
