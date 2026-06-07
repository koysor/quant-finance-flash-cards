# Annualised Sharpe Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** sharpe ratio, annualisation, volatility scaling, square root of time, performance measurement, risk-adjusted return
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The annualised Sharpe ratio is the Sharpe ratio expressed in annual units, obtained by scaling a Sharpe computed from periodic (daily, weekly, or monthly) returns. Because volatility scales with the square root of time while returns scale linearly, the annualisation factor is $\sqrt{N}$, where $N$ is the number of periods per year.

## Key Formula

$$S_{\text{ann}} = S_{\text{period}} \times \sqrt{N}$$

where $S_{\text{period}} = \dfrac{\bar{r}_{\text{excess}}}{\sigma_{\text{period}}}$ is the Sharpe computed from periodic excess returns and $N$ is the number of those periods in a year.

Standard annualisation factors:

| Frequency | $N$ | Factor |
|-----------|-----|--------|
| Daily | 252 | $\sqrt{252} \approx 15.87$ |
| Weekly | 52 | $\sqrt{52} \approx 7.21$ |
| Monthly | 12 | $\sqrt{12} \approx 3.46$ |

The formula follows from: mean scales by $N$, standard deviation by $\sqrt{N}$, so their ratio scales by $\sqrt{N}$.

## Example

A strategy has daily excess returns with mean $\bar{r}_d = 0.04\%$ and standard deviation $\sigma_d = 0.8\%$.

Daily Sharpe: $S_d = 0.04\% / 0.8\% = 0.05$

Annualised Sharpe: $S_{\text{ann}} = 0.05 \times \sqrt{252} \approx 0.05 \times 15.87 \approx 0.79$

A second strategy computed from monthly returns has $S_m = 0.23$, giving $S_{\text{ann}} = 0.23 \times \sqrt{12} \approx 0.80$ — comparable despite different frequencies.

## Remember

Annualisation makes Sharpe ratios comparable across strategies regardless of how frequently returns are measured. The $\sqrt{N}$ rule is exact only when returns are i.i.d. — in practice, autocorrelation (common in momentum strategies) inflates the annualised Sharpe because positive serial correlation makes volatility grow faster than $\sqrt{N}$, so the correct adjustment requires scaling by the actual standard deviation of annual returns, not the scaled daily figure. This is why the deflated Sharpe ratio and the probability of Sharpe ratio tests account for non-i.i.d. return structure.

