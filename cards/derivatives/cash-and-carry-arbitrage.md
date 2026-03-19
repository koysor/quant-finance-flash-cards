# Cash-and-Carry Arbitrage

**Topic:** Derivatives
**Tags:** arbitrage, forward pricing, futures, no-arbitrage, cost of carry, spot price
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

Cash-and-carry arbitrage is a riskless profit strategy that exploits a mispriced forward or futures contract by simultaneously buying the underlying asset in the spot market, financing the purchase at the risk-free rate, and entering a short forward position at the prevailing market price. If the market forward price exceeds the theoretical fair value, the trader locks in a guaranteed profit at expiry with no net risk.

## Key Formula

The fair (no-arbitrage) forward price for a non-dividend-paying asset is:

$$F^* = S_0 e^{rT}$$

where $S_0$ is the current spot price, $r$ is the continuously compounded risk-free rate, and $T$ is the time to expiry. If the market forward price $F > F^*$, an arbitrage profit of $F - F^*$ per unit is available at expiry.

## Example

Suppose a stock trades at $S_0 = £100$, the risk-free rate is $r = 5\%$ per annum, and a one-year forward is quoted at $F = £108$.

Fair value: $F^* = 100 \times e^{0.05 \times 1} \approx £105.13$.

Since $F = £108 > £105.13$, the trader:
1. Borrows £100 at 5% for one year and buys the stock.
2. Enters a short forward contract to sell the stock in one year at £108.

At expiry: delivers the stock at £108, repays the loan of £105.13, and pockets a riskless profit of **£2.87**.

## Remember

Cash-and-carry arbitrage is the practical mechanism that enforces the forward pricing formula $F^* = S_0 e^{rT}$ in real markets. Whenever a futures contract trades above fair value — for instance when a commodity futures price drifts above spot plus storage and financing costs — traders execute the carry trade, increasing supply of the forward and driving the price back to $F^*$. Understanding this keeps quants grounded: theoretical pricing bounds are not abstract; they are maintained by active arbitrage desks.
