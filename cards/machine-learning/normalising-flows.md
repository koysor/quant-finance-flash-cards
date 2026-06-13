# Normalising Flows

**Topic:** Machine Learning
**Tags:** normalising flows, generative model, invertible network, density estimation, volatility surface, implied volatility
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **normalising flow** is an invertible neural network $f_\theta$ that transforms a simple base distribution (typically $\mathcal{N}(0,I)$) into an arbitrarily complex target distribution via a sequence of differentiable, invertible transformations. Because both the forward and inverse passes are tractable, normalising flows support exact likelihood evaluation — making them ideal for learning implied volatility surfaces and generating realistic option price distributions.

## Key Formula

For an invertible mapping $\mathbf{x} = f_\theta(\mathbf{z})$ with $\mathbf{z} \sim p_Z$, the **change-of-variables formula** gives the density of $\mathbf{x}$:

$$\log p_X(\mathbf{x}) = \log p_Z(f_\theta^{-1}(\mathbf{x})) + \log\left|\det\frac{\partial f_\theta^{-1}}{\partial \mathbf{x}}\right|$$

Architectures such as **RealNVP** and **Neural Spline Flows** are constructed so the Jacobian determinant is cheap to compute (triangular or block-diagonal), making both density evaluation and sampling $O(n)$ rather than $O(n^3)$.

## Example

A normalising flow is trained on the cross-section of implied volatilities across 200 strikes and maturities on FTSE 100 options over 3 years. After training, sampling from $p_Z$ and pushing through $f_\theta$ generates synthetic vol surface snapshots that: (1) are everywhere positive, (2) satisfy approximate calendar and butterfly no-arbitrage constraints, and (3) reproduce the empirically observed correlation between ATM vol and skew. A TDBP model retrained on option paths drawn from these synthetic surfaces prices 25-delta puts 12% closer to market than one trained on Heston paths.

## Remember

Normalising flows complement Neural SDEs in the RL pricing toolkit: a Neural SDE generates **time-series paths** of the underlying; a normalising flow generates **cross-sectional snapshots** of the implied volatility surface. Together they enable a fully data-driven training regime — the IVS flow provides realistic vol surfaces to condition the SDE path generator, and the resulting option paths allow TDBP to train without any parametric model assumption. The key advantage over GANs for vol surface generation is **exact likelihood**: the flow can be evaluated at observed market surfaces to measure how well it fits, enabling proper maximum likelihood training rather than adversarial min-max optimisation.
