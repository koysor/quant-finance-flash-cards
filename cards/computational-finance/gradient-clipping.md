# Gradient Clipping

**Topic:** Computational Finance
**Tags:** gradient clipping, exploding gradient, training stability, rnn, deep learning
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Gradient clipping** prevents the exploding gradient problem by rescaling the gradient vector when its norm exceeds a threshold $\gamma$. Without clipping, a single large-gradient update can push model parameters far from any reasonable solution, crashing training — a particular risk in recurrent architectures where gradients are multiplied across many time steps.

## Key Formula

**Norm clipping** (most common): if $\|\mathbf{g}\|_2 > \gamma$, rescale before the parameter update:

$$\mathbf{g} \leftarrow \frac{\gamma}{\|\mathbf{g}\|_2}\,\mathbf{g}$$

This preserves the gradient direction whilst capping its magnitude to $\gamma$. The update rule then becomes:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta\,\text{clip}(\mathbf{g}_t, \gamma)$$

**Value clipping** (simpler, less common): clip each component independently to $[-\gamma, +\gamma]$.

The gradient norm $\|\mathbf{g}\|_2$ is monitored during training; a stable run shows smooth, bounded norms. A spike in $\|\mathbf{g}\|_2$ before clipping kicks in is a warning sign that the learning rate or architecture needs adjustment.

## Example

An LSTM trained on 10 years of daily equity returns with learning rate $\eta = 0.001$. During an early training epoch, the model encounters the 2008 financial crisis period: returns of $-9\%$ on consecutive days create a gradient norm $\|\mathbf{g}\|_2 = 48$ — roughly $24\times$ the typical norm of 2. With $\gamma = 5$, the clipped gradient has norm 5, limiting the parameter update to a safe step size. Without clipping, the $\eta \times 48 = 0.048$ update step can push weights into a region from which training never recovers.

## Remember

Gradient clipping is standard practice when training recurrent architectures (LSTM, GRU, transformer) on financial time series, where the data naturally contains extreme events — crash days, earnings surprises, liquidity crises — that produce outsized gradient signals. PyTorch exposes `torch.nn.utils.clip_grad_norm_(parameters, max_norm)`, called between `loss.backward()` and `optimiser.step()`. A typical default is $\gamma = 1.0$ for LSTMs on return series; transformers often use $\gamma = 0.5$ to 1.0. Gradient clipping is complementary to learning rate scheduling: clipping handles the magnitude of individual extreme updates, while scheduling reduces the overall step size as training progresses.
