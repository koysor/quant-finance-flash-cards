# CLO (Collateralised Loan Obligation)

**Topic:** Risk
**Tags:** CLO, collateralised loan obligation, leveraged loans, structured credit, tranching, OC test
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A Collateralised Loan Obligation (CLO) is an actively managed structured vehicle that pools corporate leveraged loans and issues tranches (AAA to equity) backed by the loan cash flows; structural protections redirect cash away from junior tranches if credit quality deteriorates.

## Key Formula

**Overcollateralisation (OC) test:**

$$\text{OC ratio} = \frac{\text{Par value of assets}}{\text{Par value of liabilities (by tranche)}} > \text{OC threshold}$$

**Interest coverage (IC) test:**

$$\text{IC ratio} = \frac{\text{Interest income from loans}}{\text{Interest due on liabilities}} > \text{IC threshold}$$

If either test fails, cash is diverted from junior to senior tranches (a "diversion" trigger).

## Example

\$500m CLO: 64% AAA notes (\$320m at SOFR+140bps), 12% AA, 7% A, 5% BBB, 3% BB, 9% equity. If OC test for the BBB tranche fails, interest that would otherwise pay equity holders is instead used to pay down AAA notes — protecting senior investors.

## Remember

Unlike a static CDO, a CLO manager actively buys and sells loans within defined reinvestment guidelines during the reinvestment period (typically 4–5 years). This means CLO credit quality depends on manager skill as well as pool construction — hence OC and IC tests act as automatic deleveraging triggers, enforcing discipline when the portfolio deteriorates.
