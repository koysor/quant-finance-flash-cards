# Sample Size Determination

**Topic:** Statistics
**Tags:** sample size, power, effect size, margin of error, confidence interval, study design
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Sample size determination** is the pre-study calculation of the minimum number of observations required to achieve a desired statistical power or confidence interval width. It balances two competing objectives: sufficient power to detect meaningful effects, and practical constraints on data collection cost. Underpowered studies produce unreliable results; oversized studies waste resources.

## Key Formula

**For a one-sample $z$-test** (two-tailed, target power $1-\beta$):

$$n = \left(\frac{(z_{\alpha/2} + z_\beta)\sigma}{\delta}\right)^2$$

where $\delta = \mu_1 - \mu_0$ is the minimum detectable effect.

**For a confidence interval of half-width $E$:**

$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$$

**For a proportion** (binomial, target margin of error $E$):

$$n = \frac{z_{\alpha/2}^2 \, p(1-p)}{E^2}$$

Use $p = 0.5$ (worst case) if the proportion is unknown.

**Common values:** $z_{0.025} = 1.96$ ($\alpha = 5\%$, two-tailed), $z_{0.20} = 0.842$ (80% power), $z_{0.10} = 1.282$ (90% power).

## Example

A bank wants a 95% confidence interval for the mean loan default rate, with margin of error $\pm 0.5\%$. Historical $\sigma \approx 5\%$.

$$n = \left(\frac{1.96 \times 5\%}{0.5\%}\right)^2 = \left(\frac{9.8\%}{0.5\%}\right)^2 = 19.6^2 \approx 384 \text{ loans}$$

To halve the margin of error to $\pm 0.25\%$ requires $4 \times 384 = 1{,}536$ loans — quadrupling sample size halves precision.

## Remember

Sample size determination is the quantitative link between **statistical power, effect size, and data requirements** in financial research. The quadratic relationship $n \propto 1/\delta^2$ explains why detecting small alpha signals requires enormous backtesting periods. In **regulatory stress testing**, sample size calculations determine how many scenarios are needed to achieve reliable CVaR estimates — EIOPA and PRA require sufficient sample depth to estimate the 1-in-200 loss, which requires hundreds of independent scenarios. The formula also shows why **variance reduction techniques** (antithetic variates, stratified sampling) are powerful: halving $\sigma^2$ halves the required $n$.
