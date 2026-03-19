# Risk Arbitrage

**Topic:** Derivatives
**Tags:** merger arbitrage, event-driven, deal risk, spread, probability
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Risk arbitrage** (also called *merger arbitrage*) is a trading strategy that exploits the spread between a target company's current share price and the announced acquisition offer price. Unlike riskless arbitrage, the profit is not guaranteed — it is contingent on the deal completing — so the spread compensates the trader for bearing **deal risk**.

## Key Formula

Let $K$ be the offer price per share, $S$ the target's current market price, and $S_f$ the price the stock would fall to if the deal breaks. The **merger spread** is:

$$\text{Spread} = K - S$$

The market-implied probability that the deal completes, $p^*$, is derived by setting the expected payoff to zero (the break-even condition):

$$p^*(K - S) + (1 - p^*)(S_f - S) = 0$$

Solving:

$$p^* = \frac{S - S_f}{K - S_f}$$

A higher quoted spread implies a lower market-implied deal probability.

## Example

A target trades at $S = \text{£}18$. The all-cash offer is $K = \text{£}20$. Analysts estimate $S_f = \text{£}14$ if the deal collapses.

$$p^* = \frac{18 - 14}{20 - 14} = \frac{4}{6} \approx 66.7\%$$

The spread of £2 represents a 33.3% implied probability of failure. A trader who believes the true completion probability exceeds 66.7% should buy at £18 — for every deal that closes, they earn £2; for every failure, they lose £4. If the true probability is, say, 80%, the expected payoff per share is $0.80 \times 2 + 0.20 \times (-4) = \text{£}0.80$.

## Remember

Risk arbitrage is the standard strategy of event-driven hedge funds during M&A activity. The merger spread is not free money — it is priced compensation for deal risk, including regulatory clearance failure, financing collapse, or a board rejection. Quantitative analysts model completion probability using deal characteristics (hostility, jurisdiction, size, strategic rationale) and update dynamically as news arrives. The framework is structurally identical to pricing a binary option: $p^*$ is the risk-neutral probability of the "deal closes" event, making the spread analogous to the premium on a digital call on deal completion.
