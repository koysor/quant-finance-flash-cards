# Coupon Bond and STRIPS

**Topic:** Fixed Income
**Tags:** coupon bond, strips, stripping, zero-coupon decomposition, fixed income, government bonds
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **fixed coupon bond** pays periodic coupons $N\delta C$ plus principal $N$ at maturity. **STRIPS** (Separate Trading of Registered Interest and Principal of Securities) are the result of splitting a coupon bond into its individual cash flows, each of which trades as an independent zero-coupon bond.

## Key Formula

Price of a fixed coupon bond at $t_0$ with $n$ coupons remaining:

$$P_{\text{bond}} = \sum_{i=1}^{n} N \delta C \cdot P(t_0, t_i) + N \cdot P(t_0, t_n)$$

| Term | Meaning |
|---|---|
| $N$ | Face value (notional) |
| $C$ | Annual coupon rate |
| $\delta$ | Accrual factor per coupon period |
| $P(t_0, t_i)$ | Discount factor from today to coupon date $t_i$ |

A coupon bond is exactly a **portfolio of zero-coupon bonds** — one for each coupon payment and one for the principal.

## Example

A 4% semi-annual US Treasury with 1 year to maturity and face value \$1,000. Two coupons of \$20 plus \$1,000 principal:

$$P = 20 \cdot P(0, 0.5) + 20 \cdot P(0, 1) + 1{,}000 \cdot P(0, 1)$$

With $P(0, 0.5) = 0.976$ and $P(0, 1) = 0.952$:

$$P = 20 \times 0.976 + 1{,}020 \times 0.952 = 19.52 + 970.80 = \$990.32$$

## Remember

The STRIPS market allows pension funds and insurance companies to match long-dated liabilities precisely: by holding only the STRIP that matures on the liability date, they eliminate coupon reinvestment risk entirely. The US Treasury has offered STRIPS since 1985; the UK offers gilt strips via GEMM dealers. STRIPS also provide clean **market-implied discount factors** at each coupon date, which are an important input to yield curve construction.
