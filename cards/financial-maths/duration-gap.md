# Duration Gap

**Topic:** Financial Mathematics
**Tags:** duration gap, ALM, IRRBB, modified duration, EVE, interest rate risk
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **duration gap** measures the mismatch between the interest-rate sensitivity of a bank's assets and liabilities. It is the weighted difference between the modified duration of assets and the modified duration of liabilities, adjusted for the leverage ratio. A positive duration gap means the bank's assets are more rate-sensitive than its liabilities, so rising rates reduce the bank's economic value of equity (EVE).

## Key Formula

$$\text{Duration Gap} = D_A - \frac{PV_L}{PV_A} \times D_L$$

where $D_A$ and $D_L$ are the modified durations of assets and liabilities, and $PV_A$, $PV_L$ are their present values.

The approximate change in EVE for a parallel rate shift $\Delta r$:

$$\Delta\text{EVE} \approx -\text{Duration Gap} \times PV_A \times \Delta r$$

| Duration Gap | Rates rise | Rates fall |
|---|---|---|
| Positive ($D_A > \frac{PV_L}{PV_A} D_L$) | EVE falls | EVE rises |
| Zero (immunised) | EVE unchanged | EVE unchanged |
| Negative ($D_A < \frac{PV_L}{PV_A} D_L$) | EVE rises | EVE falls |

## Example

A bank has:
- Assets: $PV_A = £15\text{bn}$, $D_A = 5.0$ years
- Liabilities: $PV_L = £13.5\text{bn}$, $D_L = 1.5$ years

$$\text{Duration Gap} = 5.0 - \frac{13.5}{15.0} \times 1.5 = 5.0 - 1.35 = 3.65 \text{ years}$$

If rates rise by 150 bps:

$$\Delta\text{EVE} \approx -3.65 \times 15\text{bn} \times 0.015 = -£821\text{m}$$

The bank's equity value falls by approximately £821m.

## Remember

The duration gap is the single most important number in a bank's ALM toolkit — it summarises the entire balance sheet's rate sensitivity in one figure. A typical commercial bank has a positive duration gap of 3–5 years because it lends long (mortgages, corporate loans) and borrows short (deposits, overnight funding). ALM teams manage the gap by entering interest rate swaps: receiving fixed in a swap increases liability duration, narrowing the gap. Complete immunisation (gap = zero) is rarely the target, because some duration mismatch is a deliberate source of profit — the bank earns the term premium. The Basel IRRBB framework effectively regulates how large this gap can be relative to capital.
