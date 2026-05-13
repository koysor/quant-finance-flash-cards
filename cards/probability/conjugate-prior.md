# Conjugate Prior

**Topic:** Probability
**Tags:** conjugate prior, bayesian inference, prior, posterior, beta distribution, analytical tractability
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **conjugate prior** is a prior distribution chosen so that the posterior distribution belongs to the same parametric family as the prior. When the likelihood and prior are conjugate, the Bayesian update has an analytic closed form — no numerical integration or MCMC is required.

## Key Formula

For a Binomial likelihood with success probability $p$ and a Beta prior:

$$p \sim \text{Beta}(\alpha, \beta) \xrightarrow{\text{observe } k \text{ successes in } n \text{ trials}} p \mid \text{data} \sim \text{Beta}(\alpha + k,\; \beta + n - k)$$

The posterior parameters update by simply adding the observed counts to the prior hyperparameters.

## Example

A credit analyst models the probability $p$ of default for a bond. Prior belief: $p \sim \text{Beta}(2, 18)$, implying a prior mean of $\frac{2}{20} = 10\%$. Over one year, 3 defaults are observed in 50 issuers. The posterior is:

$$p \mid \text{data} \sim \text{Beta}(2 + 3,\; 18 + 47) = \text{Beta}(5, 65)$$

Posterior mean $= \frac{5}{70} \approx 7.1\%$ — the data (6% empirical rate) pulls the estimate down from the 10% prior, weighted by the relative strength of evidence.

## Remember

Conjugate priors are the practical workhorse of Bayesian credit and actuarial models because they eliminate the computational cost of posterior estimation. The Beta–Binomial conjugate pair is used to update probability-of-default estimates as new default data arrives; the Normal–Normal conjugate is used in the Black–Litterman model to combine CAPM equilibrium returns (the prior) with investor views (the likelihood). Without conjugacy, the posterior update would require MCMC sampling — tractable for research but too slow for daily risk systems.
