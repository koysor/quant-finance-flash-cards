# Swap Curve Construction

**Topic:** Fixed Income
**Tags:** swap curve, bootstrap, discount curve, forward curve, OIS, multi-curve, SOFR
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Swap curve construction** (also called curve bootstrapping) builds a continuous discount factor function $P(0,T)$ from a set of market instruments — deposits, FRAs, interest rate futures, and par swap rates — each contributing to a specific maturity segment. The result is a self-consistent curve that exactly reprices all input instruments and can be used to discount cashflows, compute forward rates, and price derivatives at any maturity.

## Key Formula

Given par swap rates $c_1, c_2, \ldots, c_n$ at annual maturities and previously-determined discount factors $P(0,T_1),\ldots,P(0,T_{n-1})$, the next discount factor is:

$$P(0,T_n) = \frac{1 - c_n \displaystyle\sum_{i=1}^{n-1} \delta_i\,P(0,T_i)}{1 + c_n\,\delta_n}$$

The instantaneous forward rate implied by the discount curve:

$$f(0,T) = -\frac{\partial \ln P(0,T)}{\partial T}$$

**Typical instrument layering:**

| Maturity | Input instruments |
|---|---|
| O/N to 3m | Overnight deposits, SOFR/ESTR fixings |
| 3m to 2y | SOFR futures or FRAs (after convexity adjustment) |
| 2y to 30y | Par swap rates bootstrapped sequentially |

## Example

2-year annual swap rate $c_2 = 4.5\%$; 1-year discount factor $P(0,1) = 0.9569$ (from deposits/FRAs). Bootstrap:

$$P(0,2) = \frac{1 - 0.045 \times 1 \times 0.9569}{1 + 0.045 \times 1} = \frac{1 - 0.04306}{1.045} = \frac{0.95694}{1.045} = 0.9158$$

Implied 1y forward rate in 1 year: $f(1,2) = P(0,1)/P(0,2) - 1 = 0.9569/0.9158 - 1 = 4.49\%$.

## Remember

Post-2008, swap curve construction split into the **multi-curve framework**: one OIS curve (SOFR/ESTR) for discounting collateralised trades, and separate forward curves for each tenor (1m, 3m, 6m SOFR) for computing floating cashflows. The two curves diverge because unsecured interbank credit risk (which used to be embedded in LIBOR) is no longer present in collateralised OIS rates. A key practical point: the same par swap rate can imply very different forward rates depending on whether you use OIS discounting or LIBOR discounting — and the difference (the **OIS-LIBOR basis**) was as large as 350 bp during the 2008 crisis. Any interest rate model is ultimately calibrated to this bootstrapped curve.
