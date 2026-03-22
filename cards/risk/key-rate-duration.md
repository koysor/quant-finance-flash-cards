# Key Rate Duration

**Topic:** Risk
**Tags:** key rate duration, KRD, yield curve risk, DV01, duration, interest rate sensitivity
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Key rate duration (KRD)** measures the sensitivity of a bond or portfolio's price to a 1 basis point shift at a single maturity point on the yield curve, holding all other points fixed. Unlike modified duration, which assumes parallel shifts, KRD decomposes interest rate exposure across individual tenor buckets (e.g. 1y, 2y, 5y, 10y, 30y), revealing where on the curve the risk is concentrated.

## Key Formula

The key rate duration at tenor $\tau_k$:

$$\text{KRD}(\tau_k) = -\frac{1}{P} \frac{\Delta P}{\Delta r(\tau_k)}$$

where $\Delta r(\tau_k)$ is a small shift applied only at tenor $\tau_k$ (typically 1 bp), with linear interpolation to neighbouring tenors and no change elsewhere.

The sum of all key rate durations equals the effective duration:

$$D_{\text{eff}} = \sum_{k=1}^{n} \text{KRD}(\tau_k)$$

## Example

A £100m bond portfolio has the following key rate durations:

| Tenor | 2y | 5y | 10y | 30y |
|---|---|---|---|---|
| KRD | 0.8 | 2.1 | 3.5 | 1.6 |

Effective duration = 0.8 + 2.1 + 3.5 + 1.6 = **8.0 years**.

If the 10-year rate rises by 25 bps while other rates are unchanged:

$$\Delta P \approx -100\text{m} \times 3.5 \times 0.0025 = -£875{,}000$$

The KRD profile reveals that 44% of the portfolio's rate risk (3.5/8.0) sits at the 10-year point — information that a single modified duration figure of 8.0 would hide entirely.

## Remember

Key rate duration is the primary tool for managing yield curve risk. ALM desks and fixed-income portfolio managers use KRD profiles to construct hedges that neutralise exposure at specific tenors rather than relying on crude parallel-shift assumptions. For instance, a pension fund with large 30-year KRD can hedge that exposure with long-dated interest rate swaps without disturbing its short-end positioning. Basel's IRRBB framework requires banks to assess EVE sensitivity under six prescribed yield curve scenarios — flattening, steepening, and short-rate shocks — all of which produce different impacts depending on the KRD profile of the banking book.
