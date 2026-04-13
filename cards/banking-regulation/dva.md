# Debit Valuation Adjustment (DVA)

**Topic:** Banking Regulation
**Tags:** dva, xva, counterparty risk, own credit, bilateral cva
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Debit Valuation Adjustment (DVA) is the valuation adjustment a bank makes to reflect the benefit it receives from the possibility of its own default. It is the mirror of CVA: just as CVA represents the cost of the counterparty potentially defaulting, DVA represents the value to the bank of potentially defaulting on its obligations — because the counterparty bears that risk. In a symmetric bilateral framework, the fair value of a derivative includes both adjustments.

## Key Formula

In a bilateral CVA framework, the total adjustment is:

$$\text{Bilateral CVA} = \text{CVA} - \text{DVA}$$

where CVA is the bank's loss from counterparty default and DVA is the gain from the bank's own default:

$$\text{DVA} = (1-R_B)\sum_i \mathbb{E}[\max(-V_{t_i},0)] \cdot PD_B(t_i)$$

Here $R_B$ is the bank's own recovery rate, $\max(-V_{t_i},0)$ is the bank's negative exposure (the counterparty is owed money), and $PD_B(t_i)$ is the bank's own probability of default at time $t_i$.

## Example

A bank has a bilateral OTC swap where the current MtM is −£10 m (the bank owes the counterparty). If the bank's own 1-year CDS spread implies a 2% default probability and recovery is 40%, the DVA contribution is approximately $0.02 \times (1-0.4) \times £10\text{m} = £120{,}000$. This £120k is a gain on the P&L — the bank records a profit because its own creditworthiness deteriorated.

## Remember

DVA is deeply controversial because it creates a perverse accounting incentive: when a bank's own credit spreads widen (i.e., the market believes it is more likely to default), its DVA gains increase, producing a P&L profit. During the 2011 European sovereign crisis, several major banks reported large DVA gains as their own credit deteriorated — reporting profits at exactly the moment their solvency was in question. IFRS 13 requires DVA to be included in fair value, but the Basel capital framework largely excludes DVA gains from regulatory capital, recognising that a bank cannot monetise its own default. For quant developers, DVA requires the same simulation infrastructure as CVA but applied to the bank's own credit curve, creating a feedback loop that can be numerically unstable.

