# Scaling of Mean Returns with Time

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** mean, drift, scaling, time, annualisation

---

## Definition

The mean (expected) return scales **linearly** with the length of the time step. If the annualised drift is $\mu$, then the expected return over a period $\delta t$ (as a fraction of a year) is $\mu \, \delta t$. This follows from independent returns adding over successive periods.

## Key Formula

$$\text{Mean return over } \delta t = \mu \, \delta t$$

**Annualising a daily mean:**

$$\mu = \bar{R}_{\text{daily}} \times 252$$

where 252 is the approximate number of trading days per year.

## Example

If the daily mean return is $0.035\%$:

$$\mu = 0.00035 \times 252 \approx 8.8\% \text{ per year}$$

A weekly mean return (5 trading days) is:

$$\bar{R}_{\text{weekly}} = 0.00035 \times 5 = 0.175\%$$

## Remember

Mean return scaling linearly with time contrasts sharply with volatility, which scales with the square root of time. This difference is why drift dominates over long horizons but is swamped by noise in the short term — a key insight for portfolio construction and risk management.
