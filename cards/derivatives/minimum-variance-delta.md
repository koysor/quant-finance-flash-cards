# Minimum-Variance Delta

**Topic:** Derivatives
**Tags:** delta hedging, minimum variance delta, smile dynamics, vega, hedging effectiveness, sticky delta
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **minimum-variance delta (MVD)**, $\delta_{MV}$, is the hedge ratio that minimises the variance of a delta-hedged option position's daily P&L, rather than assuming a purely mechanical Black-Scholes sensitivity. It corrects $\delta_{BS}$ for the empirical fact that when the underlying moves, implied volatility tends to move with it (a negative spot–vol correlation for equity indices), so the option's true sensitivity to spot differs from the constant-volatility textbook delta.

## Key Formula

Hull and White's (2017) regression-based estimator, fitted per delta-and-maturity bucket from a time series of daily hedging errors:

$$\Delta f - \delta_{BS}\,\Delta S = \frac{\mathcal{V}_{BS}}{S\sqrt{\tau}}\left(a + b\,\delta_{BS} + c\,\delta_{BS}^2\right)\Delta S + \varepsilon$$

giving

$$\delta_{MV} = \delta_{BS} + \frac{\mathcal{V}_{BS}}{S\sqrt{\tau}}\left(a + b\,\delta_{BS} + c\,\delta_{BS}^2\right)$$

A surface-based alternative uses the local-vol surface's own strike slope, under an assumed sticky-delta smile dynamic:

$$\delta^{LV}_{MV} \approx \delta_{BS} + \mathcal{V}_{BS}\,\frac{\partial \sigma_{\text{imp}}}{\partial S}$$

where $\Delta f$ is the daily change in option price, $\mathcal{V}_{BS}$ is Black-Scholes vega, $S$ is spot, $\tau$ is time to expiry, and $a, b, c$ are regression coefficients re-estimated at each date.

## Example

An SPX call has $\delta_{BS} = 0.50$, vega $\mathcal{V}_{BS} = 12$, spot $S = 4{,}500$, and $\tau = 0.5$ years. Hull-White's fitted coefficients for this bucket are $a = -0.05$, $b = 0.10$, $c = -0.02$.

$$a + b(0.50) + c(0.50)^2 = -0.05 + 0.05 - 0.005 = -0.005$$

$$\delta_{MV} = 0.50 + \frac{12}{4500\sqrt{0.5}}\times(-0.005) = 0.50 - 0.0000188 \approx 0.49998$$

The correction is small here but grows sharply for deep OTM options where $\mathcal{V}_{BS}/(S\sqrt{\tau})$ and the smile slope are both larger, shifting the optimal hedge meaningfully away from $\delta_{BS}$.

## Remember

MVD is the practical payoff of understanding sticky-strike vs sticky-delta smile dynamics: because equity index smiles behave closer to sticky-delta than the sticky-strike dynamics implicit in $\delta_{BS}$, a hedge that ignores the spot–vol correlation is systematically biased. Its effectiveness is measured by the **Gain statistic** — the percentage reduction in hedging-error variance versus plain Black-Scholes — and is not universal: Hull and White found MVD improves hedging out-of-the-money but can underperform near-the-money, and it breaks down in regime shifts (e.g. March 2023) when implied vol stops tracking spot in the usual direction. Reporting Gain by delta and maturity bucket, not as a single aggregate number, is essential because trading activity — and therefore the aggregate statistic — is dominated by the near-forward region.
