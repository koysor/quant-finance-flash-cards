# Input Convex Neural Networks

**Topic:** Machine Learning
**Tags:** input convex neural network, icnn, convexity, no-arbitrage, option pricing, butterfly spread
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

An Input Convex Neural Network (ICNN) is an architecture that guarantees the network output is convex in its inputs by requiring all inter-layer weight matrices to have non-negative entries and using convex non-decreasing activation functions.

## Key Formula

Each hidden layer uses both a pass-through from the input $\mathbf{x}$ and a recurrent connection from the previous layer $\mathbf{z}^{(l-1)}$:

$$\mathbf{z}^{(l)} = g\!\left(W_z^{(l)}\mathbf{z}^{(l-1)} + W_x^{(l)}\mathbf{x} + \mathbf{b}^{(l)}\right), \qquad W_z^{(l)} \geq 0$$

where $g$ is a convex non-decreasing activation such as softplus: $g(x) = \ln(1 + e^x)$. The non-negativity constraint on $W_z^{(l)}$ ensures the composition of affine maps and convex activations remains convex. The unconstrained weights $W_x^{(l)}$ let the network fit the data freely at each layer without breaking convexity.

## Example

An ICNN is trained to price call options as a function of strike $K$ (with spot, expiry, and volatility fixed). Without weight constraints, 0.8% of 10,000 test strikes show butterfly violations ($\partial^2 C/\partial K^2 < 0$). With non-negative $W_z$ and softplus activations, the model achieves exactly zero butterfly violations across all test points. Mean absolute pricing error increases from \$0.018 to \$0.024 — a 33% accuracy cost for a full convexity guarantee.

## Remember

Butterfly no-arbitrage requires call prices to be convex in strike: buying the $K-\epsilon$ and $K+\epsilon$ strikes and selling two $K$ strikes must never be profitable. A soft-constraint penalty drives violations towards zero but cannot eliminate them; an ICNN eliminates them by construction. This makes ICNNs the preferred architecture in production vol surface engines, where any convexity violation would immediately be traded out by market-makers.
