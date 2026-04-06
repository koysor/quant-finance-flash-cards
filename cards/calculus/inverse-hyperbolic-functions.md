# Inverse Hyperbolic Functions

**Topic:** Calculus
**Tags:** arcsinh, arccosh, arctanh, inverse hyperbolic, logarithm, volatility models
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **inverse hyperbolic functions** are the inverses of $\sinh$, $\cosh$, and $\tanh$. Unlike inverse trig functions, they can be expressed in closed form using the natural logarithm — they are not genuinely new functions but convenient notation for certain logarithmic expressions.

## Key Formula

$$\text{arcsinh}(x) = \ln\!\left(x + \sqrt{x^2 + 1}\right), \quad x \in \mathbb{R}$$

$$\text{arccosh}(x) = \ln\!\left(x + \sqrt{x^2 - 1}\right), \quad x \geq 1$$

$$\text{arctanh}(x) = \frac{1}{2}\ln\!\left(\frac{1+x}{1-x}\right), \quad |x| < 1$$

**Derivatives:**

$$\frac{d}{dx}\text{arcsinh}(x) = \frac{1}{\sqrt{x^2+1}}, \qquad \frac{d}{dx}\text{arccosh}(x) = \frac{1}{\sqrt{x^2-1}}, \qquad \frac{d}{dx}\text{arctanh}(x) = \frac{1}{1-x^2}$$

**Fisher transformation** (arctanh applied to correlation):

$$z = \text{arctanh}(\rho) = \frac{1}{2}\ln\!\left(\frac{1+\rho}{1-\rho}\right)$$

## Example

**Fisher's $z$-transformation** maps a sample correlation $\hat{\rho} \in (-1, 1)$ to an approximately normally distributed statistic:

$$z = \text{arctanh}(\hat{\rho}) \approx \mathcal{N}\!\left(\text{arctanh}(\rho),\, \frac{1}{n-3}\right)$$

For $\hat{\rho} = 0.7$, $n = 50$:

$$z = \frac{1}{2}\ln\!\left(\frac{1.7}{0.3}\right) = \frac{1}{2}\ln(5.667) \approx 0.867$$

A 95% confidence interval for the true correlation is formed in $z$-space (where the distribution is approximately normal), then mapped back via $\tanh$. This is the standard method for hypothesis testing and confidence intervals on correlations in factor models.

## Remember

$\text{arctanh}$ is the most important inverse hyperbolic function in quantitative finance through the **Fisher $z$-transformation**. Testing whether two asset return correlations are significantly different, or constructing confidence intervals for a correlation matrix, requires mapping correlations (bounded in $(-1,1)$) to the unbounded real line where normal approximations apply. The Fisher transform does exactly this via $\text{arctanh}$. It appears in copula calibration, factor model diagnostics, and any statistical test involving sample correlations — making it far more practically relevant than its relatively obscure mathematical appearance might suggest.
