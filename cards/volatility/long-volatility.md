# Long Volatility

**Topic:** Volatility
**Tags:** long volatility, vega, options, hedging, tail risk, convexity
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A long volatility position is any portfolio or strategy that profits when the volatility of an underlying asset increases. The simplest example is buying options (calls or puts), which gain value as implied volatility rises because higher uncertainty increases the probability of a large payoff. More broadly, any position with positive **vega** — positive sensitivity to implied volatility — is described as long volatility.

## Key Formula

The P&L contribution from a change in implied volatility $\Delta\sigma$ for a position with vega $\mathcal{V}$:

$$\text{P\&L}_{\text{vol}} \approx \mathcal{V} \times \Delta\sigma$$

For a delta-hedged long option position, the realised P&L over a small time interval $dt$ depends on the difference between realised and implied variance:

$$d\text{P\&L} = \frac{1}{2}\,\Gamma\,S^2\left(\sigma_{\text{realised}}^2 - \sigma_{\text{implied}}^2\right)dt$$

A long volatility position profits when $\sigma_{\text{realised}} > \sigma_{\text{implied}}$.

## Example

A trader buys 100 ATM call options on a FTSE 100 stock at £2.50 each. The position vega is £800 per 1 percentage point change in implied volatility. If implied volatility rises from 20% to 24%:

$$\text{P\&L}_{\text{vol}} \approx £800 \times 4 = £3{,}200$$

The position gains approximately £3,200 from the volatility increase alone (before accounting for delta, theta, and other Greeks). The trader pays time decay (theta) each day as the cost of maintaining this long volatility exposure.

## Remember

Long volatility is the natural position of option buyers and tail risk hedge funds. In quantitative finance, the key insight is that buying options and delta-hedging isolates the volatility bet: the hedged position profits when the market moves more than implied volatility predicted, regardless of direction. This is why portfolio insurance and crisis-alpha strategies are fundamentally long volatility — they sacrifice steady premium (negative theta) in exchange for convex payoffs during market dislocations. The variance risk premium means implied volatility systematically exceeds realised volatility on average, so long volatility positions tend to bleed slowly but pay off spectacularly in crises.
