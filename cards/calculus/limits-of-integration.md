# Limits of Integration

**Topic:** Calculus
**Tags:** calculus, integration, definite-integral, bounds, accumulation
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **limits of integration** are the lower bound $a$ and upper bound $b$ of a definite integral. They specify the domain of accumulation — the exact interval over which the integrand is summed — and transform an indefinite antiderivative into a precise numerical value representing the net signed area under the curve on $[a, b]$.

## Key Formula

$$\int_a^b f(x)\,dx = F(b) - F(a), \qquad F'(x) = f(x)$$

The lower limit $a$ and upper limit $b$ appear as the endpoints of evaluation. Swapping the limits reverses the sign:

$$\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$$

A limit of $\pm\infty$ produces an **improper integral**, evaluated as a limit:

$$\int_a^{\infty} f(x)\,dx = \lim_{R \to \infty} \int_a^R f(x)\,dx$$

## Example

The standard normal probability density is $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$. The probability that a standard normal variable falls between $-1$ and $1$ is:

$$P(-1 \leq Z \leq 1) = \int_{-1}^{1} \phi(z)\,dz \approx 0.6827$$

Changing the limits to $[0, 1.645]$ gives $P(0 \leq Z \leq 1.645) \approx 0.45$ — the limits alone determine which probability mass is captured.

## Remember

Limits of integration directly control which scenarios enter a pricing or risk calculation. In the Black-Scholes call price, the integration lower limit is effectively the strike $K$ — the payoff $\max(S_T - K, 0)$ is non-zero only when $S_T > K$, so only that region of the lognormal density contributes to the price. In Value at Risk, the loss quantile is the lower limit of an improper integral of the loss density up to a chosen confidence level. Choosing the wrong bounds is equivalent to mispricing the event space being insured against.
