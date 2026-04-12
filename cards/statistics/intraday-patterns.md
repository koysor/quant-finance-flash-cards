# Intraday Patterns — The U-Shape

**Topic:** Statistics
**Tags:** intraday, market microstructure, bid-ask spread, volatility, vwap, execution
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Intraday trading activity and volatility follow a **U-shaped pattern** across the trading day:

- **Open (high activity):** overnight news and order imbalances are resolved; informed traders act on accumulated information, widening bid-ask spreads and spiking volume.
- **Mid-session (low activity):** informed and liquidity traders reach equilibrium; spreads narrow and volatility falls to its daily minimum.
- **Close (high activity):** portfolio rebalancing, end-of-day hedging, index-linked orders, and marking-to-market drive a second surge in volume and volatility.

At **tick frequency**, prices oscillate between the bid and ask, producing negative autocorrelation in returns — the **bid-ask bounce**. This is not a violation of the Efficient Market Hypothesis; it vanishes at coarser sampling intervals (e.g. 5-minute returns).

## Key Formula

**Bid-ask bounce** — negative autocorrelation at lag 1 for tick-level returns:

$$r_{t+1} \approx -r_t$$

equivalently, the lag-1 autocorrelation satisfies:

$$\rho_1 = \frac{\text{Cov}(r_t, r_{t-1})}{\text{Var}(r_t)} \approx -\frac{s^2/4}{\sigma^2 + s^2/4}$$

where $s$ is the bid-ask spread and $\sigma^2$ is the variance of the efficient price innovation (Roll's model). A wider spread $s$ drives $\rho_1$ more negative.

**Volume-Weighted Average Price (VWAP):**

$$\text{VWAP} = \frac{\sum_{i=1}^{N} p_i \cdot v_i}{\sum_{i=1}^{N} v_i}$$

where $p_i$ is the transaction price and $v_i$ is the volume at trade $i$ over the period. VWAP is the standard benchmark for execution quality; a buy order that achieves a price below VWAP has outperformed the market average.

## Example

SPY minute data (2011) illustrates the U-shape:

| Period | Bid-ask spread | Realised vol | Volume |
|---|---|---|---|
| First 30 min | Widest | Highest | Highest |
| Mid-session | Narrowest | Lowest | Lowest |
| Last 30 min | Wide | High | High |

A trader executing a large buy order at 9:35 faces wide spreads and high market impact. The same order executed at 12:30 achieves tighter spreads and lower slippage. A VWAP algorithm distributes the order across the day in proportion to the expected volume profile — typically heavier at open and close — to match the benchmark rather than fight it.

## Remember

The U-shape directly governs **transaction cost analysis (TCA)**: execution at open or close costs more because market impact and bid-ask spreads are both elevated. VWAP strategies spread orders across the U-shaped volume profile to minimise slippage. Intraday risk models must not assume constant volatility — a model calibrated on mid-session data will understate open and close risk. The bid-ask bounce ($\rho_1 < 0$ at tick level) must not be mistaken for a predictable return pattern; it disappears at any reasonable sampling frequency and cannot be profitably exploited after transaction costs.
