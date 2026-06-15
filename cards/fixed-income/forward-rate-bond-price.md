# Forward Rate and Bond Price Relationship

**Topic:** Fixed Income
**Tags:** forward rate, bond price, log derivative, term structure, instantaneous forward rate, hjm
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **instantaneous forward rate** $f(t,T)$ is the rate implied by the market at time $t$ for riskless borrowing over the infinitesimal interval $[T, T + dT]$ in the future. It is the marginal cost of extending a bond's maturity and is obtained as the negative logarithmic derivative of the zero-coupon bond price with respect to maturity.

## Key Formula

$$f(t,T) = -\frac{\partial \ln P(t,T)}{\partial T}$$

Inverting this relationship, the bond price is the exponential of the integrated forward rates:

$$P(t,T) = \exp\!\left(-\int_t^T f(t,u)\,du\right)$$

The continuously compounded spot rate relates to the average forward rate:

$$R(t,T) = -\frac{\ln P(t,T)}{T - t} = \frac{1}{T-t}\int_t^T f(t,u)\,du$$

At the short end, $f(t,t) = r_t$ — the instantaneous forward rate at maturity $t$ equals the current short rate.

## Example

Suppose zero-coupon bond prices at $t = 0$ are $P(0,1) = 0.952$ and $P(0,2) = 0.898$. The continuously compounded spot rates are:

$$R(0,1) = -\ln 0.952 = 4.93\%, \quad R(0,2) = -\tfrac{1}{2}\ln 0.898 = 5.36\%$$

The approximate 1-year forward rate one year from now is:

$$f \approx \frac{\ln P(0,1) - \ln P(0,2)}{1} = \ln\!\frac{0.952}{0.898} = \ln 1.060 \approx 5.83\%$$

This is the market-implied cost of borrowing for the second year.

## Remember

The formula $f = -\partial\ln P/\partial T$ is the foundation of the HJM framework: instead of modelling the short rate $r_t$, HJM models the entire curve of instantaneous forward rates $f(t,T)$ for all $T$. Because $f$ and $P$ determine each other exactly via this formula, every choice of forward rate volatility implies a unique bond pricing model. This is also why forward rate curves are more informative than yield curves: two bonds with the same yield but different maturity profiles can imply very different forward rate curves.
