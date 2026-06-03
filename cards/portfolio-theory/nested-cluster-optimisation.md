# Nested Cluster Optimisation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** nested cluster optimisation, nco, hierarchical clustering, portfolio construction, markowitz, divide and conquer
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Nested Cluster Optimisation (NCO) is a portfolio construction algorithm that groups assets into clusters of high intra-correlation, runs minimum-variance optimisation within each cluster, and then optimises across clusters as "meta-assets", reducing sensitivity to a noisy covariance matrix.

## Key Formula

For each cluster $k$ containing assets $\mathcal{C}_k$, the intra-cluster weights solve the minimum-variance problem:

$$\mathbf{w}^{(k)}_{\text{intra}} = \arg\min_{\mathbf{w}} \mathbf{w}^\top \Sigma^{(k)} \mathbf{w} \quad \text{s.t.} \quad \mathbf{1}^\top\mathbf{w} = 1$$

Each cluster becomes a meta-asset with return $r^{(k)}_t = (\mathbf{w}^{(k)}_{\text{intra}})^\top \mathbf{r}^{(k)}_t$. The inter-cluster weights $\mathbf{w}_{\text{inter}}$ are found by a second optimisation over the $K \times K$ cluster covariance matrix. The final weight for asset $i$ in cluster $k$ is:

$$w_i = w^{(k)}_{\text{intra},\,i} \times w^{(k)}_{\text{inter}}$$

## Example

Twenty equities are grouped by hierarchical clustering into four clusters: Technology (6 stocks), Financials (5), Energy (4), Consumer (5). Within Financials, minimum-variance weights are computed on the $5 \times 5$ sub-covariance matrix. The four clusters are then treated as four meta-assets and a second minimum-variance step allocates capital across them. Each sub-problem involves a small, well-conditioned matrix, so the resulting weights are stable.

## Remember

Standard Markowitz on the full covariance matrix amplifies estimation errors because highly correlated assets receive large opposing weights. NCO sidesteps this by exploiting the block structure of the correlation matrix: correlated assets are grouped first and only a single representative allocation is made across clusters. This divide-and-conquer approach produces portfolios that are more robust to parameter uncertainty and better diversified across genuine economic risk factors.
