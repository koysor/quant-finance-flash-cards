# CrashMetrics

**Topic:** Risk
**Tags:** crashmetrics, worst-case scenario, crash coefficient, stress testing, delta-gamma, platinum hedging
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

CrashMetrics (Hua and Wilmott, 1997–99) measures the worst loss a portfolio can suffer in a market crash. It assumes that in a crash every asset moves with a benchmark index, asset $i$ by $\kappa_i$ times the index move, so the portfolio's change in value depends on one variable: the size of the crash. The worst case is then found by minimising over a plausible range of crash sizes, with no correlations or volatilities needed.

## Key Formula

For an index move of $x$ (as a fraction), a delta–gamma expansion of a portfolio of derivatives on assets $S_i$ with crash coefficients $\kappa_i$ gives

$$\delta\Pi(x) = A\,x + \tfrac{1}{2}B\,x^2, \qquad A = \sum_i \Delta_i\,\kappa_i\,S_i, \qquad B = \sum_i \Gamma_i\,\kappa_i^2\,S_i^2$$

$$\text{Worst-case loss} = \min_{x^- \le x \le x^+}\ \delta\Pi(x)$$

$A$ is the crash delta and $B$ the crash gamma. If $B > 0$, the minimum may be inside the range at $x^* = -A/B$; if $B < 0$, it is at one end.

## Example

A book has crash delta $A = £2\text{m}$ and crash gamma $B = -£40\text{m}$ (short options), and crashes are taken to lie between $-30\%$ and $+10\%$:

- $\delta\Pi(-0.30) = 2\text{m} \times (-0.30) + \tfrac{1}{2}(-40\text{m})(0.09) = -0.6\text{m} - 1.8\text{m} = -£2.4\text{m}$
- $\delta\Pi(+0.10) = 0.2\text{m} - 0.2\text{m} = £0$

With $B < 0$ the worst case is at an end of the range: a loss of £2.4m in a 30% crash. A "10% fall" stress test would report only £0.4m.

## Remember

Diversification fails exactly when it is needed: in a crash correlations go to one, so a VaR model built on normal-times correlations understates the loss. CrashMetrics complements VaR by asking how bad the worst plausible crash is, and the answer guides static ("platinum") hedging: buying or selling options so the worst-case loss, or the margin it would trigger, is as small as possible.
