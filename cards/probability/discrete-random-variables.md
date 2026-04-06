# Discrete Random Variables

**Topic:** Probability
**Tags:** discrete random variable, probability distribution, expectation, variance, DRV
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **discrete random variable** (DRV) $X$ takes a countable set of values $\{x_1, x_2, \ldots\}$ with associated probabilities $P(X = x_i) = p_i$, where $p_i \geq 0$ and $\sum_i p_i = 1$. The **probability distribution** is a complete listing of all possible values and their probabilities. The **expectation** $\mathbb{E}[X]$ is the probability-weighted average; the **variance** $\text{Var}(X)$ measures spread around the mean.

## Key Formula

**Expectation:**

$$\mathbb{E}[X] = \sum_i x_i \, p_i$$

**Variance:**

$$\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2, \qquad \mathbb{E}[X^2] = \sum_i x_i^2 \, p_i$$

**Standard deviation:** $\sigma = \sqrt{\text{Var}(X)}$

**Linear transformation:** $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$, $\quad \text{Var}(aX + b) = a^2 \text{Var}(X)$

## Example

A credit event pays £0, £50, or £200 with probabilities 0.7, 0.2, 0.1:

$$\mathbb{E}[X] = 0(0.7) + 50(0.2) + 200(0.1) = 0 + 10 + 20 = £30$$

$$\mathbb{E}[X^2] = 0 + 50^2(0.2) + 200^2(0.1) = 500 + 4000 = 4500$$

$$\text{Var}(X) = 4500 - 30^2 = 4500 - 900 = 3600, \quad \sigma = £60$$

The standard deviation (£60) is twice the mean (£30), indicating high relative uncertainty.

## Remember

Discrete random variables are the building blocks of every **pricing model with discrete payoffs**. A digital option (cash-or-nothing) is exactly a DRV: it pays a fixed amount $K$ with probability $p = N(d_2)$ or zero with probability $1 - p$, so its fair value is $\mathbb{E}[X] = K \cdot N(d_2)$. The variance formula $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ also underpins the **law of total variance** used in risk decomposition: total portfolio variance equals the average of conditional variances plus the variance of conditional means.
