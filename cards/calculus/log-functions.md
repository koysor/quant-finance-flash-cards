# Log Functions

**Topic:** Calculus
**Tags:** logarithm, log base, change of base, inverse function, option pricing, returns
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

A **logarithmic function** $\log_b(x)$ is the inverse of the exponential function $b^x$: $\log_b(x) = y \iff b^y = x$. The base $b > 0$, $b \neq 1$. Logarithms convert multiplicative relationships into additive ones — the defining property that makes them fundamental in finance.

## Key Formula

**Definition:** $\log_b(x) = y \iff b^y = x$, for $x > 0$

**Common bases:**

$$\log_{10}(x) \quad \text{(common log)}, \qquad \ln(x) = \log_e(x) \quad \text{(natural log)}, \qquad \log_2(x) \quad \text{(binary log)}$$

**Change of base formula:**

$$\log_b(x) = \frac{\ln(x)}{\ln(b)} = \frac{\log_{10}(x)}{\log_{10}(b)}$$

**Derivative:**

$$\frac{d}{dx} \log_b(x) = \frac{1}{x \ln b}$$

**Key properties** (true for any base $b$):

$$\log_b(xy) = \log_b(x) + \log_b(y), \qquad \log_b\!\left(\frac{x}{y}\right) = \log_b(x) - \log_b(y), \qquad \log_b(x^n) = n\log_b(x)$$

## Example

A stock price rises from $S_0 = 100$ to $S_T = 130$. The log-return (base $e$) is:

$$r = \ln\!\left(\frac{130}{100}\right) = \ln(1.3) \approx 0.262 \approx 26.2\%$$

Using the change of base formula to convert to base 10:

$$\log_{10}(1.3) = \frac{\ln(1.3)}{\ln(10)} = \frac{0.262}{2.303} \approx 0.114$$

In practice, $\ln$ (base $e$) is used throughout quantitative finance because it gives the cleanest expressions for continuously compounded returns and GBM.

## Remember

The fundamental reason logarithms appear throughout finance is that they convert **multiplicative** price processes into **additive** return processes. If $S_T = S_0 \cdot R_1 \cdot R_2 \cdots R_n$ (product of gross returns), then $\ln(S_T/S_0) = \ln R_1 + \ln R_2 + \cdots + \ln R_n$ (sum of log-returns). Sums are governed by the Central Limit Theorem; products are not. This is why log-returns are normally distributed in the GBM model, and why $d_1 = \frac{\ln(S/K) + \ldots}{\sigma\sqrt{T}}$ contains a logarithm in the Black-Scholes formula.
