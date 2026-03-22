# Margin Call

**Topic:** Short Selling
**Tags:** margin, leverage, collateral, short selling, broker, risk management
**Created:** 2026-03-16
**Author:** Claude Sonnet 4.6

---

## Definition

A margin call occurs when the value of an investor's margin account falls below the broker's required minimum maintenance margin, forcing the investor to deposit additional funds or securities — or have positions forcibly liquidated — to restore the account to the required level.

## Key Formula

The **maintenance margin requirement** triggers a call when:

$$\text{Equity} < M_{\text{maint}} \times \text{Position Value}$$

where $\text{Equity} = \text{Account Value} - \text{Loan}$ and $M_{\text{maint}}$ is the maintenance margin ratio (typically 25–30%).

The **call amount** needed to restore equity to the initial margin level $M_{\text{init}}$:

$$\text{Call Amount} = M_{\text{init}} \times \text{Position Value} - \text{Current Equity}$$

## Example

An investor buys £10,000 of shares on 50% initial margin, borrowing £5,000. Maintenance margin is 25%.

A margin call is triggered when equity falls below $0.25 \times \text{Position Value}$:

$$0.25 \times V = V - 5{,}000 \implies V = \frac{5{,}000}{0.75} \approx £6{,}667$$

So if share value drops from £10,000 to £6,667, the broker issues a margin call. To restore to 50% initial margin at this value:

$$\text{Call Amount} = 0.50 \times £6{,}667 - £1{,}667 = £1{,}667$$

## Remember

Margin calls are a critical risk amplifier in financial markets: forced liquidations during a downturn drive prices lower, triggering further margin calls in a feedback loop. For quantitative risk managers, margin requirements directly affect a strategy's maximum leverage and must be factored into position sizing — particularly for short sellers, whose potential losses are unbounded.
