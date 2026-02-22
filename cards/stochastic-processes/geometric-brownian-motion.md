# Geometric Brownian Motion

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** GBM, stochastic processes, asset prices, lognormal, Itô's lemma

---

## Definition

**Geometric Brownian Motion (GBM)** is a continuous-time stochastic process in which the logarithm of the variable follows Brownian motion with drift. It is the standard model for equity prices because it ensures prices remain strictly positive.

## Key Formula

The stochastic differential equation (SDE) for a stock price $S_t$ under GBM:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

Dividing through by $S_t$ shows that **proportional returns** are normally distributed:

$$\frac{dS_t}{S_t} = \mu \, dt + \sigma \, dW_t$$

Applying **Itô's lemma** to $\ln S_t$ gives the closed-form solution:

$$S_T = S_0 \exp\!\left(\!\left(\mu - \frac{\sigma^2}{2}\right)\!T + \sigma W_T\right)$$

| Symbol | Meaning |
|---|---|
| $\mu$ | Drift (continuously compounded expected return) |
| $\sigma$ | Volatility (annualised standard deviation of log returns) |
| $W_T$ | Standard Brownian motion increment, $W_T \sim N(0, T)$ |

The $-\tfrac{\sigma^2}{2}$ correction arises from Itô's lemma and converts the arithmetic mean $\mu$ into a geometric mean.

## Example

A stock priced at £50 has $\mu = 10\%$, $\sigma = 25\%$, $T = 1$ year. The expected price is:

$$\mathbb{E}[S_1] = 50 \, e^{0.10} \approx \textbf{£55.26}$$

The median price (using the exponent without the correction) is:

$$S_0 \exp\!\left(\left(0.10 - \tfrac{0.0625}{2}\right)\cdot 1\right) = 50 \, e^{0.06875} \approx \textbf{£53.56}$$

## Remember

- GBM implies that **log returns** $\ln(S_T/S_0)$ are normally distributed — this is the lognormal model underpinning Black-Scholes.
- The $-\tfrac{\sigma^2}{2}$ term means that higher volatility **lowers** the median outcome (volatility drag), which is why compounding at a volatile rate is worse than compounding at the arithmetic mean.
- GBM is a simplification: real asset prices exhibit **fat tails**, **volatility clustering**, and **jumps** that GBM does not capture.
