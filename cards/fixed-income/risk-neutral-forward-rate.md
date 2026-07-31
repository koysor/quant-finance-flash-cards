# Risk-Neutral vs Real-World Forward Rates

**Topic:** Fixed Income
**Tags:** forward rate, risk-neutral measure, term premium, market price of risk, Q-measure, P-measure
**Created:** 2026-06-21
**Author:** Claude Sonnet 4.6

---

## Definition

The forward rate $f(0,T)$ implied by today's yield curve equals the **risk-neutral expectation** of the future short rate, $\mathbb{E}^Q[r_T]$, not the real-world expectation $\mathbb{E}^P[r_T]$. The gap between them is the **term premium** $\lambda(T) = f(0,T) - \mathbb{E}^P[r_T]$: the extra yield investors demand for bearing duration risk rather than rolling over short-term bills.

## Key Formula

Under the risk-neutral measure $Q$, the zero-coupon bond price and instantaneous forward rate satisfy:

$$P(0,T) = \mathbb{E}^Q\!\left[e^{-\int_0^T r_s\,ds}\right], \qquad f(0,T) = -\frac{\partial \ln P(0,T)}{\partial T}$$

Girsanov's theorem links the two measures via the market price of risk $\lambda$. For a short-rate model with constant $\lambda$:

$$dr = \underbrace{\bigl(\mu(r,t) + \lambda\sigma\bigr)}_{\text{real-world drift}}\,dt + \sigma\,dW^P \;=\; \underbrace{\eta(t)}_{\text{Q-drift}}\,dt + \sigma\,dW^Q$$

so that $\mathbb{E}^Q[r_T] \approx \mathbb{E}^P[r_T] + \lambda\sigma T$ for small $\lambda\sigma T$. The term premium grows linearly with maturity and rate volatility — longer bonds carry proportionally more duration risk.

## Example

Suppose the 5Y5Y forward rate (the 5-year rate, 5 years forward) reads 4.1%, but a survey of professional forecasters puts the expected 5-year rate in 5 years at 3.2%. The implied term premium is $4.1\% - 3.2\% = 0.9\%$, meaning markets are embedding 90 bp of compensation for duration risk at that horizon.

If rate volatility is $\sigma = 1\%$ per year and the term premium grows as $\lambda\sigma T = 0.9\%$ over 5 years, the implied market price of risk is $\lambda = 0.9\% / (1\% \times 5) = 0.18$ — a positive value consistent with investors requiring a premium for holding long-maturity bonds.

## Remember

Forward rates are not forecasts. In a normal upward-sloping yield curve, the term premium makes forwards systematically overstate where short rates will actually be — the **forward rate bias** well documented in the empirical literature. Central banks use explicit term-premium models (e.g. the ACM model published by the New York Fed, or the Kim-Wright model) to strip out the risk premium and read off what rate expectations are truly embedded in bond prices. A trader using unstripped forward rates as rate forecasts will consistently over-hedge duration.
