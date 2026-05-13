# Posterior Predictive Distribution

**Topic:** Probability
**Tags:** posterior predictive, bayesian, parameter uncertainty, scenario generation, forecasting, integration
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **posterior predictive distribution** is the distribution of a future observation $\tilde{y}$ after integrating out model parameters weighted by the posterior. It propagates full parameter uncertainty into forecasts, rather than conditioning on a single point estimate.

## Key Formula

$$p(\tilde{y} \mid \text{data}) = \int p(\tilde{y} \mid \theta)\, p(\theta \mid \text{data})\, d\theta$$

The future observation $\tilde{y}$ is averaged over all plausible parameter values $\theta$, each weighted by its posterior probability $p(\theta \mid \text{data})$.

## Example

A quant estimates a GARCH volatility model and obtains a posterior distribution over the persistence parameter $\beta \in [0.85, 0.96]$ rather than a single point estimate. The posterior predictive distribution of tomorrow's 1-day VaR is found by simulating returns for each sampled $\beta$ and averaging the resulting loss distributions. The result is a heavier-tailed predictive distribution than any single-$\beta$ model would produce, because the uncertainty in $\beta$ adds an extra source of variance beyond the model's own randomness.

## Remember

Most quantitative risk models report VaR or CVaR conditional on a single calibrated parameter set — the point estimate. The posterior predictive distribution is the Bayesian answer to "what should we actually forecast?": it incorporates estimation uncertainty so that rare but plausible parameter combinations contribute to tail predictions. This is directly relevant to regulatory stress testing, where parameter uncertainty is a recognised source of model risk that must be quantified rather than assumed away.
