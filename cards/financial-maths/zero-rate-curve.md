# Zero Rate Curve

**Topic:** Financial Mathematics
**Tags:** zero rate, spot rate, term structure, discounting, zero-coupon bond
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

The **zero rate curve** (also called the spot rate curve) plots the yield on zero-coupon bonds against maturity. Each zero rate $r(T)$ is the annualised return earned when a single cash flow is received at time $T$ — it is a pure, coupon-free discount rate with no reinvestment risk, making it the cleanest measure of the time value of money at each horizon.

## Key Formula

The **zero rate** $r(T)$ is extracted from the price $P(T)$ of a zero-coupon bond with face value £1:

$$P(T) = e^{-r(T) \cdot T} \quad \Longrightarrow \quad r(T) = -\frac{\ln P(T)}{T}$$

A cash flow $C$ received at time $T$ is discounted to its present value using the zero rate for that exact maturity:

$$PV = C \cdot e^{-r(T) \cdot T}$$

When coupon bonds are observed instead of zero-coupon prices, the curve is built by **bootstrapping** — solving for each successive zero rate using already-known shorter-maturity rates:

$$P_n = \sum_{i=1}^{n-1} c_i \, e^{-r(t_i) \cdot t_i} + (c_n + 100) \, e^{-r(t_n) \cdot t_n}$$

## Example

Two instruments are observed in the market:

- 1-year zero-coupon bond priced at £95.12 (face £100)
- 2-year annual-coupon bond with 5% coupon, priced at £99.05 (face £100)

**Step 1** — extract the 1-year zero rate:

$$r(1) = -\frac{\ln(95.12/100)}{1} = -\ln(0.9512) \approx 5.00\%$$

**Step 2** — bootstrap the 2-year zero rate using the known 1-year rate:

$$99.05 = 5 \cdot e^{-0.05 \times 1} + 105 \cdot e^{-r(2) \times 2}$$

$$e^{-2r(2)} = \frac{99.05 - 4.756}{105} = 0.8979 \quad \Rightarrow \quad r(2) \approx 5.45\%$$

## Remember

The zero rate curve is the fundamental building block of fixed-income pricing — every bond, swap, and interest rate derivative is valued by discounting each cash flow at the zero rate for its specific maturity. Unlike a par yield curve or forward rate curve, zero rates carry no reinvestment assumption, so they give an unambiguous discount factor for each date. In practice, the curve is bootstrapped from liquid instruments (government bonds, OIS swaps) and then interpolated to produce a smooth, continuous surface. Quants use the zero curve to construct discount factors, price interest rate swaps, and derive forward rates between any two dates.
