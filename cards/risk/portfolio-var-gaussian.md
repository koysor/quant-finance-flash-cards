# Portfolio VaR — Parametric (Gaussian)

**Topic:** Risk
**Tags:** var, portfolio, covariance matrix, diversification, parametric, gaussian
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Parametric portfolio VaR** extends single-asset VaR to a multi-asset portfolio by replacing the individual asset's volatility with the **portfolio volatility** $\sqrt{\mathbf{x}'\Sigma\mathbf{x}}$, where $\Sigma$ is the covariance matrix and $\mathbf{x}$ is the vector of portfolio weights.

For a fully invested portfolio with weights $\mathbf{x} = (x_1, \ldots, x_n)'$ satisfying $\mathbf{1}'\mathbf{x} = 1$:

- **Portfolio return:** $R(\mathbf{x}) = \mathbf{x}'\mathbf{R}$
- **Expected return:** $\mu(\mathbf{x}) = \mathbf{x}'\boldsymbol{\mu}$
- **Portfolio variance:** $\sigma^2(\mathbf{x}) = \mathbf{x}'\Sigma\mathbf{x}$

The covariance matrix encodes pairwise correlations, so **diversification is built in automatically** — correlated assets contribute less volatility than their individual risks would suggest.

## Key Formula

For normally distributed returns at confidence level $\alpha$:

$$\text{VaR}_\alpha(\mathbf{x}) = -\mathbf{x}'\boldsymbol{\mu} + \Phi^{-1}(\alpha)\sqrt{\mathbf{x}'\Sigma\mathbf{x}}$$

where $\Phi^{-1}(\alpha)$ is the $\alpha$-quantile of the standard normal (e.g. $\Phi^{-1}(0.99) = 2.326$).

**Diversification benefit:** because $\Sigma$ captures correlations, portfolio VaR is always less than or equal to the weighted sum of individual VaRs:

$$\text{VaR}_\alpha(\mathbf{x}) \leq \sum_i x_i \, \text{VaR}_\alpha(e_i)$$

with equality only when all pairwise correlations equal 1.

## Example

A three-stock portfolio has daily statistics:

$$\mu(\mathbf{x}) = 0.370\% \text{ per day}, \quad \sigma(\mathbf{x}) = \sqrt{\mathbf{x}'\Sigma\mathbf{x}} = 1.476\% \text{ per day}$$

**1-day 99% VaR:**

$$\text{VaR}_{0.99} = -0.370\% + 2.326 \times 1.476\% = -0.370\% + 3.433\% = 3.063\%$$

On a \$938 portfolio, this is:

$$\$938 \times 3.063\% \approx \$28.74$$

There is a 1% chance of losing more than \$28.74 on the next trading day.

## Remember

The key insight is that portfolio volatility $\sqrt{\mathbf{x}'\Sigma\mathbf{x}}$ is smaller than the weighted average of individual volatilities whenever assets are imperfectly correlated. This is the mathematical statement of **diversification** — the covariance matrix transforms individual risks into a portfolio risk that accounts for how assets move together. In practice, risk managers use this formula for **Greeks-based VaR** on linear portfolios and as the building block for more complex approaches such as historical simulation and Monte Carlo VaR.
