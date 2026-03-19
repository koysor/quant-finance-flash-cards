# Replicating Portfolio

**Topic:** Derivatives
**Tags:** replication, binomial model, no-arbitrage, delta, law of one price, option pricing
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **replicating portfolio** is a portfolio of traded assets — typically $\Delta$ shares of stock and $B$ dollars invested in a risk-free bond — constructed to exactly reproduce the payoff of a derivative in every possible future scenario. Because the replicating portfolio and the derivative deliver identical cash flows, the **law of one price** (no-arbitrage) requires them to have the same price today.

## Key Formula

In a one-step binomial model with stock prices $S_u$ (up) and $S_d$ (down) and corresponding option values $V_u$ and $V_d$:

$$\Delta = \frac{V_u - V_d}{S_u - S_d}$$

$$B = \frac{V_u - \Delta S_u}{1 + r}$$

The option price is then:

$$V_0 = \Delta S_0 + B$$

where $r$ is the risk-free rate over the period.

## Example

A stock trades at $S_0 = 100$. Next period it moves to $S_u = 110$ or $S_d = 90$. A call with strike $K = 100$ pays $V_u = 10$ or $V_d = 0$.

$$\Delta = \frac{10 - 0}{110 - 90} = 0.5$$

$$B = \frac{10 - 0.5 \times 110}{1.05} \approx -47.62$$

The replicating portfolio holds 0.5 shares and borrows £47.62 at the risk-free rate, giving $V_0 = 0.5 \times 100 - 47.62 = 2.38$.

## Remember

Replicating portfolio thinking is the conceptual heart of all derivative pricing: you never need to know investors' risk preferences or expected returns, because the price is pinned by the cost of construction. In practice, a market-maker who sells an option immediately builds the replicating portfolio (delta hedge) to lock in a riskless position — replication is both a pricing argument and a hedging strategy simultaneously.
