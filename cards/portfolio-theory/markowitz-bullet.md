# Markowitz Bullet

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** portfolio theory, efficient frontier, mean-variance, opportunity set, diversification
**Created:** 2026-04-20
**Author:** Claude Sonnet 4.6

---

## Definition

The Markowitz Bullet is the full set of achievable risk-return combinations when combining $n$ risky assets, plotted in standard-deviation/expected-return space. It forms a parabolic ("bullet") shape: the upper boundary is the efficient frontier (optimal portfolios), while the lower half contains dominated portfolios that offer the same risk for less return.

## Key Formula

For a two-asset portfolio with weights $w$ and $1-w$, correlation $\rho$, the opportunity set traces a curve parametrised by $w \in [0, 1]$:

$$\mu_p(w) = w\mu_1 + (1-w)\mu_2$$

$$\sigma_p(w) = \sqrt{w^2\sigma_1^2 + (1-w)^2\sigma_2^2 + 2w(1-w)\rho\sigma_1\sigma_2}$$

As $\rho$ decreases from $+1$ to $-1$, the bullet bows further left — maximum diversification benefit occurs at $\rho = -1$, where the bullet touches the vertical axis (zero variance is achievable).

## Example

Asset 1: $\mu_1 = 12\%$, $\sigma_1 = 20\%$. Asset 2: $\mu_2 = 6\%$, $\sigma_2 = 10\%$, $\rho = 0$.

At $w = 0.25$: $\mu_p = 7.5\%$, $\sigma_p = \sqrt{0.0625 \times 0.04 + 0.5625 \times 0.01} = \sqrt{0.008125} \approx 9.0\%$.

At $w = 0.75$: $\mu_p = 10.5\%$, $\sigma_p = \sqrt{0.5625 \times 0.04 + 0.0625 \times 0.01} = \sqrt{0.023125} \approx 15.2\%$.

The minimum-variance point lies between these, at approximately $w \approx 0.2$ ($\sigma_p \approx 8.9\%$). Below this point on the bullet, a higher-return portfolio exists at the same risk — making those portfolios inefficient.

## Remember

The bullet's leftward bow is what makes diversification quantitatively valuable: for any given return target, a mixed portfolio achieves it at lower volatility than holding either asset alone. In practice, portfolio managers use the shape of the bullet to justify combining asset classes (equities, bonds, alternatives) — the flatter and wider the bullet, the more diversification is adding value. When $\rho = +1$ the bullet collapses to a straight line and diversification provides no variance reduction at all.
