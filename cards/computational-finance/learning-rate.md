# Learning Rate

**Topic:** Computational Finance
**Tags:** learning rate, hyperparameter, gradient descent, optimisation, convergence, neural networks
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **learning rate** $\eta$ is a positive hyperparameter that controls the size of each parameter update in gradient descent. It scales the gradient before subtracting it from the current parameter values, determining how aggressively the model moves towards the cost function minimum at each iteration.

## Key Formula

Parameter update at iteration $t$:

$$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta\,\nabla J(\boldsymbol{\theta}_t)$$

- $\eta$ too large $\Rightarrow$ updates overshoot the minimum; cost may diverge.
- $\eta$ too small $\Rightarrow$ convergence is slow; training stalls.

**Learning rate schedule** (step decay):

$$\eta_t = \eta_0 \cdot \gamma^{\lfloor t / k \rfloor}, \quad \gamma < 1$$

## Example

Calibrating a GARCH model via gradient descent on the log-likelihood. With $\eta = 0.1$ the parameters oscillate and never converge. With $\eta = 0.001$ convergence is stable but requires 10,000 iterations. With $\eta = 0.01$ the optimiser converges in 500 iterations — the same cost reduction in 20× fewer steps.

## Remember

The learning rate is the single most important hyperparameter to tune in any gradient-based model. In model calibration for derivatives pricing (e.g., fitting Heston parameters), an overly large step size causes the optimiser to jump across the loss surface and miss the global minimum, while too small a rate gets trapped in flat regions — analogous to setting an inappropriate step size in Newton-Raphson root-finding.
