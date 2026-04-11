# Diversification Bounds

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** diversification, correlation, portfolio risk, bounds, variance
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The correlation $\rho_{AB} \in [-1, 1]$ sets hard limits on how much diversification is achievable. The bounds define the **best-case** and **worst-case** portfolio risk for any combination of two assets.

## Key Formula

$$|w_A\sigma_A - w_B\sigma_B| \;\leq\; \sigma_\Pi \;\leq\; w_A\sigma_A + w_B\sigma_B$$

| Correlation | Portfolio variance | Shape | Diversification |
|---|---|---|---|
| $\rho = +1$ | $(w_A\sigma_A + w_B\sigma_B)^2$ | Straight line | None |
| $-1 < \rho < +1$ | Intermediate | Hyperbola | Partial |
| $\rho = -1$ | $(w_A\sigma_A - w_B\sigma_B)^2$ | V-shape | Maximum; zero risk possible |

## Example

Asset $A$: $\sigma_A = 20\%$. Asset $B$: $\sigma_B = 10\%$. Equal weights $w_A = w_B = 0.5$.

- **Upper bound** ($\rho = +1$): $\sigma_\Pi = 0.5(20) + 0.5(10) = 15\%$
- **Lower bound** ($\rho = -1$): $\sigma_\Pi = |0.5(20) - 0.5(10)| = 5\%$
- **Actual** ($\rho = 0.3$): $\sigma_\Pi \approx 11.2\%$ — well inside the bounds

## Remember

Diversification always reduces portfolio risk below the weighted average of individual risks — unless $\rho = 1$, where risks add exactly. At $\rho = -1$, perfect cancellation is possible and a zero-variance portfolio can be constructed. In practice, equity correlations are typically between 0 and 0.7, so diversification reduces but cannot eliminate risk. This is the mathematical proof of why holding many assets is always better than holding one — provided they are not perfectly correlated.
