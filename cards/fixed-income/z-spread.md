# Z-Spread

**Topic:** Fixed Income
**Tags:** z-spread, credit spread, fixed income, discounting, bond pricing, term structure
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Z-spread** (zero-volatility spread) is the constant spread $z$ added to every point on the benchmark zero (spot) rate curve such that the sum of the bond's discounted cash flows exactly equals its observed market price. Unlike the yield spread — which compares a bond's single yield to a single benchmark yield — the Z-spread accounts for the full shape of the yield curve, making it a more precise measure of the additional return an investor earns for bearing credit and liquidity risk.

## Key Formula

For a bond with cash flows $C_i$ at times $t_i$ and market price $P$, the Z-spread $z$ solves:

$$P = \sum_{i=1}^{n} \frac{C_i}{e^{(r(t_i) + z)\, t_i}}$$

where $r(t_i)$ is the benchmark zero rate at maturity $t_i$ (expressed as a continuously compounded rate). Equivalently, using discrete compounding:

$$P = \sum_{i=1}^{n} \frac{C_i}{(1 + r(t_i) + z)^{t_i}}$$

Since no closed form exists for $z$, it is found by **numerical root-finding** (e.g. Newton–Raphson or bisection) on the equation $f(z) = P - \sum_i C_i \cdot e^{-(r(t_i)+z)\,t_i} = 0$.

## Example

A 2-year annual-coupon corporate bond pays £5 at year 1 and £105 at year 2, and trades at £98.50. The benchmark zero rates are $r(1) = 4.00\%$ and $r(2) = 4.50\%$ (continuously compounded).

Try $z = 1.50\%$ (150 bps):

$$\frac{5}{e^{(0.04 + 0.015) \times 1}} + \frac{105}{e^{(0.045 + 0.015) \times 2}} = \frac{5}{e^{0.055}} + \frac{105}{e^{0.12}}$$

$$= \frac{5}{1.0565} + \frac{105}{1.1275} \approx 4.73 + 93.13 = 97.86$$

Too low — the computed price £97.86 is below £98.50, so $z$ must be slightly smaller. Iterating gives $z \approx 1.30\%$ (130 bps), meaning the bond offers 130 bps above the risk-free curve at every maturity.

## Remember

The Z-spread is the standard measure of credit premium in investment-grade bond markets because it strips out the distorting effect of the benchmark curve's shape. When two bonds from the same issuer trade at different Z-spreads, it signals a relative-value opportunity — the wider-Z-spread bond is cheaper for the same credit risk. Crucially, the Z-spread assumes **no optionality**: for callable or putable bonds, the option-adjusted spread (OAS) extends the Z-spread framework by also removing the value of embedded options, leaving only the pure credit component.
