# Accrued Interest

**Topic:** Fixed Income
**Tags:** accrued interest, clean price, dirty price, settlement, day count
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

**Accrued interest** is the coupon income that has accumulated on a bond since the last coupon payment date but has not yet been paid to the holder. When a bond changes hands between coupon dates, the buyer compensates the seller for this accrued income. The **dirty price** (full price) is what the buyer actually pays; the **clean price** (flat price) is the quoted market price, which excludes accrued interest and remains smooth between coupons.

## Key Formula

$$\text{Dirty Price} = \text{Clean Price} + \text{Accrued Interest}$$

$$\text{Accrued Interest} = C \times \frac{t}{T}$$

where $C$ is the full coupon payment, $t$ is the number of days since the last coupon, and $T$ is the total number of days in the coupon period. The exact day count depends on the convention:

| Convention | Used for |
|-----------|---------|
| Actual/Actual (ICMA) | Government bonds (gilts, Treasuries) |
| Actual/360 | Money market, most USD swaps |
| 30/360 | Corporate bonds (USD) |

## Example

A UK gilt pays a 4% semi-annual coupon on a face value of £1,000, so each coupon is £20. Settlement is 45 days into a 184-day coupon period. Day count: Actual/Actual.

$$\text{Accrued Interest} = £20 \times \frac{45}{184} \approx £4.89$$

If the clean price is quoted at 98.50 (i.e. £985.00 per £1,000 face), the buyer pays:

$$\text{Dirty Price} = £985.00 + £4.89 = £989.89$$

The seller receives the £4.89 they earned while holding the bond, even though the coupon is not due yet.

## Remember

Clean prices are quoted in bond markets precisely because they change smoothly with yield — the sawtooth pattern of accrued interest building up and then resetting to zero on each coupon date would make it hard to observe genuine yield movements from price quotes alone. Settlement systems (Euroclear, DTC) always settle on dirty prices: every bond trade invoice uses the full price. A common pitfall for quants building fixed income analytics is to forget this distinction — using clean prices in a bond pricing formula (which should use dirty/full price) will produce incorrect yields and duration estimates, particularly for bonds close to their coupon date.
