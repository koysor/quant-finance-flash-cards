# Log Laws

**Topic:** Calculus
**Tags:** log laws, logarithm rules, algebra, log-returns, portfolio returns, simplification
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **log laws** (logarithm rules) are the algebraic identities that govern logarithms of products, quotients, and powers. They hold for any base $b > 0$, $b \neq 1$, and are valid for all $x, y > 0$.

## Key Formula

| Law | Formula | Name |
|---|---|---|
| Product | $\log_b(xy) = \log_b(x) + \log_b(y)$ | Log of a product |
| Quotient | $\log_b\!\left(\dfrac{x}{y}\right) = \log_b(x) - \log_b(y)$ | Log of a quotient |
| Power | $\log_b(x^n) = n\log_b(x)$ | Log of a power |
| Base swap | $\log_b(x) = \dfrac{\ln(x)}{\ln(b)}$ | Change of base |
| Identity | $\log_b(b) = 1$ | Log of the base |
| Zero | $\log_b(1) = 0$ | Log of one |
| Inverse | $b^{\log_b(x)} = x$ | Exponential undoes log |

## Example

Simplify the multi-period log-return of a portfolio. Gross returns over three months are $R_1 = 1.02$, $R_2 = 0.98$, $R_3 = 1.03$.

Total simple return: $R_1 \cdot R_2 \cdot R_3 - 1 = 1.02 \times 0.98 \times 1.03 - 1 \approx 2.97\%$

By the product law, the total log-return is simply:

$$\ln(R_1 R_2 R_3) = \ln R_1 + \ln R_2 + \ln R_3 \approx 0.0198 - 0.0202 + 0.0296 = 0.0292$$

The log laws convert the multiplicative compounding of gross returns into the addition of log-returns — no repeated multiplication needed.

**Log-moneyness** uses the quotient law:

$$\ln\!\left(\frac{S}{K}\right) = \ln S - \ln K$$

## Remember

The product and power laws are the two most important in quantitative finance. The **product law** explains why log-returns are additive: $\ln(S_T/S_0) = \ln(S_1/S_0) + \ln(S_2/S_1) + \cdots$. The **power law** explains why the volatility of log-returns scales with $\sqrt{T}$: $\ln(S_T/S_0) \sim \mathcal{N}(\mu T, \sigma^2 T)$, and by the power law $\sigma^2 T = (\sigma\sqrt{T})^2$. Every time a product of prices or returns is taken inside a logarithm, the product law turns it into a sum — the key step in deriving the Black-Scholes $d_1$ formula and log-return distributions.
