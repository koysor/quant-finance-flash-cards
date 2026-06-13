# One-Factor Short-Rate Model Comparison

**Topic:** Fixed Income
**Tags:** short rate, model comparison, Vasicek, CIR, Ho-Lee, Hull-White, affine model
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

All standard one-factor short-rate models share the general SDE $dr = u(r,t)\,dt + w(r,t)\,dW_t$ and produce exponential-affine bond prices $Z = e^{A(t,T) - rB(t,T)}$. They differ in whether the drift and volatility are constant or time-dependent, and whether volatility depends on the rate level.

## Key Formula

Under the risk-neutral measure:

| Model | Drift $u(r,t)$ | Volatility $w(r,t)$ | Mean reversion | Fits curve? |
|---|---|---|---|---|
| Vasicek | $a - br$ | $c$ | Yes | No |
| CIR | $a - br$ | $c\sqrt{r}$ | Yes | No |
| Ho–Lee | $a(t)$ | $c$ | No | Yes |
| Hull–White I | $a(t) - b(t)r$ | $c(t)$ | Yes | Yes |
| Hull–White II | $a(t) - b(t)r$ | $c(t)\sqrt{r}$ | Yes | Yes |

All produce bond prices $Z = e^{A(t,T) - rB(t,T)}$ where $B$ saturates at $1/b$ for Vasicek/Hull–White but equals $T - t$ for Ho–Lee (no mean reversion).

## Example

For a 5-year zero-coupon bond with $r = 4\%$: Vasicek gives $B(5) = (1 - e^{-5b})/b < 5$ due to mean reversion; Ho–Lee gives $B(5) = 5$ exactly. The shorter $B$ in Vasicek means bond prices are less sensitive to today's spot rate at long maturities — mean reversion dampens the impact of current rates on distant forwards.

## Remember

The progression from Vasicek to Hull–White II represents a systematic trade-off between **parsimony** and **calibration power**: constant parameters give interpretable, stable models that cannot fit the yield curve; time-dependent parameters sacrifice stability to match market prices exactly. In practice, banks use Hull–White I for swaptions (it fits both the yield curve and the flat volatility structure with two time-dependent parameters); CIR is preferred for credit default intensity models where negative values are inadmissible.
