# Convexity Adjustment under Stochastic Rates

**Topic:** Fixed Income
**Tags:** convexity adjustment, stochastic rates, futures, FRA, correlation, expectation
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

A **convexity adjustment** is the correction applied to a forward rate when the instrument's settlement timing creates a correlation between the payoff and the discount factor. Under stochastic rates, you cannot factor the discount factor out of the expectation, and the gap between the futures rate and the true forward rate must be corrected explicitly.

## Key Formula

For a Eurodollar futures (or STIR futures) contract versus the corresponding forward rate $F$, the convexity adjustment under the Vasicek model is approximately:

$$\text{Futures rate} \approx F + \frac{\sigma^2}{2\gamma^2}\!\left(1 - e^{-\gamma T_1}\right)\!\left(1 - e^{-\gamma T_2}\right)$$

where $T_1$ is the futures expiry and $T_2$ is the end of the underlying accrual period.

More generally, for any payoff $H(r)$ at time $T$ paid at time $T$ (not at the forward measure maturity), the corrected value is:

$$V = P(0,T)\,\mathbb{E}^{T}[H(r)] + \text{covariance correction}$$

| Situation | Convexity adjustment | Sign |
|---|---|---|
| Eurodollar futures vs FRA | Futures rate $>$ forward rate | Positive — futures holder benefits from daily P&L margining |
| CMS coupon vs swap rate | CMS rate $>$ forward swap rate | Positive — CMS is paid at coupon date, not swap maturity |
| In-arrears swap | In-arrears rate $\neq$ forward rate | Positive — fixing and payment on the same date |

## Example

With $\sigma = 1\%$, $\gamma = 0.5$, $T_1 = 2$, $T_2 = 2.25$ years: adjustment $= \frac{(0.01)^2}{2 \times 0.25}(1 - e^{-1})(1 - e^{-1.125}) = 0.0002 \times 0.632 \times 0.675 = 8.5$ bp. The Eurodollar futures rate is about 8.5 bp above the true FRA forward rate for a 2-year expiry.

## Remember

Convexity adjustments are the direct consequence of the **stochastic discount factor** in fixed-income pricing: when the discount factor is correlated with the payoff (both depend on the same rate), the expectation of their product is not the product of their expectations. The adjustment is always positive for futures versus forwards (daily margining on futures benefits the long in a falling-rate environment) and for in-arrears instruments (early settlement creates a positive correlation between the payoff and the discount factor). Ignoring convexity adjustments can cause 5–20 bp errors on 10-year+ instruments — material for precise curve construction.
