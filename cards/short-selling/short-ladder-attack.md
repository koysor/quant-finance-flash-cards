# Short Ladder Attack

**Topic:** Short Selling
**Tags:** short ladder attack, market manipulation, short selling, wash trading, price suppression
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A short ladder attack (also called a "short and distort" ladder) is a form of market manipulation in which two or more colluding parties trade a stock back and forth between themselves at progressively lower prices. Each trade prints on the tape at a lower price than the last, creating the illusion of sustained selling pressure and encouraging genuine holders to panic-sell. The manipulators then cover their short positions at the artificially depressed price.

## Key Formula

If the colluding parties execute $n$ wash trades, each stepping the price down by $\delta$, the **artificial price decline** is:

$$\Delta P = n \times \delta$$

The **profit** from covering a short position opened at $P_0$ after the ladder drives the price to $P_0 - \Delta P$:

$$\text{Profit} = Q \times \Delta P - C_{\text{borrow}} - C_{\text{execution}}$$

where $Q$ is shares shorted, $C_{\text{borrow}}$ is the borrowing cost, and $C_{\text{execution}}$ is the cost of executing the wash trades.

## Example

Two colluding traders execute 20 wash trades on a stock priced at £5.00, each stepping the price down by £0.02:

$$\Delta P = 20 \times £0.02 = £0.40$$

The stock now shows a last-traded price of £4.60. A third conspirator who shorted 100,000 shares at £5.00 covers at £4.60:

$$\text{Profit} = 100{,}000 \times £0.40 - £200 - £500 = £40{,}000 - £700 = £39{,}300$$

The wash trades themselves may involve only small volumes (e.g. 100 shares each), but their effect on the displayed price can trigger genuine selling by retail investors watching the tape.

## Remember

Short ladder attacks exploit the fact that many market participants — and algorithmic trading systems — react to last-traded prices and volume signals without distinguishing genuine order flow from wash trades. In quantitative finance, detecting such manipulation requires analysing trade-by-trade data for patterns of matched counterparties, unusually regular price decrements, and low-volume trades that move the price disproportionately. Regulators use surveillance algorithms to flag these patterns, and exchanges can halt trading when manipulation is suspected.
