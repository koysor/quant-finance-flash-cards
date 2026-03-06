# Delta (Greeks)

**Topic:** Derivatives
**Tags:** delta, Greeks, sensitivity, options, hedging, Black-Scholes
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Delta** ($\Delta$) is the first-order Greek that measures the rate of change of an option's price with respect to a small change in the underlying asset price. Formally, $\Delta = \partial V / \partial S$. It represents both the instantaneous hedge ratio and an approximate probability that the option expires in the money under the risk-neutral measure.

## Key Formula

For European options under Black-Scholes:

$$\Delta_{\text{call}} = N(d_1), \qquad \Delta_{\text{put}} = N(d_1) - 1$$

where

$$d_1 = \frac{\ln(S / K) + \left(r + \tfrac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}$$

and $N(\cdot)$ is the cumulative standard normal distribution function.

Key properties:

- Call delta ranges from $0$ to $+1$; put delta ranges from $-1$ to $0$.
- At-the-money forward options have $\Delta \approx \pm\,0.50$.
- Deep in-the-money calls approach $\Delta = 1$ (behave like the stock); deep out-of-the-money calls approach $\Delta = 0$.
- Put-call parity requires $\Delta_{\text{call}} - \Delta_{\text{put}} = 1$.

## Example

A European call has $S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 0.5$ years.

$$d_1 = \frac{\ln(1) + (0.05 + 0.02)(0.5)}{0.20\sqrt{0.5}} = \frac{0.035}{0.1414} = 0.2475$$

$$\Delta_{\text{call}} = N(0.2475) \approx 0.5977$$

If the stock rises by £1, the call price increases by approximately £0.60. The corresponding put delta is $0.5977 - 1 = -0.4023$, so the put loses about £0.40 for the same £1 rise.

## Remember

Delta is the single most important Greek for day-to-day risk management. Traders speak of being "long 500 delta" to mean their portfolio behaves as though they hold 500 shares. A delta-neutral book has zero first-order exposure to the underlying, but it is still exposed to **gamma** (how delta itself changes) and **theta** (time decay). Because delta shifts as the stock moves, hedges must be rebalanced — and the cost of that rebalancing is governed by gamma and realised volatility.
