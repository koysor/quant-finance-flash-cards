# Co-terminal Swaption Matrix

**Topic:** Fixed Income
**Tags:** swaption, co-terminal, volatility matrix, calibration, Bermudan swaption, implied vol
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **swaption volatility matrix** (or swaption cube) quotes European swaption implied volatilities by expiry and underlying swap tenor. **Co-terminal swaptions** are those whose expiry and tenor sum to a fixed final maturity — for a 10-year Bermudan, the co-terminal set is $\{1y\!\times\!9y,\;2y\!\times\!8y,\;\ldots,\;9y\!\times\!1y\}$. These are the instruments that a short-rate model must price correctly to guarantee a well-calibrated Bermudan swaption exercise boundary.

## Key Formula

A swaption matrix entry $\sigma(T_{\text{exp}}, T_{\text{tenor}})$ is the Black or normal implied vol for a European swaption with expiry $T_{\text{exp}}$ and tenor $T_{\text{tenor}}$. The co-terminal constraint fixes the final date:

$$T_{\text{exp}} + T_{\text{tenor}} = T_N \quad \text{(constant)}$$

Abbreviated example for a $T_N = 10$ yr structure (Black vols, %):

| Expiry \ Tenor | 1y | 2y | 3y | 5y | 7y | 9y |
|---|---|---|---|---|---|---|
| **1y** | 28 | 26 | 24 | 21 | 19 | **18** |
| **2y** | 26 | 24 | 22 | 20 | **18** | — |
| **3y** | 24 | 22 | 20 | **18** | — | — |
| **5y** | 21 | 19 | **17** | — | — | — |
| **9y** | **16** | — | — | — | — | — |

Bold entries on the anti-diagonal are the co-terminal swaptions for $T_N = 10$ yr. Calibration of BK or HW to these 9 prices gives a model that prices the Bermudan exactly.

## Example

A callable 10-year bond, callable annually after year 1, is equivalent to a bullet bond minus a Bermudan payer swaption with exercise dates at years 1–9. Calibrating Hull-White to the nine co-terminal swaption vols (bold above) ensures the model correctly reflects the market's view of the exercise value at each date. Failing to match the $1y\!\times\!9y$ vol would missprice the very first exercise opportunity — where early exercise is most likely if rates rise sharply shortly after issuance.

## Remember

The co-terminal diagonal is the minimal calibration set for any Bermudan swaption: these are exactly the European options embedded in the Bermudan structure. A model calibrated only to the cap/floor strip (along the first row of the matrix) fits the term structure of short-rate volatility but ignores the correlation between rates at different maturities — which is what the co-terminal vols encode. In practice, the swaption matrix is quoted in both **Black vol** (for higher-rate environments) and **normal vol** (basis points of rate, preferred post-2015 when negative rates broke Black's lognormal assumption). Converting between the two requires care near zero strike.
