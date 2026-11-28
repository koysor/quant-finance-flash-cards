# Strong Markov Property

**Topic:** Stochastic Processes
**Tags:** strong markov, stopping time, hitting time, reflection principle, barrier options, brownian motion
**Created:** 2026-11-28
**Author:** Claude Opus 5.5

---

## Definition

A process has the **strong Markov property** if the Markov property still holds when "now" is a **stopping time** $\tau$ (a random time, such as the first time a barrier is hit) rather than a fixed time $t$. Once $\tau$ has happened, the future depends only on the state $X_\tau$, not on the path that led there or on when $\tau$ occurred. Brownian motion, GBM and every standard diffusion have this property.

## Key Formula

For a stopping time $\tau$ with $\tau < \infty$:

$$\mathbb{E}\bigl[f(X_{\tau + s}) \mid \mathcal{F}_\tau\bigr] = \mathbb{E}\bigl[f(X_{\tau + s}) \mid X_\tau\bigr]$$

For Brownian motion this says the process **restarts** at $\tau$:

$$B_s = W_{\tau + s} - W_\tau \quad \text{is a fresh Brownian motion, independent of } \mathcal{F}_\tau$$

Its best-known consequence is the **reflection principle**. With $\tau_b$ the first time $W$ hits a level $b > 0$:

$$\mathbb{P}\Bigl(\max_{0 \le t \le T} W_t \ge b\Bigr) = 2\,\mathbb{P}(W_T \ge b) = 2\Bigl[1 - \Phi\Bigl(\tfrac{b}{\sqrt{T}}\Bigr)\Bigr]$$

After $\tau_b$ the restarted path is equally likely to finish above or below $b$, which gives the factor of 2.

## Example

A stock's log price is modelled as $\ln(S_t/S_0) = 0.2\,W_t$ (volatility 20%, drift ignored). What is the probability that it touches a barrier 10% above spot within one year?

The barrier in log terms is $\ln 1.1 = 0.0953$, so in units of $W$ it is $b = 0.0953 / 0.2 = 0.4766$. With $T = 1$:

$$\mathbb{P}(\text{touch}) = 2\bigl[1 - \Phi(0.4766)\bigr] = 2(1 - 0.6832) = 0.634$$

By contrast, the probability of merely **ending** above the barrier is $1 - \Phi(0.4766) = 0.317$, exactly half.

## Remember

Barrier, lookback and American option pricing all rely on the strong Markov property. When the price hits a knock-in barrier, the option becomes a vanilla whose value depends only on the price at that moment, so the knock-in is worth a vanilla started at the hitting time. The reflection principle behind closed-form barrier prices uses the same restart. For an American option, the value at the moment of early exercise depends only on the spot then. This is why a desk can price these contracts with closed forms or PDE free boundaries rather than simulating every path. The rule of thumb in the example, that the chance of touching is about twice the chance of finishing beyond the level, is how traders quickly estimate one-touch prices.
