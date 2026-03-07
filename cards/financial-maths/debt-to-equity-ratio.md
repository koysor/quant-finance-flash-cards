# Debt-to-Equity Ratio

**Topic:** Financial Mathematics
**Tags:** leverage, debt, equity, capital structure, corporate finance
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The debt-to-equity ratio (D/E) measures a company's financial leverage by comparing its total debt to shareholders' equity. It indicates how much of the firm's capital structure is financed by creditors versus owners.

## Key Formula

$$\text{D/E} = \frac{\text{Total Debt}}{\text{Shareholders' Equity}}$$

The relationship between levered and unlevered beta (the **Hamada equation**) uses D/E directly:

$$\beta_L = \beta_U \left(1 + (1 - t) \frac{D}{E}\right)$$

where $t$ is the corporate tax rate, $\beta_L$ is the levered beta, and $\beta_U$ is the unlevered (asset) beta.

## Example

A firm has total debt of £40 million and shareholders' equity of £60 million.

$$\text{D/E} = \frac{40}{60} = 0.667$$

If the firm's unlevered beta is 0.8 and the tax rate is 25%:

$$\beta_L = 0.8 \times \left(1 + (1 - 0.25) \times 0.667\right) = 0.8 \times 1.5 = 1.2$$

The debt amplifies the equity beta from 0.8 to 1.2 — shareholders bear more systematic risk because debt holders have a prior claim on cash flows.

## Remember

The D/E ratio is the corporate finance analogue of the leverage ratio used in portfolio management. In quantitative finance, it matters because higher D/E increases equity beta (via the Hamada equation), raises the cost of equity in the CAPM, and signals higher default probability in credit models. Analysts compare D/E across firms within the same sector — a bank at 10:1 is normal, but a technology firm at 10:1 would signal severe distress.
