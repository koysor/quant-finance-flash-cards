# Correlation

**Topic:** Statistics
**Tags:** statistics, correlation, covariance, portfolio theory
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

**Correlation** measures the strength and direction of the **linear relationship** between two variables. It is the normalised form of covariance, scaled to always lie between −1 and +1.

## Key Formula

**Pearson correlation coefficient:**

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \, \sigma_Y}$$

Where covariance is:

$$\text{Cov}(X, Y) = E\!\left[(X - \mu_X)(Y - \mu_Y)\right] = E[XY] - E[X]\,E[Y]$$

## Interpretation

| ρ value | Meaning |
|---|---|
| +1 | Perfect positive linear relationship |
| 0 | No linear relationship |
| −1 | Perfect negative linear relationship |

## Example

Two stocks A and B have:
- σ_A = 20%, σ_B = 15%, Cov(A, B) = 0.018

ρ = 0.018 / (0.20 × 0.15) = 0.018 / 0.030 = **0.60**

A moderate positive correlation — the stocks tend to move together.

## Remember

- **Correlation is not causation.**
- Correlation only captures **linear** relationships. Two variables can be strongly related but have ρ ≈ 0 if the relationship is non-linear.
- In portfolio construction, combining assets with **low or negative correlation** reduces overall portfolio variance — this is the mathematical basis of **diversification**.
- During a market crisis, correlations between assets often spike towards +1, precisely when you need diversification most. This is known as **correlation breakdown**.
