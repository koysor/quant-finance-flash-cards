# Sticky-Strike vs Sticky-Delta

**Topic:** Volatility
**Tags:** smile dynamics, sticky strike, sticky delta, local volatility, hedging, moneyness
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

Sticky-strike and sticky-delta are two competing rules of thumb for how the implied volatility smile behaves when the underlying spot price moves. **Sticky-strike** assumes each fixed strike keeps its implied volatility unchanged; **sticky-delta** (sticky-moneyness) assumes the smile shifts with spot so that implied volatility stays constant at a fixed level of moneyness. Which rule holds determines the correct delta to use for hedging, since it governs how much the option's implied volatility — and hence its price — is expected to change as spot moves.

## Key Formula

Under **sticky-strike**, implied volatility at a fixed strike is unchanged by a spot move:

$$\frac{\partial \sigma_{\text{imp}}(K)}{\partial S} = 0 \quad \Rightarrow \quad \delta = \delta_{BS}$$

Under **sticky-delta**, implied volatility is constant at fixed moneyness $y = \ln(K/F)$, so as spot (and hence forward $F$) moves, the smile slides with it:

$$\frac{\partial \sigma_{\text{imp}}}{\partial S}\bigg|_{\text{sticky-delta}} \approx -\frac{K}{S}\frac{\partial \sigma_{\text{imp}}}{\partial K}$$

The corrected ("smile-adjusted") delta under sticky-delta dynamics is:

$$\delta_{\text{smile}} = \delta_{BS} + \mathcal{V}_{BS}\,\frac{\partial \sigma_{\text{imp}}}{\partial S}$$

where $\mathcal{V}_{BS}$ is Black-Scholes vega. Local volatility models are internally sticky-strike; the minimum-variance delta is a sticky-delta-style correction.

## Example

SPX trades at $S = 4{,}500$. A 1-month call struck at $K = 4{,}550$ has implied vol 18%, and the smile slope is $\partial\sigma_{\text{imp}}/\partial K = -0.00008$ per point of strike (a typical downward-sloping equity skew).

If spot falls 50 points to $S = 4{,}450$: under **sticky-strike**, the $K=4{,}550$ option's IV stays at 18%. Under **sticky-delta**, the whole smile shifts down with spot, so the option — now further out-of-the-money — inherits the IV that used to sit at a strike 50 points lower, roughly $18\% + 50 \times 0.00008 \times 100 \approx 18.4\%$. The vega-weighted difference between these two IV forecasts is exactly the correction that separates $\delta_{BS}$ from a smile-consistent hedge ratio.

## Remember

This distinction is the theoretical fault line behind the minimum-variance delta: local volatility models reprice every vanilla exactly but bake in sticky-strike dynamics, while empirically equity index smiles behave closer to sticky-delta — implied vol tracks moneyness, not the absolute strike. A trader who hedges a local-vol book with $\delta_{BS}$-style deltas is implicitly betting on sticky-strike; when the market instead moves sticky-delta, the hedge is systematically wrong in a predictable direction. This is precisely the gap the minimum-variance delta closes, and it is why practitioners build local-vol pipelines in moneyness (not raw strike) and interpolate total variance rather than implied volatility — both choices lean the model closer to observed sticky-delta behaviour.
