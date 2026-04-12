# Portfolio Expected Shortfall — Parametric (Gaussian)

**Topic:** Risk
**Tags:** expected shortfall, portfolio risk, gaussian, parametric, coherent risk measure, FRTB
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Under the assumption that portfolio returns follow a multivariate normal distribution, Expected Shortfall (ES) has a **closed-form expression** driven by the portfolio weight vector and the covariance matrix. This parametric approach yields an analytic capital figure without simulation.

For a portfolio with weight vector $\mathbf{x}$, mean return vector $\boldsymbol{\mu}$, and covariance matrix $\boldsymbol{\Sigma}$, the portfolio return $R_p = \mathbf{x}'\boldsymbol{\mu}$ is normally distributed with variance $\mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}$.

## Key Formula

$$\text{ES}_\alpha(\mathbf{x}) = -\mathbf{x}'\boldsymbol{\mu} + \frac{\sqrt{\mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}}}{1-\alpha} \cdot \phi\!\left(\Phi^{-1}(\alpha)\right)$$

where:
- $\boldsymbol{\mu}$ = vector of asset mean returns
- $\boldsymbol{\Sigma}$ = covariance matrix of asset returns
- $\phi$ = standard normal PDF
- $\Phi^{-1}(\alpha)$ = $\alpha$-quantile of the standard normal (inverse CDF)

**Relationship to VaR:** the parametric Gaussian VaR replaces the PDF scaling factor with the quantile directly:

$$\text{VaR}_\alpha(\mathbf{x}) = -\mathbf{x}'\boldsymbol{\mu} + \sqrt{\mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}} \cdot \Phi^{-1}(\alpha)$$

Because $\dfrac{\phi(\Phi^{-1}(\alpha))}{1-\alpha} > \Phi^{-1}(\alpha)$ for all $\alpha > 0.5$, it follows that $\text{ES}_\alpha > \text{VaR}_\alpha$ always.

**Scaling factors at common confidence levels:**

| $\alpha$ | VaR scaling $z_\alpha$ | ES scaling $\phi(z_\alpha)/(1-\alpha)$ |
|---|---|---|
| 97.5% | 1.960 | 2.338 |
| 99.0% | 2.326 | 2.667 |

## Example

A two-asset portfolio has daily portfolio volatility $\sigma_p = \sqrt{\mathbf{x}'\boldsymbol{\Sigma}\mathbf{x}} = 1.476\%$ and daily mean return $\mathbf{x}'\boldsymbol{\mu} = 0.370\%$.

**At $\alpha = 99\%$:** the ES scaling factor is $\phi(2.326)/0.01 = 0.02665/0.01 = 2.667$.

$$\text{ES}_{99\%} = -0.370\% + 2.667 \times 1.476\% = \mathbf{3.56\%}$$

$$\text{VaR}_{99\%} = -0.370\% + 2.326 \times 1.476\% = 3.06\%$$

ES exceeds VaR by 50 basis points — the extra capital charge reflects the expected severity of losses in the worst 1% of days, not merely where the tail begins.

## Remember

Basel's **Fundamental Review of the Trading Book (FRTB)** replaced 99% VaR with **97.5% ES** as the regulatory headline metric for internal model approaches. The switch has two rationales: first, ES is a **coherent risk measure** — it satisfies subadditivity so diversification always reduces capital, unlike VaR which can penalise diversification. Second, ES captures **tail severity** not just tail probability — a desk that passes a VaR backtest can still hold inadequate capital if its worst-case losses are catastrophic. The parametric Gaussian formula makes ES operationally tractable for large portfolios: only $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are needed, and the result is a single analytic expression.
