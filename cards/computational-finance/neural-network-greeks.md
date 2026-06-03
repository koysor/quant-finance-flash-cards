# Neural Network Greeks

**Topic:** Computational Finance
**Tags:** greeks, automatic differentiation, tdbp, delta, gamma, neural network, autograd
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

Once a neural network pricer (such as TDBP) is trained, **option Greeks are computed by differentiating the network output with respect to its inputs** using automatic differentiation. Delta and gamma follow directly from one backward pass; higher-order Greeks and cross-Greeks require iterated differentiation. This produces analytic, noise-free sensitivities at the cost of a single forward-backward pass through the network.

## Key Formula

For a trained network $f_t(S;\theta)$ approximating the option price at time $t$:

$$\Delta = \frac{\partial f_t}{\partial S}, \qquad \Gamma = \frac{\partial^2 f_t}{\partial S^2}, \qquad \mathcal{V} = \frac{\partial f_t}{\partial \sigma}$$

Using reverse-mode AD (PyTorch):

```python
S = torch.tensor([95.0], requires_grad=True)
price = model(S, tau, sigma)          # forward pass

delta = torch.autograd.grad(price, S, create_graph=True)[0]
gamma = torch.autograd.grad(delta, S)[0]   # second derivative
```

All Greeks for all input dimensions are available in $O(1)$ backward passes regardless of the number of state variables.

## Example

A TDBP model for a 30-day ATM call is queried at $S = 100$, $\sigma = 0.20$, $\tau = 15$ days. Autograd returns $\Delta = 0.537$, $\Gamma = 0.048\,\text{£}^{-1}$, $\mathcal{V} = 0.182\,\text{£/vol-pt}$ in 0.3 ms — matching the Black-Scholes closed-form values to within 0.003. Finite-difference bumping the same network would require 6 additional forward passes and introduce bump-size sensitivity; autograd uses none.

## Remember

Network Greeks are only as smooth as the learned pricing function: a well-trained deep network with sufficient paths and smooth activation functions (e.g. SiLU, tanh) produces smooth delta and gamma, enabling reliable hedging. Poorly trained networks — overfit, under-regularised, or trained with ReLU activations — produce noisy gamma that oscillates between grid points, making the hedge ratio unstable. In practice, **gamma smoothness is a diagnostic for training quality**: if $\Gamma$ is noisy across $S$, the network needs more training paths or a smoother activation function before its Greeks can be trusted for live hedging.
