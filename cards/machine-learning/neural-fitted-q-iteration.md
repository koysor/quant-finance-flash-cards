# Neural Fitted Q-Iteration (NFQ)

**Topic:** Machine Learning
**Tags:** neural fitted q-iteration, nfq, batch rl, offline rl, neural network, function approximation
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Neural Fitted Q-Iteration (NFQ)** replaces the linear regressor in Fitted Q-Iteration with a neural network, enabling the algorithm to approximate complex, non-linear Q-functions over high-dimensional state spaces. Like FVI, NFQ is a **batch algorithm**: it collects all experience first, then iterates between computing Bellman targets and training the network on the full dataset — in contrast to DQN's online, incremental updates. NFQ trades the incremental flexibility of DQN for greater data efficiency and the stability of offline batch learning.

## Key Formula

**NFQ iteration** (repeat until convergence):

1. **Target computation** — for each transition $(s_i, a_i, r_i, s_i')$ in dataset $\mathcal{D}$:

$$y_i = r_i + \gamma \max_{a'} Q_{\theta_k}(s_i', a')$$

2. **Network training** — fit a new network from scratch (or fine-tune) on the full dataset:

$$\theta_{k+1} = \arg\min_\theta \frac{1}{|\mathcal{D}|}\sum_{i=1}^{|\mathcal{D}|} \left(Q_\theta(s_i, a_i) - y_i\right)^2$$

**Difference from DQN:**

| Property | NFQ | DQN |
|---|---|---|
| Data usage | Full batch per iteration | Mini-batch online |
| Target network | Not needed (full refit) | Required (separate frozen network) |
| Data efficiency | High (reuses all data) | Lower (discards old transitions) |
| Convergence | More stable offline | Faster online, less stable |
| Finance use | Historical log training | Live trading simulation |

## Example

**Multi-asset hedging with NFQ:** A 3-asset basket option hedger. State: $(S_1/K, S_2/K, S_3/K, t/T, \text{portfolio delta})$, 5 dimensions. Dataset: 50,000 historical daily hedging records from a delta-hedger.

NFQ iteration 1: targets computed using initial random $Q_{\theta_0}$; network trained for 200 epochs on all 50,000 samples. Iteration 2: targets recomputed with $Q_{\theta_1}$; network retrained from scratch. Repeat 20 iterations.

| Iteration | Hedging error (RMSE) | Training time |
|---|---|---|
| 1 | 0.082 | 45s |
| 5 | 0.031 | 225s |
| 10 | 0.019 | 450s |
| 20 | 0.014 | 900s |

After 20 iterations, NFQ achieves 0.014 RMSE — 40% below the delta-hedging baseline (0.024) — using only existing historical data, with no live trading required.

## Remember

NFQ is the method of choice when you have **a large historical dataset but cannot run new experiments**. In finance, this situation is ubiquitous: a bank has years of trade logs, but live A/B testing of RL strategies requires capital allocation, regulatory approval, and risk management oversight. NFQ extracts maximum value from the historical log by training the full network on every sample at each iteration — whereas DQN would discard most of the historical data after a single pass. The key practical difference between NFQ and DQN is stability: DQN's online updates with a replay buffer can diverge when the data distribution shifts, requiring careful tuning of the target network update frequency. NFQ avoids this entirely by refitting the network from scratch at each iteration, so the Q-function always fits the current set of Bellman targets. The cost is computational — full dataset retraining per iteration — but for offline finance applications where data is fixed and compute is cheap, NFQ's stability makes it preferable to DQN's incremental approach.
