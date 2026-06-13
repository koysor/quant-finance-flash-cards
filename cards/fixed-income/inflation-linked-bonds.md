# Inflation-Linked Bonds

**Topic:** Fixed Income
**Tags:** TIPS, inflation-linked bonds, real yield, CPI, index ratio, principal adjustment, Fisher equation
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Inflation-linked bonds (US TIPS, UK index-linked gilts, French OATi) protect investors from inflation by adjusting their principal with a price index (CPI or RPI); coupon payments are calculated on the inflation-adjusted principal.

## Key Formula

**Index ratio and adjusted principal:**

$$N_t = N_0 \times \frac{\text{CPI}_t}{\text{CPI}_0}$$

**Real coupon payment:** $c \times N_t$ (paid on adjusted face value).

**Fisher equation:**

$$(1 + r_{\text{nominal}}) = (1 + r_{\text{real}})(1 + \pi^e) \;\implies\; r_{\text{nominal}} \approx r_{\text{real}} + \pi^e$$

**Breakeven inflation:** $\pi^e_{\text{BE}} = r_{\text{nominal}} - r_{\text{real}}$ (derived from TIPS vs nominal yield).

## Example

5yr TIPS, face \$1,000, real coupon $1\%$. After 1yr, CPI has risen $3\%$: $N_1 = \$1{,}030$. Coupon $= 1\% \times \$1{,}030 = \$10.30$. At maturity, investor receives $\max(N_0, N_T)$ — the floor protects against deflation over the bond's life.

## Remember

Real yields on TIPS represent the market's consensus estimate of the risk-free real interest rate. When the Fed raises nominal rates but TIPS real yields stay flat, the market is pricing in higher inflation expectations — a signal that the central bank may have lost credibility. Institutional investors use TIPS to hedge inflation sensitivity in liabilities (pension funds, insurance).
