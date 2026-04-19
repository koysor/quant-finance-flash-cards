# Distance Metrics

**Topic:** Computational Finance
**Tags:** euclidean distance, manhattan distance, cosine similarity, knn, clustering, feature scaling
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Distance metrics** are mathematical functions that quantify how dissimilar two data points (feature vectors) are. They are fundamental to algorithms such as K-Nearest Neighbours and K-Means Clustering, which group or compare observations by proximity.

## Key Formula

**Euclidean ($L^2$):**
$$d(\mathbf{x}, \mathbf{y}) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}$$

**Manhattan ($L^1$):**
$$d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^{n}|x_i - y_i|$$

**Cosine similarity (angle-based):**
$$\cos\theta = \frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|\,\|\mathbf{y}\|}$$

## Example

Two bond portfolios described by duration, convexity, and credit spread. Euclidean distance captures overall magnitude of difference; cosine similarity measures whether the portfolios tilt in the same direction regardless of size.

## Remember

Feature scaling (z-score normalisation) is mandatory before computing any distance metric. Without it, a variable measured in basis points (small numbers) is dominated by one measured in notional (large numbers), producing meaningless distances — a common error when clustering fixed-income portfolios.
