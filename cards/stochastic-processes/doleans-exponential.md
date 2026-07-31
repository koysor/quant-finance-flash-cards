# Doléans Exponential

**Topic:** Stochastic Processes
**Tags:** doléans exponential, stochastic exponential, semimartingale, measure change, girsanov, radon-nikodym
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

The **Doléans exponential** (or stochastic exponential) of a semimartingale $M$ is the unique solution $Z$ to the linear stochastic differential equation $dZ_t = Z_{t-}\,dM_t$ with $Z_0 = 1$. It is denoted $\mathcal{E}(M)_t$ and generalises the ordinary exponential function to processes that may include jumps.

## Key Formula

For a **continuous** semimartingale $M$:

$$\mathcal{E}(M)_t = \exp\!\left(M_t - M_0 - \frac{1}{2}[M,M]_t\right)$$

where $[M,M]_t$ is the quadratic variation of $M$. For a semimartingale with jumps $\Delta M_s = M_s - M_{s-}$, the full formula is:

$$\mathcal{E}(M)_t = e^{M_t - M_0 - \frac{1}{2}[M^c,M^c]_t}\prod_{0 < s \le t}(1 + \Delta M_s)\,e^{-\Delta M_s}$$

The product over jump times ensures $\mathcal{E}(M)$ remains positive whenever $\Delta M_s > -1$ for all $s$.

## Example

Let $M_t = \theta W_t$ where $W_t$ is a standard Brownian motion and $\theta$ is a constant. Then $[M,M]_t = \theta^2 t$ and:

$$\mathcal{E}(\theta W)_t = \exp\!\left(\theta W_t - \frac{1}{2}\theta^2 t\right)$$

With $\theta = 0.3$, at $t = 1$ and $W_1 = 0.5$: $\mathcal{E}(0.3W)_1 = e^{0.3 \times 0.5 - 0.5 \times 0.09} = e^{0.105} \approx 1.111$.

This particular case is the exponential martingale familiar from Black–Scholes.

## Remember

In quantitative finance, the Doléans exponential is the mechanism that turns a local martingale into a Radon–Nikodým density process. When changing from the real-world measure $\mathbb{P}$ to a risk-neutral measure $\mathbb{Q}$, the density process is $\frac{d\mathbb{Q}}{d\mathbb{P}}\big|_{\mathcal{F}_t} = \mathcal{E}(-\lambda W)_t$, where $\lambda$ is the market price of risk. For this to define a valid probability measure, $\mathcal{E}(-\lambda W)$ must be a true martingale — the Novikov condition provides the sufficient integrability criterion that guarantees this.
