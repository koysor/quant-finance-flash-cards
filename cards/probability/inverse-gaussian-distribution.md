# Inverse Gaussian Distribution

**Topic:** Probability
**Tags:** inverse Gaussian, first passage time, Wald distribution, credit risk, skewed distribution, hitting time
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **inverse Gaussian distribution** (also called the Wald distribution) is the probability distribution of the first passage time $\tau_b$ — the time for a Brownian motion with positive drift $\mu > 0$ to first reach a fixed positive level $b$. It is right-skewed with a heavier right tail than the normal, reflecting the possibility that the process drifts close to the barrier, retreats, and takes far longer than expected to finally cross.

## Key Formula

If $X_t = \mu t + \sigma W_t$ and $\tau_b = \inf\{t \geq 0 : X_t = b\}$ with $b > 0$, $\mu > 0$, then $\tau_b \sim \text{IG}(\bar{t}, \lambda)$ with:

$$\bar{t} = \frac{b}{\mu} \quad \text{(mean)}, \qquad \lambda = \frac{b^2}{\sigma^2} \quad \text{(shape)}$$

**PDF:**

$$f(t;\, \bar{t}, \lambda) = \sqrt{\frac{\lambda}{2\pi t^3}} \exp\!\left(-\frac{\lambda(t - \bar{t})^2}{2\bar{t}^2\, t}\right), \quad t > 0$$

**Variance:** $\text{Var}[\tau_b] = \bar{t}^3/\lambda = b\sigma^2/\mu^3$

**CDF** (used directly in credit models):

$$\Pr(\tau_b \leq T) = N\!\left(\sqrt{\frac{\lambda}{T}}\left(\frac{T}{\bar{t}} - 1\right)\right) + e^{2\lambda/\bar{t}}\, N\!\left(-\sqrt{\frac{\lambda}{T}}\left(\frac{T}{\bar{t}} + 1\right)\right)$$

which is the probability that the Brownian motion with drift hits level $b$ within time $T$ — identical to the running maximum formula $\Pr(M_T \geq b)$.

## Example

A firm's log-leverage ratio follows $X_t = 0.04\,t + 0.25\,W_t$ (annual), starting at $X_0 = 0$, with default at $b = 0.6$ (log-leverage threshold).

$$\bar{t} = b/\mu = 0.6/0.04 = 15 \text{ years}, \qquad \lambda = b^2/\sigma^2 = 0.36/0.0625 = 5.76$$

$$\text{SD}[\tau_b] = \bar{t}^{3/2}/\sqrt{\lambda} = 15^{3/2}/\sqrt{5.76} \approx 58.1/2.4 \approx 24.2 \text{ years}$$

The enormous standard deviation (24 years for a mean of 15) reflects the heavy right tail: many firms would default quickly on a bad draw, while others might never default at all within a 30-year horizon.

$$\Pr(\tau_b \leq 5) \approx 4.3\%, \quad \Pr(\tau_b \leq 10) \approx 14.1\%, \quad \Pr(\tau_b \leq 20) \approx 47.2\%$$

## Remember

The inverse Gaussian is the natural distribution for time-to-event whenever the event is triggered by a random walk crossing a threshold. In **credit risk**, the Black-Cox model uses $\Pr(\tau_b \leq T)$ as the default probability, where $b$ is the log of the default threshold and the drift $\mu$ is the firm's long-run growth rate. Higher drift $\mu$ delays default (longer mean $\bar{t}$) but also reduces variance, concentrating the default time near the mean; higher volatility $\sigma$ reduces $\lambda$ and fattens the right tail, meaning more uncertainty about when (if ever) the firm defaults. The distribution is also used in mortgage prepayment modelling, where households "prepay" when their housing equity or rate incentive crosses a personal threshold.
