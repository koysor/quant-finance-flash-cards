# Short-Rate Model Parameter Stability

**Topic:** Fixed Income
**Tags:** parameter stability, rolling estimation, Vasicek, CIR, model risk, calibration, time series
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

**Parameter stability** measures how much a model's estimated parameters change across different estimation windows. A stable model produces similar $(\kappa, \theta, \sigma)$ from any reasonably sized historical sample; an unstable model requires frequent re-estimation and signals that the chosen parametric form may not be the true data-generating process.

## Key Formula

For a Vasicek/OU model $dr = \kappa(\theta - r)\,dt + \sigma\,dW$, rolling estimates over windows $[t-W, t]$ give parameter sequences $\hat\kappa_t$, $\hat\theta_t$, $\hat\sigma_t$. The **stability score** for parameter $\phi$ is:

$$S_\phi = \frac{\text{SD}(\hat\phi_t)}{\text{mean}(\lvert\hat\phi_t\rvert)}$$

Lower $S_\phi$ means more stable. Typical findings from US LIBOR data:

| Parameter | Stability (qualitative) | Reason |
|---|---|---|
| $\sigma$ (volatility) | **High** — stable | Quadratic variation converges quickly |
| $\theta$ (long-run mean) | **Medium** — regime-dependent | Drifts with monetary policy cycles |
| $\kappa$ (mean reversion speed) | **Low** — very unstable | Sensitive to period covered and rate cycle phase |

## Example

Rolling 3-year estimates of Vasicek $\kappa$ from US Treasury data (1990–2010) fluctuate between 0.05 (near-random-walk regime) and 1.8 (fast mean-reversion after 2008 crisis) — a 36× range. In contrast, $\sigma$ estimated from the same windows stays within a factor of 2. This instability in $\kappa$ means delta hedges computed with today's estimate can be badly wrong during a regime change.

## Remember

Parameter instability is the empirical argument for **calibration over fitting**: if parameters estimated from history shift so much that they misrepresent today's market, it is more honest to calibrate directly to today's prices. But calibration introduces its own instability — the time-dependent function $\eta(t)$ changes daily. The practical lesson is that no single set of parameters is reliable over long horizons, and risk management of interest rate books requires scenario analysis across plausible parameter ranges rather than a single-model view.
