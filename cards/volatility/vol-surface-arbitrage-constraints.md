# Volatility Surface Arbitrage Constraints

**Topic:** Volatility
**Tags:** arbitrage-free, volatility surface, butterfly arbitrage, calendar spread, static arbitrage, no-arbitrage
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

An implied volatility surface is **free of static arbitrage** if and only if it satisfies three families of constraints: **butterfly arbitrage** (no negative probability density at any strike), **calendar spread arbitrage** (total variance non-decreasing in maturity at each strike), and **call spread arbitrage** (call prices non-increasing in strike). Violating any constraint allows a model-free profit from a portfolio of traded options — a fundamental requirement for any vol surface used in production pricing.

## Key Formula

Let $w(k, T) = \hat{\sigma}^2(k,T)\cdot T$ be the total implied variance as a function of log-moneyness $k$ and maturity $T$.

**Butterfly arbitrage free** (positive density): the probability density of $\ln(S_T/F)$ is non-negative iff:

$$g(k) = \left(1 - \frac{k\,\partial_k w}{2w}\right)^2 - \frac{(\partial_k w)^2}{4}\!\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{\partial_{kk} w}{2} \ge 0 \quad \forall k$$

**Calendar spread arbitrage free**: for $T_1 < T_2$:

$$w(k, T_1) \le w(k, T_2) \quad \forall k$$

i.e. total implied variance must be non-decreasing in maturity at each fixed strike.

**Call spread arbitrage free**: call prices $C(K, T)$ must be non-increasing and convex in $K$, which is implied by the butterfly condition.

## Example

A normalising flow vol surface generator produces a surface with $\partial_T w(0, T) < 0$ at the 1-week to 1-month transition — a calendar spread violation. Near-dated total variance is 0.0160 ($\approx 20\%$ annualised vol for 1 week) and 1-month total variance is 0.0144 ($\approx 18\%$). Any trader can lock in a riskless profit: sell the 1-week ATM straddle and buy the 1-month ATM straddle. This violation is detected automatically by checking the calendar spread condition before using any generated surface for pricing.

## Remember

Arbitrage constraints are the **sanity checks** that any generated or calibrated vol surface must pass before being used for pricing. Normalising flows and RL-trained pricing models do not automatically respect these constraints — a flow that minimises likelihood on historical surfaces may occasionally generate a surface with a localised butterfly violation in the far wings or a calendar spread violation at short maturities. Production systems therefore apply a **post-processing filter**: check all three constraint families on the generated surface and either reject the sample or apply a convex projection to the nearest arbitrage-free surface. For SVI slices, the butterfly constraint reduces to $b(1+|\rho|) \le 2/T$, providing an analytical filter on the five SVI parameters.
