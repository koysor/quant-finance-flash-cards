# Markov State Design for Financial RL

**Topic:** Computational Finance
**Tags:** markov property, state space, rl state design, non-markovian, augmented state, path dependence
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

For an RL agent to learn a correct policy, its state $s_t$ must satisfy the **Markov property**: all information needed to predict future rewards must be contained in $s_t$ alone. In financial RL, the raw spot price $S_t$ is rarely sufficient — volatility clustering, momentum, path-dependent payoffs, and regulatory constraints each introduce history-dependence that breaks the Markov assumption and forces state augmentation.

## Key Formula

A state $s_t$ is **Markov sufficient** if:

$$P(s_{t+1}, r_{t+1} \mid s_t, a_t) = P(s_{t+1}, r_{t+1} \mid s_0, a_0, \ldots, s_t, a_t)$$

i.e. the transition and reward distributions conditioned on the full history collapse to conditioning on $s_t$ alone. Common state augmentations to restore the Markov property in finance:

| Non-Markovian feature | State augmentation |
|---|---|
| Stochastic volatility | Add $V_t$ or $\hat{\sigma}_t$ (realised vol) |
| Daily price limits (DPL) | Add $S_{t_0}$ (day-open price) for corridor boundaries |
| Path-dependent payoff (Asian) | Add running average $\bar{S}_t = \frac{1}{t}\sum_{k=0}^t S_k$ |
| Momentum / trend | Add lagged returns $(r_{t-1}, r_{t-2}, \ldots)$ |
| Current hedge position | Add $\delta_{t-1}$ to avoid transaction-cost blindness |

## Example

An RL agent prices barrier options with state $s_t = S_t$ only. It learns a good policy for paths that never approached the barrier but systematically misprices near-barrier paths — it cannot distinguish a stock at £99 that has been at £99 all day from one that touched £102 (the barrier) an hour ago. Augmenting the state with a binary barrier-hit indicator $\mathbf{1}_{[\max_{u \le t} S_u \ge B]}$ makes the state Markov and resolves the mispricing.

## Remember

State design is the most impactful modelling decision in financial RL — a poorly chosen state forces the agent to learn a suboptimal policy no matter how many training paths are used. The practical test is to ask: "given $s_t$, can an omniscient agent determine the optimal action?" If the answer involves "it depends on what happened earlier", the state is not Markov and must be augmented. For TDBP-style pricing, the state is implicitly $(S_t, t)$ — sufficient for vanilla European options but not for path-dependent exotics, which require augmented state vectors that grow the neural network's input dimension by one feature per additional Markov-restoring variable.
