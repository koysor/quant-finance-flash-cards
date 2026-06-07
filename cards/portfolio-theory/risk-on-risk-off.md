# Risk-On / Risk-Off (RORO)

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** risk-on, risk-off, roro, market sentiment, safe haven, cross-asset, correlation
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Risk-on / risk-off (RORO) describes the binary alternation in investor sentiment between seeking yield (risk-on: buying equities, emerging markets, credit, commodities) and seeking safety (risk-off: buying government bonds, USD, gold, CHF). In risk-on environments, risky assets rise in tandem while safe havens fall; in risk-off environments the relationship reverses. The phenomenon collapses cross-asset correlation structure into a single sentiment factor.

## Key Formula

A simple RORO score can be constructed from standardised returns of representative assets:

$$\text{RORO}_t = \frac{1}{K}\sum_{k=1}^{K} \text{sign}(k) \times \frac{r_{k,t} - \mu_k}{\sigma_k}$$

where sign$(k) = +1$ for risk assets (equities, EM, HY credit) and $-1$ for safe havens (USD, gold, government bonds), and returns are standardised by their historical mean $\mu_k$ and volatility $\sigma_k$. Values above zero signal risk-on; below zero signal risk-off.

Key cross-asset signals:

| Risk-On | Risk-Off |
|---------|---------|
| S&P 500 $\uparrow$ | VIX $\uparrow$ |
| EM equities $\uparrow$ | US 10-year yield $\downarrow$ |
| High-yield spreads $\downarrow$ | USD $\uparrow$ |
| Crude oil $\uparrow$ | Gold $\uparrow$ |
| AUD/USD $\uparrow$ | JPY $\uparrow$ |

## Example

On 24 February 2022 (Russia's invasion of Ukraine), a full risk-off episode lasted approximately 10 trading days: S&P 500 −6%, EM equities −8%, HY credit spreads +100bps; simultaneously gold +5%, 10-year Treasuries −30bps yield (price up), USD index +2%, JPY +3%. A simple RORO composite dropped from +0.4 (mild risk-on) to −2.1 (extreme risk-off) in two days.

## Remember

RORO is a macro risk factor that operates orthogonally to individual stock selection: the best stock-picker in the world loses money during risk-off episodes if the portfolio is long equities. For multi-asset quants, the RORO regime determines which sub-strategies are turned on — long equity momentum in risk-on, long bond momentum in risk-off. The VIX crossing 20 and the USD rising more than 1% in a week are the two most reliable short-horizon risk-off signals used by systematic macro funds; sustained inversions of the RORO composite below −1 for more than 5 consecutive days historically signal a bear market regime transition.

