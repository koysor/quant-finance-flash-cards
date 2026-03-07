# Vasicek Model

**Topic:** Stochastic Processes
**Tags:** interest rate, mean reversion, ornstein-uhlenbeck, bond pricing, short rate
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Vasicek model** is a mean-reverting stochastic differential equation for the short-term interest rate. It is an Ornstein–Uhlenbeck process applied to rates: when the rate is above its long-run mean it is pulled down, and when below it is pulled up. The model is analytically tractable but permits negative rates.

## Key Formula

$$dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$$

| Parameter | Meaning |
|---|---|
| $\kappa > 0$ | Speed of mean reversion |
| $\theta$ | Long-run mean level |
| $\sigma$ | Volatility of the short rate |

**Conditional distribution:**

$$r_t \mid r_s \sim N\!\left(r_s e^{-\kappa(t-s)} + \theta(1 - e^{-\kappa(t-s)}),\; \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(t-s)})\right)$$

**Long-run limit** ($t \to \infty$): $\;r_t \to N\!\left(\theta,\; \frac{\sigma^2}{2\kappa}\right)$

## Example

With $\kappa = 0.5$, $\theta = 4\%$, $\sigma = 1\%$, and current rate $r_0 = 6\%$, the expected rate in 2 years:

$$E[r_2] = 6\% \cdot e^{-0.5 \times 2} + 4\%(1 - e^{-1}) = 6\% \times 0.368 + 4\% \times 0.632 = 2.21\% + 2.53\% = 4.74\%$$

The rate is pulled from 6% toward the long-run mean of 4%, reaching 4.74% after 2 years.

## Remember

The Vasicek model is one of the foundational short-rate models in fixed-income quantitative finance. Its mean-reverting property captures the empirical observation that interest rates do not wander arbitrarily far from equilibrium — central banks act to pull them back. The model yields closed-form bond prices and is the basis for more sophisticated models (Hull–White, CIR). Its main limitation — normally distributed rates that can go negative — was considered a flaw until negative rates actually appeared in practice. The long-run variance $\sigma^2/(2\kappa)$ shows that faster mean reversion ($\kappa$) or lower volatility ($\sigma$) produces a tighter distribution of future rates.
