# Bond Yield

**Topic:** Fixed Income
**Tags:** bond yield, yield to maturity, ytm, internal rate of return, price-yield, fixed income
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

The **yield to maturity** (YTM) of a bond is the single constant discount rate $Y$ that equates the present value of all future cash flows to the bond's current dirty price. It is the bond's **internal rate of return** — a one-number summary that allows straightforward comparison across bonds with different maturities and coupon structures.

## Key Formula

For a bond settling on a coupon date with $n$ coupons remaining, coupon frequency $m$:

$$\text{Dirty} = \sum_{i=1}^{n} \frac{C/m}{\left(1 + Y/m\right)^{i}} + \frac{1}{\left(1 + Y/m\right)^{n}}$$

For settlement **between** coupon dates (fraction $w$ of current period remaining):

$$\text{Dirty} = \left(1 + \frac{Y}{m}\right)^{-w} \left[\sum_{i=0}^{n-1} \frac{C/m}{\left(1 + Y/m\right)^{i}} + \frac{1}{\left(1 + Y/m\right)^{n-1}}\right]$$

The **price–yield relationship is inverse and convex**: higher yield → lower price, and the curve bends so that price rises more than it falls for equal yield moves.

## Example

A 4% annual coupon bond with 3 years to maturity trades at a dirty price of 97.00 (per 100 face). Solve for $Y$:

$$97 = \frac{4}{1+Y} + \frac{4}{(1+Y)^2} + \frac{104}{(1+Y)^3} \implies Y \approx 5.07\%$$

The bond trades at a discount (price < 100) because its 4% coupon is below the market yield of ~5%.

## Remember

Yield is useful for **quoting and comparing** bonds but dangerous for **risk management**: it assumes a flat yield curve and parallel shifts. A barbell (short + long bonds) and a bullet (medium bond) with the same modified duration can have very different P&L under a steepening move — yield alone misses this entirely. For hedging, use key-rate durations against the full curve; use yield only as a shorthand for communication.
