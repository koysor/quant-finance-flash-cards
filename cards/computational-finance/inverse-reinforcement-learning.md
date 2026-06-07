# Inverse Reinforcement Learning

**Topic:** Computational Finance
**Tags:** inverse reinforcement learning, reward learning, imitation learning, behavioural finance, order flow, market microstructure
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Inverse Reinforcement Learning (IRL)** learns a reward function $R(s, a)$ from observed expert behaviour, rather than optimising a given reward. Given a set of expert trajectories $\{\tau_i\}$ (sequences of state-action pairs), IRL finds the reward function under which the expert's policy is optimal. In finance, IRL is used to infer trader objectives from order flow data — answering "what reward function explains why this market participant trades the way they do?" — and to build imitation learning agents that replicate expert execution strategies.

## Key Formula

**Maximum entropy IRL** (Ziebart et al., 2008) — the most common formulation. The expert policy is modelled as a Boltzmann distribution over trajectories:

$$P(\tau \mid R) \propto \exp\!\left(\sum_{t=0}^T R(s_t, a_t)\right)$$

The IRL objective maximises the log-likelihood of observed trajectories:

$$\max_R \sum_i \log P(\tau_i \mid R) = \max_R \sum_i \sum_t R(s_t, a_t) - \log Z(R)$$

where $Z(R) = \sum_\tau \exp(\sum_t R(s_t, a_t))$ is the partition function (computed via dynamic programming).

**Feature-matching IRL** (Abbeel & Ng): find $R = \theta^\top \phi(s,a)$ such that:

$$\mathbb{E}_{\pi_R}\!\left[\phi(s,a)\right] = \mathbb{E}_{\pi_{\text{expert}}}\!\left[\phi(s,a)\right]$$

The optimal reward weights $\theta$ match the feature expectations of the learnt policy to those of the expert.

## Example

**Inferring execution objectives from VWAP traders:** Observe 500 institutional VWAP execution trajectories: each trajectory is a sequence of order sizes placed over a trading day. Features $\phi$: (market impact per share, time remaining, inventory ratio, spread).

IRL recovers reward weights: $\theta = (−0.62,\; −0.18,\; −0.55,\; −0.25)$ — the trader penalises market impact most heavily (−0.62), then inventory imbalance (−0.55). The inferred reward implies the trader is optimising a weighted combination of execution shortfall and schedule risk — consistent with a standard VWAP mandate, but with risk aversion parameter $\lambda \approx 0.3$ estimated from the data, not assumed.

The IRL agent, trained on these trajectories, achieves 94% of the execution quality of the expert benchmark on out-of-sample data — without being told the VWAP objective explicitly.

## Remember

IRL bridges the gap between **observed market behaviour** and the **objectives that generate it**. In standard RL for optimal execution, the reward function is hand-crafted (e.g. implementation shortfall minus $\lambda \times \sigma^2$). But real institutional traders optimise objectives that are proprietary and unknown. IRL extracts those objectives from trade data, enabling three finance applications: (1) **Replicating execution algorithms** — learn the implicit reward of a smart order router and imitate it; (2) **Detecting regime change** — if the inferred reward function for a counterparty's trading shifts, their mandate or constraints may have changed; (3) **Regulatory surveillance** — the SEC uses variants of IRL to identify manipulative strategies, asking which reward function would make the observed trading pattern rational. The maximum entropy formulation is preferred because it is robust to suboptimal demonstrations — real traders are not perfectly optimal, and the Boltzmann distribution naturally assigns lower probability to worse trajectories rather than assuming the expert is infallible.
