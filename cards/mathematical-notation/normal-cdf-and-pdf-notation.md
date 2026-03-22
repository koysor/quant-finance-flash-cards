# N(d₁) and N'(d₁) Notation

**Topic:** Mathematical Notation
**Tags:** notation, normal distribution, CDF, PDF, Black-Scholes, options
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

In quantitative finance, $N(x)$ denotes the **cumulative distribution function** (CDF) of the standard normal distribution — the probability that a standard normal random variable is less than or equal to $x$. The related notation $N'(x)$ denotes the **probability density function** (PDF) — the derivative of $N(x)$ with respect to $x$. Both appear throughout options pricing, most prominently in the Black–Scholes formula.

## Key Formula

$$N(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-z^2/2} \, dz$$

$$N'(x) = \frac{dN}{dx} = \frac{1}{\sqrt{2\pi}} \, e^{-x^2/2}$$

Key properties:

- $N(0) = 0.5$, $N(-x) = 1 - N(x)$
- $N'(x) > 0$ for all $x$ (the bell curve is always positive)
- $N'(x) = N'(-x)$ (symmetric about zero)

In the Black–Scholes formula, these appear as:

$$C = S_0 \, N(d_1) - K e^{-rT} N(d_2)$$

$$\Delta = N(d_1), \qquad \Gamma = \frac{N'(d_1)}{S_0 \, \sigma \sqrt{T}}$$

## Example

Compute $N(0.35)$ and $N'(0.35)$.

**CDF:** From standard normal tables (or a calculator):

$$N(0.35) = 0.6368$$

This means there is a 63.68% probability that a standard normal variable falls below 0.35.

**PDF:**

$$N'(0.35) = \frac{1}{\sqrt{2\pi}} \, e^{-0.35^2/2} = \frac{1}{2.5066} \times e^{-0.0613} = 0.3989 \times 0.9405 = 0.3752$$

In a Black–Scholes context with $d_1 = 0.35$: the call delta is $\Delta = 0.6368$, and $N'(0.35) = 0.3752$ feeds into the gamma and vega calculations.

## Remember

Whenever you see $N(\cdot)$ in a pricing formula, it is the standard normal CDF — a probability between 0 and 1. Whenever you see $N'(\cdot)$, it is the standard normal PDF — the bell-curve height at that point. In Black–Scholes, $N(d_2)$ is the risk-neutral probability of the option expiring in the money, $N(d_1)$ is the delta, and $N'(d_1)$ appears in every second-order Greek (gamma, vega, vanna). Recognising this notation instantly is essential because virtually every closed-form result in options theory is expressed in terms of $N$ and $N'$.
