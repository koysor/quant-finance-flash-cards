# Yield Curve

**Topic:** Financial Mathematics
**Tags:** yield curve, interest rates, term structure, bonds, discounting
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

The **yield curve** is a graph plotting annualised interest rates (yields) against their maturity — from short-term (e.g. 3 months) to long-term (e.g. 30 years). It represents the **term structure of interest rates**: the set of discount rates the market applies to cash flows at different horizons.

The most common shapes are:
- **Normal (upward-sloping)** — long-term rates exceed short-term rates
- **Inverted (downward-sloping)** — short-term rates exceed long-term rates, often signalling recession
- **Flat** — rates are similar across all maturities

## Key Formula

The **spot rate** $r_n$ for maturity $n$ is extracted from the price of a zero-coupon bond:

$$P_n = \frac{1}{(1 + r_n)^n} \quad \Longrightarrow \quad r_n = P_n^{-1/n} - 1$$

The **forward rate** $f_{n-1,n}$ — the implied rate between years $n-1$ and $n$ — links adjacent spot rates:

$$f_{n-1,n} = \frac{(1 + r_n)^n}{(1 + r_{n-1})^{n-1}} - 1$$

## Example

Zero-coupon bond prices: $P_1 = 0.9524$ (1-year), $P_2 = 0.8985$ (2-year).

Spot rates:

$$r_1 = 0.9524^{-1} - 1 = 0.0500 \quad (5.00\%)$$

$$r_2 = 0.8985^{-1/2} - 1 = 0.0550 \quad (5.50\%)$$

The 1-year forward rate one year from now:

$$f_{1,2} = \frac{(1.0550)^2}{1.0500} - 1 = \frac{1.1130}{1.0500} - 1 = 0.0600 \quad (6.00\%)$$

The market implies a 6.00% rate for the second year.

## Remember

The yield curve is the foundation of fixed-income valuation — every bond, swap, and interest rate derivative is priced by discounting cash flows using rates read from (or bootstrapped from) the curve. An inverted yield curve has historically been one of the most reliable recession indicators. In quantitative finance, PCA on yield curve changes typically reveals that three factors — level, slope, and curvature — explain over 95% of all yield curve movements, making it a powerful dimensionality reduction for interest rate risk.
