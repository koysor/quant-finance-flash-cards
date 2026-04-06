# Exponential Function

**Topic:** Calculus
**Tags:** exponential, e, growth, continuous compounding, GBM, discount factor
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **exponential function** $f(x) = e^x$ is the unique function that is its own derivative: $\frac{d}{dx} e^x = e^x$. The base $e \approx 2.71828$ is Euler's number. The function is positive for all $x \in \mathbb{R}$, strictly increasing, and satisfies $e^0 = 1$.

## Key Formula

$$\frac{d}{dx} e^x = e^x, \qquad \int e^x\, dx = e^x + C$$

**Chain rule extension:**

$$\frac{d}{dx} e^{f(x)} = f'(x)\, e^{f(x)}$$

**Key properties:**

$$e^{a+b} = e^a \cdot e^b, \qquad e^{-x} = \frac{1}{e^x}, \qquad (e^a)^b = e^{ab}$$

**Limit definition of $e$:**

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n$$

**Continuous compounding** — the limiting case of $n$-times-per-year compounding at rate $r$:

$$\lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^n = e^r$$

## Example

A bond pays continuous interest at $r = 5\%$. After $T = 2$ years, £1{,}000 grows to:

$$A = 1000 \cdot e^{0.05 \times 2} = 1000 \cdot e^{0.10} \approx £1{,}105.17$$

The discount factor — the present value of £1 received in $T = 2$ years — is:

$$P = e^{-rT} = e^{-0.10} \approx 0.9048$$

Every Black-Scholes formula contains $e^{-rT}$ as its discount factor, and GBM stock prices are modelled as $S_T = S_0 e^{(\mu - \frac{1}{2}\sigma^2)T + \sigma W_T}$ — the exponential ensures $S_T > 0$ always.

## Remember

The exponential function is the engine of continuous-time finance. Its self-derivative property means that continuously compounded growth is the smoothest possible growth model — the rate of change equals the level. This is why $e^{rT}$ is the natural discount factor (not $(1+r)^T$), why GBM uses $e^{\sigma W_t}$ to model multiplicative price shocks, and why the normal distribution's density contains $e^{-x^2/2}$. Whenever a financial quantity grows or decays smoothly, the exponential function is involved.
