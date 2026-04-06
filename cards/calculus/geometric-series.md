# Geometric Series

**Topic:** Calculus
**Tags:** geometric series, common ratio, sum, present value, discounting, annuity, bonds
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **geometric series** is the sum of a geometric sequence — one in which each term is multiplied by a fixed constant $r$ called the **common ratio**. The $n$th term is $a_n = ar^{n-1}$.

## Key Formula

**Finite sum ($r \neq 1$):**

$$S_n = \frac{a(1 - r^n)}{1 - r}$$

**Infinite sum** ($|r| < 1$):

$$S_\infty = \frac{a}{1 - r}$$

The infinite series converges if and only if $|r| < 1$.

## Example

A £100 coupon bond pays £10 per year for 5 years, discounted at $r_{\text{disc}} = 8\%$. The discount factor per period is $v = 1/1.08$.

$$\text{PV of coupons} = 10v + 10v^2 + \cdots + 10v^5 = 10v \cdot \frac{1 - v^5}{1 - v} = \frac{10(1 - 1.08^{-5})}{0.08} \approx £39.93$$

This is the standard **annuity formula** — a direct application of the finite geometric series.

## Remember

**Bond pricing is a geometric series.** Every coupon is the previous one multiplied by the discount factor $v = 1/(1+r)$; summing them gives the annuity formula. An **annuity** paying £1 per period for $n$ periods has present value $a_{\overline{n}|} = (1 - v^n)/r$ — derived in one line from the geometric series formula. A **perpetuity** (infinite payments) has PV $= 1/r$, the infinite geometric series limit. The entire fixed-income toolkit — duration, convexity, swap valuation — reduces to manipulations of this one formula.
