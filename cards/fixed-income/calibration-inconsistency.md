# Calibration Inconsistency

**Topic:** Fixed Income
**Tags:** calibration, model risk, parameter instability, recalibration, Greeks, P&L
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

**Calibration inconsistency** is the unavoidable fact that a calibrated model's time-dependent parameters must be updated every time the yield curve moves. The model describes today's market perfectly but is not a self-consistent description of how rates evolve over time — it is a sophisticated interpolation tool, not a true dynamic model.

## Key Formula

At time $t^*$ the calibrated drift satisfies $Z_{\text{model}}(r,t^*;T) = Z_{\text{market}}(t^*;T)$ for all $T$. At $t^* + \Delta t$ the yield curve has moved and the constraint becomes $Z_{\text{model}}(r,t^*+\Delta t;T) = Z_{\text{market}}(t^*+\Delta t;T)$, requiring a new $\eta^*$:

$$\eta^*(t;\,\text{tomorrow}) \neq \eta^*(t;\,\text{today})$$

| Aspect | Impact |
|---|---|
| Daily recalibration required | Operational cost; risk of model flip |
| Greeks computed with $\eta^*(t;\,\text{today})$ | May be wrong tomorrow after re-fit |
| P&L attribution | Hard to separate market move from model change |
| Model risk | Apparent fit today does not guarantee fit tomorrow |

## Example

A bank prices a 5-year Bermudan swaption using a Hull–White model calibrated to today's curve. The delta (sensitivity to the 5-year swap rate) is computed as $-1.2\%$ per basis point. Tomorrow the yield curve steepens; after recalibration, the same instrument now has delta $-0.9\%$ per bp. The 0.3 bp change is entirely a model artefact — the actual delta has not changed by that amount, but the hedge portfolio built today is wrong tomorrow.

## Remember

Calibration inconsistency is the theoretical Achilles' heel of all calibrated short-rate models. A model with **constant parameters** would have stable Greeks and consistent P&L attribution, but cannot match the market. A model with **time-dependent parameters** matches the market but has unstable parameters. The tension between fit and stability is fundamental and has no clean resolution — it is why interest rate model risk is a major concern on rates trading desks.
