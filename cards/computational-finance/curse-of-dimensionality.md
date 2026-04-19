# Curse of Dimensionality

**Topic:** Computational Finance
**Tags:** dimensionality, feature selection, PCA, sparsity, machine learning, overfitting
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **curse of dimensionality** refers to the exponential growth in data volume required to maintain statistical coverage as the number of features (dimensions) increases. In high-dimensional spaces, data becomes increasingly sparse and distances between points lose their discriminating power.

## Key Formula

To fill a $d$-dimensional unit hypercube at density equivalent to covering the unit interval with $n$ points, you need $n^d$ total observations:

$$N_{\text{required}} = n^d$$

## Example

Suppose you need 10 training samples per interval for a reliable 1-D model. In 2 dimensions you need $10^2 = 100$ samples; in 10 dimensions, $10^{10}$ — far beyond any practical dataset.

## Remember

Factor models in finance directly address this problem: instead of regressing a portfolio against hundreds of individual stock returns, PCA reduces the covariance matrix to a handful of meaningful risk factors (market, value, momentum). This compression makes estimation tractable and avoids in-sample over-fitting that would destroy out-of-sample performance.
