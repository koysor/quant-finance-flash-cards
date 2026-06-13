# Black–Karasinski Model

**Topic:** Fixed Income
**Tags:** Black-Karasinski, short rate, lognormal, mean reversion, calibration, interest rate model
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Black–Karasinski (BK) model** (1991) is a lognormal short-rate model with explicit mean reversion. Rather than the rate itself, it is the **logarithm of the rate** that mean-reverts to a time-dependent level. This guarantees strictly positive rates and produces a richer volatility structure than Black–Derman–Toy, while preserving full calibration to the observed yield curve.

## Key Formula

$$d\ln r = \bigl(\theta(t) - a(t)\ln r\bigr)\,dt + \sigma(t)\,dW$$

Equivalently, writing $x = \ln r$:

$$dx = \bigl(\theta(t) - a(t) x\bigr)\,dt + \sigma(t)\,dW$$

| Parameter | Role |
|---|---|
| $\theta(t)$ | Time-dependent drift — calibrated to match the initial yield curve |
| $a(t)$ | Mean-reversion speed — always positive, rates pulled back in log space |
| $\sigma(t)$ | Log-volatility — calibrated to fit cap or swaption prices |

Bond prices and derivative values are computed by backward induction on a **trinomial tree** built in $x = \ln r$ space.

## Example

With constant parameters $a = 0.10$, $\sigma = 0.18$ and $r_0 = 5\%$: the BK log-rate process has equilibrium level $\bar x = \theta/a$, around which rates fluctuate lognormally. A trinomial tree with time steps $\Delta t = 0.25$ yr gives node spacing $\Delta x = \sigma\sqrt{3\Delta t} \approx 0.156$ in log-rate, so adjacent nodes differ by a factor of $e^{0.156} \approx 1.17$ in rate terms — a 17% relative spacing regardless of the rate level.

## Remember

BK solves the main practical defect of the Black–Derman–Toy model: in BDT the implied mean-reversion speed can become **negative at long maturities** when the cap volatility term structure is humped, producing explosive behaviour. BK makes mean-reversion an explicit, always-positive parameter $a(t)$, so long-maturity rates cannot explode. The cost is that BK produces **no closed-form bond prices** — everything requires numerical tree methods — but this is acceptable given that interest rate books are priced on trees anyway. BK remains a market standard for mortgage prepayment models and Bermudan swaption pricing where lognormal rates are assumed.
