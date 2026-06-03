# P vs Q Measures in RL Pricing

**Topic:** Computational Finance
**Tags:** p-measure, q-measure, risk-neutral pricing, reinforcement learning, pricing kernel, measure change
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

In quantitative finance, the **P-measure** (physical or real-world measure) governs actual historical price dynamics, while the **Q-measure** (risk-neutral measure) is an equivalent martingale measure under which all discounted asset prices are martingales. RL agents can be trained under either measure and can even infer the connection between them.

## Key Formula

Under Q, all risky assets earn the risk-free rate:

$$\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{B_T} \,\middle|\, \mathcal{F}_t\right] = \frac{S_t}{B_t}, \qquad B_t = e^{rt}$$

The two measures are linked via the **pricing kernel** (Radon-Nikodým derivative) $\xi_T$:

$$\mathbb{E}^{\mathbb{P}}\!\left[X_T\,\xi_T\right] = \mathbb{E}^{\mathbb{Q}}\!\left[X_T\,e^{-rT}\right]$$

Under GBM with drift $\mu$ and vol $\sigma$, the Girsanov change-of-measure adds drift correction $(\mu - r)/\sigma$ (the **market price of risk**) to convert $W_t^P \to W_t^Q$.

## Example

An RL agent trained on 10 years of S&P 500 daily returns (P-measure, drift $\mu = 8\%$) learns to forecast conditional mean returns — useful for generating trading signals. The same architecture retrained on risk-neutral simulations (Q-measure, drift $= r = 5\%$) learns to price derivatives consistently with no-arbitrage — useful for a derivatives book.

## Remember

RL pricing is **measure-flexible**: switching the training distribution from historical paths (P) to risk-neutral simulations (Q) converts the same TDBP architecture from a return forecaster to a fair-value pricer. RL can further infer the pricing kernel $\xi$ by training jointly on P and Q data, recovering the market price of risk — something classical models require separate calibration for. Traditional formulas such as Black-Scholes are strictly Q-measure constructs.
