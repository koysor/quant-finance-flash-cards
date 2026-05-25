# Entropy-Based Option Pricing

**Topic:** Derivatives
**Tags:** entropy, risk-neutral density, implied distribution, option pricing, maximum entropy, smile
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Entropy-based option pricing** recovers the risk-neutral probability density $q^*(S_T)$ implied by a set of observed option prices by selecting the density that maximises entropy (or minimises KL divergence from a prior) subject to pricing constraints. It avoids the need to assume a parametric model for the volatility smile.

## Key Formula

Given observed call prices $C_1, \ldots, C_n$ at strikes $K_1, \ldots, K_n$, find the risk-neutral density $q^*$ that solves:

$$\max_{q} \; H(q) = -\int q(s) \log q(s) \, ds$$

$$\text{subject to:} \quad e^{-rT}\int (s - K_i)^+ q(s)\, ds = C_i, \quad i = 1, \ldots, n$$

$$\int q(s)\, ds = 1, \qquad q(s) \geq 0$$

The solution has the **exponential tilting** form:

$$q^*(s) = \frac{q_0(s) \exp\!\left(-\sum_{i=1}^{n} \lambda_i (s - K_i)^+\right)}{Z}$$

where $q_0$ is a prior density (often log-normal), $\lambda_i$ are Lagrange multipliers calibrated to observed prices, and $Z$ is the normalising constant.

**Relative entropy (minimum cross-entropy) form** — minimise KL divergence from prior $q_0$:

$$\min_{q} \; D_{\text{KL}}(q \| q_0) \quad \text{subject to the same pricing constraints}$$

## Example

Three listed strikes on the FTSE 100 with 1-month expiry: $K = \{6800, 7000, 7200\}$ with observed call prices $\{220, 80, 15\}$. Taking $q_0$ as a log-normal with $\sigma = 15\%$, the maximum entropy method adjusts the three Lagrange multipliers until the model reproduces all three prices exactly. The resulting $q^*$ captures the left skew visible in the smile without requiring a parametric SV model such as Heston.

## Remember

Entropy-based option pricing is model-free in the sense that it imposes no parametric assumptions about volatility dynamics — it simply asks: "what is the most non-committal density consistent with observed market prices?" This is attractive when the number of liquid strikes is small and model mis-specification risk is high. The technique is closely related to **risk-neutral measure extraction** via the Breeden-Litzenberger formula (which requires a continuum of strikes and twice-differentiating $C(K)$): the entropy method is its practical counterpart when only a finite grid of strikes is available. In practice, the choice of prior $q_0$ matters: using the Black-Scholes log-normal as prior pulls the implied density towards normality and regularises the solution, preventing implausible spikes between strikes that unconstrained non-parametric methods can produce.
