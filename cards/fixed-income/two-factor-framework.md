# Two-Factor Interest Rate Framework

**Topic:** Fixed Income
**Tags:** two-factor model, yield curve, slope, curvature, correlated Brownians, short rate
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

A **two-factor interest rate framework** lets the bond price depend on two stochastic state variables — typically the short rate $r$ and a second factor $l$ representing curve slope, long rate, or stochastic volatility. Two factors are the minimum needed to allow yield-curve slope and curvature to evolve independently of the level.

## Key Formula

Two correlated SDEs drive the state variables:

$$dr = u(r,l,t)\,dt + w(r,l,t)\,dX_1$$

$$dl = p(r,l,t)\,dt + q(r,l,t)\,dX_2$$

$$\mathbb{E}[dX_1\,dX_2] = \rho\,dt$$

Because there are now **two** sources of randomness, a risk-free hedge requires **two** other bonds:

$$\Pi = V(r,l,t;T) - \Delta_1 V_1(r,l,t;T_1) - \Delta_2 V_2(r,l,t;T_2)$$

Each factor has its own market price of risk: $\lambda_r$ for the short-rate factor and $\lambda_l$ for the second factor.

## Example

In a two-factor model for the UK gilt curve, $r$ is the overnight rate (level factor, $\kappa_r = 0.3$) and $l$ is the 10-year rate minus the overnight rate (slope factor, $\kappa_l = 0.8$, faster mean-reverting). With $\rho = -0.4$, the two factors are negatively correlated — a surprise rate rise tends to flatten the curve. This produces a richer cross-maturity correlation structure than any one-factor model.

## Remember

A one-factor model forces a perfect correlation of 1 between all yield changes across maturities — every maturity moves in lock-step. This is empirically false: the PCA of yield curve changes shows that three factors (level, slope, curvature) explain over 99% of variance. A two-factor model is the minimum that allows the slope to change independently of the level, which is essential for pricing products such as yield curve steepeners, spread options, and CMT-indexed mortgages.
