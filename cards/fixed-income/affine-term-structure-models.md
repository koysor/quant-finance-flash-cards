# Affine Term Structure Models

**Topic:** Fixed Income
**Tags:** affine term structure, bond pricing, short rate, yield curve, closed form, risk-neutral
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Affine Term Structure Models (ATSMs) are a class of interest rate models in which zero-coupon bond yields are affine (linear plus constant) functions of a state vector, enabling closed-form bond pricing via an exponential-affine formula when the state dynamics are affine under the risk-neutral measure.

## Key Formula

The zero-coupon bond price for maturity $T$ at time $t$ is:

$$P(t, T) = \exp\!\left(A(t,T) - B(t,T)^\top X_t\right)$$

where $X_t \in \mathbb{R}^n$ is the state vector (e.g. short rate, slope factor, curvature factor), and $A(t,T) \in \mathbb{R}$ and $B(t,T) \in \mathbb{R}^n$ satisfy a system of Riccati ordinary differential equations derived from the no-arbitrage drift condition. The implied yield is affine:

$$y(t,T) = -\frac{\ln P(t,T)}{T-t} = -\frac{A(t,T)}{T-t} + \frac{B(t,T)^\top}{T-t} X_t$$

The Vasicek model (Gaussian short rate) and CIR model (square-root short rate) are one-factor ATSMs; the Nelson-Siegel and DNS models are three-factor ATSMs with level, slope, and curvature state variables.

## Example

A two-factor Gaussian ATSM is calibrated to the UK gilt curve. State vector $X_t = (r_t, s_t)$ where $r_t$ is the short rate (0.042) and $s_t$ is a slope factor (-0.012). For a 10-year gilt: $A(0,10) = 0.031$, $B(0,10)^\top = (6.32, 4.18)$. Bond price $P = e^{0.031 - 6.32 \times 0.042 - 4.18 \times (-0.012)} = e^{-0.184} = 0.832$, giving a yield of 1.84% per annum. Re-pricing after a 25bp rate move takes microseconds.

## Remember

ATSMs dominate government bond desks because the exponential-affine formula lets traders re-price entire books of bonds and interest rate swaps in real time as the yield curve shifts — no Monte Carlo simulation required. The Riccati ODE for $B(t,T)$ typically has a closed-form solution for Gaussian models (Vasicek) and must be solved numerically for square-root models (CIR). The trade-off is that the affine constraint prevents these models from fitting non-affine features such as the humped volatility structure seen in swaptions.
