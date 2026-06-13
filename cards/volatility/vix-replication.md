# VIX Replication

**Topic:** Volatility
**Tags:** VIX, variance swap, log-contract, model-free variance, options strip, S&P 500
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

VIX measures 30-day risk-neutral expected volatility of the S&P 500, computed as the square root of the model-free integrated variance estimated from a strip of OTM puts and calls — it does not assume a lognormal distribution.

## Key Formula

$$\text{VIX}^2 = \frac{2}{T} \sum_i \frac{\Delta K_i}{K_i^2}\, e^{rT}\, Q(K_i) - \frac{1}{T}\!\left(\frac{F}{K_0} - 1\right)^{\!2}$$

where $Q(K_i) = $ put price if $K_i \le F$, call price if $K_i > F$; $F$ = forward price; $K_0$ = first strike $\le F$.

This replicates a **log-contract** payoff $-2\ln(S_T/F)/T$ using a continuum of options:

$$-2\ln\frac{S_T}{F} = 2\!\int_0^F \frac{\max(K - S_T,0)}{K^2}\,dK + 2\!\int_F^\infty \frac{\max(S_T - K,0)}{K^2}\,dK$$

## Example

SPX options with 23 and 37 days to expiry are combined (interpolated to 30 days). Every listed OTM put ($K < F$) and call ($K > F$) contributes, weighted by $\Delta K_i / K_i^2$. VIX $= \sqrt{\text{result}} \times 100$. Typical range: 12–20 in calm markets, 30–80 during crises.

## Remember

VIX is "model-free" because it uses the entire option strip rather than fitting a parametric model: it captures skew and fat tails directly. The gap between $\text{VIX}^2 / 12$ and subsequent realised variance is the variance risk premium (VRP) — on average positive because sellers of variance earn a premium for bearing the risk of volatility spikes. Trading VIX futures vs the replicating strip exploits this premium.
