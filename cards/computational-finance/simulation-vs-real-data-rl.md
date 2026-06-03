# Simulation vs Real Data in RL Pricing

**Topic:** Computational Finance
**Tags:** reinforcement learning, simulation, training data, model misspecification, gbm, market data
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

RL option pricing agents require a source of price paths for training. Two strategies exist: **simulated paths** generated from a parametric model (GBM, Heston, Merton-Heston) and **real historical market paths** from observed prices. Each choice involves a fundamental trade-off between model misspecification risk and data scarcity, with material consequences for pricing accuracy and hedging performance.

## Key Formula

The training distribution shapes what the agent learns. Under simulated GBM paths with constant vol $\sigma$, the agent implicitly learns prices consistent with:

$$dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$$

Under real market paths the agent estimates:

$$P_t \approx e^{-r\Delta t}\,\hat{\mathbb{E}}_{\text{empirical}}[P_{t+1} \mid S_t]$$

The gap between the two — the **model misspecification error** — is quantified by the KL divergence between the simulated path distribution $Q_{\text{sim}}$ and the empirical distribution $Q_{\text{real}}$:

$$D_{\text{KL}}(Q_{\text{real}} \| Q_{\text{sim}}) = \mathbb{E}_{Q_{\text{real}}}\!\left[\log\frac{Q_{\text{real}}}{Q_{\text{sim}}}\right]$$

## Example

A TDBP model trained on GBM paths ($\sigma = 20\%$) prices an ATM one-month call at £2.80. When the market implies $\sigma = 25\%$ and has fat tails, the real option trades at £3.40. The £0.60 gap is entirely model misspecification error. Retraining on 5 years of real S&P 500 daily paths narrows the error to £0.15, but requires careful handling of regime changes and survivorship bias in the data.

## Remember

Simulated paths offer **unlimited data, full controllability, and no look-ahead bias**, but bake in the assumptions of the generative model — if GBM is wrong, the agent learns a systematically biased pricer. Real market paths capture **genuine non-normality, fat tails, and jumps** but are scarce (markets produce only one path per day), requiring augmentation techniques or transfer learning from simulated pre-training. The practical choice on a trading desk is often a hybrid: pre-train on millions of simulated Merton-Heston paths, then fine-tune on real market data from the target asset.
