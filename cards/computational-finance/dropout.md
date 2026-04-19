# Dropout

**Topic:** Computational Finance
**Tags:** dropout, regularisation, neural networks, overfitting, deep learning, ensemble
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Dropout** is a regularisation technique for neural networks that randomly deactivates (sets to zero) a fraction $p$ of neurons during each training step. This prevents neurons from co-adapting and forces the network to learn multiple independent representations, reducing overfitting. At inference time, all neurons are active but their outputs are scaled by $(1-p)$.

## Key Formula

For a layer with output vector $\mathbf{h}$, a random binary mask $\mathbf{m} \sim \text{Bernoulli}(1-p)^n$ is applied during training:

$$\tilde{\mathbf{h}} = \frac{\mathbf{m} \odot \mathbf{h}}{1-p}$$

The $\frac{1}{1-p}$ scaling (inverted dropout) ensures the expected output magnitude is unchanged, so no adjustment is needed at test time.

## Example

A 3-layer neural network trained to predict equity volatility has dropout rate $p=0.3$ on hidden layers. In each forward pass, 30% of neurons are randomly zeroed. After 1,000 epochs, the validation MSE is 18% lower than without dropout, and the gap between training and validation loss is much smaller — the signature of reduced overfitting.

## Remember

Dropout has an ensemble interpretation: training with dropout is approximately equivalent to training $2^n$ different sub-networks (one per possible mask) and averaging their predictions at test time. In quantitative finance this mirrors the diversification argument for ensemble models — a single overfit network memorises noise in historical prices, while the implicit ensemble induced by dropout generalises to new market regimes.
