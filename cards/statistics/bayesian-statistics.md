# Bayesian Statistics

**Topic:** Statistics
**Tags:** bayesian, prior, posterior, likelihood, parameter estimation, inference
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Bayesian statistics is a framework for updating beliefs about unknown parameters as new data arrives. It treats parameters as random variables with a **prior distribution** before data is observed, and combines the prior with the **likelihood** of the data to produce a **posterior distribution** that reflects updated beliefs.

## Key Formula

By Bayes' theorem applied to continuous parameters:

$$p(\theta \mid \text{data}) = \frac{p(\text{data} \mid \theta) \cdot p(\theta)}{p(\text{data})}$$

Where:
- $p(\theta)$ — **prior**: belief about parameter $\theta$ before seeing data
- $p(\text{data} \mid \theta)$ — **likelihood**: probability of observing the data given $\theta$
- $p(\theta \mid \text{data})$ — **posterior**: updated belief after observing data
- $p(\text{data})$ — **marginal likelihood** (normalising constant)

The posterior summarises all uncertainty about $\theta$ after incorporating the evidence:

$$\text{posterior} \propto \text{likelihood} \times \text{prior}$$

## Example

A trader believes a strategy's daily win rate $\theta$ is around 55%, modelled as a $\text{Beta}(11, 9)$ prior (mean = 0.55).

After observing 20 trades with 13 wins:

$$p(\theta \mid 13\text{ wins}) \propto \theta^{13}(1-\theta)^{7} \cdot \theta^{10}(1-\theta)^{8} = \theta^{23}(1-\theta)^{15}$$

The posterior is $\text{Beta}(24, 16)$, giving a posterior mean of $\frac{24}{40} = 0.60$.

The prior was updated from 55% to 60% win rate — the data shifted the estimate but the prior tempered the update.

## Remember

In the **Black-Litterman model**, Bayesian statistics is used directly in portfolio construction: investor views (the prior) are combined with market equilibrium returns (the likelihood) to produce a posterior expected-return vector, which then feeds into mean-variance optimisation. This prevents extreme, data-driven allocations by anchoring estimates to a structured prior.
