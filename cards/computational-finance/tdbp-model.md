# Time-Dependent Bellman Principle (TDBP)

**Topic:** Computational Finance
**Tags:** tdbp, bellman principle, option pricing, temporal difference, deep learning, backward induction
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Time-Dependent Bellman Principle (TDBP)** is a deep reinforcement learning framework for option pricing that trains one neural network per time step, propagating prices backward from maturity using the Bellman equation. It combines temporal difference learning with function approximation to learn the full option pricing surface across the entire time–space domain.

## Key Formula

The recursive pricing equation is:

$$P_t = e^{-r\Delta t}\,\mathbb{E}\!\left[P_{t+1} \mid \mathcal{F}_t\right], \qquad P_T = \text{payoff}(S_T)$$

Network $f_t(\cdot;\theta_t)$ is trained to minimise the Bellman residual:

$$\mathcal{L}(\theta_t) = \mathbb{E}\!\left[\Bigl(f_t(S_t;\theta_t) - e^{-r\Delta t}\,f_{t+1}(S_{t+1};\theta_{t+1})\Bigr)^2\right]$$

where $\theta_{t+1}$ is already trained. Training proceeds backward: $f_T \to f_{T-1} \to \cdots \to f_0$.

## Example

Pricing a 120-day European call: the model starts at day 120 with the known payoff $\max(S_{120} - K, 0)$. It trains $f_{119}$ to predict the discounted day-120 payoff, then trains $f_{118}$ using $f_{119}$ as target, continuing until $f_0$ gives the option price for any spot $S_0$. Once trained, $f_0(S_0 = 95)$ returns the price in microseconds without any Monte Carlo sampling.

## Remember

TDBP is a neural-network analogue of **backward induction** in binomial trees, but replaces the finite grid with a function approximator that covers the entire price space. Adding stochastic volatility to the state space requires only one extra input neuron — it does not multiply the grid size — avoiding the curse of dimensionality that makes high-dimensional PDE solvers impractical. The backward training structure means each network only needs to approximate a one-step conditional expectation, keeping the learning problem tractable even for exotic payoffs.
