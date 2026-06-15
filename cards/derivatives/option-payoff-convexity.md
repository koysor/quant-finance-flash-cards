# Option Payoff Convexity

**Topic:** Derivatives
**Tags:** convexity, option payoff, gamma, positive gamma, theta-gamma tradeoff, jensen
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The expiry payoff of a long option is a **convex** function of the underlying: the payoff curve bends upward. This means a large move in either direction always produces a gain larger than the delta-predicted gain — the mathematical origin of **positive gamma** for all long option positions.

## Key Formula

The kink at strike $K$ makes the payoff non-smooth; in the distributional sense:

$$\frac{d^2}{dS_T^2}\max(S_T - K,\, 0) = \delta(S_T - K) \geq 0$$

Prior to expiry this smooths to a finite positive gamma:

$$\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{N'(d_1)}{S\,\sigma\sqrt{T}} > 0$$

By Jensen's inequality, convexity means the option's value always exceeds its intrinsic value when $\sigma > 0$:

$$V = E^Q[\max(S_T - K,\,0)] \geq \max(E^Q[S_T] - K,\,0)$$

## Example

Spot $S = 100$, strike $K = 100$, $\sigma = 20\%$, $T = 1$ yr. Suppose $\Delta \approx 0.54$ and $\Gamma \approx 0.019$. If the spot moves to $S = 110$ (+10):

- Delta predicts: $+10 \times 0.54 = \$5.40$
- Gamma correction: $+\tfrac{1}{2} \times 0.019 \times 100 = +\$0.95$
- Total P&L $\approx \$6.35$ — more than the delta hedge alone

The extra \$0.95 is **gamma profit**, the reward for holding a convex payoff.

## Remember

Positive gamma is not free: the option buyer pays **theta** (time decay) to the seller in return for this convexity. In the Black–Scholes world, the two exactly cancel on average, giving the theta-gamma identity: $\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = rV$. In practice, traders buy gamma when they expect realised volatility to exceed the implied volatility embedded in the option price, and sell gamma otherwise — making option payoff convexity the central concept behind volatility trading.
