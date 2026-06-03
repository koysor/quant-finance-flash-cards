# Hull-White Model

**Topic:** Stochastic Processes
**Tags:** hull-white, short rate, yield curve, fixed income, interest rate model, bermudan swaption
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Hull-White model** (1990) extends the Vasicek model by replacing the constant mean-reversion level with a **time-dependent function** $\theta(t)$ that is chosen to fit the initial yield curve exactly. This makes Hull-White the simplest **arbitrage-free** short-rate model and the industry standard for pricing interest rate derivatives — including Bermudan swaptions — where consistency with the observed yield curve is required.

## Key Formula

Short-rate dynamics under the risk-neutral measure:

$$dr_t = \bigl(\theta(t) - \alpha r_t\bigr)\,dt + \sigma\,dW_t$$

where $\alpha > 0$ is the mean-reversion speed and $\sigma$ is the short-rate volatility. The function $\theta(t)$ is determined by the initial forward curve $f(0,t)$:

$$\theta(t) = \frac{\partial f(0,t)}{\partial t} + \alpha f(0,t) + \frac{\sigma^2}{2\alpha}\!\left(1 - e^{-2\alpha t}\right)$$

**Zero-coupon bond price** (closed form):

$$P(t,T) = A(t,T)\,e^{-B(t,T)\,r_t}, \quad B(t,T) = \frac{1 - e^{-\alpha(T-t)}}{\alpha}$$

where $A(t,T)$ depends on the initial yield curve, $\alpha$, and $\sigma$.

## Example

A Bermudan swaption is exercisable annually over 5 years on a pay-fixed 10-year swap, strike = 3%. Calibration to today's yield curve sets $\theta(t)$ automatically, and calibration to the cap/floor market sets $\alpha$ and $\sigma$ ($\alpha = 0.05$, $\sigma = 0.01$). The Longstaff-Schwartz pricer runs 100,000 Hull-White paths and estimates the swaption at 85 bps. An RL agent (OST-TDBP) trained on the same paths reproduces 83 bps — the 2 bp gap is the LSM regression approximation error. Both require the same calibration inputs; the RL agent avoids the basis-function selection step.

## Remember

Hull-White is the workhorse short-rate model on rates desks for one reason: it fits the initial yield curve **exactly by construction**, eliminating the systematic mispricing that Vasicek (constant $\theta$) introduces when the yield curve is not flat. The time-dependent $\theta(t)$ is not a free parameter but a deterministic function pinned to market data, so Hull-White has only two free parameters ($\alpha$, $\sigma$) to calibrate to volatility instruments (caps, swaptions). For RL option pricing, Hull-White provides the canonical path generator for interest rate derivatives — training TDBP or OST-TDBP on Hull-White paths produces rate-consistent pricers without the parametric limitations of Vasicek or the computational cost of LMM.
