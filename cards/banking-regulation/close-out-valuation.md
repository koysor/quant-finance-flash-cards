# ISDA Close-Out Valuation

**Topic:** Banking Regulation
**Tags:** close-out, isda, default, valuation, replacement cost
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

ISDA close-out valuation is the process by which the non-defaulting party determines the single net payment owed after terminating all trades in a netting set following a counterparty default. It is distinct from close-out netting (which determines the *scope* of trades that are terminated and netted) — close-out valuation determines the *amount* of the resulting claim. The 2002 ISDA Master Agreement introduced the Close-Out Amount methodology, replacing the older Market Quotation and Loss methods.

## Key Formula

Under the 2002 ISDA Master Agreement, the Close-Out Amount for each terminated transaction is:

$$\text{Close-Out Amount} = \text{Replacement Cost} \pm \text{Unpaid Amounts}$$

where Replacement Cost is the cost to the non-defaulting party of entering an economically equivalent transaction in the market at the time of default. The final net sum owed is:

$$\text{Net Payment} = \sum_i \text{Close-Out Amount}_i - \text{Collateral held} + \text{Collateral posted}$$

If this is positive, the defaulting party owes; if negative, the non-defaulting party owes the residual to the defaulting party's estate. A key feature is that the non-defaulting party uses "commercially reasonable procedures" to determine value, giving it significant discretion.

## Example

Bank A defaults. Counterparty B holds a netting set with 50 swaps: 30 are in-the-money to B (worth +£40 m) and 20 are out-of-the-money (worth −£25 m). Under close-out netting, the net position is +£15 m. B's Close-Out Amount = £15 m plus any unpaid coupons. B holds £10 m of collateral from A. B's unsecured claim in A's insolvency = £15 m − £10 m = £5 m, filed as an unsecured creditor.

## Remember

The 2002 ISDA "Close-Out Amount" methodology was introduced specifically to avoid the failures of the older Market Quotation method, which required the non-defaulting party to obtain actual dealer quotes for replacement trades — practically impossible during the chaotic conditions of a major dealer default. The discretion in "commercially reasonable procedures" has been a source of litigation: in the Lehman Brothers default (2008), non-defaulting parties that calculated close-out amounts using mid-market values rather than bid/offer spreads faced legal challenges from Lehman's estate. For risk managers, close-out valuation uncertainty is an underappreciated component of CVA — the modelled exposure profile assumes orderly close-out, but in a stress scenario the actual close-out price may deviate significantly from MtM.

