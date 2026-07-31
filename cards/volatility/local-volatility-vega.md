# Vega Under Local Volatility

**Topic:** Volatility
**Tags:** vega, local volatility, smile dynamics, backbone, total delta, surface bump
**Created:** 2026-07-31
**Author:** Claude Opus 5

---

## Definition

Vega under local volatility is the sensitivity obtained by perturbing the whole calibrated volatility surface and re-extracting local volatility before repricing, rather than shifting a single Black-Scholes volatility number. Because the surface moves when spot moves, it also supplies the correction that turns $\delta_{BS}$ into a smile-aware delta.

## Key Formula

The total sensitivity of an option to spot, allowing implied volatility to move with it:

$$\delta_{\text{total}} = \underbrace{\frac{\partial V}{\partial S}}_{\delta_{BS}} + \underbrace{\frac{\partial V}{\partial \sigma_{\text{imp}}}}_{\mathcal{V}_{BS}}\cdot\frac{\partial \sigma_{\text{imp}}}{\partial S}$$

The second term is entirely a modelling choice about smile dynamics:

| Assumption | $\partial\sigma_{\text{imp}}/\partial S$ | Resulting delta |
|---|---|---|
| Sticky strike | $0$ | $\delta_{BS}$ |
| Sticky delta | $-\dfrac{K}{S}\dfrac{\partial\sigma_{\text{imp}}}{\partial K}$ | $\delta_{BS}$ plus skew term |
| Local volatility backbone | $2\,\dfrac{\partial\sigma_{\text{imp}}}{\partial K}$ | $\delta^{LV}_{MV}$ |

For an exotic with no closed form, the surface vega is computed by finite difference on the calibration itself:

$$\mathcal{V}_{LV} \approx \frac{V\big(\sigma_{\text{loc}}[\,w + \epsilon\,]\big) - V\big(\sigma_{\text{loc}}[\,w - \epsilon\,]\big)}{2\epsilon}$$

where $w \pm \epsilon$ denotes bumping the total variance surface and re-running Dupire on the bumped surface.

## Example

A three-month SPX call, spot $S = 4{,}500$, at-the-money implied volatility 18%, Black-Scholes delta $0.55$ and vega $\mathcal{V}_{BS} = 897$ per unit of volatility. The fitted surface has strike slope

$$\frac{\partial \sigma_{\text{imp}}}{\partial K} = -4\times 10^{-5}\ \text{per index point}$$

The local volatility backbone doubles this, giving $\partial\sigma_{\text{imp}}/\partial S = -8\times10^{-5}$:

$$\delta^{LV}_{MV} = 0.55 + 897 \times (-8\times 10^{-5}) = 0.55 - 0.072 = 0.478$$

A 13% reduction in the hedge — on a 1,000-lot position that is roughly 72 fewer index futures held against the book.

## Remember

Two distinct pieces of information come out of a fitted surface, and only the first is reliable. The **strike slope** $\partial\sigma_{\text{imp}}/\partial K$ is directly observed from the quotes and is what makes a bumped-surface vega more honest than $\mathcal{V}_{BS}$ for a barrier or cliquet, whose value depends on the whole surface rather than on one volatility. The **backbone** $\partial\sigma_{\text{imp}}/\partial S$ is not observed at all — it is the local volatility model's assumption about how the surface will move next, and the factor of two it predicts is empirically too strong for equity indices. This is the practical warning of the Hull-White work: a delta built on the backbone can over-hedge, which is why the regression-based $\delta_{MV}$ estimated from realised daily moves often beats the surface-derived $\delta^{LV}_{MV}$ near the money, even though the surface version is the more theoretically complete construction.
