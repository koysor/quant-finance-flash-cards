# Natural Logarithm

**Topic:** Calculus
**Tags:** natural logarithm, ln, log-returns, GBM, Black-Scholes, continuous compounding
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **natural logarithm** $\ln(x) = \log_e(x)$ is the logarithm with base $e \approx 2.71828$. It is the inverse of the exponential function: $\ln(e^x) = x$ and $e^{\ln x} = x$ for all $x > 0$. It is the unique function satisfying $\frac{d}{dx}\ln(x) = \frac{1}{x}$ with $\ln(1) = 0$.

## Key Formula

$$\ln(e^x) = x, \qquad e^{\ln x} = x \quad (x > 0)$$

$$\frac{d}{dx}\ln(x) = \frac{1}{x}, \qquad \int \frac{1}{x}\, dx = \ln|x| + C$$

**Chain rule:**

$$\frac{d}{dx}\ln(f(x)) = \frac{f'(x)}{f(x)}$$

**Integral definition:**

$$\ln(x) = \int_1^x \frac{1}{t}\, dt \quad (x > 0)$$

**Taylor series** around $x = 0$:

$$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad |x| \leq 1,\; x \neq -1$$

For small $x$: $\ln(1 + x) \approx x$, so log-returns $\approx$ simple returns for small moves.

## Example

**Black-Scholes $d_1$** contains the natural logarithm of the moneyness:

$$d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

With $S = 105$, $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$:

$$\ln(105/100) = \ln(1.05) \approx 0.0488$$

$$d_1 = \frac{0.0488 + (0.05 + 0.02)}{0.20} = \frac{0.1188}{0.20} = 0.594$$

The $\ln(S/K)$ term measures log-moneyness — how far (in log space) the stock is from the strike.

## Remember

The natural logarithm transforms stock prices into log-returns: $r_t = \ln(S_t/S_{t-1})$. Log-returns are additive over time — the total log-return over $n$ periods is $\sum r_t = \ln(S_n/S_0)$ — which makes them suitable for the Central Limit Theorem and normal distribution modelling. The approximation $\ln(1+x) \approx x$ for small $x$ means that for daily returns below ~2%, log-returns and simple returns are nearly identical numerically. The Black-Scholes formula uses $\ln(S/K)$ rather than $S/K$ precisely because the log-normal distribution of $S_T$ makes $\ln S_T$ normally distributed.
