# Cokurtosis

**Topic:** Probability
**Tags:** cokurtosis, higher moments, multivariate, kurtosis, tail risk, portfolio
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Cokurtosis** is the multivariate generalisation of kurtosis: it measures the tendency of two or more variables to jointly produce extreme outcomes simultaneously. A portfolio's kurtosis — its tail risk — depends not only on individual asset kurtosis but also on the cokurtosis between assets.

## Key Formula

**Cokurtosis of $X$ with $Y$** (symmetric form):

$$\text{Cokurt}(X, X, Y, Y) = \frac{E[(X-\mu_X)^2(Y-\mu_Y)^2]}{\sigma_X^2\,\sigma_Y^2}$$

For a normal distribution, $\text{Cokurt}(X,X,Y,Y) = 1 + 2\rho_{XY}^2$ where $\rho_{XY}$ is the correlation.

**Portfolio kurtosis** (two-asset portfolio, weights $w_1, w_2$):

$$\mu_4^P = w_1^4\mu_4^1 + w_2^4\mu_4^2 + 4w_1^3w_2\,\text{Cokurt}(R_1,R_1,R_1,R_2)\,\sigma_1^3\sigma_2 + \ldots$$

The full expansion has $\binom{4+2-1}{2-1} = 5$ terms involving all combinations of the fourth-order cross-moments.

## Example

During a financial crisis, assets that appear diversified in normal markets can simultaneously experience extreme losses — this is high **positive cokurtosis** between assets and the market. The 2008 GFC showed that assets assumed to be uncorrelated (mortgages across different US regions) had high cokurtosis: they all crashed together, amplifying portfolio tail losses far beyond what individual kurtosis figures suggested.

A portfolio with high cokurtosis with the market requires higher expected return compensation — this is the economic rationale for the **co-kurtosis risk premium** in asset pricing extensions of CAPM.

## Remember

Cokurtosis explains why tail events in a portfolio are almost always worse than adding individual tail events together. When assets have positive cokurtosis, their extreme moves coincide — doubling, tripling the portfolio loss — rather than offsetting each other. This is the statistical description of "contagion." Mean-variance-skewness-kurtosis optimisation, which includes cokurtosis, is theoretically more complete than Markowitz but is computationally demanding and requires estimating a large number of higher-order cross-moments from limited data.
