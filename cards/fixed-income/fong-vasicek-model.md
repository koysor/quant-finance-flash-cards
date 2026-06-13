# Fong–Vasicek Model

**Topic:** Fixed Income
**Tags:** Fong-Vasicek, stochastic volatility, interest rate, two-factor, CIR variance, unobservable factor
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Fong–Vasicek (1991) model extends Vasicek by making the short-rate variance $V$ stochastic via a separate CIR process, creating a two-factor model in which both the rate level and its instantaneous volatility evolve randomly.

## Key Formula

$$dr = \kappa(\theta - r)\,dt + \sqrt{V}\,dX_1$$

$$dV = \gamma(\bar{V} - V)\,dt + \sigma\sqrt{V}\,dX_2, \qquad \mathbb{E}[dX_1\,dX_2] = \rho\,dt$$

Bond price: $P(r, V, t) = e^{A(t,T) + B(t,T)r + C(t,T)V}$, where $A$, $B$, $C$ satisfy ODEs — with $B$ and $C$ admitting closed-form solutions under the risk-neutral dynamics.

Implied bond yield is affine in both $r$ and $V$: $y = -A/\tau - Br/\tau - CV/\tau$.

## Example

$r = 5\%$, $V = 0.04$ (instantaneous vol $= 20\%$), $\kappa = 0.3$, $\gamma = 2.0$, $\rho = -0.5$. The negative correlation means that when rates fall suddenly (flight-to-quality), variance spikes — a stylised fact consistent with the 2008 crisis. The bond price is sensitive to both $r$ and $V$: a rise in $V$ increases option-like value in callable bonds.

## Remember

Fong–Vasicek was the first interest rate model to incorporate stochastic volatility, anticipating by a decade the widespread use of stochastic vol in equity options (Heston, 1993). Its principal limitation is that the variance factor $V$ is unobservable — unlike the short rate $r$, which is inferred from overnight deposit rates. Calibration therefore requires filtering $V$ from the cross-section of bond prices, adding substantial model risk. Later practitioner models (SABR for swaptions, Heston for caps) solved this observability problem differently.
