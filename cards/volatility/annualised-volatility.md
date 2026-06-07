# Annualised Volatility

**Topic:** Volatility
**Tags:** annualised volatility, standard deviation, square root of time, volatility convention, risk measurement
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Annualised volatility is the standard deviation of an asset's returns expressed in annual units, making volatility estimates comparable across assets, strategies, and measurement frequencies. Any periodic volatility estimate (daily, weekly, monthly) is converted to annual units by multiplying by the square root of the number of periods per year — a consequence of variance being additive for independent returns.

## Key Formula

$$\sigma_{\text{annual}} = \sigma_{\text{period}} \times \sqrt{N}$$

where $N$ is the number of periods in one year under the chosen convention:

| Frequency | Convention | $N$ | Example: $\sigma_{\text{period}} = 1\%$ |
|-----------|-----------|-----|----------------------------------------|
| Daily (trading) | 252 days/year | 252 | $1\% \times \sqrt{252} \approx 15.87\%$ |
| Daily (calendar) | 365 days/year | 365 | $1\% \times \sqrt{365} \approx 19.1\%$ |
| Weekly | 52 weeks/year | 52 | $1\% \times \sqrt{52} \approx 7.21\%$ |
| Monthly | 12 months/year | 12 | $1\% \times \sqrt{12} \approx 3.46\%$ |

The industry standard for equity and most asset classes is **252 trading days**. Fixed income and FX sometimes use 260 or 365.

## Example

A risk analyst computes three estimates of the same equity portfolio's volatility:

- **From daily returns** (past 21 days): $\sigma_d = 0.89\%$ → annualised: $0.89\% \times \sqrt{252} = 14.1\%$
- **From weekly returns** (past 4 weeks): $\sigma_w = 1.98\%$ → annualised: $1.98\% \times \sqrt{52} = 14.3\%$
- **From monthly returns** (past 12 months): $\sigma_m = 4.1\%$ → annualised: $4.1\% \times \sqrt{12} = 14.2\%$

All three give approximately the same annualised figure (14.1%–14.3%), confirming that annualisation achieves frequency independence when returns are approximately i.i.d.

## Remember

Annualised volatility is the $\sigma$ in three of the most important formulas in quantitative finance: the Black-Scholes option pricing formula (where a 1% change in annualised vol shifts the option price by its vega), the Sharpe ratio denominator (so that risk-adjusted return is always quoted in annual units regardless of how returns were measured), and VaR scaling (where the 1-day VaR is scaled to a 10-day VaR via $\times\sqrt{10}$). The 252-day convention is a market standard, not a mathematical truth — comparing a portfolio's 15% volatility (252-day convention) with a competitor's 16.2% (365-day convention) is an apples-to-oranges comparison, so always confirm the convention before benchmarking.

