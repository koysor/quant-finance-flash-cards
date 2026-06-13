# Tenor Basis Swap

**Topic:** Fixed Income
**Tags:** tenor basis, basis swap, multi-curve, SOFR, LIBOR, floating rate, spread
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

A **tenor basis swap** exchanges two floating-rate legs of different reset frequencies on the same notional — for example, 3-month SOFR versus 6-month SOFR. Neither leg pays a fixed rate; instead, a **basis spread** is added to the shorter-tenor leg to make the swap fair. Tenor basis spreads were negligible before 2008 but widened dramatically during the financial crisis, establishing the empirical reality that forward rates of different tenors cannot be modelled on a single curve.

## Key Formula

Fair value of a tenor basis swap where leg A pays $L^{3m}$ + spread $s$ quarterly and leg B pays $L^{6m}$ semi-annually:

$$\sum_{i} \delta_i^A\,P(0,T_i^A)\!\left(F_i^{3m} + s\right) = \sum_{j} \delta_j^B\,P(0,T_j^B)\,F_j^{6m}$$

Solving for the fair basis spread:

$$s = \frac{\displaystyle\sum_j \delta_j^B\,P(0,T_j^B)\,F_j^{6m} - \sum_i \delta_i^A\,P(0,T_i^A)\,F_i^{3m}}{\displaystyle\sum_i \delta_i^A\,P(0,T_i^A)}$$

All discount factors $P(0,T)$ use the OIS (SOFR/ESTR) curve; forward rates $F^{3m}$ and $F^{6m}$ are extracted from their respective tenor-specific forward curves.

| Basis swap | Typical spread (normal) | Peak spread (2008–09 crisis) |
|---|---|---|
| USD 3m vs 6m LIBOR | 5–10 bp | 30–40 bp |
| EUR 3m vs 6m EURIBOR | 10–15 bp | 25–35 bp |
| USD 1m vs 3m SOFR | 1–3 bp | — (post-LIBOR) |

## Example

A corporate treasury has issued floating-rate debt paying 6-month SOFR. Its swap book hedges with 3-month SOFR. To close the tenor mismatch it enters a 3m/6m tenor basis swap: pay 3-month SOFR flat, receive 6-month SOFR minus 12 bp (the basis). If the market basis is 12 bp, this is fair. If 6-month rates rise relative to 3-month (basis widens to 20 bp), the treasury loses 8 bp on the basis swap but gains on its underlying exposure.

## Remember

Tenor basis swaps are the proof that the pre-2008 single-curve world was built on a convenient fiction — that all LIBOR fixings, regardless of tenor, represented the same credit exposure and could be modelled off one curve. Post-2008, 6-month LIBOR embedded more bank credit risk than 3-month LIBOR (longer unsecured exposure), and the market priced this via the tenor basis spread. The existence of non-zero basis spreads forces a **multi-curve framework**: separate forward curves for each tenor (1m, 3m, 6m), all discounted at the risk-free OIS rate. Any model that conflates these curves will systematically missprice vanilla swaps by several basis points — material in large notional books.
