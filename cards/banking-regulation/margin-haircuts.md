# Regulatory Margin Haircuts

**Topic:** Banking Regulation
**Tags:** haircuts, collateral, initial margin, regulatory capital, umr
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

A regulatory margin haircut is the percentage reduction applied to the market value of non-cash collateral when calculating its credit-equivalent value for margin purposes. Haircuts reflect the risk that the collateral's value falls between the last margin call and the time it can be liquidated — they protect the receiving party against residual exposure after a counterparty default. Regulators prescribe standard haircut schedules for collateral used in bilateral derivatives, repo, and securities financing transactions.

## Key Formula

The collateral-adjusted exposure after haircuts is:

$$E^* = \max\!\left(0,\; E - C \cdot (1 - H_C) + C \cdot H_{FX}\right)$$

where $E$ is the gross exposure, $C$ is the collateral market value, $H_C$ is the asset haircut (credit and duration risk), and $H_{FX}$ is the foreign-exchange haircut (if collateral currency ≠ exposure currency). Under Basel supervisory haircuts:

| Collateral type | Residual maturity | Haircut |
|---|---|---|
| Sovereign (AAA–AA) | 0–1 yr | 0.5% |
| Sovereign (AAA–AA) | 1–5 yr | 2% |
| Sovereign (AAA–AA) | >5 yr | 4% |
| IG corporate bonds | 1–5 yr | 6% |
| Equities (main index) | — | 15% |
| Non-main index equities | — | 25% |
| FX mismatch | — | 8% |

## Example

A bank receives £10 m of 10-year AAA sovereign bonds as initial margin for a bilateral derivative, but the exposure currency is USD while collateral is in GBP. Haircut for >5 yr AAA sovereign = 4%; FX haircut = 8%. Effective collateral value = £10 m × (1 − 4%) − £10 m × 8% = £9.6 m − £0.8 m = £8.8 m. If the gross exposure is £9 m, the collateral-adjusted net exposure = £9 m − £8.8 m = £200k, which still requires additional capital or cash collateral.

## Remember

Regulatory haircuts create a direct link between collateral quality and funding cost: a firm posting high-haircut collateral (e.g. equities at 15% or non-investment-grade bonds at 25%) must post significantly more nominal value than a firm posting cash or short-dated government bonds. This drives collateral optimisation — the treasury practice of choosing which eligible assets to pledge to minimise the total funding cost across a portfolio of margin agreements. Under UMR, the ISDA SIMM IM calculation is independent of collateral quality, but the haircut then determines how much of that IM is actually satisfied by a given asset — making collateral selection a material cost driver for Phase 5 and 6 firms.

