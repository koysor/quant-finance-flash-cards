# Short Selling

**Topic:** Financial Mathematics
**Tags:** short selling, borrowing, risk, hedge funds, market neutral, profit from decline
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Short selling is the practice of borrowing a security from a broker, selling it immediately at the current market price, and later buying it back (hopefully at a lower price) to return to the lender. The short seller profits if the price falls and loses if the price rises, creating an asymmetric risk profile with limited upside but theoretically unlimited downside.

## Key Formula

The **profit or loss** from a short sale is:

$$\text{P\&L} = P_{\text{sell}} - P_{\text{buy}} - C_{\text{borrow}}$$

where $P_{\text{sell}}$ is the initial sale price, $P_{\text{buy}}$ is the repurchase (cover) price, and $C_{\text{borrow}}$ is the stock borrowing cost.

The **return on a short position** as a percentage of the sale proceeds:

$$R_{\text{short}} = \frac{P_{\text{sell}} - P_{\text{buy}} - C_{\text{borrow}}}{P_{\text{sell}}}$$

## Example

A trader shorts 1,000 shares at £20 each, receiving £20,000. The annual borrow cost is 2%, and the trader covers after 6 months when the price is £17:

$$C_{\text{borrow}} = £20{,}000 \times 0.02 \times 0.5 = £200$$

$$\text{P\&L} = £20{,}000 - £17{,}000 - £200 = £2{,}800$$

$$R_{\text{short}} = \frac{£2{,}800}{£20{,}000} = 14\%$$

However, if the price had risen to £25, the loss would be £5,000 + £200 = £5,200, a $-26\%$ return — and there is no upper bound on how high the price can go.

## Remember

Short selling is the mechanism that allows hedge funds to profit from overvalued securities and construct market-neutral portfolios. It is essential for price discovery and market efficiency, but the asymmetric risk profile — maximum gain of 100% (if the stock goes to zero) versus unlimited loss — means that position sizing and stop-loss discipline are critical. In quantitative finance, understanding short selling is a prerequisite for delta hedging, pairs trading, and any long-short strategy.
