# Security Market Line

**Topic:** Financial Mathematics
**Tags:** security market line, CAPM, beta, expected return, alpha, equilibrium pricing
**Created:** 2026-03-01
**Author:** Claude Opus 4.6

---

## Definition

The **Security Market Line (SML)** is the graphical representation of the Capital Asset Pricing Model, plotting expected return on the vertical axis against beta on the horizontal axis. In equilibrium, all correctly priced assets lie on the SML. Assets plotting above the line have positive **alpha** (underpriced), while those below have negative alpha (overpriced).

## Key Formula

The SML is the CAPM equation interpreted as a line in $(\beta, E(R))$ space:

$$E(R_i) = R_f + \beta_i \bigl(E(R_m) - R_f\bigr)$$

The **alpha** of an asset is the vertical distance from the SML:

$$\alpha_i = R_i - \bigl[R_f + \beta_i (R_m - R_f)\bigr]$$

A positive $\alpha_i$ means the asset earned more than its beta-implied return.

## Example

Suppose $R_f = 3\%$, $E(R_m) = 10\%$, and a stock has $\beta = 0.8$. The SML predicts:

$$E(R) = 3\% + 0.8 \times (10\% - 3\%) = 3\% + 5.6\% = 8.6\%$$

If the stock actually returned 11%, its alpha is:

$$\alpha = 11\% - 8.6\% = 2.4\%$$

The stock plots above the SML — it delivered 2.4% more than its systematic risk warranted, suggesting it was underpriced at the start of the period.

## Remember

The SML is the tool practitioners use to identify mispriced securities and evaluate fund manager skill. A consistently positive alpha suggests genuine stock-picking ability rather than simply taking on more market risk. Unlike the Capital Market Line (which plots against total risk $\sigma$), the SML uses only systematic risk ($\beta$), reflecting the CAPM principle that only non-diversifiable risk is compensated in equilibrium.
