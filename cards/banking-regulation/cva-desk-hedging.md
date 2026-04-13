# CVA Desk and CVA Hedging

**Topic:** Banking Regulation
**Tags:** cva, hedging, cds, xva desk, counterparty risk
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

A CVA desk is the bank function responsible for centrally managing the counterparty credit risk embedded in the derivatives book. Rather than leaving each trading desk to bear its own CVA P&L, the CVA desk buys the CVA charge from each desk at inception and hedges the resulting aggregate CVA exposure using credit default swaps (CDS), index products, and cross-gamma hedges. This centralisation allows netting of CVA across counterparties and enables efficient hedging.

## Key Formula

The CVA desk hedges two primary sensitivities:

**CS01 (Credit Spread 01):** Sensitivity of CVA to a 1 bp parallel shift in the counterparty's CDS spread:

$$\text{CS01} = \frac{\partial \text{CVA}}{\partial s} \approx (1-R) \cdot \text{EPE} \cdot \frac{\partial PD}{\partial s} \cdot \Delta t$$

**CVA Delta:** Sensitivity to the underlying market risk factors (interest rates, FX) that drive the Exposure Profile:

$$\text{CVA Delta} = \frac{\partial \text{CVA}}{\partial r_k} = (1-R)\sum_i \frac{\partial EE(t_i)}{\partial r_k} \cdot PD(t_i)$$

The desk hedges CS01 by buying single-name CDS on each counterparty and CVA Delta by trading the underlying market risk (e.g., interest rate swaps to hedge the IR component of exposure).

## Example

The CVA desk has £200k of CS01 exposure on a bank counterparty. It buys CDS protection on that counterparty with notional sized to offset: if the CDS spread widens by 1 bp, the CDS position gains approximately £200k in value, offsetting the CVA loss. The desk also has IR delta from the exposure profile: if rates rise, the swap MtM falls, reducing exposure. The desk hedges this delta by trading receiver swaps to create an offsetting P&L.

## Remember

The 2012 JP Morgan "London Whale" incident was a CVA hedging programme that became a directional credit bet. JP Morgan's CIO (Chief Investment Office) was running large credit index positions ostensibly as a CVA hedge, but the positions grew so large (notional in the hundreds of billions) that they moved the market — and when they were unwound, JP Morgan lost approximately $6 bn. The key lesson for quants is that CVA hedges are imperfect: single-name CDS liquidity is poor for most counterparties, index hedges introduce basis risk, and the cross-gamma between credit spreads and market risk factors creates P&L that is difficult to hedge cleanly. Under FRTB, the CVA desk must also satisfy the IMA PLA test at desk level, creating a direct feedback loop between the CVA pricing model and the hedging model.

