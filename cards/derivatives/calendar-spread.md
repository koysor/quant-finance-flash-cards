# Calendar Spread

**Topic:** Derivatives
**Tags:** calendar spread, time spread, horizontal spread, theta, term structure, implied volatility
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A calendar spread (time spread) sells a near-term option at strike $K$ and expiry $T_1$, and buys an otherwise identical option at the same strike with later expiry $T_2 > T_1$; it profits from time decay of the short option if the underlying stays near $K$.

## Key Formula

$$\text{Net cost} = C(K, T_2) - C(K, T_1) > 0 \quad \text{(longer-dated option is more expensive)}$$

P&L at $T_1$ (when short option expires):

$$\text{P\&L} \approx C(K, T_2 - T_1;\, S_{T_1},\, \sigma_{\text{imp},T_2}) - C(K,0;\, S_{T_1}) - \text{initial cost}$$

Maximum profit near $S_{T_1} = K$ (ATM); vega of long exceeds short, so P&L also rises if $\sigma_{\text{imp}}$ increases.

## Example

$S = 100$, $K = 100$. Sell 1-month ATM call for \$3, buy 2-month ATM call for \$4.50. Net cost $= \$1.50$. If at $T_1$ the stock is still \$100 and the 1-month call expires worthless, the remaining 1-month long call is worth roughly \$3 → profit $\approx \$1.50$.

## Remember

A calendar spread is simultaneously long theta (short option decays faster near expiry), long vega (longer-dated option is more vega-sensitive), and short the volatility term structure (profits if the near-term vol is high relative to long-term vol). This makes it attractive when front-month implied vol is elevated — e.g. into earnings — and is expected to collapse after the event while back-month vol remains elevated.
