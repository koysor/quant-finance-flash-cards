# Bessel's Correction

**Topic:** Statistics
**Tags:** Bessel's correction, degrees of freedom, sample variance, unbiased, bias
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Bessel's correction** is the use of $n-1$ rather than $n$ in the denominator of the sample variance formula. It corrects the downward bias that arises because the deviations are computed from the sample mean $\bar{X}$ — which is itself estimated from the data — rather than from the true population mean $\mu$.

## Key Formula

**Biased estimator** (divides by $n$):

$$\tilde{\sigma}^2 = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2, \qquad E[\tilde{\sigma}^2] = \frac{n-1}{n}\,\sigma^2$$

**Unbiased estimator** (Bessel's correction, divides by $n-1$):

$$s^2 = \frac{n}{n-1}\,\tilde{\sigma}^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2, \qquad E[s^2] = \sigma^2$$

**Intuition — degrees of freedom:** the $n$ deviations $(X_i - \bar{X})$ are not independent; they must sum to zero, so only $n-1$ carry independent information. Dividing by $n-1$ (the degrees of freedom) rather than $n$ accounts for this constraint.

## Example

Population: daily returns with $\sigma^2 = 4\,\%^2$. Sample size $n = 5$.

Expected value of the biased estimator: $E[\tilde{\sigma}^2] = \frac{4}{5} \times 4 = 3.2\,\%^2$ — underestimates by $0.8\,\%^2$.

Expected value with Bessel's correction: $E[s^2] = 4\,\%^2$ — correct on average.

The correction factor $n/(n-1) = 5/4 = 1.25$ grows with shrinking sample size: with $n=2$ the biased estimate is only half the true value; with $n = 100$ the correction is just 1%.

## Remember

Bessel's correction matters most when sample sizes are small — and in finance, many risk calculations use short rolling windows (10–30 days). The correction can be interpreted as a loss of one degree of freedom: using $\bar{X}$ to centre the data effectively "uses up" one observation's worth of information, leaving only $n-1$ independent pieces of information about spread. This same degree-of-freedom logic appears throughout statistics: in $t$-tests ($n-1$ d.f.), in regression residuals ($n-p$ d.f. where $p$ is the number of estimated parameters), and in the chi-squared test. Bessel's correction is the simplest instance of a general principle.
