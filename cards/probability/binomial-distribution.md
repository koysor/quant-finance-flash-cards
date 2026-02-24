# Binomial Distribution

**Topic:** Probability
**Level:** A Level Mathematics
**Tags:** distributions, probability, discrete, binomial

---

## Definition

The binomial distribution models the number of successes in a fixed number of independent trials, each with the same probability of success. It is described by two parameters:

- **n** — the number of trials
- **p** — the probability of success on each trial

Notation: $X \sim B(n, p)$

## Key Formula

The probability of exactly $k$ successes in $n$ trials is:

$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \ldots, n$$

where $\binom{n}{k} = \frac{n!}{k!(n - k)!}$ is the binomial coefficient.

| Property | Value |
|---|---|
| Mean | $np$ |
| Variance | $np(1 - p)$ |
| Skewness | $\frac{1 - 2p}{\sqrt{np(1 - p)}}$ |

## Example

A trader estimates each trade has a 55% chance of profit ($p = 0.55$). Over $n = 20$ trades, what is the probability of exactly 12 profitable trades?

$$P(X = 12) = \binom{20}{12} (0.55)^{12} (0.45)^{8} \approx 0.162$$

So there is roughly a 16.2% chance of exactly 12 winners out of 20.

## Remember

The binomial distribution is the foundation of the **binomial tree** model for option pricing. At each time step the stock price moves up or down with fixed probabilities — after $n$ steps the number of up-moves follows $B(n, p)$, and the option payoff at each terminal node is weighted by the corresponding binomial probability. In the risk-neutral framework, $p$ is replaced by the risk-neutral probability $q$, ensuring the tree prices converge to Black-Scholes as $n \to \infty$.
