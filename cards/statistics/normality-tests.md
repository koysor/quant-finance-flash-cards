# Normality Tests

**Topic:** Statistics
**Tags:** normality, hypothesis testing, goodness of fit, Shapiro-Wilk, Anderson-Darling, diagnostics
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Normality tests are statistical hypothesis tests that assess whether a data sample is consistent with having been drawn from a normal distribution. The null hypothesis is always $H_0$: the data are normally distributed; rejection indicates a significant departure that may invalidate models built on the normality assumption.

## Key Formula

**Shapiro-Wilk statistic** (most powerful for $n < 50$):

$$W = \frac{\left(\displaystyle\sum_{i=1}^{n} a_i\, x_{(i)}\right)^2}{\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

Where $x_{(i)}$ are the ordered sample values and $a_i$ are tabulated constants derived from the expected order statistics of the standard normal. $W$ ranges from 0 to 1; values close to 1 support normality.

**Comparison of common tests:**

| Test | Best for | Sensitive to |
|---|---|---|
| **Shapiro-Wilk** | Small samples ($n < 50$) | Overall shape |
| **Jarque-Bera** | Large samples ($n > 100$) | Skewness and kurtosis only |
| **Anderson-Darling** | Any size; emphasis on tails | Tail departures |
| **Kolmogorov-Smirnov** | Any distribution (not just normal) | Body of distribution |

**Python:**

```python
from scipy import stats

w_stat, p_sw  = stats.shapiro(returns)          # Shapiro-Wilk
ad_stat, crit, sig = stats.anderson(returns)    # Anderson-Darling
ks_stat, p_ks = stats.kstest(returns, 'norm',   # KS test
    args=(returns.mean(), returns.std()))
```

## Example

A risk analyst tests 30 daily log-returns ($n = 30$) against normality. Jarque-Bera is unreliable at this sample size (it requires large $n$ for the $\chi^2$ approximation to hold). Shapiro-Wilk gives $W = 0.91$, $p = 0.023$: reject normality at the 5% level. Anderson-Darling confirms the result, with the statistic exceeding the 5% critical value, with the tail emphasis revealing the culprit — two extreme observations pulling the tails heavier than normal.

## Remember

For financial return data, the choice of normality test depends on sample size and what type of departure matters most. **Jarque-Bera** is the standard for long daily return series (years of data) because it directly targets skewness and excess kurtosis — the precise departures that cause parametric VaR to underestimate tail losses. **Anderson-Darling** is preferred when tail behaviour is the primary concern, such as validating extreme value models or stress test assumptions, because it down-weights central observations and up-weights the tails relative to KS.
