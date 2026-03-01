# Poisson Distribution

**Topic:** Probability
**Tags:** distributions, probability, discrete, poisson, counting

---

## Definition

The Poisson distribution models the number of events occurring in a fixed interval of time or space, given that events happen independently at a constant average rate. It is described by one parameter:

- **λ** (lambda) — the average number of events per interval

Notation: $X \sim \text{Poisson}(\lambda)$

## Key Formula

The probability of exactly $k$ events is:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

| Property | Value |
|---|---|
| Mean | $\lambda$ |
| Variance | $\lambda$ |
| Skewness | $1 / \sqrt{\lambda}$ |

A key feature: the mean equals the variance.

## Example

A stock experiences an average of 2 jump events per year ($\lambda = 2$). What is the probability of observing exactly 3 jumps in a year?

$$P(X = 3) = \frac{2^3 e^{-2}}{3!} = \frac{8 \times 0.1353}{6} \approx 0.180$$

There is roughly an 18% chance of exactly 3 jumps.

## Remember

The Poisson distribution is central to **jump-diffusion models** (e.g. Merton's model), where sudden price jumps arrive as a Poisson process layered on top of continuous Brownian motion. It is also used in **credit risk** to model the number of defaults in a portfolio over a given period — if defaults are rare and independent, the Poisson is the natural choice.
