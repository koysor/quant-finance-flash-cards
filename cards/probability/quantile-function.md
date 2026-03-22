# Quantile Function

**Topic:** Probability
**Tags:** quantile, inverse CDF, VaR, percentile, risk measurement
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **quantile function** $Q(p) = F^{-1}(p)$ is the inverse of the CDF: given a probability $p \in (0,1)$, it returns the value $x$ such that $P(X \le x) = p$. It maps probabilities back to outcomes and is the mathematical foundation of percentiles, Value at Risk, and Monte Carlo simulation via inverse transform sampling.

## Key Formula

$$Q(p) = F^{-1}(p) = \inf\{x : F(x) \ge p\}$$

For the **standard normal** distribution:

$$Q(p) = \Phi^{-1}(p)$$

For a **general normal** $X \sim N(\mu, \sigma^2)$:

$$Q(p) = \mu + \sigma\,\Phi^{-1}(p)$$

**Common quantiles** (standard normal):

| $p$ | $Q(p)$ | Use |
|---|---|---|
| $0.01$ | $-2.326$ | 99% VaR |
| $0.05$ | $-1.645$ | 95% VaR |
| $0.50$ | $0$ | Median |
| $0.95$ | $1.645$ | 95th percentile |

## Example

A portfolio has daily returns $X \sim N(0.05\%, 1.5\%)$. Find the 99% VaR (1-day).

VaR at confidence $\alpha$ is the negative of the $1 - \alpha$ quantile:

$$\text{VaR}_{99\%} = -Q(0.01) = -(\mu + \sigma \times \Phi^{-1}(0.01))$$

$$= -(0.0005 + 0.015 \times (-2.326)) = -(0.0005 - 0.0349) = 0.0344$$

The 99% 1-day VaR is **3.44%** of portfolio value.

## Remember

The quantile function is how risk managers translate a confidence level into a monetary loss figure — VaR is literally a quantile of the loss distribution. It also powers Monte Carlo simulation: drawing $U \sim \text{Uniform}(0,1)$ and computing $X = F^{-1}(U)$ produces a sample from any target distribution (inverse transform sampling). In stress testing, regulators specify extreme quantiles (99.9% for Basel IRB capital) that sit deep in the tail, where the accuracy of the distributional assumption matters enormously — this is why fat-tailed distributions give materially different VaR figures than the normal.
