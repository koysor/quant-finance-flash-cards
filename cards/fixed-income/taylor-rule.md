# Taylor Rule

**Topic:** Fixed Income
**Tags:** taylor rule, monetary policy, inflation, output gap, neutral rate, interest rate
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The Taylor Rule is a monetary policy guideline that prescribes the short-term interest rate as a function of the inflation gap and the output gap, providing a systematic benchmark for judging whether current policy is accommodative or restrictive relative to economic conditions.

## Key Formula

$$r_t = r^* + \pi_t + \alpha(\pi_t - \pi^*) + \beta(y_t - y_t^*)$$

where $r^*$ is the neutral real rate, $\pi_t$ is current inflation, $\pi^*$ is the inflation target (typically 2%), $(y_t - y_t^*)$ is the output gap, and $\alpha, \beta > 0$ are response coefficients. Taylor's original calibration used $\alpha = \beta = 0.5$.

The coefficient $1 + \alpha > 1$ on inflation ensures that when inflation rises by 1%, the nominal rate rises by more than 1%, so the **real rate increases** and genuinely restrains the economy.

## Example

US, Q1 2022: inflation $\pi_t = 8.0\%$, inflation gap $= 6.0\%$, output gap $= +1.5\%$, neutral rate $r^* = 0.5\%$. Taylor Rule prescription: $0.5 + 8.0 + 0.5 \times 6.0 + 0.5 \times 1.5 = 12.25\%$. Actual Fed funds rate: 0.25%. The 12pp gap signalled that policy was far behind the curve, foreshadowing the fastest tightening cycle since the 1980s: the Fed subsequently raised rates from 0.25% to 5.25% in 16 months.

## Remember

Fixed income traders use Taylor Rule comparisons to anticipate central bank moves before they happen. A large positive gap (actual rate well below the rule rate) predicts aggressive future hikes, which steepens the 2–5 year part of the yield curve as the market prices in the tightening path. The Taylor Rule also underpins the expectations component in DNS and ATSM models: the rule is the structural model explaining why $\mathbb{E}_t[r_{t+k}]$ responds to macro data releases. When CPI surprises to the upside, 2-year yields rise sharply precisely because the market updates its Taylor Rule forecast of the Fed's reaction function.
