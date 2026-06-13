# Collateralised Mortgage Obligation (CMO)

**Topic:** Fixed Income
**Tags:** CMO, collateralised mortgage obligation, MBS, tranching, PAC tranche, sequential pay, prepayment
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A Collateralised Mortgage Obligation (CMO) restructures mortgage pass-through cash flows into tranches with different prepayment exposure; senior tranches (e.g. PAC bonds) receive stable scheduled cash flows, while support tranches absorb prepayment variability.

## Key Formula

**Sequential-pay structure:** principal paid to Tranche A until exhausted, then B, then C.

**PAC (Planned Amortisation Class) bond:** receives scheduled principal $P_t$ if actual prepayments stay within a collar $[\text{PSA}_{\min}, \text{PSA}_{\max}]$:

$$P_t^{\text{PAC}} = \min\bigl(P_t^{\text{PSA}_{\min}},\; P_t^{\text{PSA}_{\max}}\bigr)$$

Support (companion) tranches receive residual principal — their cash flows vary enormously with prepayment speed.

## Example

\$300m CMO backed by 30yr $6\%$ MBSs. Tranche A: \$100m, receives all principal until paid off (2–3yr average life, low prepayment risk). Tranche C: \$100m, last to receive principal (10–12yr average life, higher prepayment risk). Support tranche: absorbs prepayment swings so PAC A receives stable cash flows within 100–300% PSA.

## Remember

CMOs were invented in 1983 to create mortgage instruments with bond-like predictable cash flows — PAC tranches appealed to insurance companies and pension funds needing stable durations. The trade-off is that support tranches bear extreme prepayment convexity: in the 1994 rate rise, support tranche durations extended dramatically, causing large mark-to-market losses for holders who had not appreciated the embedded optionality.
