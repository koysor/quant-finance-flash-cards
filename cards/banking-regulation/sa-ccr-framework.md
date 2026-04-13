# SA-CCR Framework

**Topic:** Banking Regulation
**Tags:** sa-ccr, exposure at default, counterparty risk, replacement cost, add-on
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Standardised Approach for Counterparty Credit Risk (SA-CCR) is the Basel III/IV methodology for computing Exposure at Default (EAD) for OTC derivatives and securities financing transactions. It replaced the crude Current Exposure Method (CEM) by separately modelling current exposure (replacement cost) and potential future exposure (add-on), while recognising the risk-reducing effect of netting and collateral more accurately.

## Key Formula

$$EAD = \alpha \times (RC + \text{PFE}_{\text{add-on}})$$

where $\alpha = 1.4$ is a regulatory scalar, and:

**Replacement Cost (RC):** For a margined netting set:

$$RC = \max(V - C,\; 0)$$

where $V$ is the net mark-to-market and $C$ is the net collateral held (excluding IM).

**PFE Add-on:** Aggregated across five asset classes (IR, FX, Credit, Equity, Commodity):

$$\text{PFE}_{\text{add-on}} = \text{multiplier} \times \text{Aggregate Add-on}$$

$$\text{multiplier} = \min\!\left(1,\; 0.05 + 0.95\exp\!\left(\frac{V - C}{2 \times \text{Aggregate Add-on}}\right)\right)$$

## Example

A netting set has $V = £5\text{m}$, collateral $C = £3\text{m}$, and aggregate add-on = £20 m.

$$RC = \max(5 - 3, 0) = £2\text{m}$$

The multiplier (since $V > C$, i.e., portfolio is in-the-money) is capped at 1.0. $\text{PFE}_{\text{add-on}} = 1.0 \times £20\text{m} = £20\text{m}$. Thus:

$$EAD = 1.4 \times (£2\text{m} + £20\text{m}) = £30.8\text{m}$$

## Remember

The multiplier in SA-CCR is a key innovation: when a netting set is deeply out-of-the-money (negative $V$), the multiplier falls below 1, reducing EAD to reflect the lower credit risk — a counterparty default is less damaging when the bank would owe them money. SA-CCR also feeds directly into the leverage ratio's total exposure measure for derivatives, making EAD methodology critical not just for credit risk capital but for any bank constrained by its leverage ratio.
