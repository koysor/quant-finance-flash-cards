# Heath–Jarrow–Morton Framework

**Topic:** Fixed Income
**Tags:** hjm, heath-jarrow-morton, forward rate, interest rate model, no-arbitrage drift, term structure
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

The **Heath–Jarrow–Morton (HJM) framework** models the evolution of the entire instantaneous forward rate curve $f(t,u)$ directly under a no-arbitrage measure. Rather than modelling a single short rate $r_t$, HJM specifies the volatility structure $\sigma(t,u)$ of the forward rate, and the drift is then **fully determined** by the no-arbitrage condition.

## Key Formula

Forward rate dynamics under the risk-neutral measure:

$$df(t,u) = \mu(t,u)\,dt + \sigma(t,u)\,dW_t$$

**HJM no-arbitrage drift condition:**

$$\mu(t,u) = \sigma(t,u) \int_t^u \sigma(t,s)\,ds$$

The discount factor is recovered from the forward rate curve:

$$P(t,u) = \exp\!\left(-\int_t^u f(t,s)\,ds\right), \qquad r_t = f(t,t)$$

Choosing $\sigma(t,u) = \sigma e^{-\kappa(u-t)}$ recovers the **Hull–White** (extended Vasicek) short-rate model as a special case.

## Example

With constant volatility $\sigma(t,u) = \sigma$, the HJM drift is:

$$\mu(t,u) = \sigma \int_t^u \sigma\,ds = \sigma^2(u - t)$$

This is the **Ho-Lee model** — a special case of HJM with a linear drift, which allows negative rates and produces a perfectly flat forward curve under the risk-neutral measure.

## Remember

HJM is the **unifying framework** for term structure modelling: every no-arbitrage interest rate model (Vasicek, Hull-White, LIBOR Market Model) is a special case obtained by choosing a particular volatility function $\sigma(t,u)$. The critical insight is that **one cannot freely choose both drift and volatility** — the no-arbitrage condition ties the drift to the volatility, so specifying $\sigma$ alone determines the entire risk-neutral dynamics of the forward curve.
