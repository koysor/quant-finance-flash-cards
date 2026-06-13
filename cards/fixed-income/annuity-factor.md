# Annuity Factor

**Topic:** Fixed Income
**Tags:** annuity factor, swap measure, numeraire, present value, annuity, fair swap rate
**Created:** 2026-06-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **annuity factor** (also called the **level** or **PV01** of a swap) is the present value of receiving \$1 per year over the life of a swap, discounted at current market rates. It converts a fixed coupon rate into a present value and serves as the **numeraire** for the annuity measure — the probability measure under which the fair swap rate is a martingale.

## Key Formula

For a swap with payment dates $T_1 < T_2 < \cdots < T_N$ and day-count fractions $\delta_i = T_i - T_{i-1}$:

$$A(t, T_N) = \sum_{i=1}^{N} \delta_i\, P(t, T_i)$$

where $P(t, T_i)$ is the zero-coupon bond price at time $t$ for maturity $T_i$. The **fair swap rate** is then:

$$S(t) = \frac{P(t, T_0) - P(t, T_N)}{A(t, T_N)}$$

For a flat yield curve at rate $y$ with annual payments:

$$A = \frac{1 - (1+y)^{-N}}{y}$$

| Annuity factor interpretation | Meaning |
|---|---|
| Numeraire in annuity measure | $S(t)$ is a martingale under $\mathbb{Q}^A$ |
| Sensitivity measure | Change in swap PV per 1 bp change in swap rate $\approx A \times 0.0001$ |
| CMS adjustment input | $\partial A / \partial S$ appears in CMS convexity corrections |

## Example

A 5-year annual-pay swap, discount curve at $y = 4\%$:
$$A = \frac{1 - (1.04)^{-5}}{0.04} = \frac{1 - 0.8219}{0.04} = \frac{0.1781}{0.04} = 4.452 \text{ years}$$

If the 5-year swap has a fair rate of $S = 4.5\%$ and the 5y zero price is $P(0,5) = 0.8219$, the PV of the fixed leg is $4.5\% \times 4.452 = 20.0\text{ bp}$ and the floating leg pays par minus the 5y discount factor: $1 - 0.8219 = 17.81\text{ bp}$ — a \$2.2\text{ bp} mismatch, indicating the fair swap rate is not exactly 4%.

## Remember

The annuity factor is the bridge between swap rates and bond prices: it is both a **pricing tool** (scale the swap rate to get a PV) and a **measure-theoretic object** (the numeraire that makes the swap rate a martingale). This dual role is why the annuity measure is the natural measure for swaption pricing under Black's model — the swaption payoff $A(T)(S(T)-K)^+$ divided by the numeraire $A(T)$ is simply $(S(T)-K)^+$, a call option on a martingale, which Black's formula prices directly. Without understanding the annuity factor, it is impossible to correctly price swaptions or derive CMS convexity adjustments.
