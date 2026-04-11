# No-Arbitrage and Portfolio Equilibrium

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** no-arbitrage, equilibrium, zero-variance portfolio, risk-free rate, asset pricing
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

In an efficient market, any portfolio with **zero risk** must earn exactly the **risk-free rate** $R$. If it earned more, traders would borrow at $R$ and invest in the risk-free-but-higher-returning portfolio for free money. If it earned less, the opposite trade would be available. Competition eliminates both cases, forcing equilibrium.

## Key Formula

When $\rho_{AB} = -1$, a zero-variance portfolio $Z$ exists with:

$$w_A^Z = \frac{\sigma_B}{\sigma_A + \sigma_B}$$

No-arbitrage requires:

$$\mu_Z = R$$

| Scenario | Arbitrage trade | Market response |
|---|---|---|
| $\mu_Z > R$ | Borrow at $R$, invest in $Z$ → free profit | Prices adjust down until $\mu_Z = R$ |
| $\mu_Z < R$ | Short $Z$, invest proceeds at $R$ → free profit | Prices adjust up until $\mu_Z = R$ |
| $\mu_Z = R$ | No riskless profit possible | Equilibrium |

## Example

A zero-variance portfolio earns $\mu_Z = 8\%$ while $R = 4\%$. Borrow £1m at 4%, invest in $Z$: earn $80{,}000 - 40{,}000 = £40{,}000$ with zero risk. Arbitrageurs flood in, bidding up asset $B$'s price and driving $\mu_Z$ down to 4%.

## Remember

No-arbitrage is the bedrock of asset pricing: zero risk must earn $R$. This principle, first encountered in the portfolio geometry of $\rho = -1$, reappears throughout quantitative finance — it is exactly why a perfectly hedged options portfolio earns $R$ in the Black-Scholes framework. The geometry and the economics are the same argument expressed in different settings.
