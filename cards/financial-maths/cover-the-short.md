# Cover the Short

**Topic:** Financial Mathematics
**Tags:** short selling, covering, buy to cover, closing position, risk management
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Covering the short (or "buying to cover") is the act of purchasing securities in the open market to return borrowed shares and close out a short position. A short seller must eventually cover to realise any profit or limit further losses. Covering can be voluntary (the trader decides the trade has played out) or forced (triggered by a margin call or a share recall by the lender).

## Key Formula

The **realised P&L** upon covering is:

$$\text{P\&L} = Q \times (P_{\text{short}} - P_{\text{cover}}) - C_{\text{borrow}}$$

where $Q$ is the number of shares, $P_{\text{short}}$ is the original sale price, $P_{\text{cover}}$ is the repurchase price, and $C_{\text{borrow}}$ is the cumulative borrowing cost.

The **break-even cover price** (ignoring commissions) is:

$$P_{\text{break\text{-}even}} = P_{\text{short}} - \frac{C_{\text{borrow}}}{Q}$$

## Example

A trader shorts 2,000 shares at £25 each. After 3 months the borrow cost totals £300. The trader covers at £21:

$$\text{P\&L} = 2{,}000 \times (£25 - £21) - £300 = £8{,}000 - £300 = £7{,}700$$

The break-even cover price was:

$$P_{\text{break\text{-}even}} = £25 - \frac{£300}{2{,}000} = £24.85$$

Any cover price below £24.85 produces a profit; above it, a loss.

## Remember

Covering is the exit mechanism for every short trade, and its timing is one of the most consequential decisions in short-selling strategies. In quantitative finance, covering dynamics drive the feedback loops behind short squeezes — when many short sellers cover simultaneously, their collective buying pressure can amplify price moves far beyond fundamental value. Risk models must account for covering costs, including market impact: liquidating a large short position in an illiquid stock can move the price significantly against the trader, making the actual cover price worse than the mark-to-market price suggested.
