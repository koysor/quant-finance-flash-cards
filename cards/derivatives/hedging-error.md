# Hedging Error

**Topic:** Derivatives
**Tags:** hedging error, discrete hedging, gamma, rebalancing, transaction costs, P&L variance
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Hedging error is the difference between the actual P&L of a delta-hedged option position and the theoretical P&L predicted by the Black–Scholes model with continuous rebalancing. In theory, a continuously rebalanced delta hedge perfectly replicates the option, leaving zero residual risk. In practice, hedges are rebalanced at discrete intervals (hourly, daily), and each interval accumulates a small P&L error that depends on how far the underlying moves between rebalances. The aggregate hedging error over the option's life determines the actual cost of hedging versus the theoretical cost.

## Key Formula

The hedging error from a single discrete rebalance interval of length $\Delta t$:

$$\epsilon = \frac{1}{2}\,\Gamma\,S^2\left[(\Delta S / S)^2 - \sigma^2 \Delta t\right]$$

The first term is the squared realised return; the second is the expected squared return under the model. For $n$ rebalances over the option life, the **variance of the total hedging error** is approximately:

$$\text{Var}(\text{HE}) \approx \frac{1}{2}\,\sigma^4 \sum_{i=1}^{n} \Gamma_i^2 S_i^4 (\Delta t_i)^2 \times 2$$

The standard deviation of the hedging error scales as:

$$\text{std}(\text{HE}) \propto \frac{\sigma^2}{\sqrt{n}}$$

Doubling the rebalancing frequency reduces the hedging error standard deviation by $\sqrt{2}$.

## Example

A trader delta-hedges a short ATM call on a £100 stock ($\Gamma = 0.03$, $\sigma = 20\%$) and rebalances daily ($\Delta t = 1/252$). The expected daily move is $\sigma\sqrt{\Delta t} = 0.20/\sqrt{252} = 1.26\%$, or £1.26.

On one day, the stock moves £3.00 (a 3% move). The hedging error for that interval:

$$\epsilon = \frac{1}{2} \times 0.03 \times 100^2 \times \left[(0.03)^2 - (0.20)^2/252\right]$$

$$= 150 \times [0.0009 - 0.000159] = 150 \times 0.000741 = £0.111$$

The large move produced a positive hedging error (the short gamma position lost more than theta compensated for). Over a month of 22 trading days, such errors accumulate stochastically. If the trader rebalanced every hour instead (roughly 7 times per day), the standard deviation would fall by $\sqrt{7} \approx 2.6$ times.

## Remember

Hedging error is the bridge between the elegant theory of Black–Scholes and the messy reality of derivatives trading. The theoretical framework assumes continuous rebalancing at zero cost, but every real hedge is discrete and incurs transaction costs. This creates a fundamental trade-off: rebalancing more frequently reduces hedging error but increases transaction costs, while rebalancing less frequently saves on costs but increases P&L volatility. For options market-makers, managing this trade-off is a core skill — the choice of rebalancing frequency and trigger (time-based vs delta-threshold) directly affects profitability. The hedging error formula also shows why gamma is so important operationally: high-gamma positions (near-the-money, near-expiry options) produce the largest hedging errors and require the most frequent attention.
