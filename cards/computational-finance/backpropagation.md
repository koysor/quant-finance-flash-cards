# Backpropagation

**Topic:** Computational Finance
**Tags:** backpropagation, chain rule, gradient, neural network, training, automatic differentiation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Backpropagation** is the algorithm for computing the gradient of the loss function with respect to every weight in a neural network. It applies the **chain rule** of calculus backwards through the network — from the output layer to the input layer — accumulating partial derivatives at each layer. The gradients are then used by gradient descent to update the weights.

## Key Formula

**Error at output layer:**

$$\boldsymbol{\delta}^{(L)} = \nabla_{\mathbf{a}^{(L)}} \mathcal{L} \odot \sigma'\!\left(\mathbf{z}^{(L)}\right)$$

**Error backpropagated to layer $l$:**

$$\boldsymbol{\delta}^{(l)} = \left(\mathbf{W}^{(l+1)}\right)^\top \boldsymbol{\delta}^{(l+1)} \odot \sigma'\!\left(\mathbf{z}^{(l)}\right)$$

**Weight and bias gradients:**

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \boldsymbol{\delta}^{(l)}\left(\mathbf{a}^{(l-1)}\right)^\top, \qquad \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(l)}} = \boldsymbol{\delta}^{(l)}$$

where $\odot$ denotes element-wise multiplication and $\sigma'$ is the derivative of the activation function.

## Example

For a two-layer network predicting default, suppose the loss at one training example is $\mathcal{L} = 0.3$.

1. Compute $\delta^{(2)}$ at the output: $\delta = (\hat{p} - y) = 0.43 - 0 = 0.43$.
2. Backpropagate to layer 1: $\delta^{(1)} = (W^{(2)})^\top \times 0.43 \odot \sigma'(z^{(1)})$.
3. Compute $\nabla W^{(1)} = \delta^{(1)} (x)^\top$.
4. Update: $W^{(1)} \leftarrow W^{(1)} - \eta\, \nabla W^{(1)}$.

Each pass through the training set adjusts all weights by their contribution to the error.

## Remember

Backpropagation is the chain rule applied systematically through a neural network — it is not a new mathematical idea, just an efficient bookkeeping scheme. The key insight is that gradients can be **reused**: computing $\delta^{(l)}$ requires $\delta^{(l+1)}$, so a single backward pass computes all gradients simultaneously. In quantitative finance, the same algorithmic differentiation idea is used in **AAD (Adjoint Algorithmic Differentiation)** to compute the sensitivities (Greeks) of complex portfolios — AAD computes all $n$ sensitivities at once for the cost of roughly 3–5 forward evaluations, regardless of $n$. The mathematical structure of AAD is identical to backpropagation.
