# FX Quote Conventions

**Topic:** Financial Mathematics
**Tags:** fx, currency pair, base currency, quote currency, cross rate, pips
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

An exchange rate is quoted as a currency pair BASE/QUOTE: the price of one unit of the base currency in units of the quote currency. GBPUSD $= 1.3000$ means one pound costs $1.30$ dollars. A move in the fourth decimal place is one pip, and spot trades normally settle two business days later (T+2). Because every trade exchanges two currencies, a call on one currency is always a put on the other.

## Key Formula

Inverting a quote and building a cross rate from two quotes against a common currency:

$$S_{\text{USD/GBP}} = \frac{1}{S_{\text{GBP/USD}}}, \qquad S_{\text{EUR/GBP}} = \frac{S_{\text{EUR/USD}}}{S_{\text{GBP/USD}}}$$

Call–put duality: a call on the base currency struck at $K$ pays, per unit of base,

$$(S_T - K)^+ = S_T\,K\left(\frac{1}{K} - \frac{1}{S_T}\right)^+$$

that is, $K$ puts on the quote currency struck at $1/K$, with the payoff converted at $S_T$.

## Example

With GBPUSD $= 1.3000$ and EURUSD $= 1.0800$:

- USDGBP $= 1/1.3000 = 0.7692$
- EURGBP $= 1.0800 / 1.3000 = 0.8308$

A GBP call / USD put on £1,000,000 struck at $1.3000$ is the same contract as a USD put / GBP call on \$1,300,000 struck at $0.7692$: both exchange £1m for \$1.3m at expiry if it pays to do so.

## Remember

Most FX pricing errors are convention errors, not maths errors. In Garman–Kohlhagen the base currency's interest rate plays the role of a dividend yield and the quote currency's rate is the discount rate, so getting the pair the wrong way round swaps the two rates. Premiums, deltas and notionals can each be quoted in either currency, and a desk must agree which before comparing prices.
