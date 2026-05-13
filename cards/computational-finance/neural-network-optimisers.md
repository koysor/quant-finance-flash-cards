# Neural Network Optimisers

**Topic:** Computational Finance
**Tags:** optimiser, gradient descent, adam, rmsprop, learning rate, stochastic gradient descent
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **neural network optimiser** is the algorithm that updates model weights $\boldsymbol{\theta}$ to minimise the loss function $\mathcal{L}(\boldsymbol{\theta})$ during training. All optimisers follow the general rule $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \cdot \mathbf{u}$, where $\eta$ is the learning rate and $\mathbf{u}$ is the update direction, but differ in how $\mathbf{u}$ is computed and whether $\eta$ adapts per parameter.

## Key Formula

**Stochastic Gradient Descent (SGD):** $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla_{\boldsymbol{\theta}} \mathcal{L}$

**RMSProp** — scale learning rate by a moving average of squared gradients:

$$v_t = \beta v_{t-1} + (1-\beta) g_t^2, \qquad \theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{v_t + \varepsilon}} g_t$$

**Adam (Adaptive Moment Estimation)** — bias-corrected first and second moment estimates:

$$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t \qquad (\text{first moment})$$
$$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \qquad (\text{second moment})$$
$$\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}, \qquad \theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{\hat{v}_t}+\varepsilon} \hat{m}_t$$

Default: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\varepsilon = 10^{-8}$.

## Example

Training a credit default prediction network (3 hidden layers, 256 units each) on 100,000 loan records. Comparing optimisers after 50 epochs:

| Optimiser | Learning rate | Validation AUC | Wall-clock time |
|---|---|---|---|
| SGD | $0.01$ | $0.81$ | 12 min |
| RMSProp | $0.001$ | $0.86$ | 13 min |
| Adam | $0.001$ | $0.88$ | 14 min |

Adam converges to a better solution in similar time because it adapts the learning rate independently for each weight, navigating the loss surface more efficiently than a single global rate.

## Remember

In quantitative finance, Adam is the default optimiser for nearly all neural network applications — credit scoring, volatility surface fitting, regime detection — because financial data is noisy and high-dimensional, precisely the conditions where adaptive per-parameter learning rates matter most. The learning rate $\eta$ is the most sensitive hyperparameter: too large causes divergence, too small causes excessively slow convergence or trapping in a shallow local minimum. A learning rate schedule — starting at $\eta = 10^{-3}$ and decaying by 10× when validation loss plateaus — is standard practice for time series models where the loss landscape changes across training epochs as the model encounters different market periods.
