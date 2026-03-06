# Gamma (Greeks)

**Topic:** Derivatives
**Tags:** gamma, Greeks, sensitivity, options, convexity, hedging
**Created:** 2026-03-06
**Author:** Claude Opus 4.6

---

## Definition

**Gamma** ($\Gamma$) is the second-order Greek that measures the rate of change of Delta with respect to a small change in the underlying asset price. Formally, $\Gamma = \partial^2 V / \partial S^2 = \partial \Delta / \partial S$. It captures the curvature (convexity) of the option's price as a function of the underlying.

## Key Formula

For European options under Black-Scholes:

$$\Gamma = \frac{N'(d_1)}{S \, \sigma \sqrt{T}}$$

where $N'(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal PDF and

$$d_1 = \frac{\ln(S / K) + \left(r + \tfrac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}$$

Key properties:

- Gamma is **always positive** for long option positions (both calls and puts).
- Gamma is highest for **at-the-money** options near expiry.
- Gamma is the same for a call and its corresponding put (by put-call parity).
- As $T \to 0$, Gamma of an ATM option spikes towards infinity — the payoff kink sharpens.

## Example

A European call has $S = 100$, $K = 100$, $\sigma = 20\%$, $T = 0.25$ years.

$$d_1 = \frac{\ln(1) + (0.05 + 0.02)(0.25)}{0.20\sqrt{0.25}} = \frac{0.0175}{0.10} = 0.175$$

$$N'(0.175) = \frac{1}{\sqrt{2\pi}} e^{-0.175^2/2} \approx 0.3932$$

$$\Gamma = \frac{0.3932}{100 \times 0.20 \times 0.50} = \frac{0.3932}{10} = \mathbf{0.0393}$$

If the stock rises by £1, Delta increases by approximately 0.04 — the option accelerates into the money.

## Remember

Gamma is the reason delta hedging is never a one-off trade. A high-Gamma position means Delta shifts rapidly with the underlying, forcing frequent rebalancing. The cost of that rebalancing is offset by **Theta** — this is the fundamental **Gamma-Theta trade-off**: long Gamma profits from large realised moves but bleeds time decay; short Gamma collects Theta but faces explosive losses from big moves. Market makers who sell options are short Gamma and must carefully monitor their exposure near expiry, when Gamma peaks for ATM strikes.
