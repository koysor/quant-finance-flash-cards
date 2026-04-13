# Uncleared Margin Rules (UMR)

**Topic:** Banking Regulation
**Tags:** umr, initial margin, bilateral, uncleared derivatives, phase-in
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Uncleared Margin Rules (UMR) are the G20-mandated regulations requiring financial firms above certain notional thresholds to exchange both Variation Margin (VM) and Initial Margin (IM) on non-centrally cleared OTC derivatives. Implemented from 2016 in phases, UMR brought bilateral derivatives into the same collateral discipline as cleared derivatives, closing the regulatory gap that allowed large uncollateralised exposures to build up before 2008.

## Key Formula

The IM exchange obligation applies when both counterparties exceed the **Average Aggregate Notional Amount (AANA)** threshold in their group. Thresholds were phased in:

| Phase | Implementation | AANA threshold |
|---|---|---|
| 1 | Sep 2016 | > €3 tn |
| 2 | Sep 2017 | > €2.25 tn |
| 3 | Sep 2018 | > €1.5 tn |
| 4 | Sep 2019 | > €0.75 tn |
| 5 | Sep 2021 | > €50 bn |
| 6 | Sep 2022 | > €8 bn |

The IM is computed using either ISDA SIMM or a regulator-approved schedule (notional × flat percentage). A **€50 m threshold** per relationship applies before IM must actually be transferred.

## Example

Two asset managers, each with derivatives AANA above €8 bn, came into scope in Phase 6 (September 2022). They must now exchange IM on new bilateral trades — calculated via ISDA SIMM on their netting set sensitivities. If the SIMM IM for their IR swap portfolio is £120 m but each holds a €50 m threshold, net IM to transfer is max(£120 m − €50 m, 0) = £70 m, held with an independent custodian (segregated, non-rehypothecatable).

## Remember

The phase-in design of UMR was deliberate — starting with the largest dealers (Phase 1–4) allowed ISDA SIMM to be built, validated, and industry-tested before smaller buy-side firms were brought into scope. For Phase 5 and 6 firms (mid-sized asset managers, hedge funds), UMR created substantial operational burdens: they needed ISDA agreements, custodian arrangements, and SIMM-capable risk systems almost overnight. This drove demand for outsourced margin calculation services and reshaped how smaller firms structure bilateral derivative programmes — often choosing to clear more trades to avoid UMR compliance costs.
