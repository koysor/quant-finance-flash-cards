# No-Arbitrage Principle

**Topic:** Derivatives
**Tags:** no-arbitrage, hedging, risk-free rate, derivative pricing, CQF

---

## Definition

An **arbitrage** opportunity is a trading strategy that starts with zero net investment, has no probability of loss, and has a positive probability of profit. The **no-arbitrage principle** states that in an efficient market no such opportunity can persist.

The central consequence for derivatives pricing is this: any portfolio that is completely hedged — carrying no market risk — must earn exactly the risk-free interest rate $r$. If it earned more, traders would borrow at $r$ and buy the portfolio (free profit); if it earned less, they would short the portfolio and invest the proceeds at $r$ (again, free profit). Competition eliminates both cases instantly.

Because the hedged portfolio's return is pinned to $r$, the derivative's price is fully determined by the hedge ratio and the risk-free rate alone. This is why the Black-Scholes equation contains $r$ but not the stock's expected return $\mu$.

## Key Formula

Let $\Pi$ be the value of a delta-hedged portfolio (one option plus $-\Delta$ shares). Over a small time step $\delta t$ the portfolio must satisfy:

$$\Pi^{+} = \Pi^{-} = \Pi\,(1 + r\,\delta t)$$

where $\Pi^{+}$ and $\Pi^{-}$ are the portfolio values in the up and down states respectively, and $r$ is the continuously compounded risk-free rate.

Equivalently, in differential form the hedged portfolio obeys:

$$d\Pi = r\,\Pi\,dt$$

This single equation — the return on a riskless portfolio equals $r$ — is the engine that produces the Black-Scholes PDE.

## Example

Suppose a hedged portfolio is worth $\Pi = \text{£}100{,}000$ today and $r = 5\%$ per annum. Over one day ($\delta t = 1/252$):

$$\Pi_{\text{tomorrow}} = 100{,}000 \times \left(1 + \frac{0.05}{252}\right) \approx \text{£}100{,}019.84$$

If the portfolio were instead worth £100,030 in every possible state tomorrow, you could pocket £10.16 risk-free — an arbitrage. The market would immediately bid up the option (or sell the stock) until the discrepancy vanished.

## Remember

No-arbitrage is the logical backbone of every pricing model you will meet on the CQF. When you see the Black-Scholes PDE, recognise that it is simply the statement $d\Pi = r\,\Pi\,dt$ rewritten in terms of $V$, $S$, and $t$. Whenever someone quotes a "fair" derivative price, they are implicitly invoking the no-arbitrage principle: if the price were anything else, a riskless profit would exist and the market would correct it. In practice, transaction costs, funding spreads, and liquidity constraints mean small deviations can survive, but the principle remains the starting point for all quantitative pricing.
