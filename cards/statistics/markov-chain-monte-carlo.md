# Markov Chain Monte Carlo

**Topic:** Statistics
**Tags:** MCMC, bayesian, simulation, sampling, posterior, monte carlo
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Markov Chain Monte Carlo (MCMC) is a class of algorithms that generate samples from a probability distribution — typically a Bayesian posterior — that is too complex to sample directly. A Markov chain is constructed whose stationary distribution equals the target distribution; running the chain long enough produces samples that approximate it.

## Key Formula

The **Metropolis-Hastings** algorithm accepts a proposed move from $\theta$ to $\theta^*$ with probability:

$$\alpha = \min\!\left(1,\; \frac{p(\theta^* \mid \text{data})\; q(\theta \mid \theta^*)}{p(\theta \mid \text{data})\; q(\theta^* \mid \theta)}\right)$$

Where $q(\cdot \mid \cdot)$ is the proposal distribution and $p(\theta \mid \text{data})$ is the (unnormalised) posterior. Because only the **ratio** of posteriors is needed, the normalisation constant — often intractable — cancels out:

$$\frac{p(\theta^* \mid \text{data})}{p(\theta \mid \text{data})} = \frac{p(\text{data} \mid \theta^*)\, p(\theta^*)}{p(\text{data} \mid \theta)\, p(\theta)}$$

## Example

A risk manager fits a Bayesian VaR model to daily returns, with a Student-$t$ likelihood and a prior on degrees of freedom $\nu \sim \text{Uniform}(2, 30)$. The posterior $p(\nu \mid \text{returns})$ has no closed form. Running 10,000 MCMC iterations (after 1,000 burn-in steps) yields a histogram of $\nu$ samples centred near 4 — confirming fat tails — with a 95% credible interval of $[2.8,\; 6.1]$.

## Remember

MCMC is what makes Bayesian methods practical for quantitative finance. When calibrating complex models — multi-factor credit models, stochastic volatility models, or the Black-Litterman posterior — the posterior distribution over parameters is analytically intractable. MCMC replaces the impossible integral with a large sample, turning Bayesian inference from a theoretical ideal into a computationally feasible tool for risk and pricing.
