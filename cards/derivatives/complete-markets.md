# Complete Markets

**Topic:** Derivatives
**Tags:** complete market, replication, binomial model, no-arbitrage, hedging, incomplete market
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

A financial market is **complete** if every contingent claim (i.e. every possible payoff that depends on future states of the world) can be perfectly **replicated** by trading the available instruments. "Replicated" means we can construct a portfolio whose value at expiry matches the claim's payoff in every possible state, with zero residual risk.

Completeness requires that the number of linearly independent tradeable instruments equals the number of possible future states. When this condition holds, there is exactly **one** price for every derivative — the cost of building its replicating portfolio — and every risk can be hedged away entirely.

If the market is **incomplete** (more states than independent instruments), perfect replication is impossible. Multiple no-arbitrage prices then exist, and hedging leaves residual risk that cannot be eliminated.

## Key Formula

In a single-period model with $N$ future states and $M$ tradeable assets (including a risk-free bond), the market is complete if and only if the **payoff matrix** $D$ has full row rank:

$$\text{rank}(D) = N$$

where $D$ is the $N \times M$ matrix whose entry $D_{ij}$ is the payoff of asset $j$ in state $i$.

For the **binomial model** ($N = 2$ states: up and down), two instruments (stock + bond) give $M = 2$. The payoff matrix is:

$$D = \begin{pmatrix} S_u & e^{r\Delta t} \\ S_d & e^{r\Delta t} \end{pmatrix}$$

Since $S_u \neq S_d$, the rows are linearly independent, so $\text{rank}(D) = 2 = N$ and the market is complete. This guarantees a **unique** risk-neutral probability $q$.

## Example

Consider a one-period binomial tree. A stock is priced at £100 today and moves to either £120 (up) or £90 (down). The risk-free rate is $r = 5\%$ per period.

We want to replicate a call option with strike $K = £105$. The call pays £15 in the up state and £0 in the down state. We hold $\Delta$ shares and £$B$ in the bond:

$$\Delta \times 120 + B \times 1.05 = 15$$
$$\Delta \times 90 + B \times 1.05 = 0$$

Subtracting: $30\Delta = 15$, so $\Delta = 0.5$. Back-substituting: $B = \frac{0 - 0.5 \times 90}{1.05} = -42.86$.

The unique no-arbitrage price of the call is:

$$C = 0.5 \times 100 + (-42.86) = \textbf{£7.14}$$

Because the market is complete, this is the **only** price consistent with no-arbitrage. Any other price creates a riskless profit opportunity.

## Remember

- The Black-Scholes model assumes a complete market: continuous trading in the stock and a risk-free bond is sufficient to replicate any European payoff, which is why it produces a single, unique price.
- Completeness is the reason **delta hedging** works perfectly in theory — the replicating portfolio *is* the hedge.
- Real markets are incomplete: jumps, stochastic volatility, and transaction costs all introduce states that cannot be spanned by the available instruments, leading to bid-ask spreads and model-dependent prices.
- In the CQF framework, completeness connects directly to the **Fundamental Theorem of Asset Pricing**: no-arbitrage implies at least one risk-neutral measure exists; completeness implies that measure is **unique**.
