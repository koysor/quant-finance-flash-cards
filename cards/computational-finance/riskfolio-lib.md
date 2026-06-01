# Riskfolio-Lib

**Topic:** Computational Finance
**Tags:** portfolio optimisation, cvar, hierarchical risk parity, risk parity, python, convex optimisation
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Riskfolio-Lib** is an open-source Python portfolio optimisation library that extends mean-variance to 40+ risk measures — including CVaR, EVaR, CDaR, and tail risk measures — and implements Hierarchical Risk Parity (HRP), risk budgeting, and Black-Litterman alongside classical MVO, all via a unified CVXPY-based convex optimisation backend.

## Key Formula

**CVaR portfolio optimisation** (minimum tail-risk portfolio):

$$\min_{\mathbf{w}}\; \text{CVaR}_\alpha(\mathbf{w}) \quad \text{s.t.} \quad \mathbf{1}^\top\mathbf{w} = 1,\; \mathbf{w} \geq \mathbf{0}$$

**Risk budgeting** (equal risk contribution across $N$ assets):

$$RC_i(\mathbf{w}) = w_i \cdot \frac{\partial \rho(\mathbf{w})}{\partial w_i} = \frac{\rho(\mathbf{w})}{N} \quad \forall i$$

where $\rho$ is any risk measure (volatility, CVaR, CDaR). Riskfolio's API switches between these objectives by setting `model='Classic'`, `model='HRP'`, or `model='HERC'` and `rm='CVaR'`, `rm='MV'`, etc.

## Example

```python
import riskfolio as rp

port = rp.Portfolio(returns=returns)   # daily returns DataFrame
port.assets_stats(method_mu='hist', method_cov='ledoit')

w = port.optimization(
    model='Classic',
    rm='CVaR',          # minimise CVaR
    obj='MinRisk',
    hist=True,
    rf=0.0,
    l=0
)
```

For 20 global equity indices, `rm='MV'` produces a concentrated portfolio (5 assets dominate); `rm='CVaR'` spreads weight more evenly because it penalises tail losses from any single index; `rm='CDaR'` additionally avoids assets with prolonged drawdown histories, such as emerging-market indices during the 2015–2016 commodity cycle.

## Remember

Mean-variance optimisation is blind to the shape of the return distribution below the mean — it treats a strategy with occasional -30% months the same as one with smooth -3% months, provided both have the same variance. CVaR and CDaR optimisation directly penalise the left tail, producing portfolios that are more robust to stress events. Riskfolio-Lib is the reference library for this style of optimisation in Python, and the choice of risk measure is a design decision with real consequences: a fund managing drawdown-sensitive capital (endowments, insurance) should use CDaR rather than variance as its optimisation objective.
