# Asset-Backed Securities (ABS)

**Topic:** Fixed Income
**Tags:** ABS, asset-backed securities, securitisation, auto loans, credit cards, student loans, waterfall
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Asset-backed securities (ABS) are bonds whose cash flows are derived from a pool of financial assets — typically auto loans, credit card receivables, student loans, or equipment leases — structured into tranches via a special purpose vehicle (SPV).

## Key Formula

**SPV waterfall:** interest and principal flow sequentially: senior $\to$ mezzanine $\to$ equity (first loss).

**Credit enhancement:** excess spread absorbs first losses before tranche principal is impaired:

$$\text{Excess spread} = \text{Asset yield} - \text{Cost of liabilities} - \text{Servicing fee}$$

**ABS yield:** $y_{\text{ABS}} = r_f + \text{credit spread} + \text{liquidity spread} + \text{prepayment/extension risk premium}$

Unlike MBS, ABS collateral often has shorter maturities (2–5yr auto loans, revolving credit cards), reducing duration and prepayment sensitivity.

## Example

\$500m auto-loan ABS: pool of 5yr car loans at $7\%$ average yield. Senior class A (AAA, \$425m): pays SOFR+80bps. Mezzanine B (BBB, \$50m): SOFR+200bps. Equity (\$25m): residual cash flows after all fees. Excess spread $= 7\% - 4\% - 0.5\% = 2.5\%$, acting as first-loss buffer.

## Remember

ABS broadened securitisation beyond mortgages to almost any asset with predictable cash flows. The excess spread mechanism is a key protection: routine monthly losses are absorbed before any tranche takes a hit. In a stress scenario (recession → elevated auto defaults), excess spread is eroded first, then the equity tranche, allowing senior investors to be protected in most economic conditions — but not during a sharp, correlated credit deterioration.
