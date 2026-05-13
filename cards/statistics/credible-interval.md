# Credible Interval

**Topic:** Statistics
**Tags:** credible interval, bayesian, posterior, uncertainty, highest posterior density, risk estimation
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **credible interval** (also called a Bayesian confidence interval) is the range of parameter values that contains a specified posterior probability. A 95% credible interval means there is a 95% probability — given the data and prior — that the true parameter lies within that range.

## Key Formula

For posterior density $p(\theta \mid \text{data})$, the $100(1-\alpha)\%$ highest posterior density (HPD) interval $[a, b]$ satisfies:

$$\int_a^b p(\theta \mid \text{data})\, d\theta = 1 - \alpha$$

where $[a, b]$ is chosen to be the shortest interval achieving this coverage.

## Example

An analyst models daily VaR using a Bayesian Normal model. After 250 trading days of return data, the posterior for the 99th-percentile loss is $\mathcal{N}(\mu = -2.1\%, \sigma^2 = 0.04\%)$. The 95% credible interval is approximately:

$$[-2.1\% \pm 1.96 \times 0.2\%] = [-2.49\%,\; -1.71\%]$$

This means there is a 95% posterior probability that true daily VaR lies between $-2.49\%$ and $-1.71\%$ — a direct probability statement about the parameter, not about future samples.

## Remember

Credible intervals answer the question a risk manager actually wants answered: "What is the probability that the true VaR is above my regulatory threshold?" A frequentist 95% confidence interval cannot answer this — it only guarantees that 95% of intervals constructed by the same procedure contain the true value over many repetitions, not that any specific interval does. In model validation and Bayesian stress testing, credible intervals are used to quantify parameter uncertainty around loss estimates, directly informing whether a bank's capital buffer is adequate given estimation error.
