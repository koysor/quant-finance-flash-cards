# Normalisation Constant

**Topic:** Probability
**Tags:** normalisation constant, PDF, probability density, Bayes theorem, partition function, density
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **normalisation constant** is the scalar that divides an unnormalised non-negative function so that it integrates (or sums) to one, making it a valid probability density or mass function. It ensures the total probability is exactly 1. In Bayesian inference it is the marginal likelihood (evidence), which normalises the posterior distribution.

## Key Formula

For a continuous unnormalised function $\tilde{f}(x) \geq 0$:

$$Z = \int_{-\infty}^{\infty} \tilde{f}(x)\,dx, \qquad f(x) = \frac{\tilde{f}(x)}{Z}$$

**Bayes' theorem** written with the normalisation constant explicit:

$$\underbrace{p(\theta \mid x)}_{\text{posterior}} = \frac{\underbrace{p(x \mid \theta)}_{\text{likelihood}} \cdot \underbrace{p(\theta)}_{\text{prior}}}{\underbrace{\int p(x \mid \theta)\,p(\theta)\,d\theta}_{Z = \text{normalisation constant}}}$$

## Example

The standard normal density: $\tilde{f}(x) = e^{-x^2/2}$ is non-negative but integrates to $\sqrt{2\pi}$. The normalisation constant is $Z = \sqrt{2\pi}$, giving the valid PDF $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.

## Remember

In Bayesian parameter estimation for financial models (e.g. fitting a volatility model to returns), computing the normalisation constant $Z = \int p(\text{data}\mid\theta)\,p(\theta)\,d\theta$ often requires high-dimensional numerical integration that is analytically intractable. This is why Markov Chain Monte Carlo (MCMC) methods are used: they sample from the posterior proportional to $p(\text{data}\mid\theta)\cdot p(\theta)$ without ever computing $Z$, making Bayesian calibration of complex models feasible.
