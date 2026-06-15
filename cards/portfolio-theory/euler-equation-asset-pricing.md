# Euler Equation (Asset Pricing)

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** euler equation, stochastic discount factor, expected return, risk premium, asset pricing, no-arbitrage
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **asset pricing Euler equation** is the fundamental no-arbitrage condition that every asset must satisfy: the expected product of the stochastic discount factor $M_{t+1}$ and the gross return $R_{t+1}^i$ equals one. It is the master equation from which CAPM, Black–Scholes, and bond pricing all follow as special cases.

## Key Formula

For any asset $i$ with gross return $R_{t+1}^i = (P_{t+1} + D_{t+1})/P_t$:

$$E_t\!\left[M_{t+1}\,R_{t+1}^i\right] = 1$$

For a **risk-free asset** earning $R_f$:

$$E_t[M_{t+1}] = \frac{1}{R_f} \implies R_f = \frac{1}{E_t[M_{t+1}]}$$

The **risk premium** on any asset follows from the covariance with the SDF:

$$E_t[R^i] - R_f = -R_f\,\text{Cov}_t(M_{t+1},\, R_{t+1}^i)$$

Assets whose returns covary **negatively** with $M$ (they pay well when the SDF is low, i.e. when the economy is booming) command positive risk premia.

## Example

Suppose $\text{Cov}(M, R_{\text{market}}) = -0.004$ and $R_f = 1.05$. The equity risk premium is:

$$E[R_{\text{market}}] - R_f = -1.05 \times (-0.004) = 0.42\%$$

per period. Equities earn a premium because they pay off poorly in recessions when investors most need wealth — making their covariance with M negative and the risk premium positive.

## Remember

The Euler equation reveals *why* different assets have different expected returns: it is not volatility per se, but **covariance with the SDF** (i.e. covariance with bad times) that determines the risk premium. A highly volatile asset that pays off in recessions earns no premium; a low-volatility asset that fails in recessions can demand a very large one. This is why credit spreads widen in downturns — credit losses covary with the SDF, so investors demand compensation far in excess of actuarial default rates.
