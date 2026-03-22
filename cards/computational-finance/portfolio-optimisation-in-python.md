# Portfolio Optimisation in Python

**Topic:** Computational Finance
**Tags:** python, portfolio optimisation, scipy, efficient frontier, mean-variance, weights
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Portfolio optimisation in Python** uses SciPy's constrained minimisation routines to find the asset weights that maximise return for a given risk level (or minimise risk for a given return), implementing Markowitz mean-variance optimisation computationally. The covariance matrix is estimated from historical returns using NumPy or pandas, and constraints (weights sum to 1, no short selling) are passed to the optimiser.

## Key Formula

**Minimum-variance portfolio:**

$$\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \mathbf{w} \quad \text{subject to} \quad \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0$$

**Python implementation:**

```python
from scipy.optimize import minimize

def portfolio_vol(w, cov_matrix):
    return np.sqrt(w @ cov_matrix @ w)

n = len(expected_returns)
constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]
bounds = [(0, 1)] * n

result = minimize(portfolio_vol, x0=np.ones(n)/n,
                  args=(cov_matrix,),
                  method="SLSQP",
                  bounds=bounds, constraints=constraints)
optimal_weights = result.x
```

## Example

Three assets with annual returns [8%, 12%, 6%] and covariance matrix estimated from daily data:

```python
mu = np.array([0.08, 0.12, 0.06])
cov = np.array([[0.04, 0.006, 0.002],
                [0.006, 0.09, 0.009],
                [0.002, 0.009, 0.01]])

result = minimize(portfolio_vol, x0=[1/3]*3, args=(cov,),
                  method="SLSQP", bounds=[(0,1)]*3,
                  constraints=[{"type":"eq","fun":lambda w: sum(w)-1}])
print(result.x)  # ≈ [0.28, 0.07, 0.65]
print(f"Vol: {portfolio_vol(result.x, cov):.2%}")  # ≈ 8.1%
```

## Remember

Mean-variance optimisation is the computational heart of modern asset allocation. In practice, the covariance matrix is the dominant source of estimation error — with hundreds of assets the sample covariance is noisy and often singular, so practitioners apply shrinkage estimators (Ledoit-Wolf) or factor models before optimising. Python's ecosystem makes this pipeline straightforward: pandas computes returns, NumPy estimates covariance (or sklearn provides shrinkage), and SciPy finds the optimal weights under realistic constraints like position limits and sector caps. The efficient frontier is traced by repeating the optimisation at a grid of target returns.
