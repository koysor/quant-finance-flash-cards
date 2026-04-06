# Linear Data Coding

**Topic:** Statistics
**Tags:** coding, linear transformation, mean, variance, standard deviation, data transformation
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Linear coding** transforms a dataset by applying $y = ax + b$ to every observation $x$. This simplifies calculations by scaling and shifting the data (e.g. converting temperatures, rescaling prices). The key results are that the mean transforms linearly, the variance scales by $a^2$ (the shift $b$ cancels out), and the standard deviation scales by $|a|$.

## Key Formula

If $y_i = ax_i + b$ for all $i$:

$$\bar{y} = a\bar{x} + b$$

$$\text{Var}(Y) = a^2 \text{Var}(X)$$

$$\sigma_Y = |a| \cdot \sigma_X$$

**Correlation and regression are unaffected by the shift $b$:**

$$r_{XY} = r_{Y'Y} \quad \text{(linear coding preserves correlation)}$$

**Effect on regression:** if $y = ax + b$ and we regress $y$ on $w = cz + d$, the regression coefficient scales by $a/c$.

## Example

Stock prices $X$ are quoted in pence. Analyst recodes to pounds: $Y = X / 100$.

$$\bar{Y} = \bar{X} / 100, \quad \sigma_Y = \sigma_X / 100, \quad \text{Var}(Y) = \text{Var}(X) / 10{,}000$$

A regression of return on size using prices in pence gives the same $R^2$ and $t$-statistics as using prices in pounds, but the regression coefficient is 100 times smaller. Forgetting to adjust for units is a common source of errors in factor model interpretation.

## Remember

Linear coding is why **log-returns are used in quantitative finance** instead of price-level returns. Taking $r_t = \ln(S_t / S_{t-1}) = \ln S_t - \ln S_{t-1}$ is a nonlinear transformation of price, but over short intervals $r_t \approx (S_t - S_{t-1})/S_{t-1}$, which is linear in $S_t$. The linear coding results also underpin **PCA**: principal components are linear combinations of returns, and the variance of each component is the eigenvalue — which follows directly from the $\text{Var}(aX) = a^2 \text{Var}(X)$ rule extended to vectors.
