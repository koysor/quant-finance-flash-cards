# Probit Function

**Topic:** Probability
**Tags:** quantile, inverse CDF, phi, VaR, confidence level, z-score
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **probit function** $\Phi^{-1}(p)$ is the inverse of the standardised normal CDF. Given a probability $p \in (0, 1)$, it returns the unique value $z$ such that $\Phi(z) = p$. It converts a probability into a z-score — the number of standard deviations from the mean.

## Key Formula

$$z = \Phi^{-1}(p) \quad \text{where} \quad \Phi(z) = p$$

**Symmetry property:**

$$\Phi^{-1}(1 - p) = -\Phi^{-1}(p)$$

**Key quantiles used in finance:**

| Confidence level $p$ | $\Phi^{-1}(p)$ |
|---|---|
| $0.90$ | $1.282$ |
| $0.95$ | $1.645$ |
| $0.975$ | $1.960$ |
| $0.99$ | $2.326$ |
| $0.999$ | $3.090$ |

## Example

A portfolio has daily returns with mean $\mu = 0.0005$ and standard deviation $\sigma = 0.012$. Compute the 99% one-day Value at Risk.

The 1% quantile of the loss distribution uses $\Phi^{-1}(0.01) = -2.326$:

$$\text{VaR}_{99\%} = -(\mu + \sigma \times \Phi^{-1}(0.01)) = -(0.0005 + 0.012 \times (-2.326))$$

$$\text{VaR}_{99\%} = -(0.0005 - 0.02791) = 0.02741$$

The portfolio's 99% daily VaR is approximately 2.74% of its value.

## Remember

The probit function is the gateway between confidence levels and risk thresholds. Every parametric VaR calculation reduces to multiplying the portfolio volatility by a probit value: $\text{VaR}_\alpha = \sigma \times \Phi^{-1}(\alpha)$. Credit scoring models (logistic vs probit regression) use $\Phi^{-1}$ to map default probabilities to a latent normal variable — this is the foundation of the Gaussian copula model used in CDO pricing. The Basel regulatory framework specifies capital requirements using $\Phi^{-1}(0.999) = 3.090$ as the stress quantile, so a single evaluation of the probit function determines billions of pounds in bank capital buffers.
