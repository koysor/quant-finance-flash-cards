# Spot Price

**Topic:** Derivatives
**Tags:** spot price, market price, immediate delivery, cost of carry, forwards, futures
**Author:** Claude Opus 4.6

---

## Definition

The **spot price** (or cash price) is the current market price at which an asset can be bought or sold for immediate delivery and settlement. It reflects the real-time supply and demand balance in the cash market and serves as the reference point from which all derivative prices — forwards, futures, and options — are derived.

## Key Formula

The relationship between the spot price and the forward price for a non-dividend-paying asset is given by the cost-of-carry model:

$$F_0 = S_0 \, e^{rT}$$

Rearranging to express the spot price implied by an observed forward price:

$$S_0 = F_0 \, e^{-rT}$$

where $S_0$ is the current spot price, $F_0$ is the forward price, $r$ is the continuously compounded risk-free rate, and $T$ is the time to maturity in years.

## Example

Gold trades at a spot price of $S_0 = £1{,}500$ per ounce. The risk-free rate is $r = 4\%$ per annum. A dealer quotes a six-month forward at $F = £1{,}545$.

The theoretical forward price is:

$$F^* = 1{,}500 \times e^{0.04 \times 0.5} = 1{,}500 \times 1.02020 \approx £1{,}530.30$$

Since the quoted forward ($£1{,}545$) exceeds fair value ($£1{,}530.30$), the forward is overpriced relative to the spot, signalling a potential cash-and-carry arbitrage opportunity worth approximately $£1{,}545 - £1{,}530.30 = £14.70$ per ounce.

## Remember

The spot price is the anchor of all derivative pricing. Every no-arbitrage relationship — put-call parity, the cost-of-carry formula, Black-Scholes — takes the spot price as an input. In practice, traders watch the **basis** (the difference $F - S$) to gauge whether futures are trading rich or cheap relative to the cash market. A widening basis can signal changes in funding costs, storage constraints, or dividend expectations, making the spot-forward relationship a daily monitoring tool on any derivatives desk.
