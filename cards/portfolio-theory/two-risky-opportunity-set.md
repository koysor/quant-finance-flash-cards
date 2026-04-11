# Two Risky Assets — Opportunity Set

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** opportunity set, two assets, portfolio risk, hyperbola, diversification
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **opportunity set** is the set of all achievable $(\sigma_\Pi, \mu_\Pi)$ combinations when mixing two risky assets $A$ and $B$ across all possible weights. Its shape — a hyperbola — reveals the diversification benefit.

## Key Formula

With weight $w_A$ in asset $A$ and $w_B = 1 - w_A$ in asset $B$:

$$\mu_\Pi = \mu_B + w_A(\mu_A - \mu_B)$$

$$\sigma_\Pi = \sqrt{w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2\rho_{AB}\,w_A w_B\,\sigma_A\sigma_B}$$

Expected return is **linear** in $w_A$; standard deviation is **nonlinear** — it traces a hyperbola in $(\sigma, \mu)$ space.

## Example

Asset $A$: $\mu_A = 12\%$, $\sigma_A = 25\%$. Asset $B$: $\mu_B = 7\%$, $\sigma_B = 15\%$. Correlation $\rho = 0.3$.

At equal weights ($w_A = 0.5$):

$$\mu_\Pi = 9.5\%$$

$$\sigma_\Pi = \sqrt{0.25(0.0625) + 0.25(0.0225) + 2(0.3)(0.5)(0.5)(0.25)(0.15)} = \sqrt{0.027625} \approx 16.6\%$$

A naive 50/50 blend of the volatilities would give $0.5(25) + 0.5(15) = 20\%$ — the actual risk of 16.6% is lower because $\rho < 1$.

## Remember

Return mixes linearly; risk mixes nonlinearly — the result is a hyperbola. The leftward bow of the curve compared to a straight line between the two assets **is** diversification: you obtain risk levels that no weighted average of individual risks could achieve. The more negative the correlation, the greater the bow, and the more risk can be eliminated by mixing the two assets.
