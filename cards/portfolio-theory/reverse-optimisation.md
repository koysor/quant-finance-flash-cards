# Reverse Optimisation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** reverse optimisation, implied returns, Black-Litterman, equilibrium, market portfolio
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

Reverse optimisation (also called reverse engineering the market) infers the expected returns **implied** by observed portfolio weights, rather than computing weights from expected returns. Given a portfolio believed to be mean-variance optimal — typically the market-cap-weighted market portfolio — reverse optimisation recovers the return expectations that would make a rational investor choose exactly those weights.

## Key Formula

Starting from the first-order condition of mean-variance optimisation $\mathbf{w}^* = \frac{1}{\lambda}\Sigma^{-1}\boldsymbol{\mu}$, rearranging gives the **implied equilibrium returns**:

$$\boldsymbol{\Pi} = \lambda \, \Sigma \, \mathbf{w}_{\text{mkt}}$$

where $\boldsymbol{\Pi}$ is the vector of implied returns, $\lambda$ is the market risk-aversion coefficient, $\Sigma$ is the covariance matrix of asset returns, and $\mathbf{w}_{\text{mkt}}$ are the market-cap weights.

## Example

Two assets with $\lambda = 2.5$, market weights $\mathbf{w} = [0.6, 0.4]^\top$, and covariance matrix:

$$\Sigma = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{pmatrix}$$

$$\boldsymbol{\Pi} = 2.5 \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{pmatrix} \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix} = 2.5 \begin{pmatrix} 0.028 \\ 0.014 \end{pmatrix} = \begin{pmatrix} 7.0\% \\ 3.5\% \end{pmatrix}$$

These are the returns the market implicitly expects — not analyst forecasts, but the returns embedded in current prices.

## Remember

Raw analyst return forecasts fed directly into Markowitz optimisation produce unstable, concentrated portfolios because small errors in expected returns lead to extreme weight shifts. Reverse optimisation solves this by using market weights as the neutral starting point: the market portfolio is assumed to be the consensus optimal portfolio, so $\boldsymbol{\Pi}$ represents the collective wisdom of all investors. In the Black-Litterman framework, $\boldsymbol{\Pi}$ serves as the prior mean; analysts then blend in their own views as updates, producing portfolios that deviate from the market only where there is genuine conviction.
