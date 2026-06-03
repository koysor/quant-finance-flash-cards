# Term Premium

**Topic:** Fixed Income
**Tags:** term premium, bond yield, expectations hypothesis, risk premium, yield curve, duration risk
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The term premium is the additional yield investors require for holding a long-maturity bond rather than rolling over short-term bonds to the same horizon, compensating for interest rate uncertainty, inflation risk, and liquidity risk that accumulates over a longer holding period.

## Key Formula

Under the **pure expectations hypothesis**, long yields equal the average expected short rate — no term premium. In reality, the $n$-year yield decomposes as:

$$y_t(n) = \underbrace{\frac{1}{n}\sum_{k=0}^{n-1}\mathbb{E}_t[r_{t+k}]}_{\text{rate expectations}} + \underbrace{tp_t(n)}_{\text{term premium}}$$

The term premium $tp_t(n)$ is extracted as the residual between the observed yield and the model's expected short-rate path. Common extraction models include Adrian-Crump-Moench (ACM), Kim-Wright, and DNS factor decomposition. The premium is time-varying, typically positive but can turn negative during risk-off episodes when investors pay for the safety of long bonds.

## Example

US 10-year Treasury yield: 4.50%. ACM model estimates the expected average Fed funds rate over ten years at 3.80%. Extracted term premium: $tp = 4.50\% - 3.80\% = 0.70\%$. In 2021, quantitative easing suppressed the 10-year term premium to $-0.50\%$ — investors accepted yields 50bp below expected short rates for the safety and liquidity of Treasuries. As QT began in 2022, the term premium normalised, contributing 50-80bp to the rise in long yields independently of rate-hike expectations.

## Remember

When a central bank begins quantitative tightening, standard rate-expectation models predict little change in long yields because they do not model the term premium. In practice, QT reduces the central bank's demand for long-dated bonds, pushing up the term premium and long yields even without rate hikes. Bond portfolio managers who attribute all yield moves to rate expectations will systematically underestimate duration risk during balance-sheet normalisation episodes, holding too much long-dated debt when it is most vulnerable.
