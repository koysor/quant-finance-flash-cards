# First Passage Time

**Topic:** Stochastic Processes
**Tags:** first passage time, hitting time, inverse Gaussian, barrier, credit risk, perpetual option
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **first passage time** (or hitting time) $\tau_b$ is the first time a stochastic process reaches a fixed level $b$:

$$\tau_b = \inf\{t \geq 0 : X_t = b\}$$

For a drifted Brownian motion $X_t = \mu t + \sigma W_t$ starting at $X_0 = 0$ with $b > 0$, $\tau_b$ follows an **inverse Gaussian distribution** — right-skewed with a heavy right tail, reflecting the possibility that the process drifts away from the barrier and takes a very long time to return.

## Key Formula

**PDF of $\tau_b$** for $X_t = \mu t + \sigma W_t$, $b > 0$:

$$f_{\tau_b}(t) = \frac{b}{\sigma\sqrt{2\pi t^3}} \exp\!\left(-\frac{(b - \mu t)^2}{2\sigma^2 t}\right), \quad t > 0$$

**Probability of ever reaching $b$:**

$$\Pr(\tau_b < \infty) = \begin{cases} 1 & \text{if } \mu \geq 0 \\ e^{2\mu b/\sigma^2} & \text{if } \mu < 0 \end{cases}$$

When $\mu < 0$ (drift away from $b$), there is positive probability of never hitting the barrier.

**Laplace transform** (useful for perpetual option pricing):

$$E\!\left[e^{-r\tau_b}\right] = \exp\!\left(\frac{\mu b}{\sigma^2} - \frac{b}{\sigma^2}\sqrt{\mu^2 + 2r\sigma^2}\right)$$

## Example

A firm's asset value follows $V_t = V_0 \exp((\mu - \tfrac{1}{2}\sigma^2)t + \sigma W_t)$ with $V_0 = 100$, default barrier $B = 60$, $\mu = 5\%$, $\sigma = 30\%$.

Working in log-space: $X_t = \ln(V_t/B) = \ln(100/60) + \nu t + \sigma W_t$ with $\nu = \mu - \tfrac{1}{2}\sigma^2 = 0.005$ and $b_0 = \ln(100/60) \approx 0.511$ (distance to barrier).

$$\Pr(\text{default in 5 years}) = N\!\left(\frac{-b_0 + \nu \cdot 5}{\sigma\sqrt{5}}\right) + e^{2\nu b_0/\sigma^2} N\!\left(\frac{-b_0 - \nu \cdot 5}{\sigma\sqrt{5}}\right) \approx 18.4\%$$

The expected time to default, conditional on defaulting, is $b_0/\lvert\nu\rvert$ only when $\nu < 0$; here $\nu > 0$ (firm is growing) so default requires the diffusion to overcome the positive drift.

## Remember

First passage times are the mathematical foundation of **structural credit models** (Merton, Black-Cox): a firm defaults when its asset value first hits the debt barrier, and the credit spread is priced from the first passage time distribution. In option pricing, the **perpetual American put** has a closed-form solution derived from the Laplace transform $E[e^{-r\tau_b}]$ — the discount factor to the (random) exercise time. Discrete Monte Carlo simulation misses barrier crossings that occur between time steps; the Brownian bridge conditional distribution corrects for this by giving the exact probability that the path crossed the barrier between two observed points without simulating the intervening path.
