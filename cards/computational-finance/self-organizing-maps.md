# Self-Organizing Maps

**Topic:** Computational Finance
**Tags:** SOM, unsupervised learning, dimensionality reduction, clustering, visualisation, regime detection
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

A **Self-Organizing Map (SOM)** is an unsupervised neural network that projects high-dimensional data onto a low-dimensional (typically 2-D) grid of nodes while preserving topological structure: observations that are similar in the original space are mapped to nodes that are close on the grid.

## Key Formula

For input $\mathbf{x}$, the **Best Matching Unit (BMU)** is the node $\mathbf{w}^*$ with the closest weight vector:

$$\mathbf{w}^* = \arg\min_k \|\mathbf{x} - \mathbf{w}_k\|$$

Weight update for node $k$ at iteration $t$:

$$\mathbf{w}_k(t+1) = \mathbf{w}_k(t) + \alpha(t)\, h(k, \text{BMU}, t)\,[\mathbf{x} - \mathbf{w}_k(t)]$$

where $\alpha(t)$ is a decaying learning rate and $h$ is a neighbourhood function.

## Example

Map 20 years of daily macroeconomic indicators (yields, spreads, volatility, FX) onto a $10 \times 10$ SOM grid. Each cell represents a distinct macro regime; plotting the time series path across cells reveals how markets transitioned from expansion to crisis and recovery.

## Remember

Unlike PCA (which forces linear projections), a SOM learns a non-linear topology-preserving map. This makes it well suited for visualising the regime landscape of financial markets — traders and risk managers use SOM outputs to identify which historical period most resembles today's market conditions.
