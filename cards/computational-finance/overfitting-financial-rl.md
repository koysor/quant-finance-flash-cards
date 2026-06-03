# Overfitting in Financial RL

**Topic:** Computational Finance
**Tags:** overfitting, reinforcement learning, path memorisation, reward hacking, generalisation, out-of-sample
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Overfitting in financial RL** occurs when an agent learns the idiosyncratic features of its training path distribution rather than the underlying pricing or hedging relationship. Unlike classical ML overfitting (memorising training labels), RL overfitting in finance manifests as regime-specific policies, reward-hacked solutions, or path-memorised pricing that degrades sharply on out-of-sample market conditions.

## Key Formula

Three distinct failure modes, each with a different signature:

**Path memorisation**: training loss $\mathcal{L}_\text{train} \to 0$ while out-of-sample Bellman error $\mathcal{L}_\text{OOS} \gg 0$. The network fits the training path dynamics but cannot generalise.

**Reward hacking**: agent finds an unexpected policy $\pi^*$ satisfying $\sum_t r_t > \sum_t r_t^{\text{intended}}$ by exploiting a gap between the reward specification and the intended objective — e.g. reducing apparent hedging error by taking positions that reduce measured variance but increase tail risk.

**Regime overfitting**: policy performs well on in-sample regimes but degrades after a structural break. Detectable via the **Probability of Backtest Overfitting (PBO)**:

$$\text{PBO} = P\!\left(\text{rank}(\hat{S}_\text{OOS}) < \text{median}\right)$$

## Example

A TDBP agent is trained on 5 years of S&P 500 data (2015–2020, including a brief 2018 correction and the COVID crash). The agent achieves mean absolute pricing error of £0.04 in-sample. Tested on 2021–2023 (post-COVID recovery, rate-rise regime): error rises to £0.31. The agent had implicitly learnt "after a crash, vol reverts fast" — a pattern specific to 2020's QE-driven recovery — and systematically underprices options in the 2022 vol-expansion environment.

## Remember

The deepest form of overfitting in financial RL is **distributional**: the agent learns the shape of the training distribution rather than the underlying financial relationship, and this is invisible in training metrics. The diagnostic is always out-of-sample: hold out an entire regime (a full year, or a stress event) during training and evaluate both pricing accuracy and hedging P&L on it. Mitigations include **curriculum learning** (exposure to multiple simulated regimes), **experience replay** with adaptive staleness management, and **dropout** in the pricing network as a regulariser — but the most robust protection is ensuring the training distribution is broad enough that no single regime dominates it.
