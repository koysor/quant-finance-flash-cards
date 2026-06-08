# Multi-Curve Framework

**Topic:** Fixed Income
**Tags:** multi-curve, ois discounting, ibor, forward curve, post-gfc, libor-ois spread
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

The **multi-curve framework** separates fixed-income pricing into a single **discounting curve** $P(t,\cdot)$ (the OIS/collateral curve) plus one **forward curve** $F^j(t,\cdot)$ for each benchmark index $j$. It replaced the pre-2007 single-curve world, where IBOR forward rates were assumed equal to OIS-implied rates.

## Key Formula

PV of the floating leg of an IRS referencing index $j$:

$$\text{PV}_{\text{float}} = N \sum_{i=1}^{n} P(0, t_i) \cdot \delta_i \cdot F^j(0;\, \theta_i,\, t_{i-1},\, t_i)$$

Each index $j$ (EURIBOR-3M, EURIBOR-6M, SOFR, etc.) has its own forward curve with an associated pseudo-discount factor:

$$F^j(t;\, t_0, u, v) = \frac{1}{\delta}\left(\frac{P^j(t,u)}{P^j(t,v)} - 1\right)$$

$P^j$ generates forward rates but **cannot be used to discount cash flows** — only the true discounting curve $P$ can do that.

## Example

A EUR 5-year IRS (receive EURIBOR-6M, pay fixed) requires:
1. **OIS curve** built from ESTR OIS quotes — for discounting all cash flows
2. **EURIBOR-6M forward curve** — for computing expected floating coupons

Using the same single OIS curve for both, as was done before 2007, would underprice the swap by several basis points because EURIBOR contains a credit/liquidity premium over ESTR.

## Remember

On **9 August 2007**, BNP Paribas froze three money-market funds, and IBOR–OIS spreads spiked from near zero to ~150bps within weeks. This proved that IBOR rates contain credit and liquidity risk premia that overnight rates do not — the single-curve world broke irrevocably. Every modern IRS, OIS, and FRA desk maintains separate curve objects for discounting and for each IBOR/ON tenor; using the wrong curve is a model error, not a simplification.
