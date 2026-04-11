# Two-Asset Global Minimum Variance Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** global minimum variance, GMV, portfolio optimisation, efficient frontier, two assets
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **global minimum variance (GMV) portfolio** is the portfolio with the lowest achievable variance across all weight combinations of two risky assets. It is the leftmost point on the opportunity set hyperbola — the starting point of the efficient frontier.

## Key Formula

Minimise $\sigma_\Pi^2$ with respect to $w_A$ subject to $w_A + w_B = 1$:

$$w_A^G = \frac{\sigma_B^2 - \rho_{AB}\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho_{AB}\sigma_A\sigma_B}, \qquad w_B^G = 1 - w_A^G$$

**Special case** ($\rho_{AB} = 0$, uncorrelated assets):

$$w_A^G = \frac{\sigma_B^2}{\sigma_A^2 + \sigma_B^2}$$

The higher weight goes to the **lower-volatility** asset.

## Example

$\sigma_A = 20\%$, $\sigma_B = 12\%$, $\rho_{AB} = 0.2$.

$$w_A^G = \frac{0.0144 - 0.2(0.20)(0.12)}{0.0400 + 0.0144 - 2(0.2)(0.20)(0.12)} = \frac{0.0144 - 0.0048}{0.0544 - 0.0096} = \frac{0.0096}{0.0448} \approx 21.4\%$$

$$w_B^G = 78.6\%$$

$$\sigma_\Pi^G = \sqrt{(0.214)^2(0.04) + (0.786)^2(0.0144) + 2(0.2)(0.214)(0.786)(0.024)} \approx 11.1\%$$

Portfolio risk is below either individual asset's volatility.

## Remember

The GMV portfolio is the anchor of the efficient frontier. Any rational investor who cares only about minimising risk will hold it; anyone seeking both low risk and higher return will hold a portfolio on the efficient frontier above it. Notice that the GMV weight formula places the higher weight in the **lower-volatility asset** — the formula mathematically formalises the intuition that to minimise risk you should tilt towards the steadier asset.
