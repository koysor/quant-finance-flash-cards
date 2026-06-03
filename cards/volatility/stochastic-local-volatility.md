# Stochastic Local Volatility (SLV) Model

**Topic:** Volatility
**Tags:** stochastic local volatility, leverage function, heston, dupire, smile calibration, particle method
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Stochastic Local Volatility (SLV)** model combines Dupire's local volatility (exact smile fit) with Heston's stochastic volatility (realistic forward vol dynamics) by introducing a **leverage function** $L(S,t)$ that scales the stochastic variance to reproduce the market smile exactly. Pure local vol fits the smile but produces wrong forward vol dynamics; pure stochastic vol fits the smile approximately but cannot match every strike; SLV achieves both.

## Key Formula

The SLV dynamics under the risk-neutral measure are:

$$\frac{dS_t}{S_t} = r\,dt + L(S_t, t)\sqrt{V_t}\,dW_t^S$$
$$dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V, \quad \text{corr}(dW^S, dW^V) = \rho\,dt$$

The leverage function is determined by the **Gyöngy condition** — requiring that the marginal distribution of $S_t$ matches the market-implied distribution at every maturity:

$$L^2(K,T) = \frac{\sigma_\text{Dupire}^2(K,T)}{\mathbb{E}\!\left[V_T \mid S_T = K\right]}$$

The conditional expectation $\mathbb{E}[V_T \mid S_T = K]$ is computed via a **particle method** or Kolmogorov PDE.

## Example

SPX 3-month smile: 25-delta put vol = 21%, ATM = 18%, 25-delta call vol = 16.5%. Pure Heston (calibrated to ATM and 10-delta options) fits ATM and wings but misses 25-delta put by 0.8 vol points. SLV with the same Heston parameters but calibrated leverage function $L(S,t)$ fits all strikes to within 0.05 vol points. Crucially, SLV's 3-month-to-6-month forward vol smile is more realistic than Dupire's (which tends to produce flat or inverted forward smiles that cause mispricing in forward-start options).

## Remember

SLV is the production standard on equity derivatives desks because it solves the **calibration vs hedging dilemma**: local vol calibrates the smile perfectly but produces incorrect vega hedges (Greeks computed from local vol do not match the market's move when vol changes); stochastic vol produces correct vega dynamics but cannot match the full smile without SLV's leverage function. For RL, SLV paths are the most realistic training distribution for European and path-dependent option pricers — more realistic than GBM, Heston, or local vol alone — because the leverage function ensures the training paths produce the same marginal distributions as the market smile at every maturity.
