# Range Notes

**Topic:** Fixed Income
**Tags:** range note, range accrual, structured products, digital options, interest rate, coupon
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **range note** (or range accrual note) is a structured fixed-income product whose coupon accrues only on days when a reference rate (typically 3-month SOFR or EURIBOR) remains within a pre-specified corridor $[L, U]$. Days on which the rate falls outside the corridor earn no interest, so the effective coupon depends on the fraction of fixing dates the rate spends in range. The holder is implicitly selling a strip of binary options on the rate in exchange for an above-market headline coupon.

## Key Formula

**Coupon received** at maturity over $N$ fixing dates:

$$\text{Coupon} = c \cdot \frac{1}{N}\sum_{i=1}^{N} \mathbf{1}\{L \leq r_{t_i} \leq U\}$$

**Pricing:** each daily accrual is a **cash-or-nothing digital** on the rate $r_{t_i}$ staying in range. Under a short-rate model, the present value of the $i$-th accrual is:

$$V_i = c \cdot \Delta t \cdot P(0,\, t_i) \cdot \Pr^{Q^{t_i}}\!\bigl(L \leq r_{t_i} \leq U\bigr)$$

where $P(0, t_i)$ is the discount factor to the fixing date and $Q^{t_i}$ is the $t_i$-forward measure. The total note value sums these accruals plus the discounted return of par. Under Black's model for lognormal rates:

$$\Pr^{Q^{t_i}}\!\bigl(L \leq r \leq U\bigr) = N(d_U) - N(d_L), \qquad d_j = \frac{\ln(F/j) + \tfrac{1}{2}\sigma^2 t_i}{\sigma\sqrt{t_i}}$$

where $F$ is the forward rate and $j \in \{L, U\}$.

## Example

3-year range note, notional £1,000,000, corridor $[3\%, 6\%]$ on 3-month SOFR, headline coupon $c = 8\%$ p.a. (vs. a 3-year gilt at 4.2%).

If SOFR stays in the corridor on 175 of 252 business days per year:

$$\text{Effective coupon} = 8\% \times \tfrac{175}{252} \approx 5.6\%\ \text{p.a.}$$

If SOFR breaks above 6% for the final quarter (as in a rate-hiking cycle), only 189/252 days accrue:

$$\text{Effective coupon} \approx 8\% \times \tfrac{189}{252} = 6.0\%\ \text{p.a.}$$

The buyer still outperforms the gilt, but the corridor is doing work. If SOFR spikes above 6% for half the year (63 non-accrual days), the effective coupon falls to $4.0\%$ — below the gilt — with no capital upside.

## Remember

Range notes transfer corridor risk from issuer to investor: the bank pays an above-market coupon, and the investor shorts a strip of digital options on the rate staying in range. In low-volatility, range-bound rate environments these products sold widely to retail and institutional investors seeking yield enhancement. After the 2022–2023 Fed hiking cycle pushed SOFR through 5%, legacy range notes with corridors of $[0\%, 3\%]$ stopped accruing entirely despite being nominally "fixed income". Pricing requires a term-structure model calibrated to cap/floor volatilities — not just the yield curve — because the value of each digital accrual depends on the probability that the rate stays in range, which is a volatility-sensitive quantity.
