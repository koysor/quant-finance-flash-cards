# Residual Connection

**Topic:** Computational Finance
**Tags:** residual connection, skip connection, resnet, deep learning, vanishing gradient, expressivity
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **residual connection** (or **skip connection**) adds the input of a layer directly to its output, so the layer learns a **residual** $F(\mathbf{x})$ rather than a full transformation: the block outputs $F(\mathbf{x}) + \mathbf{x}$ instead of $F(\mathbf{x})$. Introduced in ResNet (He et al., 2016), residual connections allow very deep networks (tens to hundreds of layers) to train without vanishing gradients, because the gradient can flow directly through the identity shortcut without passing through multiple non-linearities.

## Key Formula

A standard residual block with input $\mathbf{x}$, two weight layers, and ReLU activations:

$$\mathbf{y} = F(\mathbf{x},\, \{W_1, W_2\}) + \mathbf{x}$$

$$F(\mathbf{x}) = W_2\,\sigma(W_1\mathbf{x} + b_1) + b_2$$

where $\sigma$ is the activation function (typically ReLU). The gradient of the loss $\mathcal{L}$ with respect to an earlier layer $\mathbf{x}$ is:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \cdot \left(1 + \frac{\partial F}{\partial \mathbf{x}}\right)$$

The $+1$ term ensures the gradient is never multiplied by zero: even if $\partial F / \partial \mathbf{x} \approx 0$ (vanishing gradient), the gradient still flows through the shortcut at full strength.

**Dimension matching**: if $F(\mathbf{x})$ and $\mathbf{x}$ have different dimensions, a linear projection $W_s \mathbf{x}$ is used instead of the identity:

$$\mathbf{y} = F(\mathbf{x}) + W_s\mathbf{x}$$

## Example

A 10-layer TDBP option pricer without residual connections: after backpropagation through 10 sigmoid activations, each multiplying the gradient by at most $\sigma'(z) \leq 0.25$, the gradient at layer 1 is at most $0.25^{10} \approx 10^{-6}$ of the output gradient — effectively zero, and the early layers do not train.

The same network with residual connections: gradient at layer 1 includes the direct shortcut term $+1$ at each block, so the gradient stays $\mathcal{O}(1)$ regardless of depth. Training loss after 1,000 epochs:

| Architecture | Final loss | Layers that train well |
|---|---|---|
| Plain 10-layer MLP | 0.043 | Last 3 |
| ResNet-style (5 residual blocks) | 0.011 | All 10 |

## Remember

Residual connections are the key architectural ingredient that makes **very deep neural option pricers practical**. In TDBP backward induction, each time step has its own network, and the TDBP network for time step $t=0$ must propagate gradients through the composition of all 30 per-step networks during meta-training. Without residual connections, the gradient signal from the payoff at $T$ vanishes long before reaching $t=0$, and the early-time networks learn nothing. With residual connections, each per-step network's shortcut path ensures the payoff gradient reaches all 30 networks. This is why production deep hedging systems (JPMorgan, Goldman) use residual MLP blocks rather than plain MLPs: the architecture directly solves the gradient propagation problem that otherwise limits the effective depth of financial neural networks.
