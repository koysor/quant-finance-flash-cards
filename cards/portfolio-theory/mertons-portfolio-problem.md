# Merton's Portfolio Problem

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** merton, optimal portfolio, stochastic control, hjb equation, power utility, continuous time
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Merton's portfolio problem** (1969, 1971) finds the dynamic allocation between a risky asset and a risk-free bond that maximises expected utility of terminal wealth, in continuous time. It is the canonical application of the HJB equation to finance and yields the celebrated result that under power (CRRA) utility the optimal risky fraction is **constant** — independent of wealth level and remaining time horizon.

## Key Formula

Risky asset: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$. Wealth process with fraction $\pi$ in risky asset:

$$dW_t = W_t\!\left[(\pi(\mu - r) + r)\,dt + \pi\sigma\,dW_t\right]$$

HJB equation for $V(t, W) = \max_\pi \mathbb{E}[U(W_T)]$:

$$V_t + \max_\pi\!\left\{W\!\left[\pi(\mu-r)+r\right]V_W + \tfrac{1}{2}W^2\pi^2\sigma^2 V_{WW}\right\} = 0$$

Optimising over $\pi$ gives the **Merton optimal fraction**:

$$\pi^* = -\frac{(\mu - r)\,V_W}{\sigma^2\,W\,V_{WW}} \xrightarrow{\text{CRRA}} \frac{\mu - r}{\gamma\,\sigma^2}$$

where $\gamma > 0$ is the coefficient of relative risk aversion. For $\mu = 10\%$, $r = 5\%$, $\sigma = 20\%$, $\gamma = 2$: $\pi^* = 62.5\%$ regardless of wealth or time.

## Example

Two investors, both with CRRA utility ($\gamma = 2$), differ only in wealth: £100k vs £10m. Merton's result says both should hold 62.5% in equities. This is counterintuitive — a wealthier investor may feel less pressure to grow assets — but is the mathematical consequence of CRRA utility's scale invariance. In practice, deviations from the Merton allocation are attributable to liquidity constraints, taxes, background income, or non-CRRA preferences.

## Remember

Merton's problem is the theoretical benchmark against which RL portfolio optimisation is measured: an RL agent trained to maximise expected power-utility terminal wealth should recover $\pi^* = (\mu - r)/(\gamma\sigma^2)$ as its policy if the world is GBM. When the RL policy deviates — as it will under stochastic volatility, transaction costs, or regime switching — the deviation from Merton quantifies the value of the more complex dynamics that the RL agent has learnt to exploit. The risk-adjusted RL reward objectives (Sharpe, Sortino) are all approximations to a utility function; Merton's problem is what you get when you are explicit about the utility form.
