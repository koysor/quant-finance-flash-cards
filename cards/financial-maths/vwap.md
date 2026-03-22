# VWAP

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** VWAP, execution benchmark, volume weighted, trading algorithm, TCA
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The volume-weighted average price (VWAP) is the average price of a security weighted by the volume traded at each price level over a specified period (typically one trading day). It serves two purposes: as an **execution benchmark** (traders aim to execute at or better than VWAP) and as a **trading algorithm** (VWAP algorithms slice large orders into smaller pieces timed to match the historical volume profile, minimising market impact).

## Key Formula

$$\text{VWAP} = \frac{\sum_{i=1}^{n} P_i \times V_i}{\sum_{i=1}^{n} V_i}$$

where $P_i$ is the price and $V_i$ is the volume of the $i$-th trade or time interval.

The **execution quality** relative to VWAP:

$$\text{Slippage} = \frac{P_{\text{exec}} - \text{VWAP}}{\text{VWAP}} \times \text{sign}$$

where sign is $+1$ for buys (positive means overpaid) and $-1$ for sells.

## Example

A stock trades during three intervals:

| Interval | Price | Volume |
|----------|-------|--------|
| Morning | £10.00 | 500,000 |
| Midday | £10.20 | 200,000 |
| Afternoon | £9.90 | 300,000 |

$$\text{VWAP} = \frac{(£10.00 \times 500{,}000) + (£10.20 \times 200{,}000) + (£9.90 \times 300{,}000)}{500{,}000 + 200{,}000 + 300{,}000}$$

$$= \frac{£5{,}000{,}000 + £2{,}040{,}000 + £2{,}970{,}000}{1{,}000{,}000} = \frac{£10{,}010{,}000}{1{,}000{,}000} = £10.01$$

A trader who bought 50,000 shares at an average of £10.05 has slippage of:

$$\text{Slippage} = \frac{£10.05 - £10.01}{£10.01} = +0.04\% \quad (\text{4 bps overpaid})$$

## Remember

VWAP is the most widely used execution benchmark in institutional trading. A VWAP algorithm breaks a large order into slices that match the stock's typical intraday volume pattern — trading more during high-volume periods (market open and close) and less during quiet midday hours. This minimises market impact because the order "hides" within normal volume. However, VWAP is a passive benchmark — it measures whether you traded at the average market price, not whether you captured the best price. For alpha-generating strategies where speed matters, implementation shortfall (decision price) is a better benchmark. Understanding VWAP is essential for any quantitative role that involves execution.
