# SOFR / IBOR Transition

**Topic:** Financial Mathematics
**Tags:** sofr, libor, ibor transition, risk-free rate, ois discounting, overnight rate
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

The **IBOR transition** is the global regulatory-driven shift away from interbank offered rates (IBORs) such as LIBOR — which were based on unsecured bank borrowing and susceptible to manipulation — towards overnight risk-free rates (RFRs) such as SOFR (Secured Overnight Financing Rate) in the US and SONIA (Sterling Overnight Index Average) in the UK. LIBOR was formally discontinued for most currencies after June 2023.

## Key Formula

LIBOR was a forward-looking term rate quoted directly for each tenor. SOFR is an overnight rate; a synthetic term rate is computed by compounding daily overnight fixings over the period:

$$R_{\text{compounded}} = \left(\prod_{i=1}^{n} \left(1 + r_i \cdot \frac{d_i}{360}\right) - 1\right) \times \frac{360}{D}$$

where $r_i$ is the SOFR fixing on day $i$, $d_i$ is the number of calendar days it applies for, and $D$ is the total number of days in the period. For discounting, the OIS discount factor to maturity $T$ is:

$$P(0, T) = e^{-r_{\text{OIS}}(T) \cdot T}$$

replacing the old LIBOR-based discount factor.

## Example

A 3-month GBP interest rate swap previously referenced 3-month LIBOR, set at the start of the period (e.g. 5.20%). Under SONIA compounding, the floating rate is not known until the end of the period — it is built up daily. If SONIA averages 5.05% over 91 days, the compounded rate is approximately:

$$R \approx 5.05\% \times \frac{91}{365} \approx 1.258\%\text{ for the quarter}$$

This backward-looking structure means counterparties cannot hedge their floating payment in advance, requiring new conventions (payment delays, lookback periods) in swap documentation.

## Remember

The transition from LIBOR to SOFR/SONIA changed fixed income and derivatives markets in two critical ways. First, **discounting**: all collateralised derivatives are now discounted on OIS curves (overnight RFR) rather than LIBOR curves, repricing every outstanding derivative book — the "big bang" discounting switch by LCH and CME in 2020 moved trillions of dollars of swaps. Second, **fallback language**: legacy LIBOR contracts needed legally binding fallback rates (RFR + a credit adjustment spread) to handle cessation. The credit adjustment spread compensates for the fact that SOFR (secured, near-risk-free) is structurally lower than LIBOR (unsecured, credit-inclusive) by roughly 26 bps for 3-month USD LIBOR.
