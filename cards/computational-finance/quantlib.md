# QuantLib

**Topic:** Computational Finance
**Tags:** derivatives pricing, fixed income, yield curve, calibration, c++, python bindings
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**QuantLib** is an open-source C++ library (with Python bindings via `QuantLib-Python`) that provides production-grade implementations of derivatives pricing models, yield curve bootstrapping, fixed income analytics, and model calibration — used by banks, asset managers, and central banks worldwide.

## Key Formula

QuantLib prices a European call by wiring together a process, an engine, and an instrument. The engine evaluates the Black-Scholes-Merton closed form:

$$C = S_0\,\Phi(d_1) - K e^{-rT}\Phi(d_2), \qquad d_{1,2} = \frac{\ln(S_0/K) + (r \pm \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

```python
import QuantLib as ql

today = ql.Date(31, 5, 2026)
ql.Settings.instance().evaluationDate = today

payoff   = ql.PlainVanillaPayoff(ql.Option.Call, 100.0)   # K=100
exercise = ql.EuropeanExercise(ql.Date(31, 5, 2027))       # T=1y
option   = ql.VanillaOption(payoff, exercise)

process  = ql.BlackScholesMertonProcess(
    ql.QuoteHandle(ql.SimpleQuote(105.0)),                 # S=105
    ql.YieldTermStructureHandle(ql.FlatForward(today, 0.02, ql.Actual365Fixed())),  # q=2%
    ql.YieldTermStructureHandle(ql.FlatForward(today, 0.05, ql.Actual365Fixed())),  # r=5%
    ql.BlackVolTermStructureHandle(ql.BlackConstantVol(today, ql.TARGET(), 0.20, ql.Actual365Fixed()))  # σ=20%
)
option.setPricingEngine(ql.AnalyticEuropeanEngine(process))
print(option.NPV())   # ≈ 14.23
```

## Remember

QuantLib is the reference implementation used to validate pricing models in derivatives desks. Its real power is in the **term structure** layer: yield curves, credit curves, and volatility surfaces are first-class objects that can be perturbed (bumped by 1 bp) to compute DV01s and Vegas automatically, without re-coding the bump logic for each instrument. For fixed income desks, `ql.DepositRateHelper`, `ql.SwapRateHelper`, and `ql.FraRateHelper` are the building blocks for bootstrapping a discount curve from market quotes — the same workflow that runs daily on every rates trading desk in the world.
