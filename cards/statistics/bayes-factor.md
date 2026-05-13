# Bayes Factor

**Topic:** Statistics
**Tags:** bayesian, model comparison, hypothesis testing, evidence, model selection
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Bayes factor is a ratio that quantifies the evidence that data provides in favour of one statistical model over another. It compares how likely the observed data is under each model, without requiring the models to be nested or a fixed significance level.

## Key Formula

For two competing models $M_1$ and $M_2$, the Bayes factor $B_{12}$ is:

$$B_{12} = \frac{P(\text{data} \mid M_1)}{P(\text{data} \mid M_2)} = \frac{\int P(\text{data} \mid \theta, M_1)\, p(\theta \mid M_1)\, d\theta}{\int P(\text{data} \mid \theta, M_2)\, p(\theta \mid M_2)\, d\theta}$$

It updates the prior odds to produce the posterior odds:

$$\underbrace{\frac{P(M_1 \mid \text{data})}{P(M_2 \mid \text{data})}}_{\text{posterior odds}} = B_{12} \times \underbrace{\frac{P(M_1)}{P(M_2)}}_{\text{prior odds}}$$

**Jeffreys' scale** for interpreting $B_{12}$:

| $B_{12}$ | Evidence for $M_1$ |
|---|---|
| 1–3 | Weak |
| 3–10 | Moderate |
| 10–100 | Strong |
| $>100$ | Decisive |

## Example

A quant compares two return models: $M_1$ (GARCH with Student-$t$ errors) vs $M_2$ (GARCH with normal errors). After fitting to 500 days of S&P 500 returns, the marginal likelihoods are $P(\text{data} \mid M_1) = 10^{-847}$ and $P(\text{data} \mid M_2) = 10^{-861}$.

$$B_{12} = \frac{10^{-847}}{10^{-861}} = 10^{14} \approx 10^{14}$$

A Bayes factor of $10^{14}$ is decisive: the data strongly favour fat-tailed errors over the normal distribution.

## Remember

Unlike classical hypothesis testing, the Bayes factor can provide evidence **in favour of** the null model — a p-value can only reject it. This makes Bayes factors useful in quantitative finance when comparing factor models: for instance, deciding whether adding a fifth factor (e.g., profitability) to the Fama-French four-factor model is justified by the data, without the multiple-comparison problems that plague sequential t-tests.
