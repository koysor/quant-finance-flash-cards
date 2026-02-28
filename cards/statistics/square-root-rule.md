# Square-Root Rule for Volatility

**Topic:** Statistics
**Tags:** volatility, standard deviation, scaling, square root, risk
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The **square-root rule** states that the standard deviation (volatility) of returns scales with the square root of the time period, not linearly. This follows from the variance addition rule for independent random variables: variances add, so standard deviations grow as $\sqrt{n}$.

## Key Formula

$$\text{Std dev over } \delta t = \sigma \sqrt{\delta t}$$

**Annualising daily volatility:**

$$\sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252}$$

**Variance addition rule (independent returns):**

$$\text{Var}_{\text{total}} = n \times \text{Var}_{\text{daily}} \quad \Rightarrow \quad \sigma_{\text{total}} = \sqrt{n} \times \sigma_{\text{daily}}$$

## Example

If daily volatility is $0.89\%$:

- Weekly (5 days): $0.89\% \times \sqrt{5} \approx 2.0\%$
- Annual (252 days): $0.89\% \times \sqrt{252} \approx 14.1\%$

A common mistake is multiplying by 252 instead of $\sqrt{252}$, which would give $224\%$ — dramatically overstating risk.

## Remember

The square-root rule underpins how VaR is scaled across time horizons and why the $\sigma \sqrt{\delta t}$ term appears in the random walk model. It also explains why short-term price movements are dominated by noise: volatility shrinks more slowly than drift as the horizon shortens.
