# Chi-Squared Distribution

**Topic:** Probability
**Tags:** distributions, probability, continuous, variance, hypothesis testing
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The chi-squared distribution is the distribution of the sum of squares of $k$ independent standard normal random variables. It is described by one parameter:

- **k** — the degrees of freedom

Notation: $X \sim \chi^2(k)$

If $Z_1, Z_2, \ldots, Z_k$ are independent $N(0, 1)$ variables, then:

$$X = Z_1^2 + Z_2^2 + \cdots + Z_k^2 \sim \chi^2(k)$$

## Key Formula

The probability density function is:

$$f(x) = \frac{x^{k/2 - 1} e^{-x/2}}{2^{k/2}\,\Gamma(k/2)}, \quad x > 0$$

| Property | Value |
|---|---|
| Mean | $k$ |
| Variance | $2k$ |
| Skewness | $\sqrt{8/k}$ |

As $k$ increases, the distribution becomes more symmetric and approaches normality.

## Example

A sample of $n = 25$ daily returns has sample variance $s^2 = 0.0004$. To test whether the true variance equals $\sigma_0^2 = 0.0003$:

$$\chi^2 = \frac{(n - 1) s^2}{\sigma_0^2} = \frac{24 \times 0.0004}{0.0003} = 32.0$$

With 24 degrees of freedom, the 5% critical value is 36.4. Since $32.0 < 36.4$, we do not reject the null hypothesis — the observed variance is consistent with $\sigma_0^2$.

## Remember

The chi-squared distribution is essential for **testing volatility assumptions** in quantitative finance. When you estimate variance from a sample, the test statistic follows a chi-squared distribution — this lets you assess whether realised volatility has changed significantly. It also appears in the **likelihood ratio test**, used to compare nested models (e.g. GARCH variants), and in **goodness-of-fit tests** that check whether return distributions match a theoretical model.
