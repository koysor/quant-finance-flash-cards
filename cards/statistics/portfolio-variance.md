# Portfolio Variance

**Topic:** Statistics
**Tags:** portfolio variance, diversification, covariance, mean-variance, risk
**Author:** Claude Opus 4.6

---

## Definition

**Portfolio variance** measures the total risk of a portfolio by combining the individual asset variances with the covariances between every pair of assets. It captures how the weights, volatilities, and co-movements of the constituent assets interact to determine the overall portfolio risk.

## Key Formula

**Two-asset portfolio:**

$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \, \text{Cov}(R_1, R_2)$$

Equivalently, using correlation:

$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2$$

**General $n$-asset portfolio (matrix form):**

$$\sigma_p^2 = \mathbf{w}^\top \Sigma \, \mathbf{w}$$

## Example

Two assets: $\sigma_1 = 25\%$, $\sigma_2 = 10\%$, $\rho = -0.4$, with weights $w_1 = 0.4$, $w_2 = 0.6$.

$$\sigma_p^2 = 0.4^2 \times 0.25^2 + 0.6^2 \times 0.10^2 + 2 \times 0.4 \times 0.6 \times (-0.4) \times 0.25 \times 0.10$$

$$= 0.0100 + 0.0036 - 0.0048 = 0.0088$$

$$\sigma_p = \sqrt{0.0088} \approx 9.4\%$$

The portfolio volatility (9.4%) is lower than either asset's weighted contribution alone — the negative correlation creates a diversification benefit.

## Remember

Portfolio variance is the objective function that Markowitz optimisation minimises. The key insight is that the cross-terms (covariance contributions) can be negative, allowing the portfolio to have less risk than any individual asset. This is why diversification works: as $\rho$ decreases, the cross-terms shrink or turn negative, pulling portfolio variance down. In practice, the minimum-variance portfolio often outperforms naive allocations precisely because it exploits these covariance relationships — but only if the covariance estimates are accurate.
