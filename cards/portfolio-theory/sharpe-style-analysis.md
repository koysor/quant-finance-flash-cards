# Sharpe Style Analysis

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** sharpe style analysis, returns-based style analysis, factor model, fund manager, rbsa, ols
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Sharpe Style Analysis** (Returns-Based Style Analysis, RBSA) determines a fund manager's investment style by regressing their historical excess returns against the returns of a set of asset class or style indices. The regression coefficients — constrained to be non-negative and sum to one — reveal the effective style exposures without requiring access to the fund's holdings.

## Key Formula

Regress fund returns $R_p$ against $K$ style index returns $F_1, \ldots, F_K$:

$$R_p^t = \sum_{k=1}^{K} w_k F_k^t + \varepsilon^t$$

subject to:
$$w_k \geq 0 \quad \forall k, \qquad \sum_{k=1}^{K} w_k = 1$$

Solved via constrained least squares. The $R^2$ of the regression measures the **style fit**: how much return variation is explained by passive style exposures. The residual $\varepsilon_t$ represents **selection return** — the manager's active contribution beyond style tilts.

## Example

A self-described "growth equity" fund. RBSA regressing 36 months of monthly returns against: US Large Growth (weight 0.45), US Large Value (0.20), US Mid Growth (0.25), US Small Cap (0.10). $R^2 = 0.94$. Conclusion: 94% of return variation is explained by these four passive indices; the fund effectively acts as a blended index product. Selection return (alpha from stock picking) $\approx -0.3\%$ per year after fees.

## Remember

RBSA is the standard tool for detecting **style drift** — when a fund manager's actual exposures diverge from their stated mandate — without requiring transparency into holdings. In performance attribution, RBSA separates the **style return** (passive beta exposure, which investors could replicate cheaply with ETFs) from the **selection return** (true active skill). A fund charging 2% management fees with $R^2 = 0.95$ and negative selection return is essentially an expensive index fund — a finding that drives significant capital reallocation in institutional due diligence.
