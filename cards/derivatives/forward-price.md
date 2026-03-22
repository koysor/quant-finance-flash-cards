# Forward Price

**Topic:** Derivatives
**Tags:** forwards, no-arbitrage, cost of carry, risk-free rate, derivatives pricing
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **forward price** is the agreed delivery price in a forward contract such that the contract has zero value at inception. It is determined by no-arbitrage arguments: the forward price must equal the spot price grown at the cost of carry over the contract's life, otherwise a riskless profit would be available.

## Key Formula

For a non-dividend-paying asset with spot price $S_0$, risk-free rate $r$, and time to maturity $T$:

$$F_0 = S_0 \, e^{rT}$$

For an asset paying a continuous dividend yield $q$:

$$F_0 = S_0 \, e^{(r - q)T}$$

The value of an existing long forward contract with delivery price $K$ at time $t$ is:

$$V_t = S_t \, e^{-q(T-t)} - K \, e^{-r(T-t)}$$

## Example

A stock trades at $S_0 = £100$ and the continuously compounded risk-free rate is $r = 5\%$ per annum. The stock pays no dividends and the forward contract matures in one year ($T = 1$).

$$F_0 = 100 \times e^{0.05 \times 1} = 100 \times 1.05127 \approx £105.13$$

If the forward were quoted at £107, you could sell the forward, borrow £100 at 5%, buy the stock, and lock in a riskless profit of $£107 - £105.13 = £1.87$ at maturity.

## Remember

The forward price is not a forecast of where the spot price will be at maturity — it is the unique price that prevents arbitrage given today's spot price and carrying costs. In practice, deviations between quoted forwards and the theoretical cost-of-carry formula signal funding costs, repo rates, or dividend expectations that the market is pricing in. Traders use this relationship daily to identify mispricings in equity index futures, FX forwards, and commodity contracts.
