# Variance Risk Premium

**Topic:** Volatility
**Tags:** variance risk premium, implied volatility, realised volatility, volatility trading, risk premia
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **variance risk premium** (VRP) is the systematic difference between implied variance (the market's expectation of future volatility, as priced into options) and subsequent realised variance. Empirically, implied volatility exceeds realised volatility on average, so the VRP is persistently positive. This premium represents the compensation investors demand for bearing volatility risk — effectively the cost of portfolio insurance. It is one of the most robust and well-documented risk premia in financial markets.

## Key Formula

$$\text{VRP}_t = \sigma_{\text{impl},t}^2 - \mathbb{E}_t[\sigma_{\text{real},t \to T}^2]$$

In practice, the ex-post VRP is measured as:

$$\widehat{\text{VRP}}_t = \sigma_{\text{impl},t}^2 - \sigma_{\text{real},t \to T}^2$$

A common proxy uses the VIX index for implied variance and subsequent 30-day realised variance:

$$\widehat{\text{VRP}}_t = \text{VIX}_t^2 - \text{RV}_{t,30}^2$$

The annualised VRP for the S&P 500 has averaged roughly 4–5 variance points (approximately 2–3 volatility points) since 1990.

## Example

On a given date, the VIX stands at 20% (implied variance $= 0.04$). Over the next 30 days, the S&P 500 realises 16% volatility (realised variance $= 0.0256$):

$$\widehat{\text{VRP}} = 0.0400 - 0.0256 = 0.0144$$

In volatility terms: $20\% - 16\% = 4\%$ points.

A trader who sold a 30-day variance swap at 20 vol and held to expiry would capture this 4-point spread, earning approximately $4\% \times \text{vega notional}$ before transaction costs.

## Remember

The VRP is the fundamental reason that systematic option-selling strategies (such as covered calls, short straddles, and short variance swaps) are profitable on average. However, the premium exists precisely because it carries significant left-tail risk: during crises, realised volatility spikes far above implied (e.g. the VRP turned deeply negative in March 2020), generating catastrophic losses for short-vol positions. Understanding the VRP is essential for anyone constructing volatility portfolios — it determines whether you are paying for insurance or collecting it, and at what expected cost.
