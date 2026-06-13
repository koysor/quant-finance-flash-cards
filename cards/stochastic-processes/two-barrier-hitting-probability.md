# Two-Barrier Hitting Probability

**Topic:** Stochastic Processes
**Tags:** hitting probability, two barriers, scale function, double barrier, credit risk, GBM
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **two-barrier hitting probability** answers: given a process $X_t$ currently between a lower barrier $L$ and an upper barrier $U$, what is the probability that it hits $U$ before hitting $L$? For a drifted Brownian motion, this is derived via the **scale function** — a monotone function $s(x)$ that turns $X_t$ into a martingale, so that the hitting probability equals a simple ratio of scale function values.

## Key Formula

For $X_t = \mu t + \sigma W_t$ starting at $x \in (L, U)$, the **scale function** is $s(x) = e^{-2\mu x/\sigma^2}$ (or $s(x) = x$ if $\mu = 0$). The probability of hitting $U$ before $L$ is:

$$\Pr_x(\tau_U < \tau_L) = \frac{s(x) - s(L)}{s(U) - s(L)}$$

**Explicit form** for $\mu \neq 0$:

$$\Pr_x(\tau_U < \tau_L) = \frac{e^{-2\mu x/\sigma^2} - e^{-2\mu L/\sigma^2}}{e^{-2\mu U/\sigma^2} - e^{-2\mu L/\sigma^2}}$$

**Zero-drift special case** ($\mu = 0$, pure diffusion):

$$\Pr_x(\tau_U < \tau_L) = \frac{x - L}{U - L}$$

The probability is purely geometric — proportional to the fraction of the corridor already covered. Positive drift biases the probability upward; negative drift downward.

**For GBM** (replace $x$ with $\ln S_0$, $L$ with $\ln B_L$, $U$ with $\ln B_U$, $\mu$ with $\nu = r - \tfrac{1}{2}\sigma^2$):

$$\Pr(S_t \text{ hits } B_U \text{ first}) = \frac{(S_0/B_L)^\theta - 1}{(B_U/B_L)^\theta - 1}, \qquad \theta = \frac{2\nu}{\sigma^2} = \frac{2r}{\sigma^2} - 1$$

## Example

GBM with $S_0 = 100$, $B_L = 80$, $B_U = 130$, $r = 5\%$, $\sigma = 20\%$.

$$\nu = 0.05 - 0.02 = 0.03, \qquad \theta = \frac{2(0.03)}{0.04} = 1.5$$

$$(S_0/B_L)^\theta = (100/80)^{1.5} = 1.25^{1.5} \approx 1.398$$

$$(B_U/B_L)^\theta = (130/80)^{1.5} = 1.625^{1.5} \approx 2.072$$

$$\Pr(\text{hit } B_U = 130 \text{ first}) = \frac{1.398 - 1}{2.072 - 1} = \frac{0.398}{1.072} \approx 37.1\%$$

Complementary: $\Pr(\text{hit } B_L = 80 \text{ first}) \approx 62.9\%$. Despite the positive drift, the stock is closer to the lower barrier (£20 below vs £30 above) and the diffusion dominates at this horizon.

## Remember

The scale function result is the exact analogue of the zero-drift geometric ratio, extended to handle drift through the exponential weighting $e^{-2\mu x/\sigma^2}$. In **credit modelling**, the two-barrier problem describes a firm that can be upgraded (hits upper barrier first) or default (hits lower barrier first) — the hitting probability gives the risk-neutral probability of each outcome without solving the full first passage time distribution. In **double-barrier option pricing**, the same probability determines the composition of the infinite image series: each image term is weighted by the probability of crossing that image barrier, and the series converges quickly because hitting probability decays geometrically in the number of reflections.
