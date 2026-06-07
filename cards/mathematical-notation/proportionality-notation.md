# Proportionality Notation

**Topic:** Mathematical Notation
**Tags:** notation, proportionality, bayesian, density, scaling, inference
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The symbol **$\propto$** (read "is proportional to") means two quantities have a fixed ratio: $f(x) \propto g(x)$ means $f(x) = c \cdot g(x)$ for some positive constant $c$ that does not depend on $x$. It is used whenever the exact normalisation constant is unknown, irrelevant, or inconvenient to compute — particularly in Bayesian statistics, where the normalisation integral is often intractable.

## Key Formula

$$f(x) \propto g(x) \iff f(x) = c \cdot g(x) \text{ for some constant } c > 0$$

The most important application in quantitative finance is **Bayes' theorem in proportionality form**:

$$\underbrace{p(\theta \mid \text{data})}_{\text{posterior}} \propto \underbrace{p(\text{data} \mid \theta)}_{\text{likelihood}} \times \underbrace{p(\theta)}_{\text{prior}}$$

The normalising constant is $p(\text{data}) = \int p(\text{data} \mid \theta)\,p(\theta)\,d\theta$ — often intractable — but it does not depend on $\theta$, so it can be absorbed into $\propto$ when the goal is only to find the shape of the posterior or its mode.

**Log form** (used in maximum likelihood and MAP estimation):

$$\log p(\theta \mid \text{data}) = \log p(\text{data} \mid \theta) + \log p(\theta) + \text{const}$$

## Example

Calibrating a GBM drift $\mu$ from observed log-returns $r_1, \ldots, r_n \sim N(\mu - \tfrac{1}{2}\sigma^2, \sigma^2)$ with a Gaussian prior $\mu \sim N(\mu_0, \tau^2)$:

$$p(\mu \mid \mathbf{r}) \propto \underbrace{\prod_{i=1}^n \exp\!\left(-\frac{(r_i - \mu + \frac{1}{2}\sigma^2)^2}{2\sigma^2}\right)}_{\text{likelihood}} \times \underbrace{\exp\!\left(-\frac{(\mu - \mu_0)^2}{2\tau^2}\right)}_{\text{prior}}$$

Completing the square in $\mu$ gives a Gaussian posterior — the $\propto$ symbol lets you drop the $(2\pi)^{n/2}\sigma^n$ term from the likelihood and the $1/\sqrt{2\pi\tau^2}$ from the prior without keeping track of them, because they are constants with respect to $\mu$.

The posterior mean is the precision-weighted average:

$$\hat{\mu}_{\text{posterior}} = \frac{\bar{r}/\sigma^2 + \mu_0/\tau^2}{n/\sigma^2 + 1/\tau^2}$$

## Remember

The $\propto$ symbol is the CQF shorthand for "I will find the normalisation constant later — or I do not need it." In **Bayesian parameter estimation** for financial models (volatility, drift, mean-reversion speed), the posterior is almost always written in proportionality form because the evidence integral $p(\text{data})$ is a high-dimensional integral with no closed form. Dropping it with $\propto$ focuses attention on the functional form of the posterior rather than its absolute value. In **importance sampling**, the optimal proposal is $q^*(x) \propto \lvert f(x)\rvert\,p(x)$ — again a proportionality statement, because the exact normalisation is unknown but the shape determines where to concentrate simulation effort. Seeing $\propto$ in a derivation is a signal to ask: "what is being held constant here, and why does its exact value not matter?"
