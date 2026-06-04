# Neural Networks as Dynamical Systems

**Topic:** Computational Finance
**Tags:** neural ode, dynamical systems, continuous depth, residual network, time series
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

Viewing a **neural network as a dynamical system** treats the forward pass through the layers as a discrete-time (or continuous-time) evolution of a hidden state. A residual network (ResNet) block $\mathbf{h}_{t+1} = \mathbf{h}_t + f(\mathbf{h}_t, \theta_t)$ is precisely an Euler discretisation of the ODE $d\mathbf{h}/dt = f(\mathbf{h}, t, \theta)$. Taking the layer-count to infinity recovers the **Neural ODE** (Chen et al., 2018): a network parameterised by a differential equation rather than a sequence of discrete transformations.

## Key Formula

A Neural ODE defines the hidden state evolution via:

$$\frac{d\mathbf{h}(t)}{dt} = f_\theta(\mathbf{h}(t), t), \qquad \mathbf{h}(0) = \mathbf{x}$$

The output is $\mathbf{h}(T)$, computed by a black-box ODE solver (e.g. Runge-Kutta). Gradients are computed via the **adjoint method** rather than backpropagation through solver steps:

$$\frac{dL}{d\theta} = -\int_T^0 \mathbf{a}(t)^\top \frac{\partial f_\theta}{\partial \theta}\,dt, \qquad \frac{d\mathbf{a}}{dt} = -\mathbf{a}(t)^\top \frac{\partial f_\theta}{\partial \mathbf{h}}$$

where $\mathbf{a}(t) = dL/d\mathbf{h}(t)$ is the adjoint state — memory cost is $O(1)$ in depth.

## Example

A Neural ODE models the evolution of a portfolio's latent state (factor exposures, regime) as a continuous-time ODE driven by market data. Given observations at irregular times $t_1 < t_2 < \cdots < t_n$ (e.g. trades, news events), the ODE solver integrates forward from each observation to the next — unlike RNNs, no fixed time-step grid is required. This naturally handles the irregularly-spaced tick data that is standard in financial markets.

## Remember

The dynamical systems view is not just a theoretical curiosity — it resolves a practical problem in financial time-series modelling: traditional RNNs and LSTMs require uniformly-spaced inputs, but financial data arrives irregularly (order flow, corporate announcements, macro releases). Neural ODEs solve this by treating the hidden state as a continuous trajectory, evaluated at whatever times observations arrive. The Neural SDE extension adds stochastic forcing, making it directly applicable to latent stochastic volatility modelling — a Neural ODE in the drift plus a learnable diffusion coefficient.
