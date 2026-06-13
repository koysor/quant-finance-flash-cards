# Shifted SABR Model

**Topic:** Volatility
**Tags:** shifted SABR, negative rates, vol smile, EUR swaptions, displacement, SABR extension
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Shifted SABR extends the SABR model to negative interest rate environments by displacing the forward rate $F \to F + s$ by a positive shift $s$, so the effective forward is always positive and standard SABR dynamics and the Hagan approximation remain applicable.

## Key Formula

Shifted forward $\tilde{F} = F + s$ follows SABR dynamics:

$$d\tilde{F} = \alpha\,\tilde{F}^\beta\,dW_1, \qquad d\alpha = \nu\alpha\,dW_2, \qquad \mathbb{E}[dW_1\,dW_2] = \rho\,dt$$

Implied vol under Hagan approximation (applied with shifted inputs $\tilde{F} = F + s$, $\tilde{K} = K + s$):

$$\sigma_{\text{imp}}(\tilde{F}, \tilde{K}) \approx \frac{\alpha}{(\tilde{F}\tilde{K})^{(1-\beta)/2}}\cdot\left(1 + \text{smile corrections in } \rho, \nu, \beta\right)$$

**Choice of shift $s$:** set $s$ large enough that $F + s > 0$ for all plausible rate scenarios, typically:

| Market | Typical shift $s$ |
|---|---|
| EUR swaptions (2014–2022) | 1–3% |
| CHF/JPY swaptions | 1–5% |
| USD swaptions (post-2020) | 0.5–1% |

A larger $s$ gives more room for rates to fall negative but steepens the effective vol smile at low strikes.

## Example

EUR 10Y swap rate $F = -0.5\%$, shift $s = 3\%$, so $\tilde{F} = 2.5\%$. Strike $K = -1.0\%$ maps to $\tilde{K} = 2.0\%$. The Hagan formula applied to $(\tilde{F}, \tilde{K}) = (2.5\%, 2.0\%)$ returns a Black vol in the shifted world; the market quotes this as the implied vol for the original $(F, K) = (-0.5\%, -1.0\%)$ pair. Swaption prices use Black's formula on the shifted forward $\tilde{F}$ rather than the original $F$.

## Remember

Shifted SABR became the EUR rates desk standard after 2014 when the ECB pushed the deposit rate negative and EUR 5Y swap rates fell through zero. The shift $s$ is a modelling convention, not a market observable — different banks use different shifts, which means implied vols are only comparable if you know the shift used. In practice, risk systems must store both the shift and the SABR parameters to consistently re-price options, and calibrating across a shift-change (e.g. widening $s$ from 1% to 3%) requires re-stripping the whole vol surface.
