# Stochastic Discount Factor

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** stochastic discount factor, pricing kernel, risk-neutral pricing, asset pricing, sharpe ratio
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **stochastic discount factor** (SDF), also called the **pricing kernel**, is a random variable $M_{t,T}$ such that the price of any asset equals the expectation — under the physical measure $\mathbb{P}$ — of the SDF multiplied by the asset's future payoff. It encodes both time value and risk aversion in a single object.

## Key Formula

For any asset with time-$T$ payoff $V_T$:

$$V_t = E_t^{\mathbb{P}}\!\left[M_{t,T} \cdot V_T\right]$$

Under the risk-neutral measure $\mathbb{Q}$, the SDF takes the special form:

$$M_{t,T} = e^{-\int_t^T r_s\,ds} \cdot \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T}$$

The Sharpe ratio of any asset is bounded by the **volatility of the SDF**:

$$\frac{E^{\mathbb{P}}[R] - r_f}{\text{std}(R)} \leq \frac{\text{std}(M)}{E^{\mathbb{P}}[M]}$$

This Hansen–Jagannathan bound is the theoretical maximum Sharpe ratio achievable by any portfolio.

## Example

Suppose the SDF has $E^{\mathbb{P}}[M] = 0.95$ (5% risk-free rate) and $\text{std}(M) = 0.30$. The bound says no portfolio can have a Sharpe ratio above $0.30/0.95 \approx 0.316$ annually. A fund claiming a Sharpe ratio of 1.0 under these conditions would violate the bound and imply either mis-stated returns or a missing risk factor.

## Remember

The SDF is the unifying object behind all asset pricing: Black–Scholes risk-neutral pricing (SDF = $e^{-rT}$ times the Radon–Nikodym derivative), CAPM (SDF linear in market return), and bond pricing (SDF = $e^{-\int r\,ds}$ under $\mathbb{Q}$) are all special cases. When a new pricing model is proposed, the first question is whether it implies a well-behaved SDF — positive, with moments that are consistent with observed Sharpe ratios.
