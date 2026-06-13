# Short-Rate SDE

**Topic:** Fixed Income
**Tags:** short rate, SDE, drift, diffusion, one-factor model, mean reversion
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The general one-factor short-rate model specifies the spot rate $r$ as a solution to a stochastic differential equation (SDE) with state-dependent drift $u(r,t)$ and volatility $w(r,t)$. The choice of these two functions completely defines the model; all named models (Vasicek, CIR, Hull–White) are special cases.

## Key Formula

$$dr = u(r,t)\,dt + w(r,t)\,dX$$

where $dX = \sqrt{dt}\,Z$, $Z \sim \mathcal{N}(0,1)$ is the Brownian increment.

| Model | $u(r,t)$ | $w(r,t)$ |
|---|---|---|
| Vasicek | $\eta - \gamma r$ | $\sqrt{\beta}$ |
| CIR | $\eta - \gamma r$ | $\sqrt{\alpha r}$ |
| Hull–White | $\eta(t) - \gamma(t)r$ | $\sqrt{\beta(t)}$ |

This is the **real-world** ($\mathbb{P}$-measure) SDE. The pricing PDE uses the **risk-neutral drift** $u - \lambda w$, where $\lambda(r,t)$ is the market price of interest rate risk.

## Example

For CIR with $\eta = 0.02$, $\gamma = 0.5$, $\alpha = 0.04$ and current rate $r = 3\%$, the instantaneous drift is $0.02 - 0.5 \times 0.03 = 0.005$ (the rate is below its long-run mean of $\eta/\gamma = 4\%$ so the drift is positive, pushing it up). The diffusion is $\sqrt{0.04 \times 0.03} = 3.46\%$ per $\sqrt{\text{year}}$.

## Remember

The short-rate SDE is the starting point for all one-factor fixed-income models. The drift $u$ determines mean-reversion behaviour; the volatility $w$ determines the model's distributional properties — in particular, whether $w \propto \sqrt{r}$ (CIR) prevents negative rates while $w = \text{const}$ (Vasicek) allows them. Never use the real-world drift $u$ for pricing: always substitute the risk-neutral drift $u - \lambda w$ into the pricing PDE.
