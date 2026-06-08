# Zero-Coupon Bond

**Topic:** Fixed Income
**Tags:** zero-coupon bond, discount factor, present value, term structure, building block
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **zero-coupon bond** (ZCB) is the simplest fixed-income instrument: it pays a single fixed notional $N$ in a given currency at maturity $T$ and nothing before. Its present value defines the **discount factor** $P(s,t)$ — the price at time $s$ of a promise to pay \$1 at time $t > s$.

## Key Formula

$$P(s, t) = \text{present value at } s \text{ of } \$1 \text{ paid at } t$$

$$\text{PV}(s) = N \cdot P(s, T)$$

Key properties:

| Property | Value |
|---|---|
| $P(t, t)$ | $1$ — a payment due now is worth its face value |
| $P(s, t)$ for $t > s$ | $(0, 1)$ — future cash flows are worth less today |
| As $T \to \infty$ | $P(0, T) \to 0$ |

Every fixed-income cash flow stream prices as:

$$\text{PV}(s) = \sum_{i=1}^{n} c_i \, P(s, t_i)$$

## Example

A ZCB pays $\$1{,}000$ in 5 years. If the 5-year discount factor is $P(0, 5) = 0.85$, its present value is:

$$\text{PV} = 1{,}000 \times 0.85 = \$850$$

Equivalently, the continuously compounded zero rate $r$ satisfies $P(0,5) = e^{-5r}$, giving $r = -\ln(0.85)/5 = 3.27\%$.

## Remember

The discount factor $P(s,t)$ is the single fundamental object in fixed income — all rates (yield, par rate, zero rate, forward rate) are just functions of it. In practice, pure ZCBs exist only for short maturities (Treasury bills) and via **STRIPS** at longer maturities; for everything else, the discount factor is inferred from liquid market instruments during curve calibration.
