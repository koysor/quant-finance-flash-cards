# Online Learning for RL Pricers

**Topic:** Computational Finance
**Tags:** online learning, model updating, continual learning, staleness, fine-tuning, deployment
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Online learning** for RL pricers incrementally updates a deployed model as new market data arrives, without full retraining from scratch. The central challenge is **staleness**: a model trained on historical paths gradually mispricices as market conditions evolve, yet naive fine-tuning on recent data causes **catastrophic forgetting** of previously learned dynamics.

## Key Formula

Three update strategies, each trading off adaptation speed against stability:

**Scheduled full retrain**: replace $\theta_\text{old}$ with $\theta_\text{new}$ trained from scratch on a rolling window every period $T_\text{retrain}$. No forgetting, but expensive and discontinuous.

**Fine-tuning with learning rate decay**: update $\theta$ on recent paths $\mathcal{D}_\text{new}$ with a small learning rate $\eta_\text{ft} \ll \eta_\text{train}$:
$$\theta \leftarrow \theta - \eta_\text{ft}\,\nabla_\theta \mathcal{L}(\theta;\,\mathcal{D}_\text{new})$$

**Elastic Weight Consolidation (EWC)**: regularise fine-tuning to protect weights important for past tasks, weighted by Fisher information $F_i$:
$$\mathcal{L}_\text{EWC}(\theta) = \mathcal{L}(\theta;\,\mathcal{D}_\text{new}) + \frac{\lambda}{2}\sum_i F_i(\theta_i - \theta_i^*)^2$$

## Example

A TDBP pricer for 30-day ATM options is trained in January (on GBM paths, $\sigma = 18\%$). By March, realised vol has risen to 28% and the model overprices puts by £0.35. Three responses: (1) full retrain takes 4 hours; (2) fine-tuning with $\eta_\text{ft} = 0.001$ on 10,000 fresh paths converges in 20 minutes, reducing the error to £0.06, but degrades pricing accuracy on low-vol scenarios; (3) EWC fine-tuning achieves £0.09 error on high-vol paths while preserving £0.04 error on low-vol paths — retaining both regimes.

## Remember

The staleness-forgetting tension is the core challenge of deployed RL pricers: the model must adapt to new vol regimes quickly enough to remain accurate but slowly enough to retain knowledge of historical dynamics that may recur. In practice, **monitoring triggers** are more effective than scheduled updates — track the rolling out-of-sample Bellman error on live paths, and trigger a fine-tuning or full retrain only when it exceeds a threshold. This avoids unnecessary retraining during stable periods while ensuring rapid response to genuine regime changes.
