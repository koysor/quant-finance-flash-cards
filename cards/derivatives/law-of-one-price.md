# Law of One Price

**Topic:** Derivatives
**Tags:** arbitrage, replication, no-arbitrage, pricing, derivatives, portfolio
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Law of One Price states that if two portfolios produce identical payoffs in every possible future state of the world, they must have the same price today in an arbitrage-free market.

Formally: if $V_A(T) = V_B(T)$ almost surely, then $V_A(0) = V_B(0)$.

If the prices differ, a riskless profit can be obtained by buying the cheaper portfolio and short-selling the more expensive one — a strategy that earns a guaranteed positive return with zero net investment.

## Key Formula

$$V_A(T) = V_B(T) \; \text{a.s.} \implies V_A(0) = V_B(0)$$

Equivalently, if $V_A(T) = V_B(T)$ almost surely and $V_A(0) < V_B(0)$, then the arbitrage profit today is:

$$\pi = V_B(0) - V_A(0) > 0$$

by selling $B$ and buying $A$, with zero net payoff at time $T$.

## Example

Consider a European call option $C$ and a replicating portfolio $\Delta S + B$ (holding $\Delta$ units of stock $S$ and cash $B$). If both are constructed so that their values agree at expiry in every state:

$$C(T) = \Delta S(T) + B(T) \quad \text{in all states}$$

then by the Law of One Price:

$$C(0) = \Delta S(0) + B(0)$$

This is the foundation of the Black–Scholes replication argument — the option price today equals the cost of its replicating portfolio.

## Remember

The Law of One Price is the single axiom that underpins almost all derivative pricing. Whenever you see a replicating portfolio argument — Black–Scholes, binomial trees, put-call parity — the conclusion that "the derivative equals the portfolio's value" rests entirely on this law. If markets allowed two identical payoff streams to trade at different prices, traders would instantly arbitrage the gap, so the assumption is realistic in liquid markets.
