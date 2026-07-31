# Derman's Skew Rule of Thumb

**Topic:** Volatility
**Tags:** local volatility, skew, rule of two, backbone, derman, volatility smile
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

Derman's rule of thumb — the "rule of two" — states that when the implied volatility skew is approximately linear in strike, the local volatility skew is twice as steep. Equivalently, local volatility falls twice as fast with spot as implied volatility falls with strike.

## Key Formula

For a smile that is linear near the money over the relevant range,

$$\sigma_{\text{imp}}(K, T) \approx \sigma_0 - b\,(K - S_0)$$

the local volatility function implied by Dupire's equation is, to first order,

$$\sigma_{\text{loc}}(S, T) \approx \sigma_0 - 2b\,(S - S_0)$$

The factor of two comes from implied volatility being an *average* of local volatilities along the path from $S_0$ to $K$: if the local function has slope $-2b$, its running average from $S_0$ to $K$ has slope $-b$, exactly half.

The same rule gives the **backbone** — how at-the-money implied volatility itself moves when spot moves:

$$\frac{\partial \sigma_{\text{ATM}}}{\partial S} \approx 2\,\frac{\partial \sigma_{\text{imp}}}{\partial K}$$

## Example

Three-month SPX options with spot at 4,500 show at-the-money implied volatility of 18%, falling to 17.6% at a strike of 4,600. The implied skew is

$$b = \frac{0.180 - 0.176}{100} = 4\times 10^{-5}\ \text{per index point}$$

Derman's rule then predicts a local volatility at $S = 4{,}600$ of

$$\sigma_{\text{loc}} \approx 0.180 - 2(4\times 10^{-5})(100) = 0.180 - 0.008 = 17.2\%$$

and a backbone of $\partial\sigma_{\text{ATM}}/\partial S \approx -8\times10^{-5}$: a 100-point rally should drag at-the-money implied volatility down by 0.8 volatility points.

## Remember

This is the fastest sanity check on an extracted local volatility surface. Having differentiated a fitted surface numerically to get $\sigma_{\text{loc}}$, compare its near-the-money slope with twice the implied skew — if the ratio is nowhere near two, the derivatives have been corrupted by quote noise or the interpolation has introduced spurious curvature, and the problem is in the pipeline rather than in the market. The backbone form carries a stronger warning for hedging: it is the local volatility model's *prediction* of smile dynamics, and it is empirically too aggressive for equity indices. Real at-the-money volatility typically moves by less than twice the skew, which is precisely why a surface-derived $\delta_{MV}^{LV}$ can over-correct the Black-Scholes delta and end up hedging worse than a regression-fitted minimum-variance delta.
