# Beta Distribution

**Topic:** Probability
**Tags:** beta distribution, bounded, conjugate prior, recovery rate, Bayesian
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Beta distribution** $\text{Beta}(\alpha, \beta)$ is a continuous distribution on $[0, 1]$, parameterised by two positive shape parameters $\alpha$ and $\beta$. Its flexibility makes it ideal for modelling probabilities and proportions — quantities bounded between 0 and 1. It is the **conjugate prior** for the Bernoulli and binomial likelihood in Bayesian inference.

## Key Formula

**PDF:**

$$f(x; \alpha, \beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, \quad x \in [0,1]$$

where the **Beta function** $B(\alpha,\beta) = \dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.

**Mean and variance:**

$$\mathbb{E}[X] = \frac{\alpha}{\alpha+\beta}, \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$$

**Shape:** $\alpha = \beta = 1$ gives the Uniform[0,1]; $\alpha, \beta > 1$ gives a unimodal bell shape; $\alpha < 1$ or $\beta < 1$ gives a U-shape.

## Example

A bank estimates recovery rates on defaulted loans. Historical data shows 40% average recovery with moderate dispersion. Fitting $\text{Beta}(\alpha, \beta)$:

$$\frac{\alpha}{\alpha+\beta} = 0.40 \implies \beta = 1.5\alpha$$

With $\alpha = 2$, $\beta = 3$: Var $= \frac{6}{25 \times 6} = 0.04$, so $\sigma \approx 20\%$. This is used as the recovery rate distribution in Monte Carlo CDO simulation.

## Remember

The Beta distribution is the standard model for **loss given default (LGD)** in credit risk. Regulatory capital (Basel IRB) requires banks to estimate LGD as a probability-weighted average, but the **distribution** of LGD — bounded in $[0,1]$ and typically right-skewed — is Beta. The conjugate prior property is used in **Bayesian credit models**: starting from a $\text{Beta}(\alpha, \beta)$ prior on PD, observing $k$ defaults in $n$ trials, the posterior is $\text{Beta}(\alpha + k, \beta + n - k)$ — updating beliefs without refitting the entire model.
