# Conditional Expectation

**Topic:** Probability
**Tags:** conditional expectation, tower property, filtration, information, martingale, risk-neutral pricing
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The **conditional expectation** $\mathbb{E}[X \mid \mathcal{F}_t]$ is the best estimate of a random variable $X$ given the information available at time $t$, encoded in the filtration $\mathcal{F}_t$. It is itself a random variable — a function of the observed information — and reduces to a deterministic number once the information set is realised.

## Key Formula

**Tower property** (law of iterated expectations): for $s \leq t$,

$$\mathbb{E}\!\left[\mathbb{E}[X \mid \mathcal{F}_t] \,\Big|\, \mathcal{F}_s\right] = \mathbb{E}[X \mid \mathcal{F}_s]$$

**Taking out what is known**: if $Y$ is $\mathcal{F}_t$-measurable,

$$\mathbb{E}[YX \mid \mathcal{F}_t] = Y\,\mathbb{E}[X \mid \mathcal{F}_t]$$

**Martingale property** in this language:

$$\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s \quad \Leftrightarrow \quad M \text{ is a martingale}$$

## Example

A bond pays £100 in one year. At time 0, knowing only today's yield curve, $\mathbb{E}[\text{payoff} \mid \mathcal{F}_0] = 100 \cdot e^{-r}$. Six months later, if rates have moved, the conditional expectation $\mathbb{E}[\text{payoff} \mid \mathcal{F}_{0.5}]$ is updated to reflect the new information — a higher price if rates fell.

## Remember

The tower property is the mathematical foundation of risk-neutral pricing: the price of a derivative at time $s$ is the conditional expectation under the risk-neutral measure of its discounted payoff given $\mathcal{F}_s$. Backward induction in binomial trees and the Feynman-Kac formula both exploit the tower property — the price today is the conditional expectation of the price tomorrow, which is itself the conditional expectation of the price the day after, all the way to expiry.
