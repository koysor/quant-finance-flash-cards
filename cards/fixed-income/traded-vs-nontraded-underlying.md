# Traded vs Non-Traded Underlying

**Topic:** Fixed Income
**Tags:** market price of risk, traded asset, non-traded variable, risk-neutral drift, no-arbitrage
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

A **traded asset** (e.g. a stock price $S$) can be bought and sold, so its risk-neutral drift is automatically the risk-free rate $r$ by no-arbitrage. A **non-traded variable** (e.g. the short rate $r$, implied volatility $\sigma$) cannot be held directly; investors must be compensated for bearing its risk, and this compensation — the market price of risk $\lambda$ — explicitly enters the pricing PDE.

## Key Formula

| Modelled quantity | Risk-neutral drift |
|---|---|
| Traded asset (e.g. $S$) | $r$ (risk-free rate) |
| Non-traded variable (e.g. $r$, $\sigma$) | real drift $-\;\lambda \times$ volatility |

For a non-traded variable $x$ with real drift $\mu_x$ and volatility $\sigma_x$:

$$\mu_x^{\mathbb{Q}} = \mu_x - \lambda_x\,\sigma_x$$

For the Vasicek short rate: real drift $= \eta - \gamma r$; risk-neutral drift $= (\eta - \lambda\sqrt{\beta}) - \gamma r$.

## Example

In stochastic volatility models (e.g. Heston), the variance $v$ is non-traded, so the pricing PDE includes a market-price-of-risk correction $\lambda_v$ multiplied by the volatility of $v$. Omitting $\lambda_v$ — treating $v$ as if it were traded — produces option prices that are inconsistent with market-quoted smiles. Estimating $\lambda_v$ from options is a standard calibration step.

## Remember

This rule is the conceptual heart of fixed-income modelling. In equity Black–Scholes, the stock hedges itself so $\lambda$ drops out of the formula. In interest rate models the short rate cannot hedge itself, so $\lambda$ stays in the PDE and must be calibrated. Whenever you see a pricing PDE with a drift adjustment of the form "real drift $-\;\lambda \times$ vol", you are pricing a **non-traded underlying** — a flag that model risk is higher because $\lambda$ must be estimated, not eliminated.
