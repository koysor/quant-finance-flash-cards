# Convexity

**Topic:** Financial Mathematics
**Tags:** convexity, bonds, duration, interest rate risk, fixed income, yield
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Convexity** is the second-order measure of a bond's price sensitivity to changes in yield. Because the price–yield relationship is curved (not linear), duration alone — a first-order measure — underestimates price gains when yields fall and overestimates losses when yields rise. Convexity captures this curvature and corrects the duration approximation for large yield moves.

## Key Formula

The full two-term price change approximation for a bond with modified duration $D_{\text{mod}}$ and convexity $C$ is:

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \tfrac{1}{2} \cdot C \cdot (\Delta y)^2$$

Convexity itself is defined as the second derivative of price with respect to yield, scaled by price:

$$C = \frac{1}{P} \cdot \frac{d^2 P}{dy^2} = \frac{1}{P} \sum_{t=1}^{n} \frac{t(t+1) \cdot CF_t}{(1+y)^{t+2}}$$

where $CF_t$ is the cash flow (coupon or face value) at time $t$, $y$ is the yield per period, and $P$ is the bond price.

## Example

A 10-year gilt has a modified duration of 7.5 and a convexity of 75. Yields rise by 100 bp (i.e. $\Delta y = 0.01$).

Duration-only estimate:

$$\frac{\Delta P}{P} \approx -7.5 \times 0.01 = -7.50\%$$

With the convexity correction:

$$\frac{\Delta P}{P} \approx -7.5 \times 0.01 + \tfrac{1}{2} \times 75 \times (0.01)^2 = -7.50\% + 0.375\% = -7.125\%$$

The convexity term adds back 0.375%, reducing the estimated loss. For a yield fall of the same magnitude, convexity adds to the gain — the bond benefits symmetrically from large moves.

## Remember

Convexity explains the **asymmetry of bond returns**: when yields move significantly in either direction, a bond always performs slightly better than duration predicts. This is why bonds with higher convexity command a premium — all else equal, investors prefer more convexity. In portfolio management, a trader who is "long convexity" profits from large yield moves in either direction, whilst a trader who is "short convexity" (e.g. via mortgage-backed securities with prepayment risk) is exposed to losses from large moves. Convexity also underpins the gamma of interest rate options: both measure second-order sensitivity to the underlying variable.
