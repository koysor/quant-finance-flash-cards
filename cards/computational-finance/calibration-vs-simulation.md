# Calibration vs Simulation-Based Pricing

**Topic:** Computational Finance
**Tags:** calibration, simulation, model-free, parametric model, ivs fitting, rl pricing, pricing paradigm
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

Two philosophically distinct approaches exist for derivatives pricing. **Calibration** fits a parametric model's parameters to today's market prices, then uses the model to price illiquid instruments consistently. **Simulation-based pricing** (e.g. TDBP) trains a learning agent directly on a distribution of price paths and infers fair values from the path data, without fitting any parametric model to market quotes.

## Key Formula

**Calibration** finds parameters $\theta^*$ minimising the weighted market fit:

$$\theta^* = \arg\min_\theta \sum_{i=1}^{N} w_i \bigl(C_i^{\text{model}}(\theta) - C_i^{\text{market}}\bigr)^2$$

**Simulation-based pricing** trains on paths $\{S_t^{(j)}\}$ drawn from distribution $P$ and minimises the Bellman residual:

$$\mathcal{L}(\theta) = \mathbb{E}_P\!\left[\Bigl(f_t(S_t;\theta) - e^{-r\Delta t}f_{t+1}(S_{t+1};\theta^-)\Bigr)^2\right]$$

No explicit parametric form for $P$ is assumed — only path samples.

## Example

To price a barrier option on a stock with stochastic volatility and discrete dividends: the **calibration route** requires (1) fitting Heston parameters to the vanilla surface, (2) extending to a local-stochastic vol model, (3) adjusting for dividends via pure process mapping, and (4) solving the barrier PDE or running Monte Carlo — four separate stages, each introducing error. The **simulation route** trains a TDBP agent on realistic paths (including stochastic vol and dividend drops) in one stage, pricing the barrier option as a direct output.

## Remember

Calibration is **model-consistent** but fragile: small changes in the vanilla surface can flip calibrated parameters discontinuously (the ill-posedness problem), and the model may price exotic instruments inconsistently with hedging instruments used in practice. Simulation-based pricing is **data-consistent** but requires a good path generator — if the training distribution is unrealistic, the agent learns a biased pricer. On a live derivatives desk, calibration dominates for flow vanilla books (speed, interpretability, regulatory compliance); simulation-based RL is emerging for bespoke exotics and dynamic hedging where model misspecification costs are highest.
