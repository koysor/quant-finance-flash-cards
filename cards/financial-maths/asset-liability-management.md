# Asset-Liability Management

**Topic:** Financial Mathematics
**Tags:** ALM, treasury, banking, IRRBB, liquidity, funding, hedging
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Asset-Liability Management (ALM)** is the practice of managing a bank's balance sheet to control mismatches between assets and liabilities in terms of interest rate sensitivity, maturity, currency, and liquidity. The ALM function — typically housed in the bank's treasury — monitors and hedges IRRBB, manages the liquidity buffer, sets internal funds transfer pricing, and ensures the bank can meet its obligations under both normal and stressed conditions.

## Key Formula

The **funds transfer pricing (FTP)** rate for an internal loan from treasury to a business unit:

$$\text{FTP rate} = r_{\text{matched-maturity}} + \text{liquidity premium} + \text{credit spread}$$

The **net interest margin (NIM)** managed by ALM:

$$\text{NIM} = \frac{\text{NII}}{\text{Average earning assets}} \times 100\%$$

ALM targets a NIM range while keeping IRRBB metrics within limits:

$$|\Delta\text{EVE}| \le \text{EVE limit} \quad \text{and} \quad |\Delta\text{NII}| \le \text{NII limit}$$

## Example

A bank's ALM committee reviews the following position:
- Duration gap: 3.8 years (assets longer than liabilities)
- EVE sensitivity to +200 bps: $-$£650m (13% of Tier 1 capital)
- NII sensitivity to +200 bps: +£40m (NII rises because more assets reprice)

The EVE limit is 15% of Tier 1, so the current position is within tolerance. However, the ALM team decides to reduce the gap from 3.8 to 2.5 years by entering £4bn of receive-fixed 5-year interest rate swaps. This increases liability duration, narrows the gap, and reduces the EVE sensitivity to $-$£430m.

## Remember

ALM is where all IRRBB concepts come together operationally. The ALM desk does not aim to eliminate all risk — some duration mismatch is a deliberate source of profit (the term premium) — but rather to keep the risk within board-approved limits while optimising NII. The key trade-off is between EVE stability (long-run solvency) and NII maximisation (short-run earnings), which often pull in opposite directions. Modern ALM uses scenario analysis, behavioural modelling of deposits and prepayments, and interest rate derivatives (swaps, swaptions, caps) to shape the risk profile. Funds transfer pricing ensures that each business unit is charged for the rate and liquidity risk it creates, aligning incentives across the bank.
