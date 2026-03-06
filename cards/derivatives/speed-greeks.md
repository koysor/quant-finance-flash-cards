# Speed (Greeks)

**Topic:** Derivatives
**Tags:** speed, Greeks, sensitivity, options, gamma, third-order
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Speed** is the third-order Greek that measures the rate of change of Gamma with respect to a change in the underlying asset price. Formally, $\text{Speed} = \partial \Gamma / \partial S = \partial^3 V / \partial S^3$. It tells a trader how stable their Gamma exposure is as the underlying moves.

## Key Formula

For European options under Black-Scholes:

$$\text{Speed} = -\frac{\Gamma}{S}\left(\frac{d_1}{\sigma\sqrt{T}} + 1\right)$$

where $\Gamma = N'(d_1) / (S\sigma\sqrt{T})$.

Key properties:

- Speed is **negative** for ATM calls when $d_1 > 0$ — Gamma decreases as the stock rises past the strike.
- Speed is largest in magnitude near the money and close to expiry, where Gamma itself is most sensitive.
- For a delta-hedged book, Speed determines how quickly the Gamma profile shifts and whether Gamma hedges hold.

## Example

A European call has $S = 100$, $K = 100$, $\sigma = 20\%$, $T = 0.25$ years, with $\Gamma = 0.0393$ and $d_1 = 0.175$.

$$\text{Speed} = -\frac{0.0393}{100}\left(\frac{0.175}{0.20 \times 0.50} + 1\right) = -0.000393 \times (1.75 + 1) = \mathbf{-0.00108}$$

If the stock rises by £1, Gamma changes by approximately $-0.00108$ — falling from 0.0393 to about 0.0382. The hedge is becoming less convex as the option moves into the money.

## Remember

Speed matters most to **exotic options desks** and large portfolio managers who hedge Gamma itself. A barrier option near its knock-out level can have extreme Speed — Gamma shifts violently as the spot approaches the barrier, making Gamma hedges unreliable. Market makers running large books of short-dated options near expiry also monitor Speed, because Gamma can swing from near-zero to very large over a small price range, and Speed quantifies exactly how fast that transition occurs. It is the third-order term in the Taylor expansion of the option price and is usually negligible for vanilla positions away from expiry.
