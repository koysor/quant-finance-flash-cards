# Triangular Arbitrage

**Topic:** Derivatives
**Tags:** arbitrage, foreign exchange, cross rates, no-arbitrage, currency, fx
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

Triangular arbitrage exploits inconsistent exchange rate quotes across three currencies. If the implied cross rate derived from two bilateral quotes differs from the directly quoted cross rate, a trader can cycle through all three conversions — starting and ending in the same currency — and lock in a risk-free profit. The opportunity is instantaneous and self-eliminating: arbitrageurs' trades immediately drive prices back into line.

## Key Formula

Let $S(A/B)$ denote the spot rate of currency $A$ in units of currency $B$ (i.e. one unit of $A$ buys $S(A/B)$ units of $B$). The no-arbitrage condition for three currencies $A$, $B$, $C$ is:

$$S(A/B) \times S(B/C) \times S(C/A) = 1$$

If the product exceeds 1, converting $A \to B \to C \to A$ yields a profit; if it is less than 1, the reverse cycle $A \to C \to B \to A$ is profitable. The deviation from unity measures the gross arbitrage margin before transaction costs.

## Example

Suppose the following mid-market quotes are observed:

- EUR/USD = 1.10 (1 EUR buys 1.10 USD)
- GBP/USD = 1.25 (1 GBP buys 1.25 USD)
- EUR/GBP = 0.90 (1 EUR buys 0.90 GBP)

Check the no-arbitrage condition. The implied EUR/GBP cross rate from the first two quotes is $1.10 / 1.25 = 0.88$, but the quoted rate is $0.90$. So:

$$1.10 \times (1/1.25) \times (1/0.90) = 1.10 \times 0.80 \times 1.1\overline{1} \approx 0.978 \neq 1$$

Starting with £1,000,000:

1. Buy EUR: $£1{,}000{,}000 \times 0.90 = £1{,}000{,}000$ → wait, convert using EUR/GBP: $1{,}000{,}000 \div 0.90 \approx 1{,}111{,}111$ EUR
2. Sell EUR for USD: $1{,}111{,}111 \times 1.10 \approx \$1{,}222{,}222$ USD
3. Buy GBP: $1{,}222{,}222 \div 1.25 \approx £977{,}778$

Here the cycle produces a loss, so the profitable direction is $A \to B \to C \to A$ starting with EUR. The key point is that any deviation from the parity condition creates an exploitable opportunity in one of the two directions.

## Remember

Triangular arbitrage is a cornerstone of modern FX markets: it is the mechanism by which dealers' competing quotes are continuously disciplined. In practice, the deviations that survive are tiny (often less than one pip) and vanish in milliseconds — accessible only to high-frequency traders with co-located systems. For quant finance purposes, the condition $S(A/B) \times S(B/C) \times S(C/A) = 1$ is the FX analogue of the law of one price and underpins the construction of consistent cross-rate matrices in multi-currency derivatives pricing.
