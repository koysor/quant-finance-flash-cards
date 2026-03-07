# Short Squeeze

**Topic:** Financial Mathematics
**Tags:** short squeeze, short selling, feedback loop, short interest, forced buying
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A short squeeze occurs when a heavily shorted stock's price rises sharply, forcing short sellers to buy back shares to cover their positions or meet margin calls. This forced buying creates additional upward pressure on the price, triggering a self-reinforcing feedback loop that can drive the stock far above its fundamental value.

## Key Formula

The **short interest ratio** (days to cover) measures squeeze vulnerability:

$$\text{Days to Cover} = \frac{\text{Shares Sold Short}}{\text{Average Daily Volume}}$$

The **loss on a short position** as the price rises from $P_0$ to $P_1$:

$$\text{Loss} = Q \times (P_1 - P_0) + C_{\text{borrow}}$$

where $Q$ is the number of shares shorted. Unlike a long position, there is **no upper bound** on this loss since $P_1$ can rise without limit.

## Example

A stock trades at £10 with 5 million shares sold short and average daily volume of 1 million shares:

$$\text{Days to Cover} = \frac{5{,}000{,}000}{1{,}000{,}000} = 5 \text{ days}$$

If the price jumps to £18, a short seller who sold 100,000 shares faces:

$$\text{Loss} = 100{,}000 \times (£18 - £10) = £800{,}000$$

With a maintenance margin of 30%, the margin call triggers when equity falls below 30% of position value. At £18 the position value is £1,800,000, requiring equity of £540,000 — but the trader's equity has dropped by £800,000. The broker forces a buy-back, pushing the price even higher.

## Remember

Short squeezes are a critical risk in quantitative strategies that involve short positions. The GameStop episode of January 2021 demonstrated that a days-to-cover ratio above 5, combined with coordinated buying, can produce price increases of 10x or more in days. Risk models must account for the **nonlinear feedback** between price, margin, and forced covering — standard VaR models assume positions can be unwound at market prices, but during a squeeze, liquidity evaporates and the cost of covering can far exceed the model's worst-case estimate. Monitoring short interest ratios is therefore essential for any fund running short positions.
