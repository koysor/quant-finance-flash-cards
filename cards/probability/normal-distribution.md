# Normal Distribution

**Topic:** Probability
**Level:** A Level Mathematics
**Tags:** distributions, probability, continuous
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

A continuous probability distribution that is symmetric about its mean. Described by two parameters:

- **μ** (mu) — the mean (centre of the distribution)
- **σ** (sigma) — the standard deviation (spread)

Notation: X ~ N(μ, σ²)

## Key Formula

The probability density function (PDF) is:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

The **standard normal** Z ~ N(0, 1) is obtained by standardising:

$$Z = \frac{X - \mu}{\sigma}$$

## Key Properties

| Property | Value |
|---|---|
| Mean | μ |
| Variance | σ² |
| Skewness | 0 |
| Kurtosis | 3 |

The **68–95–99.7 rule**: approximately 68%, 95%, and 99.7% of values lie within 1, 2, and 3 standard deviations of the mean.

## Example

A stock's daily returns are X ~ N(0.001, 0.02²).

What is the probability of a return below −0.04?

Standardise: Z = (−0.04 − 0.001) / 0.02 = −2.05

From Z-tables: P(Z < −2.05) ≈ 0.020 (i.e., roughly a 2% chance).

## Remember

The normal distribution is the cornerstone of classical finance. Asset returns are **often assumed** to be normally distributed, but in practice exhibit **fat tails** (excess kurtosis) — a key limitation to be aware of in risk management.
