# Gamma Distribution

**Topic:** Probability
**Tags:** gamma distribution, shape, rate, waiting time, loss severity, chi-squared
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gamma distribution** $\text{Gamma}(\alpha, \beta)$ is a continuous distribution on $(0, \infty)$ parameterised by shape $\alpha > 0$ and rate $\beta > 0$ (or equivalently scale $\theta = 1/\beta$). It generalises the exponential distribution ($\alpha = 1$) and arises as the sum of $\alpha$ independent exponential random variables. The chi-squared distribution is a special case: $\chi^2_k = \text{Gamma}(k/2, 1/2)$.

## Key Formula

**PDF:**

$$f(x; \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0$$

**Mean and variance:**

$$\mathbb{E}[X] = \frac{\alpha}{\beta}, \qquad \text{Var}(X) = \frac{\alpha}{\beta^2}$$

**Reproductive property:** if $X_i \sim \text{Gamma}(\alpha_i, \beta)$ independently, then $\sum X_i \sim \text{Gamma}(\sum \alpha_i, \beta)$.

**MGF:** $M(t) = \left(\frac{\beta}{\beta - t}\right)^\alpha$ for $t < \beta$.

## Example

Insurance claim severities are modelled with $\text{Gamma}(2, 0.5)$ (shape 2, rate 0.5):

$$\mathbb{E}[X] = 2/0.5 = 4 \text{ (£k)}, \qquad \text{Var}(X) = 2/0.25 = 8, \quad \sigma \approx £2.83\text{k}$$

The total loss from 10 independent claims $\sim \text{Gamma}(20, 0.5)$ by the reproductive property, with mean £40k.

## Remember

The Gamma distribution is the workhorse for **loss severity modelling** in insurance, operational risk, and credit. Under Basel Advanced Measurement Approach (AMA), operational risk losses are often modelled with Gamma or lognormal severity distributions combined with Poisson frequency distributions — the resulting **compound distribution** gives total annual loss. The chi-squared connection means every regression test statistic (F-test, likelihood ratio test) ultimately traces back to sums of squared normals, which are Gamma-distributed — linking the Gamma directly to the core of statistical inference in finance.
