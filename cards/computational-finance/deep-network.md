# Deep Network

**Topic:** Computational Finance
**Tags:** deep learning, hidden layers, hierarchical features, expressivity, depth, neural network
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **deep network** is a neural network with multiple hidden layers (typically three or more), enabling it to learn hierarchical representations. Each layer transforms its input into increasingly abstract features: early layers detect simple patterns, later layers compose these into complex task-relevant representations. Depth is distinct from width — adding layers adds representational hierarchy, not merely capacity.

## Key Formula

A deep network with $L$ hidden layers computes the composition:

$$\hat{y} = f_L \circ f_{L-1} \circ \cdots \circ f_1(\mathbf{x}), \qquad f_l(\mathbf{a}) = \sigma\!\left(\mathbf{W}^{(l)}\mathbf{a} + \mathbf{b}^{(l)}\right)$$

A key **expressivity result**: a ReLU network of depth $L$ and width $w$ can produce $O\!\left((w/d)^{d(L-1)} w\right)$ linear activation regions in $\mathbb{R}^d$, whereas a single-hidden-layer network with the same total parameters produces far fewer. Certain functions that require exponentially many neurons in a shallow network need only polynomially many neurons in a deep one.

## Example

A shallow network (1 hidden layer, 512 neurons) and a deep network (4 hidden layers, 64 neurons each, totalling 256 neurons) are both trained to price a one-year European call from inputs $(S, K, \sigma, r, T)$:

| Architecture | Parameters | Test MAE |
|---|---|---|
| Shallow (1 × 512) | ~2,600 | £0.12 |
| Deep (4 × 64) | ~1,400 | £0.04 |

The deep network achieves lower error with fewer parameters because it learns the compositional structure of the Black–Scholes formula — log-moneyness, cumulative normal, discounting — across successive layers.

## Remember

Depth is what makes neural networks practical for options pricing. The Black–Scholes price is itself a composition: a log-moneyness feeds into a $d_1/d_2$ calculation, which feeds into a cumulative normal, which feeds into a discounted expectation. A deep network mirrors this layered structure, with each hidden layer roughly corresponding to one stage of the calculation. Shallow networks must approximate the entire mapping in a single step and require exponentially more neurons to match a deep network's accuracy. In practice, quant desks use 3–6 hidden layers for surrogate pricers and neural-network volatility surfaces, with depth matched to the product's payoff complexity rather than the number of input risk factors.
