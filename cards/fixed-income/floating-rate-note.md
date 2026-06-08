# Floating Rate Note

**Topic:** Fixed Income
**Tags:** floating rate note, frn, par reset, ibor, overnight compounded, duration, structured product
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **floating rate note** (FRN) is a bond whose coupon resets periodically to a benchmark rate (IBOR or compounded overnight) plus a fixed spread. Because the coupon adjusts to market rates at each reset date, an FRN with zero spread reprices to **par at every fixing date**, giving it approximately zero duration.

## Key Formula

Each coupon period $[t_{i-1}, t_i]$ pays:

**IBOR FRN (traditional):**

$$\text{Coupon}_i = N \cdot \delta_i \cdot \bigl(L^j(t_{i-1}) + s\bigr)$$

**Overnight compounded FRN (modern GBP/USD):**

$$\text{Coupon}_i = N \cdot \delta_i \cdot \left(\text{CompON}_{[t_{i-1},t_i]} + s\right)$$

**Par value property** (when spread $s = 0$): discounting all future coupons at the same benchmark rate yields exactly par at each reset date, so:

$$P_{\text{FRN}}(t_i^-) = N$$

## Example

A 3-year SONIA FRN, notional \$100m, spread = 0. At each quarterly reset date the bond reprices to \$100m regardless of where SONIA has moved. If SONIA rises from 4% to 5%, an equivalent fixed-rate bond would lose value but the FRN stays at par.

## Remember

The par-reset property makes FRNs a natural floating-rate hedge for banks that fund themselves at overnight rates (deposits) and lend via FRNs. However, the spread $s$ over the benchmark is fixed at issuance, so an FRN's **credit spread risk** is as large as that of a fixed-rate bond — only the interest rate duration is near zero. Modern FRNs referencing compounded overnight rates (SOFR, SONIA) have largely replaced IBOR-linked FRNs following the LIBOR transition.
