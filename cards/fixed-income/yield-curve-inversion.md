# Yield Curve Inversion

**Topic:** Fixed Income
**Tags:** yield curve inversion, recession indicator, 2s10s spread, rate expectations, term structure, monetary policy
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Yield curve inversion occurs when short-term interest rates exceed long-term rates — most commonly measured by the 2-year minus 10-year Treasury spread turning negative — signalling that markets price in future rate cuts and that current policy is restrictive relative to the long-run neutral rate.

## Key Formula

The 2s10s spread decomposes via the DNS framework into expectations and risk premium components:

$$\underbrace{y_t(10) - y_t(2)}_{\text{2s10s spread}} = \underbrace{\left[\frac{1}{10}\sum_{k=0}^{9}\mathbb{E}_t[r_{t+k}] - \frac{1}{2}\sum_{k=0}^{1}\mathbb{E}_t[r_{t+k}]\right]}_{\text{expectations slope}} + \underbrace{\bigl[tp_t(10) - tp_t(2)\bigr]}_{\text{term premium slope}}$$

Inversion (spread $< 0$) requires the expectations slope to turn sufficiently negative — markets pricing in more rate cuts over the long horizon than the short. Under the Taylor Rule logic, this occurs when the current policy rate exceeds its long-run prescription, so the market anticipates eventual normalisation downward.

## Example

US yield curve, July 2023: 2-year yield 4.87%, 10-year yield 3.97%, 2s10s spread $= -0.90\%$ — the deepest inversion since 1981. DNS decomposition: expectations slope $-0.70\%$ (markets pricing in $\sim$175bp of cuts over the following decade) plus term premium slope $-0.20\%$ (flight-to-safety demand compressing long-term risk premia). The Federal Reserve began cutting rates 14 months later, confirming the expectations component's signal.

## Remember

Every US recession since 1955 has been preceded by a 2s10s inversion, making it the single most-watched macro indicator on fixed income desks. The mechanism is straightforward: the 2-year yield prices the expected path of short rates over two years (heavily influenced by near-term Taylor Rule deviations), while the 10-year yield prices a 10-year weighted average. When today's policy rate is above its long-run neutral level — as it must be to fight inflation — the short end rises above the long end, and the inversion persists until either the central bank cuts or growth expectations recover enough to revise the rate path upward.
