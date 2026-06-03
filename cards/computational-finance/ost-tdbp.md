# Optimal Stopping Time TDBP (OST-TDBP)

**Topic:** Computational Finance
**Tags:** american options, optimal stopping, tdbp, early exercise, continuation value, reinforcement learning
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**OST-TDBP (Optimal Stopping Time TDBP)** extends the standard TDBP framework to price **American options** and other early-exercise derivatives. At each time step the agent compares the immediate exercise payoff with a neural-network estimate of the continuation value and chooses the larger — correctly identifying whether to exercise or hold.

## Key Formula

The American option price satisfies the **Bellman optimality equation with early exercise**:

$$P_t = \max\!\left(g(S_t),\; e^{-r\Delta t}\,\mathbb{E}\!\left[P_{t+1} \mid \mathcal{F}_t\right]\right)$$

where $g(S_t)$ is the immediate payoff (e.g. $\max(K - S_t, 0)$ for an American put) and the expectation is the continuation value approximated by the neural network. Terminal condition: $P_T = g(S_T)$.

Training works backward: the network at time $t$ is trained to predict $\max(g(S_t),\, e^{-r\Delta t} \hat{P}_{t+1}(S_{t+1}))$, using the already-trained network at $t+1$ as the target.

## Example

American put with $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year. At $S_{0.5} = 60$ (deep in the money), the immediate payoff is £40 while the continuation value is £37. OST-TDBP correctly prices $P_{0.5} = 40$. At $S_{0.5} = 98$ the continuation value exceeds £2, so the model correctly defers exercise.

## Remember

OST-TDBP learns the **free exercise boundary** — the critical stock price below which early exercise is optimal — without ever solving the free-boundary PDE explicitly. It is model-free: the same algorithm prices American options on assets with DPLs, stochastic volatility, or jumps by simply training on different path distributions, whereas Longstaff-Schwartz regression requires careful basis-function selection for each new model and can be inaccurate far from the money.
