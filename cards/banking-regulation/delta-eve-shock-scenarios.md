# Prescribed Interest Rate Shock Scenarios (ΔEVE)

**Topic:** Banking Regulation
**Tags:** IRRBB, EVE, shock scenarios, parallel shift, steepener, flattener, Basel
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The Basel IRRBB standard prescribes **six interest rate shock scenarios** that every bank applies to its banking book when measuring the change in economic value of equity, $\Delta\text{EVE}$. They are designed to capture both parallel and non-parallel movements of the yield curve. The shock sizes are set per currency from historical rate moves, and were recalibrated in 2024 (effective 1 January 2026).

## Key Formula

| # | Scenario | Shape of the shock |
|---|---|---|
| 1 | Parallel up | All tenors rise by the same amount |
| 2 | Parallel down | All tenors fall by the same amount |
| 3 | Steepener | Short rates fall, long rates rise |
| 4 | Flattener | Short rates rise, long rates fall |
| 5 | Short rates up | Shock concentrated at the short end |
| 6 | Short rates down | Shock concentrated at the short end |

For each scenario $k$, discount the banking book's net cash flows $CF(t)$ (asset inflows minus liability outflows) on the base and shocked curves:

$$\Delta\text{EVE}_k = \sum_t CF(t)\,\bigl[DF_k(t) - DF_0(t)\bigr]$$

The reported exposure is the **largest loss across the six scenarios**, $\max_k\bigl(-\Delta\text{EVE}_k\bigr)$.

## Example

An illustrative bank computes $\Delta\text{EVE}$ in each scenario (£m): parallel up $-420$, parallel down $+150$, steepener $-90$, flattener $-260$, short up $-180$, short down $+60$. The worst case is parallel up, a loss of **£420m**, and that is the figure compared with the supervisory threshold.

## Remember

A single parallel shock would miss risks that only appear when the curve changes shape: a bank funding long fixed-rate assets with short deposits is hurt by rising short rates and by a flattener, which a single parallel shock would understate. The six scenarios are a coarse but common yardstick, so supervisors can compare banks on the same footing. They sit alongside, not in place of, the bank's own internal scenarios.
