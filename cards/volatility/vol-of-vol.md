# Vol of Vol

**Topic:** Volatility
**Tags:** vol of vol, volvol, stochastic volatility, heston, smile curvature, variance process
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Vol of vol ($\xi$, also written volvol) is the volatility of the variance process in a stochastic volatility model; it is the primary driver of implied volatility smile curvature — the degree to which wings are elevated relative to the at-the-money level.

## Key Formula

In the Heston model the variance $V_t$ follows:

$$dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$$

The effect of $\xi$ on smile curvature is captured by the leading-order approximation for short maturities:

$$\text{ATM smile curvature} \approx \frac{\xi^2}{8\kappa T}$$

A higher $\xi$ steepens the wings (raises far OTM implied vols relative to ATM) without changing the ATM level $\sqrt{\theta}$, while the mean-reversion speed $\kappa$ controls how quickly the curvature decays with maturity — larger $\kappa$ flattens the smile for longer-dated options.

## Example

Two Heston calibrations to SPX options both fit the ATM implied vol of 18%. Calibration A: $\xi = 0.30$ — the 10-delta put implied vol is 22.5% (4.5-point wing). Calibration B: $\xi = 0.80$ — the same 10-delta put implied vol is 27.1% (9.1-point wing). Both models price ATM options identically; Calibration B's higher vol of vol makes far-out-of-the-money puts considerably more expensive, reflecting fatter tails in the risk-neutral distribution.

## Remember

Vol of vol is the key risk factor for second-order volatility products: VIX options, variance swaps on variance, and volatility-of-volatility swaps. A trader long a VIX call profits if VIX rises, but the payoff is also amplified by how much VIX itself fluctuates — i.e. by $\xi$. Mis-estimating vol of vol causes systematic mis-pricing of these instruments and of gap risk in leveraged volatility strategies, where a sudden spike in $\xi$ can cause losses far beyond those predicted by a constant-vol-of-vol model.
