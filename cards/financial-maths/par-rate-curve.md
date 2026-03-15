# Par Rate Curve

**Topic:** Financial Mathematics
**Tags:** par rate, yield curve, fixed income, bonds, bootstrapping, term structure
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

The **par rate curve** plots the coupon rate at which a bond of each maturity would be priced exactly at par (face value). It is derived from the spot (zero-coupon) rate curve and represents the fixed rate that makes the present value of all cash flows — coupons plus principal — equal to 100.

## Key Formula

For a bond with annual coupons paying at times $t_1, t_2, \ldots, t_n = T$, the par rate $c_T$ satisfies:

$$100 = \sum_{i=1}^{n} \frac{c_T \cdot 100}{(1 + r_{t_i})^{t_i}} + \frac{100}{(1 + r_T)^T}$$

Rearranging to solve for the par rate:

$$c_T = \frac{1 - d_T}{\sum_{i=1}^{n} d_{t_i}}$$

where $d_{t_i} = \dfrac{1}{(1 + r_{t_i})^{t_i}}$ is the discount factor for maturity $t_i$.

## Example

Suppose the spot rates are $r_1 = 4\%$ and $r_2 = 5\%$. The 2-year par rate is:

$$d_1 = \frac{1}{1.04} \approx 0.9615, \quad d_2 = \frac{1}{(1.05)^2} \approx 0.9070$$

$$c_2 = \frac{1 - 0.9070}{0.9615 + 0.9070} = \frac{0.0930}{1.8685} \approx 4.98\%$$

A 2-year bond paying annual coupons of 4.98% on a £100 face value would trade at exactly £100.

## Remember

The par rate curve is the form of the yield curve most visible in government bond markets, since newly issued sovereign bonds are typically priced at par. Fixed income traders use the par curve to quickly gauge whether an existing bond is trading at a premium or discount to the current market. The relationship between par rates and spot rates is fundamental to bootstrapping: par rates are the market inputs, and the spot (zero-coupon) curve is extracted from them iteratively. Swap fixed rates are essentially par rates — the fixed leg of an interest rate swap is set so the swap has zero initial value, which is exactly the par rate condition.
