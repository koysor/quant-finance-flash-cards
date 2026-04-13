# ISDA SIMM

**Topic:** Banking Regulation
**Tags:** simm, initial margin, sensitivity, bilateral, uncleared derivatives
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

ISDA SIMM (Standard Initial Margin Model) is the industry-standard sensitivity-based model for calculating Initial Margin on non-centrally cleared (bilateral) OTC derivatives. It was developed by ISDA following the 2016 UMR (Uncleared Margin Rules) that mandated IM exchange between large dealers, providing a common methodology so that two counterparties can independently compute and agree on the same IM amount.

## Key Formula

For each risk class $r$ (Interest Rate, FX, Credit, Equity, Commodity), sensitivities $s_{ik}$ (Delta, Vega, or Curvature) are multiplied by supervisory risk weights $RW_k$ to produce weighted sensitivities $WS_{ik}$. Within each bucket $b$ these are aggregated using a correlation matrix $\rho$:

$$K_b = \sqrt{\sum_i WS_{ib}^2 + \sum_{i \neq j} \rho_{ij} WS_{ib} WS_{jb}}$$

Across buckets the margin for risk class $r$ is:

$$IM_r = \sqrt{\sum_b K_b^2 + \sum_{b \neq c} \gamma_{bc} K_b K_c}$$

Total IM is the sum across risk classes: $IM = \sum_r IM_r$.

## Example

A EUR interest rate swap has a DV01 (delta sensitivity) of £50,000 per bp. SIMM's supervisory risk weight for 5-year EUR rates is approximately 46 bps. Weighted sensitivity $WS = £50{,}000 \times 46 = £2.3\text{m}$. With no offsets from other instruments, $IM_{\text{IR}} = £2.3\text{m}$ — the IM required just for this one delta.

## Remember

SIMM replaced the older "schedule" approach (a flat percentage of notional) with a Greeks-based calculation that recognises hedging and diversification — a well-hedged book pays far less IM than a directional one. For dealers, SIMM created an incentive to share accurate sensitivity data with counterparties; for risk managers, it means IM is now directly tied to the Greeks reported by the front-office system, so any discrepancy in sensitivity calculations translates immediately into IM disputes.
