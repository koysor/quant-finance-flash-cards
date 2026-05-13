# Correlation Distance Matrix

**Topic:** Computational Finance
**Tags:** correlation distance, distance matrix, hierarchical clustering, hrp, portfolio construction, metric space
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **correlation distance matrix** converts a pairwise correlation matrix into a valid metric space suitable for clustering algorithms. Raw correlation is not a distance (it does not satisfy the triangle inequality and takes values in $[-1, 1]$); the standard transformation produces a proper distance that equals zero for perfectly correlated assets and two for perfectly anti-correlated ones.

## Key Formula

For assets $i$ and $j$ with correlation $\rho_{ij} \in [-1, 1]$:

$$d_{ij} = \sqrt{2(1 - \rho_{ij})}, \qquad d_{ij} \in [0, 2]$$

**Properties:**
- $d_{ij} = 0 \iff \rho_{ij} = 1$ (perfect co-movement)
- $d_{ij} = \sqrt{2} \iff \rho_{ij} = 0$ (uncorrelated)
- $d_{ij} = 2 \iff \rho_{ij} = -1$ (perfect anti-correlation)
- Satisfies the triangle inequality — a valid metric

An alternative formulation $d_{ij} = 1 - |\rho_{ij}|$ treats positive and negative correlation as equivalent (useful when anti-correlated pairs should be clustered together as hedges).

## Example

Three assets: US Equity ($\rho$ with EU Equity $= 0.85$, with Bonds $= -0.30$). Distances: $d_{\text{US-EU}} = \sqrt{2(1-0.85)} = 0.55$ (close — clusters together); $d_{\text{US-Bond}} = \sqrt{2(1-(-0.30))} = 1.61$ (distant — different clusters). Ward's linkage on this matrix first merges US and EU Equity, confirming that geography-within-equity is the tightest co-movement relationship.

## Remember

The correlation distance matrix is the standard input to hierarchical clustering and HRP in finance because it is constructed entirely from return co-movements, requiring no price-level assumptions. The $\sqrt{2(1-\rho)}$ form (not simple $1-\rho$) is used because it satisfies the triangle inequality, which is a formal requirement for hierarchical clustering linkage methods to produce a valid dendrogram. In practice, the correlation matrix is estimated on rolling windows or with shrinkage estimators (Ledoit-Wolf) to stabilise the distance structure across market regimes.
