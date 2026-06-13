# Degrees of Freedom in Yield-Curve Calibration

**Topic:** Fixed Income
**Tags:** calibration, degrees of freedom, time-dependent parameters, yield curve, infinite dimensions
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

A yield curve is a continuous function of maturity, representing infinitely many observable prices. A model with only finitely many constant parameters can match at most finitely many maturities. **Making a parameter a free function of time** creates an infinite-dimensional parameter space — one free value per instant — providing enough flexibility to match the entire curve simultaneously.

## Key Formula

| Model | Free parameters | Curve maturities matched |
|---|---|---|
| Vasicek ($\eta, \gamma, c$ constant) | 3 | At most 3 |
| Ho–Lee ($\eta(t)$ free function) | $\infty$ (one per $t$) | All |
| Hull–White ($\eta(t)$ free, $\gamma, c$ fixed) | $\infty$ | All |

The **calibration formula** for Ho–Lee sets a constraint on $\eta^*$ at each maturity:

$$\eta^*(T) = c^2(T - t^*) - \frac{\partial^2}{\partial T^2}\log Z_M(t^*;T)$$

Each maturity $T$ provides one equation; the free function $\eta^*(t)$ provides one free value per $t$ — the system is exactly determined.

## Example

A flat yield curve at 4% can be matched by constant $\eta = 0.04$ in Vasicek. But the actual UK gilt curve on any given day has a specific shape with, say, 20 quoted maturities. A constant-parameter Vasicek model can minimise pricing error across those 20 maturities but cannot match all of them exactly. Ho–Lee with a piecewise-linear $\eta(t)$ — one free parameter per maturity bucket — can match all 20 exactly.

## Remember

The shift from finite to infinite degrees of freedom is what separates **statistical models** (Vasicek, CIR — a few parameters that might be stable over time) from **calibration models** (Ho–Lee, Hull–White — a free function that changes daily). More degrees of freedom always improve today's fit but at the cost of **overfit**: the daily-recalibrated $\eta(t)$ absorbs market noise as well as signal, leading to parameter instability and unreliable sensitivities (Greeks).
