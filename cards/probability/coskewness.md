# Coskewness

**Topic:** Probability
**Tags:** coskewness, higher moments, multivariate, skewness, portfolio risk
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Coskewness** is the multivariate generalisation of skewness: it measures the tendency of two (or three) random variables to be jointly skewed — to experience extreme values in the same direction simultaneously. A portfolio's skewness depends not only on individual asset skewness but also on the coskewness between assets.

## Key Formula

**Coskewness of $X$ with $Y$** (the most common form):

$$\text{Coskew}(X, X, Y) = \frac{E[(X-\mu_X)^2(Y-\mu_Y)]}{\sigma_X^2\,\sigma_Y}$$

**Coskewness of $X$, $Y$, $Z$:**

$$\text{Coskew}(X, Y, Z) = \frac{E[(X-\mu_X)(Y-\mu_Y)(Z-\mu_Z)]}{\sigma_X\,\sigma_Y\,\sigma_Z}$$

**Portfolio skewness** (two-asset portfolio with weights $w_1, w_2$):

$$\mu_3^P = w_1^3\mu_3^1 + w_2^3\mu_3^2 + 3w_1^2 w_2\,\text{Coskew}(R_1, R_1, R_2) + 3w_1 w_2^2\,\text{Coskew}(R_1, R_2, R_2)$$

## Example

During market crashes, most assets fall simultaneously — this is **negative coskewness** between assets and the market. An asset with large negative coskewness with the market portfolio amplifies the portfolio's left-tail risk in downturns.

A crash-protected strategy (long puts, long volatility) has **positive coskewness** with the market: it pays off when the market crashes, offsetting the portfolio's negative coskewness and reducing left-tail risk. Investors may accept lower expected returns for this hedging benefit.

## Remember

Mean-variance optimisation ignores skewness and kurtosis. Coskewness matters whenever a portfolio's tail behaviour is important — and it usually is. Negative coskewness between an asset and the market is analogous to a high beta during crashes: both expose the portfolio to the same downside at the same time. Including coskewness in portfolio optimisation leads to portfolios that are less exposed to crash risk, at the cost of some expected return.
