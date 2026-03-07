# Triangular Arbitrage

**Topic:** Financial Mathematics
**Tags:** arbitrage, foreign exchange, cross rates, market efficiency, FX
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

**Triangular arbitrage** exploits an inconsistency among three exchange rates in the foreign exchange market. When the actual cross-rate between two currencies differs from the rate implied by their quotes against a third currency, a trader can cycle funds through all three currencies and return to the starting currency with a guaranteed profit.

## Key Formula

For three currencies with rates $S_{A/B}$ (units of $A$ per unit of $B$), the no-arbitrage condition is:

$$S_{A/B} \times S_{B/C} \times S_{C/A} = 1$$

If the product exceeds 1, an arbitrage profit exists by trading in the direction $A \to B \to C \to A$. If it is less than 1, the profitable direction is reversed.

The implied cross-rate and the arbitrage profit per unit of starting currency are:

$$S_{A/C}^{\text{implied}} = S_{A/B} \times S_{B/C}$$

$$\pi = \left|S_{A/C}^{\text{implied}} - S_{A/C}^{\text{actual}}\right|$$

## Example

Observed rates: EUR/USD $= 1.1000$, GBP/USD $= 1.3200$, EUR/GBP $= 0.8400$.

Check the no-arbitrage condition (expressing everything as "per USD"):

$$\frac{1}{1.1000} \times 1.3200 \times 0.8400 = 0.9091 \times 1.3200 \times 0.8400 = 1.0080$$

Since $1.0080 > 1$, an arbitrage exists. Starting with $\$100{,}000$:

1. Buy EUR: $100{,}000 / 1.1000 = €\,90{,}909.09$
2. Buy GBP: $90{,}909.09 \times 0.8400 = £\,76{,}363.64$
3. Sell GBP for USD: $76{,}363.64 \times 1.3200 = \$100{,}800.00$

**Riskless profit: $800.00** (0.80%, before transaction costs).

## Remember

Triangular arbitrage is the purest real-world example of riskless arbitrage in action. In modern FX markets, high-frequency trading algorithms monitor millions of cross-rate combinations and close mispricings within milliseconds, so profitable opportunities are fleeting and tiny — typically a fraction of a basis point. The no-arbitrage condition $S_{A/B} \times S_{B/C} \times S_{C/A} = 1$ is effectively enforced in real time by these algorithms, making it the FX market's version of the law of one price. For a quant, the key practical constraint is the **bid–ask spread**: the mispricing must exceed the cost of three round-trip trades to yield a genuine profit, which is why triangular arbitrage is dominated by firms with the lowest latency and tightest spread access.
