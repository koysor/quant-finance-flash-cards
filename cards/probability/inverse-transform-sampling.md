# Inverse Transform Sampling

**Topic:** Probability
**Tags:** inverse CDF, sampling, simulation, random numbers, uniform distribution, Monte Carlo
**Author:** Claude Opus 4.6

---

## Definition

**Inverse transform sampling** is a method for generating random draws from any continuous distribution using only uniform random numbers. It works by passing a uniform $U \sim \text{Uniform}(0, 1)$ through the inverse cumulative distribution function $F^{-1}$, producing a random variable with the desired distribution.

## Key Formula

If $U \sim \text{Uniform}(0, 1)$ and $F$ is the CDF of the target distribution, then:

$$X = F^{-1}(U)$$

has CDF $F$. This works because $P(X \leq x) = P(F^{-1}(U) \leq x) = P(U \leq F(x)) = F(x)$.

**For the standard normal distribution:**

$$\phi = \Phi^{-1}(U)$$

where $\Phi^{-1}$ is the inverse of the standard normal CDF (the probit function).

**Alternative (CLT approximation):** sum 12 independent uniforms and subtract 6:

$$\phi \approx \left(\sum_{i=1}^{12} U_i\right) - 6$$

This gives mean 0 (since $12 \times \frac{1}{2} - 6 = 0$) and variance 1 (since $12 \times \frac{1}{12} = 1$).

| Method | Accuracy | Speed | Tail behaviour |
|---|---|---|---|
| Inverse CDF | Exact | Slower | Full tails |
| Sum of 12 uniforms | Approximate | Faster | Bounded to $[-6, 6]$ |

## Example

To generate an exponential random variable with rate $\lambda = 2$, the CDF is $F(x) = 1 - e^{-2x}$ and the inverse is $F^{-1}(u) = -\frac{1}{2}\ln(1 - u)$. Drawing $U = 0.7$ gives $X = -\frac{1}{2}\ln(0.3) \approx 0.602$.

## Remember

Inverse transform sampling is the theoretical foundation for generating random draws from any distribution in Monte Carlo simulation. Every SDE simulation requires draws from $\mathcal{N}(0, 1)$, which are produced by applying $\Phi^{-1}$ to uniform random numbers. The method is exact but requires evaluating the inverse CDF; for the normal distribution, fast polynomial approximations are used in practice.
