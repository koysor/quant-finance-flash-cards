# Logarithmic and Exponential Functions

**Topic:** Calculus
**Tags:** logarithm, exponential, derivatives, continuous compounding, log-returns
**Created:** 2026-02-28 20:46:20
**Author:** Claude Opus 4.6

---

## Definition

The natural exponential function $e^x$ and the natural logarithm $\ln x$ are inverses of each other: $\ln(e^x) = x$ and $e^{\ln x} = x$ for $x > 0$. They are the most important pair of functions in quantitative finance because they convert between multiplicative and additive processes.

## Key Formula

Derivatives:

$$\frac{d}{dx} e^x = e^x, \qquad \frac{d}{dx} \ln x = \frac{1}{x}$$

For a composite function:

$$\frac{d}{dx} e^{f(x)} = f'(x)\,e^{f(x)}, \qquad \frac{d}{dx} \ln f(x) = \frac{f'(x)}{f(x)}$$

Log laws:

$$\ln(ab) = \ln a + \ln b, \qquad \ln\!\left(\frac{a}{b}\right) = \ln a - \ln b, \qquad \ln(a^n) = n\ln a$$

## Example

Differentiate $f(x) = \ln(3x^2 + 1)$.

Using the chain rule: $f'(x) = \frac{6x}{3x^2 + 1}$.

At $x = 2$: $f'(2) = \frac{12}{13} \approx 0.923$.

Continuous compounding: invest £1{,}000 at $r = 5\%$ for 3 years.

$$A = 1000 \times e^{0.05 \times 3} = 1000 \times e^{0.15} \approx £1{,}161.83$$

## Remember

Log-returns $r_t = \ln(S_t / S_{t-1})$ are the foundation of quantitative finance modelling because they are **additive over time**: the total log-return is simply $\sum r_t$, unlike simple returns which compound multiplicatively. The lognormal model $S_T = S_0 e^{(\mu - \frac{1}{2}\sigma^2)T + \sigma W_T}$ uses the exponential to guarantee positive stock prices, while continuous compounding $e^{rT}$ is the natural discount factor in derivatives pricing. Every time you see $e$ or $\ln$ in a pricing formula, it traces back to these two functions and their inverse relationship.
