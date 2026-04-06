# Periodic Function

**Topic:** Calculus
**Tags:** periodic, period, frequency, Fourier, seasonality, mean reversion
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A function $f$ is **periodic** with period $T > 0$ if $f(x + T) = f(x)$ for all $x$ in its domain. The smallest such $T$ is the **fundamental period**. The shape of the function repeats exactly every $T$ units. The **frequency** is $f = 1/T$ and the **angular frequency** is $\omega = 2\pi/T$.

## Key Formula

**Periodicity condition:**

$$f(x + T) = f(x) \quad \text{for all } x$$

**Key periodic functions and their periods:**

| Function | Period |
|---|---|
| $\sin(\omega x)$ | $2\pi / \omega$ |
| $\cos(\omega x)$ | $2\pi / \omega$ |
| $\tan(\omega x)$ | $\pi / \omega$ |

**Fourier series** — any periodic function with period $T$ can be decomposed as:

$$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{2\pi n x}{T}\right) + b_n \sin\!\left(\frac{2\pi n x}{T}\right) \right]$$

This expresses any periodic behaviour as a sum of sinusoidal components at integer multiples of the fundamental frequency.

## Example

Electricity prices exhibit daily and weekly periodicity. A simple model for the periodic component of power prices:

$$p(t) = A\sin\!\left(\frac{2\pi t}{24}\right) + B\cos\!\left(\frac{2\pi t}{24}\right)$$

where $t$ is in hours. Period $= 24$ hours, angular frequency $\omega = 2\pi/24$. The coefficients $A$ and $B$ are estimated from data and capture the daily demand cycle (peak morning and evening, trough overnight).

## Remember

Periodic functions are the building blocks of **Fourier analysis**, which underpins characteristic function-based option pricing. Any option payoff or distribution can be decomposed into periodic (sinusoidal) components via the Fourier transform — even though option prices themselves are not periodic, the mathematical machinery of periodic functions is the engine under the hood. In commodity and energy markets, seasonality is explicitly modelled as a periodic function superimposed on a stochastic mean-reverting process.
