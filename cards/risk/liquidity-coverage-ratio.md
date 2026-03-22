# Liquidity Coverage Ratio

**Topic:** Risk
**Tags:** LCR, liquidity risk, Basel III, HQLA, stress testing, banking regulation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **Liquidity Coverage Ratio (LCR)** is a Basel III regulatory standard requiring banks to hold sufficient high-quality liquid assets (HQLA) to survive a 30-day stress scenario of net cash outflows. The ratio ensures that a bank can meet its short-term obligations — deposit withdrawals, maturing wholesale funding, margin calls — without relying on central bank lending or fire-selling illiquid assets.

## Key Formula

$$\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total net cash outflows over 30 days}} \times 100\% \geq 100\%$$

where:

$$\text{Net outflows} = \text{Total expected outflows} - \min(\text{Total expected inflows},\; 0.75 \times \text{Total expected outflows})$$

The inflow cap at 75% prevents banks from relying too heavily on expected inflows to meet the requirement.

## Example

A bank reports:
- HQLA: £45bn (government bonds, central bank reserves)
- Stressed outflows over 30 days: £52bn (retail deposit run-off £8bn, wholesale funding maturing £30bn, derivatives margin calls £14bn)
- Stressed inflows: £15bn (loan repayments, contractual receivables)

Net outflows = £52bn − min(£15bn, 0.75 × £52bn) = £52bn − £15bn = **£37bn**

$$\text{LCR} = \frac{£45\text{bn}}{£37\text{bn}} \times 100\% = 121.6\%$$

The bank exceeds the 100% minimum, meaning it holds a £8bn liquidity surplus above the regulatory floor.

## Remember

The LCR interacts directly with ALM because the composition of the HQLA buffer (mostly government bonds) adds duration to the asset side of the balance sheet, potentially increasing the EVE sensitivity to interest rate changes. A bank forced to hold £45bn of long-dated gilts for LCR compliance has simultaneously created a large interest rate position that the ALM desk must manage. The 2023 UK gilt crisis illustrated this tension: pension funds and banks holding large gilt portfolios for liquidity purposes faced mark-to-market losses when rates spiked, creating a feedback loop between liquidity regulation and interest rate risk. The LCR run-off rates for different deposit types also interact with NMD modelling — Basel assumes 5–10% run-off for stable retail deposits versus 25–40% for less stable deposits, establishing a regulatory floor for deposit stickiness assumptions.
