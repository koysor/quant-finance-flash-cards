# Copulas

**Topic:** Probability
**Tags:** copulas, tail dependence, joint distribution, credit risk, multivariate
**Author:** Claude Opus 4.6

---

## Definition

A **copula** is a function that joins marginal distributions into a joint distribution, separating the dependence structure from the individual variable behaviours. Sklar's theorem guarantees that any joint distribution can be decomposed into its marginals and a copula. This allows modelling complex dependencies — including asymmetric tail dependence — that the multivariate normal cannot capture.

## Key Formula

**Sklar's theorem:** For any joint CDF $F(x, y)$ with marginals $F_X(x)$ and $F_Y(y)$, there exists a copula $C$ such that:

$$F(x, y) = C\!\left(F_X(x), \; F_Y(y)\right)$$

**Gaussian copula** (most widely used):

$$C_\rho^{\text{Ga}}(u, v) = \Phi_2\!\left(\Phi^{-1}(u), \; \Phi^{-1}(v); \; \rho\right)$$

where $\Phi^{-1}$ is the standard normal quantile function and $\Phi_2$ is the bivariate normal CDF with correlation $\rho$.

**Tail dependence coefficient** (lower tail):

$$\lambda_L = \lim_{u \to 0^+} P\!\left(Y \leq F_Y^{-1}(u) \mid X \leq F_X^{-1}(u)\right)$$

The Gaussian copula has $\lambda_L = 0$ for $\rho < 1$, meaning it underestimates joint extreme events.

## Example

Two assets each have Student-$t$ marginals with 5 degrees of freedom. We model their dependence using a Clayton copula with parameter $\theta = 2$.

The lower tail dependence is $\lambda_L = 2^{-1/\theta} = 2^{-0.5} \approx 0.71$.

This means that when one asset is in its worst 1% of outcomes, there is a 71% probability the other is also in its worst 1%. A Gaussian copula with the same rank correlation would give $\lambda_L = 0$ — dramatically underestimating joint crash risk.

## Remember

The Gaussian copula became infamous after the 2008 financial crisis. David Li's 2000 paper used it to price collateralised debt obligations (CDOs), but the model's zero tail dependence meant it systematically underpriced the risk of widespread simultaneous defaults. When the housing market collapsed, losses were far more correlated than the Gaussian copula predicted. The lesson is that the choice of copula — not just the marginals or the correlation — determines how a model handles joint extremes. Student-$t$ and Clayton copulas, which have non-zero tail dependence, are now preferred for credit risk and portfolio stress testing.
