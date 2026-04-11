# Chi-Squared Test

**Topic:** Statistics
**Tags:** chi-squared, goodness of fit, independence, categorical, contingency table, observed, expected
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **chi-squared test** is used for two purposes: (1) **goodness-of-fit** — testing whether observed categorical frequencies match a specified theoretical distribution; (2) **test of independence** — testing whether two categorical variables are associated in a contingency table. Both use the same chi-squared test statistic, which compares observed counts $O_i$ to expected counts $E_i$ under $H_0$.

## Key Formula

**Test statistic:**

$$\chi^2 = \sum_{i} \frac{(O_i - E_i)^2}{E_i}$$

Under $H_0$, $\chi^2 \sim \chi^2_\nu$ where $\nu$ is the degrees of freedom.

**Goodness-of-fit:** $\nu = k - 1 - p$ where $k$ = number of categories, $p$ = estimated parameters.

**Independence ($r \times c$ table):** $\nu = (r-1)(c-1)$, expected cell count $E_{ij} = \frac{(\text{row total}_i)(\text{col total}_j)}{n}$.

**Rule of thumb:** all expected counts should be $\geq 5$; merge cells if necessary.

## Example

A risk model predicts returns follow $N(0, \sigma^2)$. Over 250 days, observed vs expected counts in 5 tail buckets:

| Region | Observed | Expected |
|---|---|---|
| $< -2\sigma$ | 12 | 5.7 |
| $-2\sigma$ to $-\sigma$ | 25 | 54.0 |
| $-\sigma$ to $+\sigma$ | 172 | 170.5 |
| $+\sigma$ to $+2\sigma$ | 30 | 54.0 |
| $> +2\sigma$ | 11 | 5.7 |

$$\chi^2 \approx \frac{(12-5.7)^2}{5.7} + \ldots \approx 48.4 > \chi^2_{4,\,0.001} = 18.5$$

Strongly reject normality — the model underestimates tail frequency.

## Remember

The chi-squared goodness-of-fit test is the statistical foundation of **VaR model backtesting via the traffic light framework**: the Basel approach counts exceedances and effectively performs a chi-squared test on tail frequency. The independence test appears in **credit portfolio validation** — testing whether obligor defaults are independent across sectors (cells of a sector × default contingency table). A significant chi-squared test of independence means **correlation in defaults exists**, requiring a copula model rather than independent-default assumption. Large $\chi^2$ values in either test are a model validation red flag.
