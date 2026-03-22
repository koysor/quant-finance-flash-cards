# Forward Rate Curve

**Topic:** Fixed Income
**Tags:** forward rates, yield curve, bootstrapping, term structure, interest rates, fixed income
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **forward rate curve** plots the implied interest rates between pairs of future dates, derived from today's zero-coupon (spot) curve. Each point on the forward curve answers the question: "What rate does the market imply for lending between date $T_1$ and date $T_2$?" The forward curve is obtained from the zero curve via **bootstrapping** — reading off the rates that make today's bond prices internally consistent.

## Key Formula

The **continuously compounded forward rate** $f(T_1, T_2)$ implied by spot rates $r(T_1)$ and $r(T_2)$:

$$f(T_1, T_2) = \frac{r(T_2)\,T_2 - r(T_1)\,T_1}{T_2 - T_1}$$

For annual compounding, the equivalent relationship using discount factors $P(T) = (1 + r_T)^{-T}$:

$$1 + f_{T_1, T_2} = \frac{P(T_1)}{P(T_2)} = \frac{(1 + r_{T_2})^{T_2}}{(1 + r_{T_1})^{T_1}}$$

The **instantaneous forward rate** $f(T)$ at maturity $T$, for a continuously compounded spot curve $r(T)$:

$$f(T) = r(T) + T\,\frac{\partial r}{\partial T}$$

## Example

The 1-year spot rate is 4.00% and the 2-year spot rate is 4.50% (both continuously compounded).

The 1-year forward rate, one year from now:

$$f(1, 2) = \frac{0.045 \times 2 - 0.040 \times 1}{2 - 1} = \frac{0.090 - 0.040}{1} = 0.050 \quad (5.00\%)$$

The market therefore implies a 5.00% rate for lending during year 2. This is higher than the 2-year spot rate because the spot rate is an average; the forward rate reveals the marginal rate embedded at that horizon.

## Remember

The forward rate curve is the market's best guess at future short-term rates and is central to fixed income trading. Interest rate swap pricing relies on projecting floating leg cash flows using forward rates bootstrapped from the OIS or LIBOR swap curve — a £100m 5-year swap's floating payments are each discounted at spot rates but sized using forward rates. When the forward curve lies above (below) the spot curve, it implies the market expects rates to rise (fall), a key input for duration management and yield curve trading strategies.
