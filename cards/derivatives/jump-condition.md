# Jump Condition

**Topic:** Derivatives
**Tags:** jump condition, discrete dividend, finite difference, pde, boundary condition, option pricing
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **jump condition** is a constraint imposed at an interior time slice of the option pricing PDE where the model undergoes an instantaneous discontinuity, ensuring the solution remains financially consistent across that instant. The most common example is the **discrete dividend jump condition**: when a stock pays a cash dividend $D$ at ex-dividend date $t_D$, the stock price drops immediately and the option value must satisfy a matching condition before and after $t_D$.

## Key Formula

At the ex-dividend date, the stock price falls:

$$S(t_D^+) = S(t_D^-) - D$$

No-arbitrage requires the option value to satisfy the jump condition:

$$V(S,\; t_D^-) = V(S - D,\; t_D^+)$$

In a finite-difference scheme, this is applied between two backward induction sweeps: after solving back to $t_D^+$, the value grid is remapped to the shifted spot $S - D$ to produce $V(\cdot, t_D^-)$ before the sweep continues to earlier times.

## Example

A European call on a stock with $K = \£100$ pays a dividend $D = \£3$ at $t_D = 3$ months; $T = 6$ months. Solving the PDE backward from $T$ to $t_D^+$ gives, for example, $V(100,\, t_D^+) = 5.20$ and $V(103,\, t_D^+) = 6.80$. Applying the jump condition:

$$V(103,\; t_D^-) = V(103 - 3,\; t_D^+) = V(100,\; t_D^+) = 5.20$$

The pricer uses $5.20$, not $6.80$, for the spot-$\£103$ node just before the dividend, then continues the backward sweep to $t = 0$.

## Remember

Failing to implement dividend jump conditions is one of the most common sources of systematic mispricing in equity option pricers. A Black-Scholes formula that substitutes a continuous dividend yield overestimates call prices on stocks with lumpy quarterly dividends, because it spreads the dividend drop smoothly over time rather than concentrating it on the ex-date. On equity derivatives desks, every PDE solver carries an explicit dividend schedule and applies a jump condition at each ex-date — this is often the first bug a junior quant encounters when their freshly built pricer produces deltas that jump discontinuously across a dividend date. The same pattern (interrupt the backward sweep, update values, continue) appears for Bermudan exercise decisions and coupon payments in structured products.
