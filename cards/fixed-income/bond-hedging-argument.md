# Bond Hedging Argument

**Topic:** Fixed Income
**Tags:** bond hedging, no-arbitrage, market price of risk, fixed income, interest rate risk, portfolio construction
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

Because the short rate $r$ is not a traded asset, a fixed-income derivative cannot be hedged directly against $r$. Instead, **one bond must be hedged against a second bond of a different maturity**. The no-arbitrage condition on this hedge portfolio forces a universal pricing equation — the fixed-income pricing PDE — that every bond must satisfy.

## Key Formula

Hold one unit of bond $V_1$ (maturing at $T_1$) and short $\Delta$ units of bond $V_2$ (maturing at $T_2$):

$$\Pi = V_1 - \Delta V_2$$

To eliminate the random term $\propto dX$ in $d\Pi$, set:

$$\Delta = \frac{\partial V_1/\partial r}{\partial V_2/\partial r}$$

Since $\Pi$ is then instantaneously risk-free, it must earn the risk-free rate:

$$d\Pi = r\,\Pi\,dt$$

Substituting and rearranging yields the **universal constraint** — for any bond $V$ with maturity $T$:

$$\frac{\frac{\partial V}{\partial t} + \frac{1}{2}w^2\frac{\partial^2 V}{\partial r^2} + u\frac{\partial V}{\partial r} - rV}{w\frac{\partial V}{\partial r}} = \lambda(r,t)$$

where $\lambda$ (the market price of risk) depends only on $r$ and $t$, not on $T$.

## Example

Suppose a 2-year bond has $\partial V_1/\partial r = -0.80$ and a 5-year bond has $\partial V_2/\partial r = -2.10$. The hedge ratio is $\Delta = 0.80/2.10 = 0.381$: short 0.381 units of the 5-year bond per unit of the 2-year bond to create a locally risk-free portfolio. Any deviation from this ratio leaves residual interest rate risk.

## Remember

The bond hedging argument is the fixed-income analogue of the Black–Scholes delta-hedging argument, but with a crucial twist: because $r$ cannot be traded, the hedge must use two instruments denominated in $r$. The consequence is that the market price of risk $\lambda$ cannot be determined from within the model — it must be inferred from market prices — whereas in equity Black–Scholes the market price of risk cancels out entirely.
