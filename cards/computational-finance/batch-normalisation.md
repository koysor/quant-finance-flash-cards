# Batch Normalisation

**Topic:** Computational Finance
**Tags:** batch normalisation, deep learning, training stability, internal covariate shift, neural networks, regularisation
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Batch normalisation** standardises the inputs to each layer within a mini-batch during training, then applies learned scale $\gamma$ and shift $\beta$ parameters. It reduces internal covariate shift — the change in each layer's input distribution as earlier layers update — allowing deeper networks to train faster and more stably.

## Key Formula

For a mini-batch $\mathcal{B} = \{x_1,\ldots,x_b\}$ feeding into a layer:

$$\hat{x}_i = \frac{x_i - \mu_\mathcal{B}}{\sqrt{\sigma^2_\mathcal{B} + \varepsilon}}, \qquad y_i = \gamma\,\hat{x}_i + \beta$$

where $\mu_\mathcal{B}$ and $\sigma^2_\mathcal{B}$ are the batch mean and variance, $\varepsilon$ is a small constant for numerical stability, and $\gamma, \beta$ are learnable parameters restored by the network if normalisation hurts expressiveness.

## Example

A 10-layer neural network predicting intraday volatility trains without batch normalisation: gradients vanish in early layers and training stalls after 200 epochs. Adding batch normalisation after each hidden layer: gradients flow to all layers, training converges in 80 epochs, and validation MSE improves by 15%.

## Remember

Batch normalisation is the practical solution to a fundamental problem in deep financial networks: input features (price level, volume, spreads) span orders of magnitude and their distributions shift as the market regime changes. Just as z-score normalisation of raw features is mandatory before distance-based ML algorithms, batch normalisation applies the same logic inside the network at every layer — ensuring stable gradient flow regardless of the scale of upstream activations.
