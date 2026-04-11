# Systematic vs Idiosyncratic Risk

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** systematic risk, idiosyncratic risk, beta, diversification, CAPM
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

Every asset's total risk decomposes into two components: **systematic risk** (driven by economy-wide factors, cannot be diversified away) and **idiosyncratic risk** (firm-specific, eliminated by diversification). Only systematic risk is priced by the market.

## Key Formula

$$\sigma_I^2 = \underbrace{\beta_I^2\sigma_M^2}_{\text{systematic}} + \underbrace{e_I^2}_{\text{idiosyncratic}}$$

| Risk type | Also called | Source | Diversifiable? | Priced? |
|---|---|---|---|---|
| Systematic | Market risk, beta risk | Economy-wide shocks | No | Yes |
| Idiosyncratic | Specific risk, residual | Firm-specific events | Yes | No |

In a well-diversified $N$-asset portfolio, idiosyncratic terms average out:

$$\sigma_\Pi \;\approx\; \beta_\Pi \sigma_M \quad \text{as } N \to \infty$$

## Example

An asset with $\beta = 1.5$, $\sigma_M = 15\%$, $e = 10\%$:

$$\sigma_I = \sqrt{(1.5)^2(0.15)^2 + (0.10)^2} = \sqrt{0.0506 + 0.01} = \sqrt{0.0606} \approx 24.6\%$$

Systematic: $1.5 \times 15\% = 22.5\%$ of total risk; idiosyncratic: $10\%$.

An investor holding this asset in a diversified portfolio only "uses up" 22.5% of total risk in terms of portfolio contribution — the 10% idiosyncratic is irrelevant.

## Remember

The decomposition $\sigma^2 = \beta^2\sigma_M^2 + e^2$ is why CAPM says expected return depends only on $\beta$, not on total volatility. An investor who diversifies pays nothing to eliminate idiosyncratic risk, so the market will not compensate for it. This is why two stocks with the same total volatility can have very different expected returns if their betas differ — only the systematic component earns a risk premium.
