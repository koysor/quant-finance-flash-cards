# Zero-Variance Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** zero variance, perfect negative correlation, no-arbitrage, risk-free rate, hedging
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

When two assets have **perfect negative correlation** ($\rho = -1$), a portfolio exists with **zero variance**. Their returns move in exactly opposite directions, so the risks cancel completely. No-arbitrage then forces the return of this portfolio to equal the risk-free rate.

## Key Formula

Set $\sigma_\Pi = w_A\sigma_A - w_B\sigma_B = 0$:

$$w_A^Z = \frac{\sigma_B}{\sigma_A + \sigma_B}, \qquad w_B^Z = \frac{\sigma_A}{\sigma_A + \sigma_B}$$

The expected return of the zero-variance portfolio:

$$\mu_Z = \mu_B + \frac{\sigma_B}{\sigma_A + \sigma_B}(\mu_A - \mu_B)$$

**No-arbitrage condition:** in equilibrium,

$$\mu_Z = R$$

## Example

$\mu_A = 12\%$, $\sigma_A = 20\%$, $\mu_B = 6\%$, $\sigma_B = 10\%$, $\rho = -1$.

$$w_A^Z = \frac{10}{30} = 33.3\%, \qquad w_B^Z = 66.7\%$$

$$\mu_Z = 6 + \frac{1}{3}(6) = 8\%$$

If the risk-free rate is $R = 5\%$ then $\mu_Z = 8\% \neq R$: an arbitrageur could borrow at 5% and invest in the zero-risk portfolio for a free 3% per year. Competition drives prices to restore $\mu_Z = R$.

## Remember

The zero-variance portfolio sits on the vertical axis ($\sigma = 0$) of the risk-return diagram. No-arbitrage demands it earns exactly the risk-free rate — if it earned more, riskless profit would be available; if less, the opposite trade would be taken. This is the same principle that pins the price of every hedged portfolio in derivatives: zero risk must earn $R$.
