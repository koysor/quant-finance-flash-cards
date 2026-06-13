# Forward Volatility

**Topic:** Volatility
**Tags:** forward volatility, forward variance, implied volatility, term structure, forward-start options, cliquets
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Forward volatility (or forward implied vol) is the implied volatility for a future time period $[T_1, T_2]$, implied by today's vol surface; it governs the pricing of forward-start options and cliquets, which depend on future smiles rather than today's.

## Key Formula

**Forward variance** (variance being additive):

$$\sigma_f^2(T_1, T_2) = \frac{\sigma_{\text{imp}}^2(T_2)\cdot T_2 - \sigma_{\text{imp}}^2(T_1)\cdot T_1}{T_2 - T_1}$$

**Forward vol:** $\sigma_f(T_1, T_2) = \sqrt{\sigma_f^2(T_1, T_2)}$

For forward-start ATM options starting at $T_1$ and expiring at $T_2$, today's price is approximately:

$$C_{\text{forward-start}} \approx N(d^+) - N(d^-), \quad d^\pm = \pm \tfrac{1}{2}\sigma_f\sqrt{T_2 - T_1}$$

## Example

6-month implied vol $= 20\%$, 3-month implied vol $= 18\%$. Forward variance $= (0.04 \times 0.5 - 0.0324 \times 0.25) / 0.25 = (0.02 - 0.0081)/0.25 = 0.0476$. Forward vol for months 3–6 $= \sqrt{0.0476} = 21.8\%$ — above the 6-month level, indicating the term structure of vol is upward-sloping for this period.

## Remember

Forward vols expose the model-dependence of exotic pricing: local vol models predict that forward smiles flatten over time (Dupire's surface), while stochastic vol models (Heston, SABR) generate richer forward smile dynamics. Cliquets and autocallables are highly sensitive to forward vol — a model that fits today's smile perfectly can still misprices these products if its forward vol dynamics are wrong.
