# Total Return Swap

**Topic:** Derivatives
**Tags:** total return swap, TRS, credit derivatives, synthetic exposure, leverage, funded vs unfunded
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A total return swap (TRS) exchanges the total return of a reference asset (coupons or dividends plus price change) for a floating payment (typically SOFR plus a spread); the total return receiver gains synthetic long exposure without owning the asset.

## Key Formula

At each reset date $t_i$:

$$\text{TRS payer pays: } \frac{S_{t_i} - S_{t_{i-1}}}{S_{t_{i-1}}} \cdot N + \text{income on }N$$

$$\text{TRS receiver pays: } (r_{\text{float}} + s) \cdot N \cdot \Delta t$$

Net P&L to receiver per period $= \text{total return on reference asset} - (\text{SOFR} + s)$.

If the reference asset falls in value, the TRS payer receives the deficit from the receiver.

## Example

Reference: \$100m equity portfolio. In Q1: portfolio rises 3% and pays 0.5% dividends — total return $= 3.5\%$. Receiver pays SOFR $5\% \times 0.25 = 1.25\%$ plus spread $0.5\% \times 0.25 = 0.125\%$. Net gain to receiver $= 3.5\% - 1.375\% = 2.125\%$ on \$100m $=$ \$2.125m.

## Remember

TRS allow investors to gain leveraged exposure to assets they cannot or do not want to hold on balance sheet. The Archegos Capital collapse (March 2021) illustrates the systemic risk: Archegos accumulated over \$50bn of synthetic equity exposure via TRS with multiple prime brokers — none of whom had visibility into the total position — causing \$10bn+ losses when the positions were forcibly unwound.
