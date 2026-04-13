# Close-out Netting

**Topic:** Banking Regulation
**Tags:** netting, isda, counterparty risk, exposure, credit risk
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Close-out netting is a contractual mechanism — enshrined in the ISDA Master Agreement — that, upon a counterparty's default, terminates all outstanding transactions simultaneously, marks each to market, and nets the resulting values into a single payment obligation. It replaces a gross web of individual claims with one net figure, dramatically reducing both credit exposure and systemic risk.

## Key Formula

Without netting, the exposure is the sum of all positive values (gross exposure):

$$\text{Gross Exposure} = \sum_{i:\, V_i > 0} V_i$$

With close-out netting, exposure is the net value across all trades (floored at zero):

$$\text{Net Exposure} = \max\!\left(\sum_i V_i,\; 0\right)$$

The **netting ratio** measures the capital efficiency gained:

$$\text{Netting Ratio} = \frac{\text{Net Exposure}}{\text{Gross Exposure}} < 1$$

A netting ratio of 0.2 means capital is calculated on 20% of the gross mark-to-market.

## Example

Bank A has five trades with Counterparty B: values +£80 m, +£40 m, −£60 m, −£30 m, +£20 m.

- Gross exposure (what must be collateralised without netting): £80 m + £40 m + £20 m = **£140 m**
- Net exposure (with netting): £80 + £40 − £60 − £30 + £20 = **£50 m**

Capital requirement falls to 36% of the unnetteed figure — a capital saving of £90 m in exposure terms.

## Remember

Close-out netting is only legally effective where it is recognised in the relevant jurisdiction — in some emerging-market jurisdictions, insolvency courts have attempted to "cherry-pick" trades (keeping only losing ones to sue on), which would destroy the netting benefit. This is why ISDA invests heavily in legal opinions across 70+ jurisdictions: a single jurisdiction where netting is unenforceable can expose a dealer to gross rather than net exposure on their entire book with counterparties in that country, materially understating their regulatory capital requirement.
