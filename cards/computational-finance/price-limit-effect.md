# Price Limit Effect (PLE)

**Topic:** Computational Finance
**Tags:** price limit effect, daily price limits, option pricing, regulatory bias, black-scholes
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **price limit effect (PLE)** measures the proportional change in an option's fair value caused by regulatory daily price limits, relative to the unconstrained Black-Scholes price. It quantifies the bias introduced when the underlying asset's price distribution is truncated or reflected at the corridor boundaries.

## Key Formula

$$\text{PLE}(t,S) = \frac{C_{\text{limit}}(t,S) - C_{\text{ref}}(t,S)}{C_{\text{ref}}(t,S)}$$

where $C_{\text{limit}}$ is the option price computed under price-limit constraints (via RL or Monte Carlo on constrained paths) and $C_{\text{ref}}$ is the Black-Scholes reference price. PLE is typically:
- **Negative** for call options under an absorbing upper boundary (upside is capped)
- **Positive** for put options near an absorbing lower boundary (downside protection enhanced)
- **Converges to zero** as the corridor width $\alpha, \beta \to \infty$

## Example

A one-month at-the-money call is priced at £3.20 by Black-Scholes ($\sigma = 25\%$). Under a ±5% daily limit with an absorbing upper boundary, an RL model prices it at £2.75. The PLE is $(2.75 - 3.20)/3.20 = -14\%$. Tightening to ±2% widens the PLE to $-28\%$, as more paths hit the boundary.

## Remember

The PLE is a regulatory "tax" on derivatives written on limit-constrained assets: sellers of calls systematically over-hedge and buyers systematically overpay when using Black-Scholes on limit-bound markets. Exchanges in China, South Korea, and Taiwan impose DPLs, so PLEs on equity options there can be economically significant — making RL-based pricing methods valuable for any options market maker operating on these exchanges.
