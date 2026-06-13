# Multi-Armed Bandit

**Topic:** Machine Learning
**Tags:** multi-armed bandit, explore-exploit, reinforcement learning, ucb, regret
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **multi-armed bandit** problem is a sequential decision problem in which an agent repeatedly chooses among $K$ actions ("arms"), each yielding a stochastic reward from an unknown distribution. The agent must balance **exploration** (trying arms to learn their reward distributions) against **exploitation** (choosing the arm currently believed to be best). It is a special case of reinforcement learning with a single state — there is no state transition, only an action and an immediate reward.

## Key Formula

The **Upper Confidence Bound (UCB1)** algorithm selects the arm that maximises:

$$a_t = \arg\max_{k}\left\{\hat{\mu}_k + \sqrt{\frac{2 \ln t}{n_k}}\right\}$$

where $\hat{\mu}_k$ is the sample mean reward of arm $k$, $n_k$ is the number of times arm $k$ has been pulled, and $t$ is the total number of rounds so far. The second term is a confidence bonus that shrinks as an arm is pulled more.

Performance is measured by **cumulative regret**:

$$R_T = T\mu^* - \sum_{t=1}^{T} \mathbb{E}[r_{a_t}]$$

where $\mu^* = \max_k \mu_k$ is the mean reward of the best arm. UCB1 achieves $R_T = O(\sqrt{KT \ln T})$.

## Example

A quant team tests three execution algorithms (TWAP, VWAP, Implementation Shortfall) on live orders. Each day they must choose which algorithm to deploy. After 30 days:

| Algorithm | Times used ($n_k$) | Mean IS (bps, $\hat{\mu}_k$) | UCB bonus ($t=30$) | UCB score |
|-----------|-------------------|------------------------------|---------------------|-----------|
| TWAP | 12 | 4.2 | 1.12 | 5.32 |
| VWAP | 10 | 4.8 | 1.23 | 6.03 |
| IS | 8 | 3.9 | 1.38 | 5.28 |

UCB1 selects VWAP (highest UCB score) but continues to explore IS and TWAP to narrow uncertainty.

## Remember

The multi-armed bandit framework is directly applicable to **A/B testing of trading strategies**: rather than committing to a fixed exploration period before exploiting the best strategy, bandit algorithms continuously adapt, allocating more capital to strategies that perform well while maintaining enough exploration to detect regime changes. In practice, **Thompson Sampling** (a Bayesian bandit algorithm) is popular in quantitative finance because it naturally handles uncertainty and degrades gracefully when reward distributions shift — a common occurrence in live markets. Bandit methods are also used in hyperparameter tuning of ML models deployed in production trading systems.
