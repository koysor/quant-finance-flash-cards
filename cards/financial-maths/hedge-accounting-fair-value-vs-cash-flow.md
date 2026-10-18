# Hedge Accounting: Fair Value versus Cash Flow Hedges

**Topic:** Financial Mathematics
**Tags:** hedge accounting, fair value hedge, cash flow hedge, IFRS 9, OCI, swaps
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Hedge accounting lets a bank match the accounting for a derivative with the accounting for the item it hedges, so that an economic hedge does not produce profit-and-loss volatility. The two main models used for banking-book interest rate hedges are the **fair value hedge** and the **cash flow hedge**.

## Key Formula

| | Fair value hedge | Cash flow hedge |
|---|---|---|
| Hedged risk | Change in fair value of a fixed-rate item | Variability of future floating cash flows |
| Typical position | Pay-fixed swap on fixed-rate loans or bonds | Pay-fixed swap on floating-rate funding |
| Derivative gains and losses | Profit and loss | Effective part in **other comprehensive income** (OCI), then recycled |
| Hedged item | Carrying amount adjusted for the hedged risk, through profit and loss | Not remeasured |

Net profit and loss impact is the **ineffective part**:

$$\text{P\&L impact} = \Delta FV_{\text{swap}} + \Delta FV_{\text{hedged item, hedged risk}}$$

## Example

A bank hedges £1bn of fixed-rate loans (duration 4.1) with a pay-fixed swap. Rates rise by 100 bp:

- Swap gain $\approx 1\text{bn} \times 4.1 \times 1\% = £41\text{m}$ (profit and loss).
- Loan fair value change from the hedged risk $\approx -£41\text{m}$ (profit and loss).
- Net impact $\approx 0$.

In a cash flow hedge of £1bn of floating-rate deposits, the same £41m swap gain goes to OCI and is released into profit and loss as the higher floating interest is paid.

## Remember

Hedge accounting follows the intent of the hedge, so documentation and effectiveness matter: without them the swap is carried at fair value and its swings hit earnings while the loan is at amortised cost. Banks that hedge whole portfolios of loans and deposits use macro hedging, and IFRS 9 lets them continue the older macro hedge accounting rules while a new standard is developed. The accounting choice does not change the economic exposure measured by EVE or NII.
