# Non-ergodic Markets

**Topic:** Risk
**Tags:** ergodicity, non-ergodic, regime change, model risk, volatility estimation, structural break
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A market is non-ergodic when the time average of a single historical path does not converge to the ensemble average across many possible paths. Structural breaks, regime changes, and fat-tailed jumps all violate the ergodicity assumption, making statistics estimated from historical data unreliable proxies for future risk.

## Key Formula

The key distinction is between time-average and ensemble-average growth:

$$g_{\text{time}} = \lim_{T\to\infty} \frac{1}{T}\int_0^T \ln(1+r_t)\,dt, \qquad g_{\text{ensemble}} = \ln \mathbb{E}[1+r]$$

Jensen's inequality implies $g_{\text{time}} \leq g_{\text{ensemble}}$, with equality only if returns are ergodic. Under multiplicative compounding of log-normal returns with drift $\mu$ and volatility $\sigma$:

$$g_{\text{time}} = \mu - \frac{\sigma^2}{2} < \mu = g_{\text{ensemble}}$$

The gap $\frac{\sigma^2}{2}$ is the volatility drag — the cost of non-ergodicity under compounding.

## Example

A risk manager estimates 1-year 99% VaR using ten years of daily returns from 2000–2009. The regime includes both the dot-com crash (2000–2002) and the 2008 financial crisis. Averaging over this single path conflates two distinct regimes; the resulting VaR estimate reflects the historical mixture, not the current regime's risk profile. An out-of-sample backtest on 2010–2020 data shows systematic VaR breaches during calm periods (VaR overstated) and underestimation during the 2020 COVID crash (regime break again).

## Remember

Historical VaR and Expected Shortfall implicitly assume ergodicity: one long historical path is treated as equivalent to many parallel realisations of today's risk. Structural breaks (e.g. regulatory changes, central bank regime shifts, COVID-19) destroy this equivalence. Practitioners address this with rolling windows, EWMA weighting, or regime-switching models — each a practical workaround for the non-ergodicity of real markets.
