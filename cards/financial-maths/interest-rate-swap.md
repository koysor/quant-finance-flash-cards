# Interest Rate Swap

**Topic:** Financial Mathematics
**Tags:** interest rate swap, fixed income, par swap rate, derivatives, discounting, libor
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

An **interest rate swap (IRS)** is an over-the-counter contract in which two parties agree to exchange periodic cash flows: one pays a fixed rate (the **par swap rate**) and the other pays a floating rate (historically LIBOR, now typically SOFR or SONIA) on the same notional principal. The notional is never exchanged; only the net interest difference changes hands at each payment date. The par swap rate is chosen at inception so that the swap has zero initial value to both parties.

## Key Formula

The **fixed leg** present value equals the sum of discounted fixed coupons:

$$PV_{\text{fixed}} = N \cdot c \cdot \sum_{i=1}^{n} d(t_i)$$

The **floating leg** present value, assuming the floating rate resets to market, equals:

$$PV_{\text{float}} = N \cdot \left[1 - d(t_n)\right]$$

where $N$ is the notional, $d(t_i) = \frac{1}{(1+r_{t_i})^{t_i}}$ is the discount factor, and $r_{t_i}$ is the zero rate for maturity $t_i$. Setting $PV_{\text{fixed}} = PV_{\text{float}}$ at inception gives the **par swap rate**:

$$c^* = \frac{1 - d(t_n)}{\displaystyle\sum_{i=1}^{n} d(t_i)}$$

## Example

A 2-year annual-pay GBP swap uses spot rates $r_1 = 4\%$ and $r_2 = 5\%$. Discount factors:

$$d_1 = \frac{1}{1.04} \approx 0.9615, \quad d_2 = \frac{1}{(1.05)^2} \approx 0.9070$$

Par swap rate on £1,000,000 notional:

$$c^* = \frac{1 - 0.9070}{0.9615 + 0.9070} = \frac{0.0930}{1.8685} \approx 4.98\%$$

The fixed-rate payer pays £49,800 per year and receives the floating rate payment. At inception, both legs are worth £1,000,000, so the swap has zero cost to enter.

## Remember

The par swap rate is mathematically identical to the par bond coupon rate — it is the rate that makes the fixed leg worth par, which is why the swap curve and the par rate curve are closely linked. In practice, interest rate swaps are the most liquid instrument in the rates market, with daily volumes dwarfing bond markets. A rates trader uses swaps to hedge DV01 exposure, express views on the yield curve, or convert a fixed-coupon bond into a synthetic floating-rate note via an asset swap. Because the fixed leg of a swap equals the par rate, bootstrapping the zero (spot) curve from swap rates is the standard method for constructing the discount curve used to price all fixed-income instruments.
