# Alpha and Beta

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** alpha, beta, systematic risk, excess return, capm, performance attribution
**Author:** Claude Opus 4.6

---

## Definition

In finance, **beta** ($\beta$) measures the sensitivity of an asset's return to the overall market return — it captures systematic risk that cannot be diversified away. **Alpha** ($\alpha$) is the excess return above what the asset's beta exposure would predict, representing the value added (or destroyed) by active management.

## Key Formula

From the Capital Asset Pricing Model, the expected return of an asset is:

$$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$

Alpha is the difference between the actual return and the CAPM-predicted return:

$$\alpha_i = R_i - \left[ R_f + \beta_i (R_m - R_f) \right]$$

Beta is estimated by regression:

$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

## Example

A fund has $\beta = 1.2$. The risk-free rate is 3% and the market returned 10%. The CAPM-predicted return is:

$$E[R] = 0.03 + 1.2 \times (0.10 - 0.03) = 0.03 + 0.084 = 0.114$$

If the fund actually returned 14%:

$$\alpha = 0.14 - 0.114 = 0.026$$

The fund generated 2.6% alpha — return above and beyond what its market exposure alone would explain.

## Remember

Alpha and beta are the fundamental decomposition of investment returns. Passive index funds deliver pure beta at low cost; hedge funds charge premium fees (typically "2 and 20") on the promise of generating positive alpha. In quantitative finance, every performance attribution, factor model, and risk budget starts by separating the return you could have earned passively (beta) from the return earned through skill or strategy (alpha).
