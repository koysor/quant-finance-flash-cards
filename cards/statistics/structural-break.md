# Structural Break

**Topic:** Statistics
**Tags:** structural break, chow test, parameter instability, regime change, cointegration, financial crisis
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A structural break is a point in time $\tau$ at which the parameters of a statistical model change permanently, so that estimates based on the full sample give a misleading picture of both sub-periods. Structural breaks are a specific form of non-stationarity caused by economic crises, policy shifts, or technological change — unlike random-walk non-stationarity they are sharp and irreversible.

## Key Formula

**Chow test** (known breakpoint $\tau$): Fit three OLS regressions — pre-break sample ($RSS_1$, $T_1$ obs), post-break sample ($RSS_2$, $T_2$ obs), and pooled ($RSS$, $T = T_1 + T_2$ obs):

$$F = \frac{(RSS - RSS_1 - RSS_2)/k}{(RSS_1 + RSS_2)/(T - 2k)} \;\sim\; F_{k,\; T-2k}$$

where $k$ = number of estimated parameters. Reject $H_0$ (no break) if $F > F_{k, T-2k}^{\alpha}$.

**Unknown breakpoint:** The **Bai-Perron** test searches all candidate break dates and selects the one that maximises the $F$-statistic:

$$\hat{\tau} = \arg\max_\tau F(\tau)$$

with critical values adjusted for the search over $\tau$.

## Example

CAPM regression $R_t^{\text{bank}} = \alpha + \beta R_t^{\text{market}} + \varepsilon_t$ for a UK bank stock, daily data 2003–2012. Chow test at $\tau = $ September 2008: $F = 18.4 > F_{2,\,2260}^{1\%} \approx 4.6$ — strong evidence of a break.

Pre-crisis estimate: $\hat{\beta} = 1.1$. Post-crisis estimate: $\hat{\beta} = 1.8$. Using the pooled estimate $\hat{\beta} = 1.3$ for risk calculations understates post-2008 market sensitivity by 28%, causing systematic underestimation of the bank's tail risk.

## Remember

Structural breaks are the most important practical limitation of **backtested risk and pricing models**. A VaR model calibrated entirely on pre-2007 data assigns low probability to the volatility regime that materialised in 2008 — not because of model error, but because the pre-break data was genuinely drawn from a different distribution. Risk managers address this with **rolling estimation windows** (typically 1–2 years) that discard stale pre-break data, at the cost of statistical precision. Cointegration-based pairs trading is particularly vulnerable: a structural break in the long-run relationship between two assets permanently dissolves the cointegrating spread, turning a spread trade into an unhedged directional bet.
