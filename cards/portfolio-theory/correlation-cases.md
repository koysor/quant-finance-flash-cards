# Correlation Cases

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** correlation, diversification, opportunity set, portfolio risk, special cases
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The correlation $\rho_{AB}$ between two assets determines the shape of the opportunity set. Three special values — $+1$, $-1$, and $0$ — illustrate the full range of diversification possibilities and set the geometric intuition for portfolio theory.

## Key Formula

The three cases derive from $\sigma_\Pi^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2\rho_{AB}w_Aw_B\sigma_A\sigma_B$:

| Correlation | Formula for $\sigma_\Pi$ | Shape | Zero-variance possible? |
|---|---|---|---|
| $\rho = +1$ | $w_A\sigma_A + w_B\sigma_B$ | Straight line | No |
| $\rho = 0$ | $\sqrt{w_A^2\sigma_A^2 + w_B^2\sigma_B^2}$ | Hyperbola (moderate bow) | No |
| $\rho = -1$ | $\lvert w_A\sigma_A - w_B\sigma_B \rvert$ | V-shape (two straight lines) | **Yes** |

## Example

Assets with $\sigma_A = 20\%$, $\sigma_B = 10\%$, equal weights:

- $\rho = +1$: $\sigma_\Pi = 15\%$ (no benefit)
- $\rho = 0$: $\sigma_\Pi = \sqrt{0.25(0.04) + 0.25(0.01)} = \sqrt{0.0125} \approx 11.2\%$
- $\rho = -1$: $\sigma_\Pi = |10\% - 5\%| = 5\%$ (or zero at $w_A = 1/3$)

## Remember

The shape of the opportunity set tells you how much diversification the two assets offer. A straight line ($\rho = 1$) means none; a hyperbola means partial benefit; a V-shape ($\rho = -1$) means perfect hedging is possible. Real equity pairs typically have $\rho$ between 0.3 and 0.7, producing a moderately bowed hyperbola — significant but not complete diversification. Understanding these three cases builds the geometric intuition underlying the entire efficient frontier framework.
