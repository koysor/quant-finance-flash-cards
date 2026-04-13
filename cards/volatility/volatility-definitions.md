# Five Definitions of Volatility

**Topic:** Volatility
**Tags:** parameter volatility, realised volatility, conditional volatility, stochastic volatility, implied volatility, variance risk premium
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Volatility is not a single concept — five distinct definitions coexist in quantitative finance, each arising from a different modelling assumption. The choice of definition determines how volatility is estimated, forecasted, traded, and interpreted.

## Key Formula

| Definition | Symbol | Formula | Source |
|---|---|---|---|
| Parameter (GBM) | $\sigma$ | Constant in $\frac{dS}{S} = \mu\,dt + \sigma\,dW$ | Model assumption |
| Realised (ex-post) | $\hat{\sigma}$ | $\hat{\sigma} = \sqrt{\dfrac{1}{T}\sum_{i=1}^{T} r_i^2}$ | Historical returns |
| Conditional (ARCH/GARCH) | $\sqrt{h_t}$ | $h_t = \text{Var}(r_t \mid \mathcal{I}_{t-1})$ | Filter on past data |
| Stochastic | $\sigma_t$ | $d\sigma_t = \alpha(\cdot)\,dt + \xi\,dZ_t$, $\rho_{WZ} = \rho$ | Own SDE |
| Implied | $\sigma_{\text{impl}}$ | Solve $C_{\text{market}} = C_{\text{BS}}(S, K, r, T, \sigma_{\text{impl}})$ | Option market price |

Here $r_i = \ln(S_i/S_{i-1})$ is the log-return, $\mathcal{I}_{t-1}$ is the information set at time $t-1$, and $dZ_t$ is a second Brownian motion (possibly correlated with $dW_t$).

## Example

Consider a FTSE 100 stock over a one-month window where daily log-returns are available and a one-month at-the-money call is trading.

- **Parameter vol:** the GBM model is calibrated with $\sigma = 18\%$ (annualised) from a historical window — this is fixed for all future simulations.
- **Realised vol:** computing $\hat{\sigma}$ from the past 21 daily returns gives $15\%$ annualised — lower than the model because the past month was calm.
- **Conditional vol (GARCH):** the GARCH(1,1) filter, reacting to last week's sharp move, yields $\sqrt{h_t} = 22\%$ — it is forward-looking within the historical information set.
- **Stochastic vol:** in the Heston model $\sigma_t$ follows a mean-reverting CIR process with its own random shocks, so today's level is a latent state variable, not a single number.
- **Implied vol:** the market call price implies $\sigma_{\text{impl}} = 20\%$ — reflecting the market's expectation and risk premium, not just historical behaviour.

All five numbers describe the same underlying asset yet differ because they answer different questions.

## Remember

- **Risk models** (VaR, CVaR) typically use **realised volatility** estimated from historical returns.
- **ARCH and GARCH** target **conditional volatility** — they extract the time-varying variance that is forecastable from past squared residuals.
- **Derivatives pricing** in the Black-Scholes framework plugs in **parameter volatility**; in practice traders back out **implied volatility** from market prices and quote in those terms.
- **Exotic and smile-consistent models** (Heston, SABR) use **stochastic volatility** to capture the vol-of-vol and correlation skew that a flat $\sigma$ cannot.
- The gap between **implied** and **realised** volatility is the **variance risk premium** — historically implied vol exceeds realised vol on average, which is the P&L source for short-volatility strategies.
