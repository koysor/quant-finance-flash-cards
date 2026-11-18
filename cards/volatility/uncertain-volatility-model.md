# Uncertain Volatility Model

**Topic:** Volatility
**Tags:** uncertain volatility, worst-case pricing, black-scholes-barenblatt, gamma, nonlinear pde, model risk
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

The uncertain volatility model (Avellaneda, Levy and Parás, 1995; Lyons, 1995) drops the assumption that volatility is known and assumes only that it stays within a band, $\sigma^- \le \sigma \le \sigma^+$. Instead of one price it gives a range: the worst-case value to a holder and the best-case value. Each is found by letting volatility take whichever extreme hurts (or helps) the hedged position most at every point in $(S, t)$.

## Key Formula

The worst-case value for a long position solves the nonlinear **Black–Scholes–Barenblatt equation**:

$$\frac{\partial V}{\partial t} + \tfrac{1}{2}\,\sigma(\Gamma)^2 S^2\,\Gamma + rS\frac{\partial V}{\partial S} - rV = 0, \qquad \Gamma = \frac{\partial^2 V}{\partial S^2}$$

$$\sigma(\Gamma) = \begin{cases} \sigma^+ & \text{if } \Gamma < 0 \\ \sigma^- & \text{if } \Gamma > 0 \end{cases}$$

The best-case value swaps the two choices. Because $\sigma$ depends on the sign of $\Gamma$, the equation is nonlinear and is solved numerically, for example by finite differences.

## Example

An at-the-money call with $S = K = £100$, $T = 1$ year, $r = 5\%$ and a volatility band of $15\%$ to $25\%$.

A vanilla call has $\Gamma > 0$ everywhere, so the worst case uses $\sigma^- = 15\%$ throughout and the best case uses $\sigma^+ = 25\%$:

- worst case (bid): Black–Scholes at $15\%$ gives $£8.59$
- best case (ask): Black–Scholes at $25\%$ gives $£12.34$

The Black–Scholes price at a single "best guess" of $20\%$ is $£10.45$, inside the range. For a call spread, gamma changes sign across the strikes, so neither extreme volatility applies everywhere: the PDE must be solved, and the range is narrower than pricing each leg separately would suggest.

## Remember

The model turns volatility risk into a price range a dealer can quote, and it exposes a trap that a single-volatility model hides: a barrier option or call spread can show zero vega at one volatility while carrying large volatility risk, because gamma changes sign. The model is nonlinear, so a portfolio is worth more than the sum of its parts, and adding traded options as static hedges tightens an otherwise untradeably wide spread. Always price the whole book, not each trade.
