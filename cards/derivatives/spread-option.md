# Spread Option

**Topic:** Derivatives
**Tags:** spread option, Kirk approximation, multi-asset, energy derivatives, basis risk, correlation
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **spread option** pays $\max(S_T^{(1)} - S_T^{(2)} - K, 0)$ at expiry — the excess of one asset price over another, minus a strike. Common in energy markets (crude oil vs refinery products, gas vs power) and fixed income (yield curve steepeners), spread options are fundamentally multi-asset instruments whose price depends critically on the correlation $\rho$ between the two underlyings.

## Key Formula

**Kirk's approximation** (1995) reduces the two-asset problem to a single-asset Black-Scholes formula by approximating $S_T^{(1)} - K$ as a log-normal:

$$C_\text{Kirk} = F_1 N(d_1) - (F_2 + K)\,N(d_2)$$

where $F_i = S_i^{(0)} e^{(r - q_i)T}$ are the forwards, and the effective volatility is:

$$\sigma_\text{Kirk} = \sqrt{\sigma_1^2 - 2\rho\,\sigma_1\sigma_2\,\frac{F_2}{F_2 + K} + \sigma_2^2\left(\frac{F_2}{F_2 + K}\right)^2}$$

with $d_{1,2} = \bigl(\ln(F_1/(F_2+K)) \pm \tfrac{1}{2}\sigma_\text{Kirk}^2 T\bigr)/(\sigma_\text{Kirk}\sqrt{T})$.

## Example

Brent crude ($S^{(1)} = \$80$) vs WTI crude ($S^{(2)} = \$76$), $K = \$3$, $T = 3$ months, $\sigma_1 = 30\%$, $\sigma_2 = 28\%$, $\rho = 0.92$, $r = 5\%$. Kirk gives $\sigma_\text{Kirk} = 10.2\%$ — the high correlation reduces the effective vol dramatically from either individual vol. The spread call is priced at \$1.47. A Monte Carlo RL pricer trained on correlated GBM paths prices it at \$1.51, capturing the non-linearity that Kirk's log-normal approximation misses when $K$ is large relative to $F_2$.

## Remember

Spread option pricing makes correlation a first-order risk factor rather than a second-order correction: at $\rho \to 1$, the spread variance collapses to zero and the option is essentially worthless; at $\rho \to -1$, the two assets diverge and the option becomes very valuable. RL pricers have a natural advantage over Kirk's approximation for spread options when the strike $K$ is large relative to $F_2$ (making the log-normal approximation inaccurate) or when the individual assets have stochastic volatility — the RL agent simply trains on correlated Heston paths and learns the correct pricing function without any analytical approximation.
