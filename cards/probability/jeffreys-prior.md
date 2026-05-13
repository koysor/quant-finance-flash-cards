# Jeffreys Prior

**Topic:** Probability
**Tags:** jeffreys prior, non-informative prior, bayesian, invariance, fisher information, objective bayes
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **Jeffreys prior** is a non-informative prior distribution proportional to the square root of the determinant of the Fisher information matrix. It is the unique prior that is invariant under reparametrisation — if you transform the parameter, the Jeffreys prior transforms consistently, unlike an arbitrary flat prior.

## Key Formula

For a model with parameter $\theta$ and log-likelihood $\ell(\theta)$, the Jeffreys prior is:

$$p(\theta) \propto \sqrt{I(\theta)}, \qquad I(\theta) = -\mathbb{E}\!\left[\frac{\partial^2 \ell(\theta)}{\partial \theta^2}\right]$$

where $I(\theta)$ is the Fisher information. For the Binomial model with success probability $p$, $I(p) = \frac{1}{p(1-p)}$, so the Jeffreys prior is $\text{Beta}(\tfrac{1}{2}, \tfrac{1}{2})$.

## Example

A risk manager wants to estimate the probability of default $p$ from 20 historical observations with no prior view. A flat prior $p \sim \text{Uniform}(0,1)$ assigns equal density to $p = 0.01$ and $p = 0.5$, but these are not equivalent: a flat prior on $p$ becomes a non-flat prior after the logit transform $\log\frac{p}{1-p}$. The Jeffreys prior $\text{Beta}(\tfrac{1}{2}, \tfrac{1}{2})$ is flat on the logit scale and on the original scale simultaneously, giving an estimate that does not depend on how the problem is parameterised.

## Remember

The Jeffreys prior solves the "reference prior" problem in quantitative finance: when calibrating models to limited data (e.g. default frequencies for rare rating grades, or jump intensities from short return histories), analysts need a prior that expresses ignorance without inadvertently favouring certain parameterisations. A flat prior on volatility $\sigma$ is non-flat on variance $\sigma^2$ — it implicitly encodes a belief. The Jeffreys prior is the principled, parameter-free starting point before any market data arrives.
