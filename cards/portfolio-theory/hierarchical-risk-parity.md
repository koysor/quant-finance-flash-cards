# Hierarchical Risk Parity

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** hierarchical risk parity, hrp, clustering, portfolio construction, diversification, covariance matrix
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Hierarchical Risk Parity (HRP)**, developed by Marcos López de Prado (2016), is a portfolio construction method that uses hierarchical clustering to allocate weights in a way that respects the correlation structure of assets. Unlike Markowitz mean-variance optimisation, HRP requires no matrix inversion and is robust to estimation error in the covariance matrix.

## Key Formula

**Three-step algorithm:**

1. **Tree clustering** — build a hierarchical clustering dendrogram on assets using correlation distance $d_{ij} = \sqrt{2(1-\rho_{ij})}$ with Ward's linkage

2. **Quasi-diagonalisation** — reorder the covariance matrix rows/columns so correlated assets are adjacent, following the dendrogram leaf order

3. **Recursive bisection** — allocate risk top-down by splitting the dendrogram at each node, proportional to the inverse of each sub-portfolio's variance:

$$w_i \propto \frac{1}{\sigma_{\text{cluster}_i}^2}$$

The result is a set of weights where each branch of the hierarchy receives a budget inversely proportional to its risk.

## Example

10 assets in two clusters: Equities (5 stocks, $\sigma_{\text{eq}} = 0.18$) and Fixed Income (5 bonds, $\sigma_{\text{fi}} = 0.06$). Inverse variance split: equities get weight $\frac{1/0.18^2}{1/0.18^2 + 1/0.06^2} \approx 10\%$, fixed income $\approx 90\%$. Within equities, the 5 stocks receive weights by recursive bisection of the sub-dendrogram. Final portfolio is dominated by fixed income — matching the lower-risk branch.

## Remember

HRP solves the core weakness of Markowitz optimisation: the covariance matrix inversion amplifies estimation errors, producing extreme and unstable weights. By replacing matrix inversion with recursive bisection guided by clustering, HRP produces diversified portfolios that are robust out-of-sample. López de Prado showed that HRP consistently outperforms Markowitz, equal-weight, and inverse-volatility portfolios on out-of-sample Sharpe ratio — making it the benchmark for modern quantitative portfolio construction alongside risk parity.
