# Theoretical vs Market Yield Curve

**Topic:** Fixed Income
**Tags:** yield curve, calibration, model risk, arbitrage, mispricing, relative value
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **theoretical yield curve** is the set of zero-coupon bond prices (or yields) implied by a model with fixed parameters. The **market yield curve** is what actually trades. A mismatch between the two is either a problem to fix (for pricing desks) or an opportunity to exploit (for relative-value traders).

## Key Formula

For a model with constant parameters producing yield $Y_{\text{model}}(T)$ at each maturity $T$:

$$\text{Mismatch}(T) = Y_{\text{market}}(T) - Y_{\text{model}}(T)$$

If calibration is applied by making $\eta \to \eta(t)$, the mismatch is forced to zero for all $T$ simultaneously. If the model is time-series fitted, the mismatch represents the model's view of relative richness/cheapness.

| Scenario | Mismatch | Interpretation |
|---|---|---|
| Exotic pricing desk | Bad — fix via calibration | Inconsistent with vanilla hedges |
| Relative-value fund | Good — signals opportunity | Basis for trade entry |

## Example

A constant-parameter Vasicek model fit to 2010–2020 data implies a 10-year yield of 2.8% in June 2021. The market 10-year yield is 1.5%. The 130 bp mismatch is not a bug for a relative-value trader; it suggests 10-year rates are rich and the fund should position for higher yields. For an exotic desk, the same 130 bp gap means that any option priced with this model will be inconsistent with market swap prices.

## Remember

The yield curve mismatch is a single number with radically different interpretations depending on the user's objective. The key question is whether you are trying to price risk relative to the market (calibrate) or find where the market has deviated from fair value (fit). Confusing the two — using a calibrated model to claim mispricing — is a common source of false trading signals.
