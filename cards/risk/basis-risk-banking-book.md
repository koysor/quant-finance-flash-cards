# Basis Risk (Banking Book)

**Topic:** Risk
**Tags:** basis risk, IRRBB, reference rate, hedge mismatch, SONIA, base rate
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Basis risk** in the banking book arises when the reference rates on a bank's assets and liabilities move by different amounts, even though both are nominally "floating". For example, mortgage rates may be linked to the Bank of England base rate while wholesale funding is priced off SONIA — when these rates diverge, the hedge breaks down and NII is affected. Basis risk is one of the four IRRBB sub-risks alongside repricing, yield curve, and optionality risk.

## Key Formula

The NII impact from basis risk over a period:

$$\Delta\text{NII}_{\text{basis}} = V \times (\Delta r_{\text{asset}} - \Delta r_{\text{liability}})$$

where $V$ is the notional volume of the mismatched position and $\Delta r_{\text{asset}}$, $\Delta r_{\text{liability}}$ are the rate changes on the respective reference rates.

The **basis spread** is:

$$\text{Basis} = r_{\text{asset reference}} - r_{\text{liability reference}}$$

Basis risk materialises when $\Delta\text{Basis} \ne 0$.

## Example

A bank has £8bn of tracker mortgages linked to the BoE base rate and funds them with £8bn of SONIA-linked wholesale borrowing. Currently both rates are 5.00%.

If the BoE raises the base rate by 25 bps but SONIA rises by 35 bps (due to money market dynamics):

$$\Delta\text{NII}_{\text{basis}} = 8\text{bn} \times (0.0025 - 0.0035) = 8\text{bn} \times (-0.0010) = -£8\text{m}$$

The bank loses £8m annualised because its funding cost rose more than its asset income.

## Remember

Basis risk is often called the "hidden" IRRBB risk because it is invisible to simple repricing gap or duration gap analysis — both sides reprice at the same time, so the gap is zero, yet a spread divergence still causes losses. The LIBOR-to-SOFR transition increased awareness of basis risk as banks migrated assets and liabilities to different replacement rates at different speeds. Managing basis risk requires tracking the spread between every pair of reference rates in the banking book and either accepting the exposure or hedging it with basis swaps. Basel's IRRBB standards explicitly require banks to identify and quantify basis risk as a distinct component of their interest rate risk framework.
