# Interest Rate Risk in the Banking Book

**Topic:** Banking Regulation
**Tags:** IRRBB, banking book, interest rate risk, Basel, ALM, regulation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Interest Rate Risk in the Banking Book (IRRBB)** is the risk that changes in interest rates adversely affect a bank's earnings or the economic value of its banking book — the portfolio of assets and liabilities held to maturity (loans, deposits, bonds) rather than for trading. Unlike market risk in the trading book, IRRBB arises from maturity and repricing mismatches between a bank's assets and liabilities and is governed by the Basel Committee's Pillar 2 framework.

## Key Formula

IRRBB is measured through two complementary lenses:

**Economic Value of Equity (EVE):**

$$\Delta \text{EVE} = \sum_{t} \Delta r(t) \cdot PV01(t)$$

where $PV01(t)$ is the present-value sensitivity to a 1 bp rate move at tenor $t$.

**Net Interest Income (NII):**

$$\Delta \text{NII} = \sum_{i} \text{Gap}_i \times \Delta r_i$$

where $\text{Gap}_i$ is the repricing gap (rate-sensitive assets minus rate-sensitive liabilities) in time bucket $i$.

Basel prescribes **six interest rate shock scenarios** (parallel up/down, steepener, flattener, short-rate up/down) and an **outlier test**: if the worst-case $\Delta\text{EVE}$ exceeds 15% of Tier 1 capital, the supervisor may require additional capital.

## Example

A bank has £10bn of 5-year fixed-rate mortgages funded by £10bn of overnight deposits. Rates rise by 200 bps uniformly.

- **EVE impact:** The mortgages' present value falls by roughly $10\text{bn} \times 4.2 \times 0.02 = £840\text{m}$ (duration $\approx 4.2$). The deposits, being overnight, barely change. EVE drops by ~£840m.
- **NII impact (year 1):** Deposit funding costs rise immediately by $10\text{bn} \times 0.02 = £200\text{m}$, but mortgage income is locked at the old rate. NII falls by £200m in the first year.

## Remember

IRRBB is the dominant risk for most commercial banks — far larger than their trading book exposure. The dual-lens approach (EVE for solvency, NII for earnings) is essential because they can give opposite signals: a bank with long-duration assets and short-duration liabilities loses EVE when rates rise but may eventually earn more NII as assets reprice higher. Regulators require banks to manage both perspectives simultaneously, which is why asset-liability management (ALM) desks sit at the heart of every bank's treasury function.
