# Vanishing Gradient Problem

**Topic:** Computational Finance
**Tags:** vanishing gradient, exploding gradient, backpropagation, deep learning, gradient clipping, rnn
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **vanishing gradient problem** occurs during backpropagation in deep networks when the gradient of the loss with respect to early-layer weights becomes exponentially small as it is multiplied through many layers. The weights in early layers receive negligible updates and the network fails to learn long-range dependencies. The symmetric failure — **exploding gradients** — occurs when the gradient grows exponentially, causing training instability.

## Key Formula

In a network with $L$ layers, the gradient flowing back to layer $l$ involves a chain of Jacobians:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(L)}} \cdot \prod_{k=l}^{L-1} \frac{\partial \mathbf{a}^{(k+1)}}{\partial \mathbf{a}^{(k)}}$$

Each factor is $\mathbf{W}^{(k)} \cdot \text{diag}(g'(\mathbf{z}^{(k)}))$. For sigmoid activations, $|g'(z)| \leq 0.25$, so:

$$\left\|\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}}\right\| \approx \left\|\frac{\partial \mathcal{L}}{\partial \mathbf{a}^{(L)}}\right\| \cdot \prod_{k=l}^{L-1} |\lambda_{\max}^{(k)}| \cdot 0.25^{L-l}$$

With $L - l = 10$ layers and sigmoid: $0.25^{10} \approx 10^{-6}$ — the gradient has effectively vanished.

**Solutions:**

| Problem | Fix |
|---|---|
| Vanishing (sigmoid/tanh) | Use ReLU / Leaky ReLU |
| Vanishing (RNN temporal) | Use LSTM / GRU gates |
| Exploding gradients | Gradient clipping: $\mathbf{g} \leftarrow \mathbf{g} \cdot \min\!\left(1, \frac{\tau}{\|\mathbf{g}\|}\right)$ |
| Both | Batch normalisation, residual connections |

## Example

A 12-layer network with sigmoid activations trained to classify credit default. Gradient norms by layer at epoch 5:

| Layer | Gradient norm |
|---|---|
| Layer 12 (output) | $0.42$ |
| Layer 8 | $0.0031$ |
| Layer 4 | $2.1 \times 10^{-5}$ |
| Layer 1 (input) | $4.7 \times 10^{-8}$ |

The first 4 layers receive essentially zero gradient — their weights do not update. Replacing sigmoid with ReLU: layer 1 gradient norm = $0.19$. All layers train effectively.

## Remember

The vanishing gradient problem explains two architectural decisions that are ubiquitous in financial deep learning: (1) **ReLU as the default hidden-layer activation** — its constant gradient of 1 for positive inputs does not decay through layers, unlike sigmoid's maximum of 0.25; (2) **LSTMs and GRUs for sequential financial data** — their gating mechanisms create additive (not multiplicative) pathways for gradient flow through time, enabling the network to learn that a credit spread spike 60 days ago is still relevant to today's default probability. Gradient clipping with $\tau = 1.0$ is a standard training safeguard for RNNs on financial data where occasional sharp market moves create large input gradients that would otherwise cause exploding updates and destabilise the model.
