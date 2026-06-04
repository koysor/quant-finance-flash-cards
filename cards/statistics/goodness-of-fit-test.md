# Goodness-of-Fit Test

**Topic:** Statistics
**Tags:** goodness-of-fit, chi-squared, kolmogorov-smirnov, distribution testing, model validation
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A goodness-of-fit test measures how well observed data matches a hypothesised probability distribution. It produces a test statistic and p-value that quantify the evidence against the null hypothesis that the data came from the specified distribution.

## Key Formula

**Chi-squared goodness-of-fit statistic:**

$$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$

where $O_i$ is the observed frequency in bin $i$, $E_i = n \cdot p_i$ is the expected frequency under the null distribution, and the statistic follows a $\chi^2$ distribution with $k - 1 - m$ degrees of freedom ($m$ = number of estimated parameters).

**Kolmogorov-Smirnov statistic** (for continuous distributions):

$$D_n = \sup_x \lvert F_n(x) - F_0(x) \rvert$$

where $F_n$ is the empirical CDF and $F_0$ is the hypothesised CDF. Reject $H_0$ if $D_n$ exceeds the critical value from KS tables.

## Example

A risk analyst fits a normal distribution to 250 daily equity returns ($\hat{\mu} = 0.04\%$, $\hat{\sigma} = 1.1\%$) and runs a Jarque-Bera test. The test statistic is 18.3 with a p-value of 0.0001, far below the 5% threshold. The analyst rejects normality and switches to a Student's $t$-distribution with estimated degrees of freedom $\hat{\nu} = 5$ before computing parametric VaR.

## Remember

Goodness-of-fit tests are the gateway check before relying on any parametric model in finance. If equity returns fail a normality test, the parametric VaR formula — which assumes returns are normally distributed — will systematically underestimate tail losses. Regulators require model validation under **FRTB**, and a failed goodness-of-fit test is one of the signals that triggers a review of a bank's internal model approval status.
