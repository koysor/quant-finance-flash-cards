# Model Validation for RL Pricers

**Topic:** Computational Finance
**Tags:** model validation, neural network pricer, benchmarking, hedging backtest, stress testing, model risk
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Model validation for RL pricers** is the systematic process of establishing that a trained neural network pricing model is fit for purpose — accurate relative to reference models, stable across training seeds, consistent in its Greeks, and robust to market stress. It mirrors the SR 11-7 independent validation framework but adds RL-specific checks absent from classical model validation.

## Key Formula

The core validation suite produces four metrics:

**1. Pricing accuracy** vs reference model (Carr-Madan, Longstaff-Schwartz):
$$\text{MAE} = \frac{1}{N}\sum_{i=1}^N \lvert P_\theta(S_i, \tau_i) - P_\text{ref}(S_i, \tau_i)\rvert$$

**2. Hedging P&L backtest** on out-of-sample paths:
$$\text{std}(\Pi_T) = \text{std}\!\left(\sum_{t=0}^{T-1} \Delta_\theta(S_t, \tau_t)\,\Delta S_t - (P_T - P_0)\right)$$

**3. Greeks stability** across random training seeds:
$$\sigma_\text{seed}(\Delta_\theta) = \text{std}_{k=1}^K\!\left[\Delta_{\theta_k}(S, \tau)\right] \quad \text{(should be }\ll\text{bid-ask spread)}$$

**4. Stress test deviation** at tail scenarios (VIX $>$ 40, spot gap $>$ 10%):
$$\text{tail MAE} = \frac{1}{\lvert\mathcal{S}\rvert}\sum_{i \in \mathcal{S}} \lvert P_\theta(S_i, \tau_i) - P_\text{ref}(S_i, \tau_i)\rvert$$

## Example

A TDBP European call pricer undergoes validation: (1) MAE vs Black-Scholes = £0.06 across 10,000 test states — acceptable; (2) hedging P&L std = £0.38 on 1,000 out-of-sample GBM paths vs £0.41 for BS delta — passes; (3) delta std across 10 random seeds = 0.004 — stable; (4) tail MAE at VIX $> 40$ scenarios = £0.41 — fails the stress test. Root cause: the model was trained on paths with $\sigma \le 35\%$; retraining with $\sigma \in [5\%, 60\%]$ reduces tail MAE to £0.09.

## Remember

RL pricers face a validation challenge that classical models do not: there is no analytical formula to compare against as a ground truth — the reference price itself comes from Monte Carlo or numerical PDE, introducing its own approximation error. The practical resolution is to treat the validation as **relative**, not absolute: the RL pricer must be as accurate as the reference model across a representative test set, hedge as well in a live P&L backtest, and produce stable Greeks that a human risk manager can interpret. Regulatory approval under SR 11-7 additionally requires demonstrating that the model's limitations are documented, its assumptions are tested, and an independent team (not the developers) has verified its accuracy — a governance challenge that currently limits RL pricer deployment on regulated derivatives desks.
