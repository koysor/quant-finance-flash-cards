# FRTB Overview

**Topic:** Banking Regulation
**Tags:** frtb, market risk, expected shortfall, internal models, p&l attribution
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Fundamental Review of the Trading Book (FRTB), finalised as part of Basel IV, is the comprehensive overhaul of bank market risk capital rules. It replaces VaR (99%, 10-day) with Expected Shortfall (97.5%, stressed) as the risk measure, moves capital calculation from business-line level to individual trading-desk level, introduces the P&L Attribution (PLA) test to validate internal models at desk level, and reforms the boundary between the banking book and trading book to prevent regulatory arbitrage.

## Key Formula

Under the **Internal Models Approach (IMA)**, desk-level capital is based on a stressed ES:

$$\text{IMA Capital} = \max\!\left(IMCC_{t-1},\; \rho \cdot \overline{IMCC}_{60}\right) + SES$$

where $IMCC$ (Internal Models Capital Charge) is a liquidity-horizon-adjusted ES using reduced factor sets, $\rho = 1.5$ is the multiplier, and $SES$ is the Stress Scenario add-on for non-modellable risk factors.

Under the **Standardised Approach (SA)**, capital is the sum of the Sensitivity-Based Method, Default Risk Charge, and Residual Risk Add-on:

$$\text{SA Capital} = SBM + DRC + RRAO$$

A desk must pass both the **Backtesting test** (≤ 12 exceptions at 99% over 250 days) and the **PLA test** (portfolio-level ES from the full model must align with the risk-theoretical P&L from the reduced model) to use IMA; failure forces the desk to SA.

## Example

A rates desk passes its P&L attribution test: the ratio of RTPL variance to HPL variance is between 0.8 and 1.2, and the Spearman correlation between the two is above 0.8. It is approved for IMA. A nearby credit desk fails the PLA test (RTPL/HPL variance ratio = 1.6), forcing it to the SA. The bank must report both desk capitals separately and sum them — it cannot offset IMA savings in rates against SA costs in credit.

## Remember

FRTB's shift from business-line to desk-level capital is the most operationally significant change: banks must now maintain fully documented, regulator-approved risk models at the individual desk level rather than at the aggregate level. This means that a trading desk cannot hide poor model performance in the averaging across a large business — every desk must independently justify its capital methodology. For quant developers, the PLA test creates a direct feedback loop between the front-office pricing model and the risk model: if they diverge materially in their P&L predictions, the desk loses IMA approval and faces higher SA capital.
