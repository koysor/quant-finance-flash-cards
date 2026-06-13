# Calibration vs Time-Series Fitting

**Topic:** Fixed Income
**Tags:** calibration, time-series fitting, yield curve, model risk, arbitrage
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

**Calibration** forces a model to exactly reproduce today's observed market prices by making one or more parameters a free function of time. **Time-series fitting** estimates constant parameters from historical data to best describe how rates have evolved. The two approaches serve opposite goals: calibration prices exotics consistently with vanilla hedges; fitting hunts for relative-value mispricings.

## Key Formula

| Approach | What is matched | Typical use |
|---|---|---|
| Calibration | $Z_{\text{model}}(r,t;T) = Z_{\text{market}}(t;T)$ for all $T$ | Exotic pricing desks |
| Time-series fitting | $\min_\theta \sum_{t}(r_{t+1} - u(r_t;\theta)\Delta t)^2$ | Relative-value / arbitrage |

If you calibrate, the theoretical and market yield curves coincide by construction — there is no mismatch to exploit. If you fit from history, the mismatch between theoretical and market prices is the source of any trading signal.

## Example

A bank's rates desk calibrates Hull–White daily to the swap curve, ensuring that vanilla swaps are repriced exactly and complex structures (callable bonds, Bermudan swaptions) are priced consistently with them. A macro hedge fund fits a constant-parameter CIR model to 10 years of historical data; when the model indicates the 10-year yield is 30 bp cheap, the fund buys the bond.

## Remember

Calibration and time-series fitting are mutually exclusive signals: if you calibrate, the model cannot show mispricing because it was built to eliminate it. Knowing which mode your model is in is fundamental to interpreting its output. In practice, most sell-side trading systems calibrate; most buy-side relative-value strategies fit. Attempting to do both simultaneously leads to a category error.
