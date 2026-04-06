# Radon-Nikodym Derivative Notation

**Topic:** Mathematical Notation
**Tags:** notation, Radon-Nikodym, change of measure, density, risk-neutral, Girsanov
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

The **Radon-Nikodym derivative** $\frac{d\mathbb{Q}}{d\mathbb{P}}$ is the density of one probability measure with respect to another. It answers: "how much more (or less) weight does $\mathbb{Q}$ place on outcome $\omega$ compared with $\mathbb{P}$?"

| Symbol | Read as | Meaning |
|---|---|---|
| $\frac{d\mathbb{Q}}{d\mathbb{P}}$ | "dQ over dP" | Radon-Nikodym derivative of $\mathbb{Q}$ w.r.t. $\mathbb{P}$ |
| $\left.\frac{d\mathbb{Q}}{d\mathbb{P}}\right\vert_{\mathcal{F}_t}$ | "RN derivative at time $t$" | The density restricted to information up to time $t$ |
| $Z_t = E^{\mathbb{P}}\!\left[\frac{d\mathbb{Q}}{d\mathbb{P}} \,\middle|\, \mathcal{F}_t\right]$ | "likelihood ratio process" | The martingale density process under $\mathbb{P}$ |
| $\mathbb{Q} \ll \mathbb{P}$ | "$\mathbb{Q}$ absolutely continuous w.r.t. $\mathbb{P}$" | $\mathbb{Q}$ assigns zero probability to any event with $\mathbb{P}$-probability zero |

## Key Formula

**Change-of-measure formula:**

$$E^{\mathbb{Q}}[X] = E^{\mathbb{P}}\!\left[X \cdot \frac{d\mathbb{Q}}{d\mathbb{P}}\right]$$

**Girsanov's theorem** — if $\frac{d\mathbb{Q}}{d\mathbb{P}} = \exp\!\left(-\int_0^T \lambda_t \, dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T \lambda_t^2 \, dt\right)$ then:

$$W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \lambda_s \, ds$$

is a Brownian motion under $\mathbb{Q}$.

## Example

Under the real-world measure $\mathbb{P}$, a stock follows $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t^{\mathbb{P}}$ with $\mu = 0.10$ and $r = 0.04$, $\sigma = 0.20$. The market price of risk is $\lambda = (\mu - r)/\sigma = 0.30$.

The risk-neutral density is:

$$\frac{d\mathbb{Q}}{d\mathbb{P}} = e^{-\lambda W_T^{\mathbb{P}} - \frac{1}{2}\lambda^2 T} = e^{-0.3 W_T^{\mathbb{P}} - 0.045T}$$

Under $\mathbb{Q}$, the drift of $S_t$ becomes $r = 0.04$, matching the risk-free rate.

## Remember

The Radon-Nikodym derivative is the mathematical machinery that makes risk-neutral pricing work. In the real world ($\mathbb{P}$), investors demand a risk premium above $r$ to hold risky assets. In the risk-neutral world ($\mathbb{Q}$), all assets earn $r$ — but this is not wishful thinking: $\mathbb{Q}$ is a mathematically constructed measure, and $d\mathbb{Q}/d\mathbb{P}$ is precisely the adjustment factor that accounts for the missing risk premium. Every derivative price is a $\mathbb{Q}$-expectation, and every risk management calculation is a $\mathbb{P}$-expectation — the density $d\mathbb{Q}/d\mathbb{P}$ is what connects the two.
