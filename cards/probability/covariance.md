# Covariance

**Topic:** Probability
**Tags:** covariance, correlation, joint distribution, portfolio risk, linear dependence
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Covariance** $\text{Cov}(X, Y)$ measures the degree to which two random variables move together: a positive value indicates they tend to move in the same direction, a negative value indicates opposite directions, and zero indicates no linear dependence.

$$\text{Cov}(X, Y) = E\!\left[(X - \mu_X)(Y - \mu_Y)\right] = E[XY] - \mu_X \mu_Y$$

## Key Formula

**Computational shortcut:**

$$\text{Cov}(X, Y) = E[XY] - E[X]\,E[Y]$$

**Symmetry and linearity:**

$$\text{Cov}(X, Y) = \text{Cov}(Y, X)$$

$$\text{Cov}(aX + b,\, cY + d) = ac\,\text{Cov}(X, Y)$$

**Relationship to correlation:**

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X\,\sigma_Y}, \qquad -1 \le \rho_{XY} \le 1$$

**Special cases:**

$$\text{Cov}(X, X) = \text{Var}(X)$$

$$X \perp\!\!\!\perp Y \implies \text{Cov}(X, Y) = 0 \quad \text{(converse not generally true)}$$

## Example

Stock $A$ has $\sigma_A = 15\%$, stock $B$ has $\sigma_B = 10\%$, and their correlation is $\rho = 0.3$.

$$\text{Cov}(R_A, R_B) = \rho\,\sigma_A\,\sigma_B = 0.3 \times 0.15 \times 0.10 = 0.0045$$

For a portfolio with weights $w_A = 0.6$, $w_B = 0.4$:

$$\text{Var}(R_P) = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2\,w_A w_B\,\text{Cov}(R_A, R_B)$$

$$= 0.36(0.0225) + 0.16(0.01) + 2(0.6)(0.4)(0.0045) = 0.0081 + 0.0016 + 0.00216 = 0.01186$$

## Remember

Covariance is the engine of diversification. In a two-asset portfolio, reducing covariance (or equivalently, correlation) lowers portfolio variance without affecting expected return — this is the key mechanism in Markowitz optimisation. The sign and magnitude of covariance between assets determines whether combining them reduces or amplifies risk. A zero-covariance pair is not necessarily independent, but independent assets always have zero covariance — a subtle but important distinction for model assumptions in multi-factor risk models.
