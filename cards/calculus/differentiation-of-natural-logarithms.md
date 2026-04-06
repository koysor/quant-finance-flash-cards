# Differentiation of Natural Logarithms

**Topic:** Calculus
**Tags:** natural logarithm, differentiation, chain rule, log-returns, Black-Scholes
**Created:** 2026-04-05
**Author:** Claude Sonnet 4.6

---

## Definition

The derivative of the natural logarithm $\ln(x)$ is $\frac{1}{x}$, valid for $x > 0$. When the argument is a differentiable function $f(x)$ rather than a bare variable, the chain rule extends this to $\frac{f'(x)}{f(x)}$ — the ratio of the function's derivative to the function itself.

## Key Formula

**Basic rule:**

$$\frac{d}{dx}\ln(x) = \frac{1}{x}, \quad x > 0$$

**With chain rule** — if $u = f(x)$ is differentiable:

$$\frac{d}{dx}\ln(f(x)) = \frac{f'(x)}{f(x)}$$

**Logarithmic differentiation** — useful when $y = f(x)^{g(x)}$:

$$\ln y = g(x)\ln f(x) \implies \frac{1}{y}\frac{dy}{dx} = g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}$$

## Example

Differentiate $f(x) = \ln(3x^2 + 5x)$.

Let $u = 3x^2 + 5x$, so $u' = 6x + 5$.

$$f'(x) = \frac{6x + 5}{3x^2 + 5x}$$

At $x = 2$: $f'(2) = \frac{12 + 5}{12 + 10} = \frac{17}{22} \approx 0.773$.

**Finance application:** the log-return on a stock is $r = \ln(S_t / S_{t-1})$. Differentiating this with respect to $S_t$ gives $\partial r / \partial S_t = 1/S_t$, confirming that a one-unit rise in the stock price changes the log-return by $1/S_t$ — a smaller effect when prices are higher.

## Remember

The rule $\frac{d}{dx}\ln(f(x)) = \frac{f'(x)}{f(x)}$ lies at the heart of Black-Scholes sensitivity analysis. In the $d_1$ formula, $\ln(S/K)$ must be differentiated with respect to $S$ to obtain Delta; the result $\partial\ln(S/K)/\partial S = 1/S$ feeds directly into $\partial d_1/\partial S = 1/(S\sigma\sqrt{T})$. Logarithmic differentiation is also the standard technique for verifying that geometric Brownian motion $S_t = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t}$ satisfies its SDE — taking $\ln S_t$ and differentiating converts a multiplicative process into an additive one.
