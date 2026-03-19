# Riskless Arbitrage

**Topic:** Derivatives
**Tags:** arbitrage, no-arbitrage, replication, derivatives pricing, risk-free profit
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **riskless arbitrage** is a trading strategy that simultaneously satisfies three conditions: it requires zero net investment, it cannot result in a loss under any market scenario, and it has a strictly positive probability of generating profit. In an efficient, frictionless market such opportunities are assumed not to exist — any fleeting arbitrage is eliminated almost instantly by traders exploiting it.

## Key Formula

Let $V(t)$ be the value of an arbitrage portfolio at time $t$. The three conditions that define a riskless arbitrage are:

$$V(0) = 0 \quad \text{(zero initial cost)}$$

$$\Pr\bigl(V(T) \geq 0\bigr) = 1 \quad \text{(no loss in any scenario)}$$

$$\Pr\bigl(V(T) > 0\bigr) > 0 \quad \text{(positive probability of profit)}$$

A typical arbitrage strategy exploits a price discrepancy between two equivalent portfolios. If portfolio $A$ and portfolio $B$ have identical future payoffs but different prices today, then:

$$\text{Arbitrage profit} = P_A - P_B \quad \text{(buy the cheap, sell the expensive)}$$

## Example

Suppose put-call parity is violated. A European call costs £9, a European put costs £3, the stock trades at £52, the strike is £50, $r = 4\%$, and $T = 1$ year.

Parity requires $C - P = S_0 - Ke^{-rT}$:

$$9 - 3 = 6, \qquad 52 - 50e^{-0.04} = 52 - 48.04 = 3.96$$

The left side (£6) exceeds the right side (£3.96) — the call is overpriced relative to the put. The arbitrage is:

1. **Sell** the call for £9 and **buy** the put for £3 → net receipt of £6.
2. **Buy** the stock for £52 and **borrow** £48.04 at 4% → net cost of £3.96.
3. Total upfront cash flow: $6 - 3.96 = \textbf{£2.04}$ received at $t=0$.
4. At expiry, the long stock + long put + short call exactly cancel regardless of $S_T$, leaving the £2.04 (plus interest) as riskless profit.

## Remember

The three conditions above are not just a textbook definition — they are the engine behind every derivatives pricing formula. When you price a call using the binomial model or Black-Scholes, you are implicitly finding the unique price at which no riskless arbitrage exists. If the market price deviates, a quantitative trader constructs the replicating portfolio, pockets the difference, and the market corrects. In practice, transaction costs, bid-ask spreads, and funding constraints create a narrow band around fair value within which small mispricings survive, but the idealised no-arbitrage assumption remains the bedrock of all derivatives mathematics.
