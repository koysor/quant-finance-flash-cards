# PyPortfolioOpt

**Topic:** Computational Finance
**Tags:** portfolio optimisation, efficient frontier, black-litterman, hierarchical risk parity, covariance shrinkage, python
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**PyPortfolioOpt** is an open-source Python library for portfolio optimisation that wraps mean-variance, Black-Litterman, Hierarchical Risk Parity, and CVaR optimisation in a clean scikit-learn-style API, handling covariance estimation, weight constraints, and transaction cost penalties out of the box.

## Key Formula

The core `EfficientFrontier` class solves the maximum Sharpe optimisation:

$$\max_{\mathbf{w}}\; \frac{\mathbf{w}^\top\boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^\top\hat{\boldsymbol{\Sigma}}\mathbf{w}}} \quad \text{s.t.} \quad \mathbf{1}^\top\mathbf{w} = 1,\; \mathbf{w} \geq \mathbf{0}$$

where $\hat{\boldsymbol{\Sigma}}$ is a shrinkage estimator (Ledoit-Wolf or Oracle Approximating) rather than the raw sample covariance, stabilising the weight vector when $N \approx T$. The HRP variant replaces this convex programme with a hierarchical clustering step:

$$\mathbf{w}^{\text{HRP}} = \text{RecursiveBisection}\!\left(\text{HClust}(\hat{\boldsymbol{\Sigma}})\right)$$

## Example

```python
from pypfopt import EfficientFrontier, risk_models, expected_returns

mu    = expected_returns.mean_historical_return(prices)
S     = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

ef    = EfficientFrontier(mu, S)
ef.add_constraint(lambda w: w >= 0.02)   # minimum 2% per asset
ef.add_constraint(lambda w: w <= 0.30)   # maximum 30% per asset
weights = ef.max_sharpe()
ef.portfolio_performance(verbose=True)
# Expected annual return: 14.3%, Volatility: 10.1%, Sharpe: 1.42
```

Switching to `ef.min_volatility()` or `ef.efficient_risk(0.08)` requires changing one line, making PyPortfolioOpt ideal for rapid strategy comparison.

## Remember

The most dangerous failure mode of mean-variance optimisation is covariance estimation error: the raw sample covariance matrix is unreliable when the number of assets $N$ approaches the number of observations $T$ (a common situation with monthly returns on 50+ assets). PyPortfolioOpt's Ledoit-Wolf shrinkage estimator blends the sample covariance toward a structured target, producing a well-conditioned matrix whose inverse (used in the optimisation) does not amplify estimation errors into extreme weights. This single improvement — using a shrinkage covariance rather than the raw sample matrix — is responsible for most of the practical difference between a "textbook" Markowitz portfolio and a deployable one.
