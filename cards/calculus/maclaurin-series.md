# Maclaurin Series

**Topic:** Calculus
**Tags:** maclaurin series, taylor series, power series, approximation, exponential, trigonometry
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Maclaurin series** is the special case of the Taylor series expanded about $a = 0$. It expresses a smooth function $f(x)$ as an infinite power series in $x$, where each coefficient is determined by the value of a derivative of $f$ at the origin. The series is exact wherever it converges.

## Key Formula

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\, x^n = f(0) + f'(0)\,x + \frac{f''(0)}{2!}\,x^2 + \frac{f'''(0)}{3!}\,x^3 + \cdots$$

**Standard Maclaurin series:**

$$e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \quad (\text{all } x)$$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \quad (\text{all } x)$$

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \quad (\text{all } x)$$

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad (-1 < x \leq 1)$$

## Example

Compute $\cos(0.1)$ to five decimal places using the Maclaurin series.

$$\cos(0.1) \approx 1 - \frac{(0.1)^2}{2} + \frac{(0.1)^4}{24} = 1 - 0.005 + 0.0000042 \approx 0.99500$$

The exact value is $0.99500417\ldots$ — the two-term approximation is already accurate to 5 decimal places because $0.1$ is small.

## Remember

The Maclaurin series of $e^x$ is the backbone of **continuous-time finance**. The GBM stock price $S_T = S_0 e^{(\mu - \frac{1}{2}\sigma^2)T + \sigma W_T}$ uses $e^x$ directly; the CRR binomial tree approximates the up-factor $u = e^{\sigma\sqrt{\delta t}} \approx 1 + \sigma\sqrt{\delta t}$ using the first two Maclaurin terms. In Black-Scholes derivations, $e^{-rT} \approx 1 - rT$ (first-order Maclaurin) is used to simplify pricing formulas for short maturities. Every time a quant writes "for small $x$, $e^x \approx 1 + x$", they are quoting the first two terms of the Maclaurin series.
