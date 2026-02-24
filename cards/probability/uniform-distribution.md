# Uniform Distribution

**Topic:** Probability
**Level:** A Level Mathematics
**Tags:** distributions, probability, continuous, uniform, simulation

---

## Definition

The continuous uniform distribution assigns equal probability to all values in an interval $[a, b]$. Every outcome in the range is equally likely.

Notation: $X \sim U(a, b)$

## Key Formula

The probability density function is:

$$f(x) = \frac{1}{b - a}, \quad a \leq x \leq b$$

The cumulative distribution function is:

$$F(x) = \frac{x - a}{b - a}$$

| Property | Value |
|---|---|
| Mean | $\frac{a + b}{2}$ |
| Variance | $\frac{(b - a)^2}{12}$ |

## Example

A random number $U$ is drawn from $U(0, 1)$. To simulate a stock's daily return from a normal distribution, you apply the inverse CDF (quantile function):

$$Z = \Phi^{-1}(U)$$

If $U = 0.975$, then $Z = \Phi^{-1}(0.975) = 1.96$, giving a return 1.96 standard deviations above the mean.

## Remember

The uniform distribution is the engine behind **Monte Carlo simulation**. Every random number generator starts with $U(0, 1)$ draws, which are then transformed into any target distribution via the **inverse transform method**: if $U \sim U(0, 1)$ and $F$ is the desired CDF, then $X = F^{-1}(U)$ has the target distribution. This technique powers the simulation of stock paths, option pricing, and risk calculations.
