# Callable Bond

**Topic:** Fixed Income
**Tags:** callable bond, embedded option, negative convexity, option-adjusted spread, yield to call
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

A **callable bond** is a bond that gives the issuer the right — but not the obligation — to redeem the bond before its stated maturity at a pre-specified call price (usually par or par plus a small premium). This embedded call option benefits the issuer: when interest rates fall, the issuer can call the bond and refinance at lower rates. The investor bears this reinvestment risk and therefore demands a higher yield than on an equivalent non-callable bond.

## Key Formula

The callable bond can be decomposed as:

$$P_{\text{callable}} = P_{\text{straight}} - C_{\text{call}}$$

where $P_{\text{straight}}$ is the price of an otherwise identical non-callable bond and $C_{\text{call}}$ is the value of the embedded call option. Equivalently, the **option-adjusted spread (OAS)** removes the option cost to compare yield on an option-free basis:

$$\text{Yield}_{\text{callable}} = \text{Yield}_{\text{straight}} + \text{Option Cost (in yield terms)}$$

The **yield to call (YTC)** is the IRR assuming the bond is called at the first call date:

$$P = \sum_{t=1}^{T_{\text{call}}} \frac{C}{(1+\text{YTC})^t} + \frac{\text{Call Price}}{(1+\text{YTC})^{T_{\text{call}}}}$$

## Example

A 10-year, 5% coupon bond callable after 3 years at par (\$100) is priced at \$98. The YTC (first call date):

$$98 = \sum_{t=1}^{3} \frac{5}{(1+\text{YTC})^t} + \frac{100}{(1+\text{YTC})^3}$$

Solving numerically: YTC $\approx$ 5.72% — higher than the yield to maturity because the investor is compensated for the call risk. If rates fall below 5%, the issuer will almost certainly call, leaving the investor to reinvest at prevailing lower rates.

## Remember

Callable bonds exhibit **negative convexity** at low yields: when rates fall, the bond price rises less than for a straight bond because the probability of being called increases and caps the price near the call price. This makes callable bonds behave differently from Treasuries in a bull market for rates — duration decreases as yields fall (the opposite of positive convexity). Mortgage-backed securities (MBS) exhibit the same negative convexity due to homeowner prepayment optionality, which is why the OAS framework was originally developed for the MBS market. Risk managers must model the call option explicitly (e.g. using a Hull-White interest rate model) rather than relying on modified duration alone.
