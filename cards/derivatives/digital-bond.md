# Digital Bond

**Topic:** Derivatives
**Tags:** digital bond, binary option, risk-neutral probability, cash-or-nothing, option decomposition, black-scholes
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **digital bond** is a derivative that pays £1 if the underlying $S_T \geq K$ at maturity and zero otherwise — it is the unit-payout cash-or-nothing option. Its price equals the discounted risk-neutral probability of exercise, making it the fundamental instrument for reading implied probabilities directly from option markets. Together with the digital share, it decomposes every European vanilla call.

## Key Formula

$$D_B = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[\mathbf{1}_{\{S_T \geq K\}}\right] = e^{-rT}\,N(d_2)$$

where

$$d_2 = \frac{\ln(S/K) + (r - \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

**Call decomposition** — any European call can be written:

$$C = D_S - K \cdot D_B = S\,N(d_1) - K\,e^{-rT}\,N(d_2)$$

**Delta** of the digital bond (peaks at-the-money, falls to zero deep in/out):

$$\frac{\partial D_B}{\partial S} = \frac{e^{-rT}\,N'(d_2)}{S\,\sigma\sqrt{T}}$$

## Example

$S = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

$$d_2 = \frac{\ln(1) + (0.05 - 0.02) \times 1}{0.20} = \frac{0.03}{0.20} = 0.15$$

$$D_B = e^{-0.05} \times N(0.15) = 0.9512 \times 0.5596 = £0.532$$

The digital bond costs £0.532, so the market implies a 55.96% risk-neutral probability of the stock finishing above £100 in one year. The full call price:

$$C = 100 \times N(0.35) - 100 \times 0.532 = £63.68 - £53.20 = £10.48$$

confirming the Black-Scholes formula by decomposition ($d_1 = 0.35$, $N(d_1) = 0.6368$).

## Remember

The digital bond gamma is the sharpest hedging challenge in listed derivatives: near expiry with $S \approx K$, a small move in the underlying creates a large jump in the delta, causing severe daily P&L swings. Experienced traders replace digital payoffs with **call spreads** — long call at $K - \varepsilon$, short call at $K + \varepsilon$ — to smooth the gamma at the cost of slightly mis-matching the payoff. Barrier-option pricing produces similar digital bond exposures at the barrier level, which is why barrier trades are routinely delta-hedged with a call spread overlay rather than the theoretical delta.
