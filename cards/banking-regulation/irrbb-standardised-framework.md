# IRRBB Standardised Framework

**Topic:** Banking Regulation
**Tags:** IRRBB, standardised framework, cash flow slotting, non-maturity deposits, behavioural assumptions, Basel
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The **IRRBB standardised framework** is the common method in the Basel standard for measuring $\Delta\text{EVE}$, which banks may adopt and supervisors may require. Instead of each bank's own models, it standardises the maturity schedule, the shock scenarios and the treatment of the main behavioural positions, so results are comparable across banks.

## Key Formula

Each banking-book position is converted into cash flows and **slotted into time buckets** by repricing date:

$$\text{EVE} = \sum_{b} CF_b \cdot DF(t_b)$$

where $t_b$ is the midpoint of bucket $b$. Positions without a contractual date are given behavioural cash flows:

| Position | Treatment |
|---|---|
| Fixed-rate loans and bonds | Slotted at the contractual cash flow dates (adjusted for prepayments where relevant) |
| Floating-rate items | Slotted at the next repricing date |
| Non-maturity deposits | Split into **core** (stable) and **non-core**; non-core goes in the overnight bucket, core is spread out to a capped average maturity |
| Retail versus wholesale | Separated, because their stability differs |

## Example

An illustrative bank holds £10bn of retail savings. Suppose the core share is estimated at 60%. Then £4bn (non-core) is slotted overnight, while £6bn (core) is spread across buckets out to a maximum average maturity of around five years. Treating all £10bn as overnight would show no interest rate risk on the liability side; the slotting recognises that £6bn behaves like multi-year funding.

## Remember

Behavioural assumptions are the largest source of judgement in IRRBB: the core share and average maturity of deposits can move the measured $\Delta\text{EVE}$ by hundreds of millions. The standardised caps stop banks from claiming implausibly long deposit lives to flatter their exposure, which is why supervisors scrutinise any internal estimate that exceeds them.
