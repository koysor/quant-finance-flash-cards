# Minkowski Distance

**Topic:** Computational Finance
**Tags:** minkowski distance, euclidean distance, manhattan distance, knn, distance metrics, feature scaling
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Minkowski distance** is a generalised distance metric parameterised by $p$ that unifies Euclidean and Manhattan distance as special cases. It quantifies the dissimilarity between two feature vectors $\mathbf{x}$ and $\mathbf{y}$ in $N$-dimensional space.

## Key Formula

$$d_p(\mathbf{x}, \mathbf{y}) = \left(\sum_{n=1}^{N} |x_n - y_n|^p\right)^{1/p}$$

| $p$ | Name | Properties |
|---|---|---|
| 1 | Manhattan ($\ell_1$) | Robust to outliers; sparse paths |
| 2 | Euclidean ($\ell_2$) | Smooth; most common default |
| $\infty$ | Chebyshev | $\max_n \lvert x_n - y_n\rvert$ — worst single feature |

As $p \to \infty$: $d_\infty(\mathbf{x}, \mathbf{y}) = \max_n |x_n - y_n|$, so only the largest feature difference matters.

## Example

Two equity factor vectors: $\mathbf{x} = (0.5, 1.2)$ (momentum, value) and $\mathbf{y} = (0.1, 0.8)$. Differences: $|0.5-0.1|=0.4$, $|1.2-0.8|=0.4$.

- $p=1$: $d_1 = 0.4 + 0.4 = 0.8$
- $p=2$: $d_2 = \sqrt{0.4^2 + 0.4^2} = \sqrt{0.32} \approx 0.566$
- $p=\infty$: $d_\infty = \max(0.4, 0.4) = 0.4$

The $p$ choice affects which stocks are classified as "nearest neighbours" and therefore which trades the KNN signal recommends.

## Remember

Distance metric choice matters because KNN is purely distance-based — the $p$ parameter changes which observations are considered similar. In financial factor models, Manhattan distance ($p=1$) is preferred when features have fat-tailed distributions (e.g. return-based signals), as it is less dominated by outlier feature differences than Euclidean distance. Feature scaling (standardisation) is mandatory regardless of $p$ choice, because Minkowski distance gives more weight to features with larger raw scales.
