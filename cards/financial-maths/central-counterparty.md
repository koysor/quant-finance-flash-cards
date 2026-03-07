# Central Counterparty

**Topic:** Financial Mathematics
**Tags:** central counterparty, ccp, clearing, netting, systemic risk, margin
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A central counterparty (CCP) is a clearing house that interposes itself between the buyer and seller of a financial contract, becoming the buyer to every seller and the seller to every buyer. This process, called novation, replaces bilateral counterparty risk with a single, well-capitalised entity that guarantees performance on both sides.

## Key Formula

The **multilateral netting benefit** of a CCP reduces total exposure. For $n$ participants, each with bilateral exposures:

$$\text{Bilateral Exposure} = \sum_{i \neq j} \max(V_{ij}, 0)$$

$$\text{CCP Net Exposure} = \sum_{i} \max\left(\sum_{j} V_{ij}, \; 0\right)$$

The **netting efficiency**:

$$\text{Netting Ratio} = 1 - \frac{\text{CCP Net Exposure}}{\text{Bilateral Exposure}}$$

Typical netting ratios for interest rate derivatives exceed 90%, meaning the CCP reduces total exposure by over 90%.

## Example

Three banks have the following bilateral swap exposures (in £ millions):

| | Bank A owes | Bank B owes | Bank C owes |
|---|---|---|---|
| Bank A | — | 5 | 3 |
| Bank B | 8 | — | 2 |
| Bank C | 1 | 4 | — |

Bilateral gross exposure: $5 + 3 + 8 + 2 + 1 + 4 = £23\text{m}$

With CCP netting, each bank's net position:
- Bank A: $(8 + 1) - (5 + 3) = +£1\text{m}$ (net receiver)
- Bank B: $(5 + 4) - (8 + 2) = -£1\text{m}$ (net payer)
- Bank C: $(3 + 2) - (1 + 4) = £0$ (flat)

Total CCP exposure: $£1\text{m}$. Netting ratio: $1 - 1/23 = 96\%$.

## Remember

CCPs are the regulatory centrepiece of post-2008 derivatives reform. EMIR (Europe) and Dodd-Frank (US) mandate that standardised OTC derivatives are cleared through CCPs, concentrating counterparty risk in well-regulated institutions with tiered default waterfalls — initial margin, default fund contributions, and CCP equity. For quantitative analysts, central clearing changes the economics of derivatives: trades cleared through CCPs require initial margin (adding funding cost) but eliminate bilateral CVA charges. The trade-off between margin costs and CVA savings is a key input to optimal clearing decisions. However, CCPs themselves have become "too important to fail" — their potential failure is now considered the single largest systemic risk in financial markets.
