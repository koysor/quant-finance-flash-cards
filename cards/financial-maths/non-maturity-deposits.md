# Non-Maturity Deposits

**Topic:** Financial Mathematics
**Tags:** NMD, deposits, behavioural modelling, IRRBB, core deposits, ALM
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Non-maturity deposits (NMDs)** are bank liabilities with no contractual maturity — current accounts, savings accounts, and instant-access deposits that customers can withdraw at any time. Despite the lack of a fixed term, empirical evidence shows that a large proportion of NMDs are "sticky": balances remain stable for years, acting as de facto long-term funding. Modelling the behavioural maturity of NMDs is the single biggest challenge in IRRBB measurement because it determines the effective duration of the bank's largest liability class.

## Key Formula

A common NMD behavioural model splits the balance into **core** (stable) and **non-core** (volatile) components:

$$B(t) = B_{\text{core}} \cdot e^{-\lambda_c t} + B_{\text{non-core}} \cdot e^{-\lambda_n t}$$

where $\lambda_c$ and $\lambda_n$ are decay rates for core and non-core balances ($\lambda_c \ll \lambda_n$).

The **behavioural duration** of the NMD portfolio:

$$D_{\text{NMD}} = \frac{B_{\text{core}}}{B_{\text{total}}} \times \frac{1}{\lambda_c} + \frac{B_{\text{non-core}}}{B_{\text{total}}} \times \frac{1}{\lambda_n}$$

Basel caps the average behavioural repricing maturity at **5 years** for the core component.

## Example

A bank has £12bn of savings deposits. Analysis shows:
- **Core (stable):** 70% = £8.4bn, with average life $1/\lambda_c = 4.0$ years
- **Non-core (volatile):** 30% = £3.6bn, with average life $1/\lambda_n = 0.5$ years

$$D_{\text{NMD}} = 0.70 \times 4.0 + 0.30 \times 0.5 = 2.80 + 0.15 = 2.95 \text{ years}$$

If the bank treated all NMDs as overnight (zero duration), the duration gap would be much larger. The behavioural model recognises that £8.4bn of "sticky" deposits effectively behave like 4-year term funding, substantially reducing the bank's measured IRRBB exposure.

## Remember

NMD modelling is arguably the most consequential assumption in the entire IRRBB framework — shifting the assumed behavioural maturity of deposits by one year can change the duration gap by over a year and EVE sensitivity by hundreds of millions. The 2023 collapse of Silicon Valley Bank illustrated the danger: SVB treated its deposits as stable long-term funding, but when depositors withdrew en masse, the bank faced a liquidity crisis and a crystallised EVE loss simultaneously. Basel's IRRBB standards impose a 5-year cap on core NMD repricing maturity to prevent overly optimistic assumptions. ALM teams calibrate NMD models from historical deposit flow data, segmented by product type, customer type, and rate sensitivity — but these models are inherently backward-looking, making them fragile in unprecedented rate environments.
