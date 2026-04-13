# Wrong-Way Risk

**Topic:** Banking Regulation
**Tags:** wrong-way risk, counterparty risk, correlation, cva, exposure
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Wrong-Way Risk (WWR) arises when a bank's exposure to a counterparty is positively correlated with the counterparty's probability of default — so that exactly when the counterparty is most likely to default, the bank is owed the most money. This is the worst-case combination for counterparty credit risk and invalidates the standard CVA formula, which assumes exposure and default probability are independent.

## Key Formula

Under independence, CVA decomposes cleanly:

$$\text{CVA}_{\text{independent}} = (1-R)\sum_i EE(t_i) \cdot PD(t_i)$$

Under wrong-way risk, the exposure and default probability co-move, so the correct expression replaces $EE(t_i)$ with the conditional expected exposure given default:

$$\text{CVA}_{\text{WWR}} = (1-R)\sum_i \mathbb{E}[\max(V_{t_i}, 0) \mid \tau = t_i] \cdot PD(t_i)$$

where $\mathbb{E}[\max(V_{t_i}, 0) \mid \tau = t_i] \gg EE(t_i)$ when WWR is present — exposure is systematically above average precisely at the moment of default.

## Example

A bank sells credit protection (via a CDS) on Company X to Counterparty Y, and receives a premium. If Counterparty Y's own creditworthiness is correlated with Company X's credit quality — for example, both are banks in the same sector — then when Company X deteriorates, the CDS gains value to the bank (large positive exposure) while simultaneously Counterparty Y is more likely to default. This is Specific Wrong-Way Risk: the reference entity and the counterparty are directly linked.

## Remember

WWR was central to the AIG failure in 2008: AIG had sold massive amounts of credit protection on mortgage-backed securities to large banks, creating a situation where, as the housing market deteriorated, the value of protection purchased from AIG soared (large exposure) while simultaneously AIG's own solvency collapsed (large PD). The Basel CVA capital framework introduced a 1.4× scalar (the alpha multiplier in SA-CCR) partly to approximate WWR — but for concentrated specific wrong-way risk exposures, firms must model WWR explicitly by simulating correlated paths of exposure and credit quality.
