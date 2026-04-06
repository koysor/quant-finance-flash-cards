# Gradient Descent

**Topic:** Computational Finance
**Tags:** gradient descent, optimisation, learning rate, loss function, calibration, iterative
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Gradient descent** is an iterative optimisation algorithm that minimises a differentiable loss function $\mathcal{L}(\mathbf{w})$ by repeatedly updating the parameters $\mathbf{w}$ in the direction opposite to the gradient — the direction of steepest descent. It is the standard training algorithm for machine learning models and is also used directly for model calibration in quantitative finance.

## Key Formula

**Update rule:**

$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta\, \nabla_\mathbf{w} \mathcal{L}(\mathbf{w}_t)$$

where $\eta > 0$ is the **learning rate** (step size) and $\nabla_\mathbf{w} \mathcal{L}$ is the gradient of the loss with respect to the parameters.

**Convergence condition** (for convex $\mathcal{L}$): the algorithm converges to the global minimum; for non-convex losses it converges to a local minimum.

**Variants:**
- **Batch GD:** gradient over all $n$ samples — exact but slow.
- **Stochastic GD (SGD):** gradient over one sample — fast but noisy.
- **Mini-batch GD:** gradient over a small batch — standard in practice.

## Example

Calibrate a one-factor model to 5 market option prices. The loss is $\mathcal{L}(\sigma) = \sum_{i=1}^5 (\text{BS}(\sigma) - C_i^{\text{mkt}})^2$.

Starting from $\sigma_0 = 0.30$, with $\eta = 0.01$:

$$\sigma_1 = 0.30 - 0.01 \times \frac{\partial \mathcal{L}}{\partial \sigma}\bigg|_{0.30}$$

Each step moves $\sigma$ towards the implied volatility that minimises squared pricing error. After ~20 iterations the algorithm converges to $\sigma^* \approx 0.22$.

## Remember

Gradient descent is the engine of **model calibration** in quantitative finance. Calibrating the Heston stochastic volatility model requires fitting five parameters $(\kappa, \theta, \xi, \rho, v_0)$ to minimise the sum of squared differences between model and market option prices — a non-convex optimisation solved by gradient-based methods. The learning rate $\eta$ is the key tuning parameter: too large and the algorithm overshoots the minimum (prices oscillate); too small and convergence is impractically slow. Adaptive methods such as Adam adjust $\eta$ per parameter, making them the practical choice for high-dimensional calibration problems.
