# Catastrophic Forgetting

**Topic:** Computational Finance
**Tags:** catastrophic forgetting, continual learning, elastic weight consolidation, fine-tuning, neural network, regime change
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Catastrophic forgetting** (McCloskey & Cohen, 1989) occurs when a neural network trained sequentially on multiple tasks loses performance on earlier tasks as it adapts to later ones. In financial RL, it manifests when fine-tuning a trained option pricer on recent market data erases the pricing knowledge acquired from earlier regimes — the model becomes accurate for current conditions but fails on scenarios it previously handled correctly.

## Key Formula

The mechanism is gradient interference: the gradient update for new data $\mathcal{D}_\text{new}$ points in a direction that increases loss on old data $\mathcal{D}_\text{old}$:

$$\nabla_\theta \mathcal{L}(\theta;\,\mathcal{D}_\text{new}) \cdot \nabla_\theta \mathcal{L}(\theta;\,\mathcal{D}_\text{old}) < 0$$

**Elastic Weight Consolidation (EWC)** prevents forgetting by penalising changes to parameters important for old tasks, using the Fisher information matrix $F$ as an importance estimate:

$$\mathcal{L}_\text{EWC} = \mathcal{L}_\text{new} + \frac{\lambda}{2}\sum_i F_i\,(\theta_i - \theta_i^*)^2$$

where $\theta_i^*$ are the weights after old-task training. Parameters with high Fisher information (large $F_i$) are heavily penalised for drifting.

## Example

A TDBP model trained on 2018–2021 data prices ATM puts correctly across low, medium, and high vol environments. Fine-tuned on 100,000 paths from the 2022 rate-rise environment (high vol, negative skew), the model now prices high-vol puts well but its 2019 low-vol pricing error increases from £0.04 to £0.31 — it has forgotten the low-vol regime entirely. EWC fine-tuning with $\lambda = 500$: high-vol error = £0.08, low-vol error = £0.07. The Fisher penalty identified the early network layers as high-importance for low-vol pricing and protected them during the fine-tuning update.

## Remember

Catastrophic forgetting is why **naive fine-tuning is dangerous for deployed RL pricers**: a crisis-driven fine-tune can destroy years of learned vol surface knowledge in a matter of hours. The practical mitigations form a hierarchy: (1) use a **replay buffer** mixing old and new paths during fine-tuning; (2) apply **EWC** to anchor important weights; (3) maintain a **model ensemble** where the old model and the fine-tuned model are weighted by their recent out-of-sample performance. In the context of SR 11-7 model governance, any fine-tuning that changes pricing by more than a materiality threshold triggers a re-validation — making controlled forgetting prevention not just a performance requirement but a regulatory one.
