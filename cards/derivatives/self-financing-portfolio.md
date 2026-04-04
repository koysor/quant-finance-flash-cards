# Self-Financing Portfolio

**Topic:** Derivatives
**Tags:** self-financing, replication, no-arbitrage, portfolio, Black-Scholes, hedging
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

A self-financing portfolio is a trading strategy in which all changes in portfolio value come solely from gains and losses on the assets held — no external cash is injected or withdrawn after the initial investment. When the portfolio is rebalanced (for example, to adjust a delta hedge), the proceeds from selling one asset are used entirely to purchase another. This constraint is essential for derivatives pricing: the replicating portfolio that justifies an option's price must be self-financing, otherwise the "replication" would require additional funding and the no-arbitrage price would be incorrect.

## Key Formula

For a portfolio of $\Delta_t$ shares of stock $S$ and $B_t$ in a risk-free bond, the self-financing condition requires:

$$dV_t = \Delta_t \, dS_t + r \, B_t \, dt$$

where $V_t = \Delta_t S_t + B_t$ is the portfolio value. Equivalently, any rebalancing at time $t$ must satisfy:

$$\Delta_{t^+} S_t + B_{t^+} = \Delta_{t^-} S_t + B_{t^-}$$

That is, the portfolio value immediately before and after rebalancing is the same — shares are traded at the prevailing price with no cash added or removed. In integral form:

$$V_t = V_0 + \int_0^t \Delta_s \, dS_s + \int_0^t r \, B_s \, ds$$

## Example

A trader replicates a call option by holding $\Delta = 0.60$ shares at £100 per share and borrowing £25 from the bond (at 5% annual rate). Portfolio value: $0.60 \times £100 - £25 = £35$.

The stock rises to £105. The new delta is 0.68. The trader must buy $0.08$ additional shares at £105, costing £8.40. Under the self-financing constraint, this £8.40 comes from increased borrowing:

$$B_{\text{new}} = -£25 \times (1 + 0.05/252) - £8.40 = -£33.40$$

New portfolio value: $0.68 \times £105 - £33.40 = £71.40 - £33.40 = £38.00$. The increase from £35 to £38 came entirely from the stock's price appreciation ($0.60 \times £5 = £3.00$) — no external cash was added.

## Remember

The self-financing condition is the hidden assumption that makes Black–Scholes pricing work. When we say "the option price equals the cost of the replicating portfolio", we implicitly assume that once the initial investment is made, the replicating strategy funds itself through trading — no further capital calls are needed. If rebalancing required injecting extra cash, the replication cost would depend on the path of the underlying, and the unique no-arbitrage price would collapse. For quant practitioners, violations of self-financing in practice — through transaction costs, bid-ask spreads, and margin requirements — are the fundamental reason that real-world hedging is imperfect and that options carry a bid-ask spread beyond the theoretical Black–Scholes price.
