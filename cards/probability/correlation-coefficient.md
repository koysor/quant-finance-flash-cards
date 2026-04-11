# Correlation Coefficient

**Topic:** Probability
**Tags:** correlation, covariance, linear dependence, portfolio risk, diversification
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Pearson correlation coefficient** $\rho_{XY}$ is the normalised form of covariance: it scales $\text{Cov}(X, Y)$ by the product of the two standard deviations so the result always lies in $[-1, 1]$, making it a dimensionless, comparable measure of linear dependence.

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X\,\sigma_Y} = \frac{E[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\,\sigma_Y}$$

## Key Formula

$$-1 \le \rho_{XY} \le 1$$

| $\rho$ | Meaning |
|---|---|
| $+1$ | Perfect positive linear relationship |
| $0$ | No linear relationship |
| $-1$ | Perfect negative linear relationship |

**Recovering covariance from correlation:**

$$\text{Cov}(X, Y) = \rho_{XY}\,\sigma_X\,\sigma_Y$$

**Portfolio variance** (two assets, weights $w_1$, $w_2$):

$$\text{Var}(R_P) = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2\,w_1 w_2\,\rho_{12}\,\sigma_1\,\sigma_2$$

**Key property:** $\rho_{XY} = 0$ does not imply independence; it only means no *linear* dependence. Independent random variables always satisfy $\rho = 0$, but the converse is not generally true.

## Example

Stock $A$: $\sigma_A = 20\%$. Stock $B$: $\sigma_B = 15\%$. $\text{Cov}(R_A, R_B) = 0.018$.

$$\rho_{AB} = \frac{0.018}{0.20 \times 0.15} = \frac{0.018}{0.030} = 0.60$$

For a 50/50 portfolio:

$$\text{Var}(R_P) = 0.25(0.04) + 0.25(0.0225) + 2(0.25)(0.60)(0.20)(0.15)$$

$$= 0.01 + 0.005625 + 0.009 = 0.024625, \qquad \sigma_P \approx 15.7\%$$

Compare: if $\rho = 0$, then $\sigma_P \approx 12.5\%$ — lower correlation produces more diversification benefit.

## Remember

Correlation is the single parameter that controls how much diversification a two-asset portfolio achieves. Reducing $\rho$ from $1$ to $0$ to $-1$ monotonically reduces portfolio variance for fixed weights and individual volatilities — this is the mathematical mechanism behind the entire concept of diversification. In practice, correlations between risky assets are not stable: they tend to spike towards $+1$ during market crises (correlation breakdown), precisely when diversification is most needed, which is why multi-asset risk models must treat correlation as time-varying rather than constant.
