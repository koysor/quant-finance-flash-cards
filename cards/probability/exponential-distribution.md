# Exponential Distribution

**Topic:** Probability
**Tags:** distributions, probability, continuous, exponential, survival
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

The exponential distribution models the time between events in a Poisson process — the waiting time until the next event occurs. It is described by one parameter:

- **λ** (lambda) — the rate parameter (average number of events per unit time)

Notation: $X \sim \text{Exp}(\lambda)$

Its defining property is **memorylessness**: the probability of waiting a further $s$ units is the same regardless of how long you have already waited.

$$P(X > s + t \mid X > t) = P(X > s)$$

## Key Formula

The probability density function is:

$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

The cumulative distribution function is:

$$F(x) = 1 - e^{-\lambda x}$$

| Property | Value |
|---|---|
| Mean | $1 / \lambda$ |
| Variance | $1 / \lambda^2$ |
| Median | $\ln 2 / \lambda$ |

## Example

A bond has a constant default intensity (hazard rate) of $\lambda = 0.03$ per year. What is the probability it defaults within 5 years?

$$P(X \leq 5) = 1 - e^{-0.03 \times 5} = 1 - e^{-0.15} \approx 0.139$$

There is roughly a 13.9% chance of default within 5 years.

## Remember

The exponential distribution underpins **hazard rate models** in credit risk. The default intensity $\lambda(t)$ is the instantaneous rate at which a firm defaults, and the survival probability $P(\tau > t) = e^{-\int_0^t \lambda(s)\,ds}$ generalises the exponential when the hazard rate varies with time. Credit default swap pricing relies directly on this framework.
