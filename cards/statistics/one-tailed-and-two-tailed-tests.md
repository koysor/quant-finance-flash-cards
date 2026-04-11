# One-Tailed and Two-Tailed Tests

**Topic:** Statistics
**Tags:** one-tailed, two-tailed, hypothesis testing, directional, p-value, significance
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **one-tailed test** (one-sided) tests whether a parameter is specifically **greater than** or **less than** a reference value — the alternative hypothesis has a direction. A **two-tailed test** (two-sided) tests whether a parameter is **different from** a reference value in either direction. One-tailed tests have more power against the specified direction but cannot detect deviations in the opposite direction; two-tailed tests are more conservative but symmetric.

## Key Formula

Let $z$ be the test statistic under $H_0: \mu = \mu_0$.

**Two-tailed** $H_1: \mu \neq \mu_0$:

$$p = 2\,\Phi(-|z|), \qquad \text{reject if } |z| > z_{\alpha/2}$$

**Upper one-tailed** $H_1: \mu > \mu_0$:

$$p = 1 - \Phi(z), \qquad \text{reject if } z > z_\alpha$$

**Lower one-tailed** $H_1: \mu < \mu_0$:

$$p = \Phi(z), \qquad \text{reject if } z < -z_\alpha$$

At $\alpha = 5\%$: two-tailed critical value $z_{0.025} = 1.96$; one-tailed critical value $z_{0.05} = 1.645$.

## Example

A quant tests whether a new execution algorithm reduces market impact. The null is $H_0: \mu_{\text{impact}} = 0$ bps improvement.

**Two-tailed** $H_1: \mu \neq 0$: appropriate if we want to detect any change (improvement or deterioration). Reject at 5% if $|z| > 1.96$.

**Upper one-tailed** $H_1: \mu > 0$: appropriate if we only care whether the algorithm helps (we would not deploy an algorithm that increases impact). Reject at 5% if $z > 1.645$.

With $z = 1.75$: two-tailed $p = 0.080$ (fail to reject); one-tailed $p = 0.040$ (reject). The choice of tail matters.

## Remember

The choice between one- and two-tailed tests must be made **before seeing the data** — choosing after seeing the result inflates Type I error. In quantitative finance, **one-tailed tests are appropriate for strategies where only one direction of the alternative is actionable**: testing whether a factor has a positive return premium (we would not use a factor with a negative premium), or whether VaR model exceedances are too frequent (too few exceedances is not a problem). **Two-tailed tests are appropriate for model validation**: testing whether regression residuals have zero mean, whether a correlation is non-zero, or whether two risk models give the same VaR estimates.
