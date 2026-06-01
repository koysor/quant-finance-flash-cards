# Gauss–Markov Theorem

**Topic:** Statistics
**Tags:** regression, OLS, BLUE, assumptions, heteroskedasticity, autocorrelation
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gauss–Markov theorem** states that, under five classical assumptions, the OLS estimator is the **Best Linear Unbiased Estimator (BLUE)** — it has the smallest variance among all linear unbiased estimators of the regression coefficients. "Best" means minimum variance; "linear" means the estimator is a linear function of $y$; "unbiased" means $E[\hat{\boldsymbol{\beta}}] = \boldsymbol{\beta}$.

## Key Formula

The five Gauss–Markov assumptions:

| # | Assumption | Violation in finance |
|---|---|---|
| 1 | Linearity: $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$ | Non-linear factor payoffs |
| 2 | Full rank: $\text{rank}(\mathbf{X}) = k$ | Multicollinearity |
| 3 | Strict exogeneity: $E[\boldsymbol{\varepsilon} \mid \mathbf{X}] = \mathbf{0}$ | Endogenous factors |
| 4 | Homoskedasticity: $\text{Var}(\varepsilon_i) = \sigma^2$ | ARCH/GARCH volatility clustering |
| 5 | No autocorrelation: $\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$ | Serial correlation in returns |

When assumptions 4 or 5 fail, OLS remains unbiased but is no longer BLUE; GLS becomes the efficient estimator instead.

## Example

A CAPM regression of daily stock returns over one year ($n = 252$) is tested for the Gauss–Markov conditions. The Durbin–Watson statistic of 1.45 (below the lower bound of 1.73 at 5%) rejects assumption 5 — residuals are positively autocorrelated. The Breusch–Pagan test rejects assumption 4 — residual variance is higher in volatile market periods. OLS coefficients are still unbiased, but standard errors are understated, so t-statistics overstate significance. The fix: Newey–West standard errors, which correct for both heteroskedasticity and autocorrelation simultaneously.

## Remember

The Gauss–Markov theorem is the theoretical foundation that justifies OLS, and understanding which assumptions it makes is what separates naïve regression from rigorous quantitative analysis. In practice, assumptions 4 and 5 are almost always violated with financial return data — daily returns cluster in volatility (ARCH effects) and exhibit serial correlation. This does not invalidate OLS coefficient estimates, but it does invalidate the standard errors and all significance tests derived from them. Robust standard errors (White for heteroskedasticity, Newey–West for autocorrelation) should be the default in any regression on financial time series, not an afterthought.
