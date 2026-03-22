# Transaction Cost Analysis

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** transaction cost analysis, TCA, market impact, slippage, execution quality
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Transaction cost analysis (TCA) is the measurement and decomposition of the total cost of executing a trade, beyond the explicit commission paid to the broker. The dominant component is **market impact** — the adverse price movement caused by the trade itself. TCA decomposes the gap between the decision price (when the PM decides to trade) and the final execution price into components: timing delay, market impact, spread cost, and commission. Minimising transaction costs is critical because they directly erode alpha.

## Key Formula

The **implementation shortfall** (total execution cost) is:

$$\text{IS} = \frac{P_{\text{exec}} - P_{\text{decision}}}{P_{\text{decision}}} \times \text{sign}$$

where $P_{\text{decision}}$ is the price when the trade was decided, $P_{\text{exec}}$ is the volume-weighted average execution price, and sign is $+1$ for buys, $-1$ for sells.

The **square-root market impact model** estimates permanent impact:

$$\Delta P = \sigma \times k \times \sqrt{\frac{Q}{V}}$$

where $\sigma$ is daily volatility, $Q$ is the order quantity, $V$ is average daily volume, and $k$ is a calibration constant (typically 0.5–1.5).

## Example

A PM decides to buy 200,000 shares at a decision price of £10.00. The stock has daily volatility of 2% and average daily volume of 1,000,000 shares. Using $k = 1.0$:

$$\Delta P = 0.02 \times 1.0 \times \sqrt{\frac{200{,}000}{1{,}000{,}000}} = 0.02 \times \sqrt{0.20} = 0.02 \times 0.447 = £0.0089$$

Expected market impact: £0.0089 per share, or 0.089% of the price. On 200,000 shares:

$$C_{\text{impact}} = 200{,}000 \times £0.0089 = £1{,}789$$

If the spread cost is £0.01 per share (£2,000) and commission is £500, total execution cost:

$$C_{\text{total}} = £1{,}789 + £2{,}000 + £500 = £4{,}289 \quad (0.214\% \text{ of trade value})$$

If the PM's expected alpha on this trade is only 0.30%, transaction costs consume 71% of the anticipated profit.

## Remember

Transaction costs are the silent killer of alpha in quantitative finance. The square-root impact model shows that costs scale with the square root of order size relative to volume — doubling the order does not double the impact, but trading a large fraction of daily volume becomes prohibitively expensive. This is why strategy capacity is finite: as a fund grows, market impact erodes the very alpha it is trying to capture. Effective TCA is essential for portfolio managers because it informs optimal trade scheduling (VWAP, TWAP, implementation shortfall algorithms), determines whether a signal is profitable net of costs, and provides a feedback loop to improve execution over time.
