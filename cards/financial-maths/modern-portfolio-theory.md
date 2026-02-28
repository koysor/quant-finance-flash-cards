# Modern Portfolio Theory

**Topic:** Financial Mathematics
**Tags:** portfolio theory, diversification, efficient frontier, mean-variance, optimisation
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

**Modern Portfolio Theory (MPT)**, introduced by Harry Markowitz in 1952, is a framework for constructing portfolios that maximise expected return for a given level of risk (measured by variance). The central insight is that an asset's risk should not be evaluated in isolation but by its contribution to the overall portfolio — diversification across imperfectly correlated assets reduces total risk without necessarily sacrificing return.

## Key Formula

For a portfolio of $n$ assets with weight vector $\mathbf{w}$, expected return vector $\boldsymbol{\mu}$, and covariance matrix $\Sigma$:

$$\mu_p = \mathbf{w}^\top \boldsymbol{\mu} = \sum_{i=1}^{n} w_i \mu_i$$

$$\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w} = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}$$

The **minimum-variance portfolio** for a target return $\mu^*$ solves:

$$\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \, \mathbf{w} \quad \text{subject to} \quad \mathbf{w}^\top \boldsymbol{\mu} = \mu^*, \quad \mathbf{w}^\top \mathbf{1} = 1$$

## Example

Two assets: A has $\mu_A = 10\%$, $\sigma_A = 20\%$; B has $\mu_B = 6\%$, $\sigma_B = 10\%$; correlation $\rho = 0.3$.

A 50/50 portfolio ($w_A = w_B = 0.5$):

$$\mu_p = 0.5 \times 10 + 0.5 \times 6 = 8\%$$

$$\sigma_p^2 = 0.5^2 \times 20^2 + 0.5^2 \times 10^2 + 2 \times 0.5 \times 0.5 \times 0.3 \times 20 \times 10 = 100 + 25 + 30 = 155$$

$$\sigma_p = \sqrt{155} \approx 12.4\%$$

The portfolio volatility (12.4%) is lower than the weighted average of the individual volatilities ($0.5 \times 20 + 0.5 \times 10 = 15\%$) — this is the **diversification benefit** from imperfect correlation.

## Remember

MPT is the theoretical foundation for almost every quantitative allocation strategy, from index funds to risk-parity portfolios. The key practical limitation is that the covariance matrix $\Sigma$ must be estimated from historical data, and estimation error in $\Sigma$ can dominate the optimisation — leading to unstable, extreme weights. This is why real-world implementations use shrinkage estimators, factor models, or constraints to regularise the optimisation. Despite its simplifying assumptions (normal returns, static correlations), MPT formalised the idea that **diversification is the only free lunch in finance**.
