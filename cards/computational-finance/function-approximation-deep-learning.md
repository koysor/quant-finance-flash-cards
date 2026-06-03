# Function Approximation with Deep Learning

**Topic:** Computational Finance
**Tags:** function approximation, neural network, mlp, deep learning, reinforcement learning, curse of dimensionality
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Function approximation** in RL replaces discrete lookup tables with a parameterised function — typically a deep neural network — to estimate value functions or option prices over a continuous, infinite-dimensional state space. This is essential in finance, where state variables such as stock price, time-to-maturity, and volatility are real-valued and continuous.

## Key Formula

A **multi-layer perceptron (MLP)** with parameters $\theta$ approximates the pricing function $f$:

$$\hat{P}(s;\theta) \approx f(s), \qquad s = (S_t,\; \tau,\; V_t,\; \ldots)$$

Parameters are updated by gradient descent to minimise the Bellman residual:

$$\mathcal{L}(\theta) = \mathbb{E}\!\left[\Bigl(\hat{P}(s_t;\theta) - e^{-r\Delta t}\hat{P}(s_{t+1};\theta^{-})\Bigr)^2\right]$$

where $\theta^{-}$ denotes a periodically frozen **target network** that stabilises training.

## Example

Instead of pricing a call at every integer stock price from £50 to £150, an MLP is trained on 10,000 random $(S_t, \tau)$ pairs drawn from the state distribution. After training, it predicts the price at $S = 87.43$ with under £0.03 error — the network generalises the pricing curve to points it never saw during training.

## Remember

Function approximation is what allows RL to overcome the **curse of dimensionality**: each extra state variable (e.g. stochastic volatility $V_t$) adds one input neuron rather than multiplying the grid size exponentially. The TDBP model uses one MLP per time step, each learning a slice of the pricing surface for that date — a design that keeps the network architecture simple while covering the full time–space domain.
