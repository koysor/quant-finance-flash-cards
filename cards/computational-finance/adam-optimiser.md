# Adam Optimiser

**Topic:** Computational Finance
**Tags:** Adam, optimiser, adaptive learning rate, momentum, gradient descent, deep learning
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Adam** (Adaptive Moment Estimation) is a gradient-based optimisation algorithm that maintains a separate, adaptive learning rate for each parameter by tracking both the first moment (mean) and second moment (uncentred variance) of the gradient history. It combines the benefits of momentum (faster convergence) and RMSProp (robustness to varying gradient magnitudes).

## Key Formula

At step $t$, given gradient $\mathbf{g}_t = \nabla J(\boldsymbol{\theta}_{t-1})$:

$$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1-\beta_1)\mathbf{g}_t \quad\text{(1st moment)}$$
$$\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1-\beta_2)\mathbf{g}_t^2 \quad\text{(2nd moment)}$$

Bias-corrected estimates and update:
$$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1-\beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1-\beta_2^t}$$
$$\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t}+\varepsilon}\,\hat{\mathbf{m}}_t$$

Defaults: $\beta_1=0.9$, $\beta_2=0.999$, $\varepsilon=10^{-8}$.

## Example

Training a neural network to predict intraday volatility. Parameters with consistently large gradients (e.g. input-layer weights connected to highly variable volume features) receive smaller effective learning rates; parameters with small, noisy gradients receive larger steps — Adam automatically balances the update sizes across all 10,000 parameters.

## Remember

Adam is the default optimiser for neural network training in quantitative finance because financial data is heterogeneous: some features (e.g. price level) have orders-of-magnitude larger gradients than others (e.g. normalised RSI). Adam's per-parameter adaptive rates prevent dominant features from monopolising learning, making it far more robust than vanilla SGD on raw financial inputs without careful manual feature scaling.
