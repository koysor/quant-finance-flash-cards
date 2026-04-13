# Expected Loss

**Topic:** Banking Regulation
**Tags:** expected loss, probability of default, loss given default, exposure at default, credit risk
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Expected Loss (EL) is the average credit loss a bank anticipates over a given period — the statistical mean of the credit loss distribution. It is treated as a predictable cost of lending and should be covered by loan pricing (interest margin) and accounting provisions, not by regulatory capital. Capital is reserved for the unexpected losses that exceed the mean in bad years.

## Key Formula

$$EL = PD \times LGD \times EAD$$

- $PD$ — Probability of Default: the likelihood the borrower fails to meet obligations within one year
- $LGD$ — Loss Given Default: the fraction of exposure lost after recovery proceedings (= $1 -$ recovery rate)
- $EAD$ — Exposure at Default: the amount outstanding at the time of default (including undrawn credit lines)

For a portfolio: $EL_{\text{portfolio}} = \sum_{i} PD_i \times LGD_i \times EAD_i$ (additive under independence).

## Example

A bank has a £500,000 unsecured personal loan with: $PD = 2\%$, $LGD = 60\%$, $EAD = £500{,}000$.

$$EL = 0.02 \times 0.60 \times £500{,}000 = £6{,}000$$

The bank prices this loan to recover £6,000 per year in expected credit costs (embedded in the interest margin) and sets aside a £6,000 provision under IFRS 9. No regulatory capital is charged against this £6,000 — capital covers the tail beyond EL.

## Remember

The EL = PD × LGD × EAD decomposition is the foundation of the Basel Internal Ratings-Based (IRB) approach: under Foundation IRB, banks supply their own PD estimates while the regulator provides LGD; under Advanced IRB, banks estimate all three parameters. The distinction between EL (covered by pricing and provisions) and Unexpected Loss (covered by capital) is the conceptual core of the Basel credit risk framework — confusing the two leads to either under-provisioning or over-capitalising, both of which impair a bank's returns on equity.
