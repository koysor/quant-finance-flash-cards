# Expected Value

**Topic:** Probability
**Level:** A Level Mathematics
**Tags:** probability, expectation, discrete, continuous

---

## Definition

The **expected value** (or expectation) E[X] of a random variable X is the probability-weighted average of all possible outcomes. It represents the long-run average if an experiment is repeated many times.

## Key Formula

**Discrete** random variable:

$$E[X] = \sum_{i} x_i \, P(X = x_i)$$

**Continuous** random variable:

$$E[X] = \int_{-\infty}^{\infty} x \, f(x) \, dx$$

**Linearity of expectation** (always holds, even for dependent variables):

$$E[aX + bY] = a\,E[X] + b\,E[Y]$$

## Example

A derivative pays £10 if a coin lands heads, and −£5 if tails. Each outcome has probability 0.5.

$$E[\text{payoff}] = 10 \times 0.5 + (-5) \times 0.5 = 5 - 2.5 = \textbf{£2.50}$$

The fair price of the derivative (ignoring discounting) is £2.50.

## Remember

- Expected value is **not** the most likely outcome — it is the mean.
- For a fair game: E[payoff] = 0.
- In pricing, risk-neutral expectation replaces real-world probabilities with **risk-neutral probabilities** (Q-measure). This is fundamental to derivatives pricing.
