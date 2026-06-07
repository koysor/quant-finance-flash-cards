# Behaviour Cloning

**Topic:** Computational Finance
**Tags:** behaviour cloning, imitation learning, supervised learning, offline rl, execution, initialisation
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Behaviour cloning (BC)** learns a policy by treating expert demonstrations as a supervised learning problem: the state is the input and the expert's action is the target label. Unlike inverse reinforcement learning, BC does not recover a reward function — it simply regresses the policy directly onto the observed state–action pairs. BC is the simplest form of imitation learning, requires no reward signal, and is widely used to initialise RL agents from historical trade data before fine-tuning with reward optimisation.

## Key Formula

Given a dataset of expert trajectories $\mathcal{D} = \{(s_i, a_i^*)\}$, behaviour cloning minimises the supervised loss:

**Discrete actions** (classification — e.g. hold vs exercise vs hedge):

$$\mathcal{L}_{\text{BC}}(\theta) = -\frac{1}{|\mathcal{D}|}\sum_{i=1}^{|\mathcal{D}|} \log \pi_\theta(a_i^* \mid s_i)$$

**Continuous actions** (regression — e.g. hedge ratio, order size):

$$\mathcal{L}_{\text{BC}}(\theta) = \frac{1}{|\mathcal{D}|}\sum_{i=1}^{|\mathcal{D}|} \|a_i^* - \pi_\theta(s_i)\|^2$$

**Compounding error (covariate shift):** BC's key failure mode — errors compound over time. If the cloned policy makes a small error at $t=1$, it visits states not in the training data at $t=2$, where its actions are unconstrained and errors grow:

$$\text{Total error after } T \text{ steps} \sim O(\epsilon T^2)$$

where $\epsilon$ is the per-step cloning error. This is why BC alone is insufficient for long-horizon problems.

**DAgger fix:** iteratively add the cloned policy's visited states to the training set and query the expert for labels, reducing compounding error to $O(\epsilon T)$.

## Example

**Initialising a delta-hedging RL agent from historical logs.** Dataset: 100,000 daily $(S_t/K, \sigma_{\text{impl}}, \tau, \Delta_{\text{current}})$ → hedge ratio observations from a Black–Scholes delta hedger.

BC trains a 2-layer MLP on this data in 10 minutes. The cloned policy achieves 96% of Black–Scholes delta accuracy out-of-the-box.

When this BC-initialised network is used as the starting point for PPO fine-tuning with a transaction-cost reward:

| Initialisation | PPO episodes to converge | Final hedging RMSE |
|---|---|---|
| Random weights | 500,000 | 0.018 |
| BC-initialised | 50,000 | 0.013 |

BC initialisation gives a 10× speed-up in convergence and a better final policy — the agent starts near the Black–Scholes solution and then learns the transaction-cost adjustments rather than learning hedging from scratch.

## Remember

Behaviour cloning is the **warm start** for financial RL. Training a hedging or execution agent from random policy initialisation in a live (or paper trading) environment is prohibitively expensive: the agent must explore millions of suboptimal actions before finding good strategies. BC bypasses this exploration phase by giving the agent a sensible starting point — the historical expert policy — after which a relatively small number of RL fine-tuning steps learns the improvements. The standard production pipeline at quantitative desks is: (1) BC on 3–5 years of historical logs to build the base policy; (2) offline RL (CQL or NFQ) to fine-tune on the same logs with a reward signal; (3) paper trading for online RL validation before live deployment. BC alone fails for long-horizon problems due to compounding errors, but as an initialisation step it dramatically reduces the data and compute needed for step (2).
