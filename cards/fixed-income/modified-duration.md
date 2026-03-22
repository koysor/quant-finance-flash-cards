# Modified Duration

**Topic:** Fixed Income
**Tags:** modified duration, fixed income, bonds, interest rate risk, sensitivity, duration
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Modified duration** is the percentage change in a bond's price for a one-percentage-point (100 bp) increase in yield. It is the Macaulay duration — the weighted-average time to receive the bond's cash flows, with weights equal to the present value of each cash flow as a fraction of total price — divided by one plus the periodic yield.

## Key Formula

$$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + y/m}$$

where $D_{\text{mac}}$ is the Macaulay duration (in years), $y$ is the annual yield, and $m$ is the number of coupon periods per year. The Macaulay duration is:

$$D_{\text{mac}} = \frac{1}{P} \sum_{t=1}^{n} t \cdot \frac{CF_t}{(1 + y/m)^t}$$

The resulting price sensitivity relationship is:

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y$$

## Example

A 3-year bond has a face value of £1,000, a 5% annual coupon, and a yield of 5% (so it prices at par: $P = £1{,}000$). The Macaulay duration is:

$$D_{\text{mac}} = \frac{1 \times 47.62 + 2 \times 45.35 + 3 \times 907.03}{1{,}000} = \frac{47.62 + 90.70 + 2{,}721.09}{1{,}000} \approx 2.86 \text{ years}$$

Modified duration (annual coupons, $m = 1$):

$$D_{\text{mod}} = \frac{2.86}{1.05} \approx 2.72$$

A 1% rise in yield reduces the bond's price by approximately $2.72\% \times £1{,}000 = £27.20$.

## Remember

Modified duration is the key tool for managing **parallel yield curve risk**: a trader compares the modified duration of a bond against a benchmark to quantify how much the position will gain or lose per 100 bp of yield movement. It is the direct precursor to DV01 — multiply modified duration by price and $0.0001$ to convert to a per-basis-point cash figure. Bonds with longer maturities and lower coupons have higher modified duration, making them more sensitive to rate changes and therefore riskier in a rising-rate environment.
