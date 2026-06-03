# Conversion Factor

**Topic:** Fixed Income
**Tags:** conversion factor, bond futures, invoice price, notional coupon, delivery basket, standardisation
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A conversion factor (CF) is the price per £1 nominal of a deliverable bond computed at the futures contract's notional coupon (typically 6%), used to scale invoice prices so that bonds of any coupon and maturity can compete on equal terms within the delivery basket.

## Key Formula

The conversion factor is the present value of the bond's cash flows discounted at the notional coupon rate $y_0 = 6\%$ (semi-annual: 3% per period), divided by 100:

$$CF_i = \frac{1}{100}\left[\frac{c_i}{2} \cdot \frac{1 - (1.03)^{-2n_i}}{0.03} + \frac{100}{(1.03)^{2n_i}}\right]$$

where $c_i$ is the annual coupon rate (%) and $n_i$ is years to maturity. The **invoice price** paid by the futures long on delivery is:

$$\text{Invoice price} = F \times CF_i + \text{accrued interest}_i$$

A bond with coupon exactly 6% has $CF = 1.00$; higher-coupon bonds have $CF > 1$ and lower-coupon bonds have $CF < 1$.

## Example

Two UK gilts eligible for a 10-year futures contract with $F = 112.00$. Gilt A: 4% coupon, 10 years to maturity — $CF_A = 0.8516$, invoice price $= 112.00 \times 0.8516 = \pounds 95.38$. Gilt B: 8% coupon, 10 years — $CF_B = 1.1469$, invoice price $= 112.00 \times 1.1469 = \pounds 128.45$. Without conversion factors, the short would always deliver the cheapest-priced bond; the CF system ensures both bonds are roughly equivalent in invoice value, so the short's choice depends only on residual pricing inefficiencies.

## Remember

Conversion factors would perfectly equalise all deliverable bonds only if the yield curve were flat at 6%. In reality, the yield curve slopes and levels deviate from 6%, so one bond is always marginally cheaper to deliver than the rest — the CTD. When actual yields are above 6%, low-coupon long-duration bonds tend to be CTD (CF undervalues them relative to the market); when yields are below 6%, high-coupon shorter-duration bonds become CTD. This yield-dependent CTD switching is the root cause of the delivery option embedded in bond futures.
