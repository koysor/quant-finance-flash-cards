# Runaway Short

**Topic:** Short Selling
**Tags:** short selling, runaway short, unlimited loss, risk management, margin
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A runaway short is a short position in which the underlying security's price rises rapidly and persistently, causing mounting losses that the short seller cannot or does not close in time. Unlike a long position where the maximum loss is the amount invested, a runaway short can produce theoretically unlimited losses because there is no upper bound on a stock's price. The term emphasises the feedback dynamic: as the price rises, margin requirements increase, borrowing costs may spike, and liquidity to cover can dry up.

## Key Formula

The **unrealised loss** on an uncovered short position is:

$$L(t) = Q \times \bigl(P(t) - P_0\bigr) + C_{\text{borrow}}(t)$$

where $P_0$ is the original short sale price, $P(t)$ is the current market price, $Q$ is the number of shares, and $C_{\text{borrow}}(t)$ is the accumulated borrowing cost. Note that $L(t) \to \infty$ as $P(t) \to \infty$.

The **margin deficit** triggering a forced close is:

$$\text{Deficit} = \bigl(|V_{\text{short}}| \times m\bigr) - E(t)$$

where $m$ is the maintenance margin ratio and $E(t)$ is the trader's remaining equity.

## Example

A trader shorts 5,000 shares at £12. Over two weeks the stock rallies to £30 due to a takeover bid:

$$L = 5{,}000 \times (£30 - £12) = £90{,}000$$

The original short proceeds were £60,000, so the loss already exceeds the entire initial position value by £30,000. If the broker requires 40% maintenance margin:

$$\text{Required equity} = 5{,}000 \times £30 \times 0.40 = £60{,}000$$

The trader's equity is $£60{,}000 - £90{,}000 = -£30{,}000$. The account is deeply in deficit, and the broker will force-cover the position, likely at prices above £30 due to market impact.

## Remember

The runaway short is the worst-case scenario for any short-selling strategy and the reason that professional risk management insists on stop-loss orders, position size limits, and real-time margin monitoring. In quantitative finance, the asymmetry between long and short risk profiles — bounded loss versus unbounded loss — means that portfolio optimisation models must treat short positions differently. Standard symmetric return distributions understate the tail risk of shorts, and historical VaR can fail catastrophically during a runaway event because the loss distribution is fat-tailed and positively skewed for short positions.
