# Weight Initialisation

**Topic:** Computational Finance
**Tags:** weight initialisation, xavier, he initialisation, vanishing gradient, deep learning, training stability
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Weight initialisation** is the procedure for setting neural network weights before training begins. Poor initialisation causes vanishing or exploding gradients in the very first backward pass, before any learning occurs. The goal is to preserve the variance of activations and gradients across layers so that the gradient signal neither shrinks to zero nor grows unboundedly as it propagates through a deep network.

## Key Formula

**Xavier (Glorot) initialisation** — designed for sigmoid/tanh activations:

$$W_{ij} \sim \mathcal{U}\!\left(-\sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}},\; +\sqrt{\frac{6}{n_{\text{in}} + n_{\text{out}}}}\right)$$

or equivalently $W_{ij} \sim \mathcal{N}\!\left(0,\; \frac{2}{n_{\text{in}} + n_{\text{out}}}\right)$

**He initialisation** — designed for ReLU activations (accounts for ReLU zeroing half the inputs):

$$W_{ij} \sim \mathcal{N}\!\left(0,\; \frac{2}{n_{\text{in}}}\right)$$

where $n_{\text{in}}$ is the number of inputs to the layer and $n_{\text{out}}$ is the number of outputs.

**Intuition**: variance of activations $\approx 1$ at every layer requires $\text{Var}(W) \cdot n_{\text{in}} = 1$, giving $\text{Var}(W) = 1/n_{\text{in}}$. ReLU kills negative activations (halving effective variance), so He initialisation doubles this: $\text{Var}(W) = 2/n_{\text{in}}$.

## Example

A 10-layer credit default network (512 units, ReLU activations). Using naive initialisation $W_{ij} \sim \mathcal{N}(0, 1)$:
- Layer 1 activation std: $22.6$
- Layer 10 activation std: $3.1 \times 10^8$ — gradient explodes; training diverges in 3 epochs.

Switching to He initialisation $W_{ij} \sim \mathcal{N}(0, 2/512)$:
- Layer 1 activation std: $1.02$
- Layer 10 activation std: $0.97$ — stable across all layers; model converges in 40 epochs to validation AUC 0.89.

## Remember

Weight initialisation is the one hyperparameter that must be set correctly before any training begins — unlike learning rate or dropout, a bad initialisation cannot be recovered from because the gradient signal is corrupted from the very first backward pass. The rule is simple in practice: use **He initialisation for ReLU/Leaky ReLU hidden layers** and **Xavier for sigmoid/tanh layers** — both are available as defaults in PyTorch (`torch.nn.init`) and TensorFlow. In quantitative finance, initialisation matters most for very deep networks (6+ layers) used in credit scoring or order flow prediction; for shallow networks (1–3 layers) applied to low-dimensional factor data, initialisation choice has minimal impact because gradients do not travel far enough to vanish significantly.
