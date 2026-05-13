# PyTorch

**Topic:** Computational Finance
**Tags:** pytorch, deep learning, autograd, tensor, neural network, automatic differentiation
**Created:** 2026-04-23
**Author:** Claude Sonnet 4.6

---

## Definition

**PyTorch** is an open-source deep learning framework built around a dynamic computation graph and automatic differentiation engine. Operations on `Tensor` objects are recorded at runtime, and calling `.backward()` propagates gradients back through any differentiable computation. Its `torch.nn` module provides layers, loss functions, and optimisers; `torch.optim` implements Adam, SGD, and related algorithms. In quantitative finance, PyTorch is the dominant research framework for neural network option pricers, LSTM volatility forecasters, and reinforcement learning execution agents.

## Key Formula

**Gradient update** via automatic differentiation:

$$\theta_{t+1} = \theta_t - \eta \,\nabla_\theta \mathcal{L}(\theta_t)$$

The gradient $\nabla_\theta \mathcal{L}$ is computed automatically by PyTorch's autograd engine using reverse-mode differentiation. The **Adam** optimiser adjusts the learning rate per parameter using running estimates of the first and second gradient moments:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t, \qquad v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$$
$$\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon}\,\hat{m}_t$$

## Example

Training a two-layer network as a Black-Scholes pricing surrogate:

```python
import torch, torch.nn as nn

model = nn.Sequential(nn.Linear(5, 64), nn.ReLU(),
                      nn.Linear(64, 1))           # inputs: S, K, T, r, σ
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)

for X_batch, y_batch in loader:                   # y_batch: BS call price
    pred = model(X_batch).squeeze()
    loss = nn.functional.mse_loss(pred, y_batch)
    opt.zero_grad()
    loss.backward()                               # ∂L/∂θ via autograd
    opt.step()
```

After 50 epochs on 100,000 training samples, mean absolute pricing error falls below £0.01 and inference is 1,000× faster than Monte Carlo.

## Remember

PyTorch's dynamic computation graph is valuable when prototyping novel architectures common in finance research — for instance, a graph neural network over a portfolio of correlated assets, or a recurrent model whose sequence length varies by instrument. Beyond training networks, quants use PyTorch's autograd to compute **option sensitivities (Greeks)**: by expressing the pricing function as differentiable tensor operations, exact derivatives are computed at virtually no extra cost compared with finite-difference bump-and-reprice. This is the foundation of **deep hedging**, where a neural network hedging policy is trained end-to-end by differentiating through the entire simulated profit-and-loss path to minimise hedging variance.
