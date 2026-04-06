# Definite Integral

**Topic:** Calculus
**Tags:** calculus, integration, area, bounds, probability
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

A definite integral accumulates a function $f(x)$ over a closed interval $[a, b]$, yielding a single number that represents the signed area between the curve and the $x$-axis. Where $f(x) > 0$ the contribution is positive; where $f(x) < 0$ it is negative.

## Key Formula

$$\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \, \Delta x$$

Evaluated using the Fundamental Theorem of Calculus (Part 2):

$$\int_a^b f(x) \, dx = F(b) - F(a), \qquad \text{where } F'(x) = f(x)$$

Key properties:

$$\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx \qquad \text{(reversing limits changes sign)}$$

$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx \qquad \text{(additivity)}$$

## Example

Find the probability that a standard normal random variable $Z$ lies between $0$ and $1$.

$$P(0 \le Z \le 1) = \int_0^1 \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, dx$$

Using the standard normal CDF $\Phi$:

$$= \Phi(1) - \Phi(0) = 0.8413 - 0.5000 = 0.3413$$

So there is roughly a 34% chance the outcome falls within one standard deviation above the mean.

## Remember

The definite integral is the engine behind the Black-Scholes formula: the option price is the discounted expected payoff under the risk-neutral measure, computed as $\int_{-\infty}^{\infty} \max(S_T - K, 0) \, \phi(S_T) \, dS_T$, where $\phi$ is the risk-neutral density. Evaluating this integral produces the $N(d_1)$ and $N(d_2)$ terms that traders quote every day.
