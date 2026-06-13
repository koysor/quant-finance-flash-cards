# Shifted Black Model

**Topic:** Fixed Income
**Tags:** shifted Black, displaced diffusion, negative rates, swaption, Black vol, shift parameter
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **shifted Black model** (also called displaced diffusion) extends Black's lognormal swaption formula to handle negative or near-zero rates by adding a constant **shift** $\alpha > 0$ to the forward rate, making the effective underlying $F + \alpha$ strictly positive. The standard Black formula then applies to $(F + \alpha)$ with strike $(K + \alpha)$, preserving the closed-form structure without abandoning lognormal dynamics.

## Key Formula

The shifted forward rate satisfies:

$$d(F + \alpha) = \sigma_s\,(F + \alpha)\,dW$$

Payer swaption price under the shifted Black model:

$$V = A(0)\!\left[(F + \alpha)\,N(d_1) - (K + \alpha)\,N(d_2)\right]$$

$$d_{1,2} = \frac{\ln\!\dfrac{F+\alpha}{K+\alpha} \pm \tfrac{1}{2}\sigma_s^2 T}{\sigma_s\sqrt{T}}$$

**Conversion between shifted-Black and normal vol** (approximate, ATM):

$$\sigma_N \approx \sigma_s\,(F + \alpha)$$

| Shift $\alpha$ | Effective floor | Common use |
|---|---|---|
| 1% (100 bp) | $F > -1\%$ | EUR swaptions (moderate NIRP) |
| 3% (300 bp) | $F > -3\%$ | JPY swaptions (deep NIRP era) |
| 0 | $F > 0$ (standard Black) | Pre-2015 all markets |

## Example

EUR 5y5y payer swaption: $F = -0.20\%$, $K = 0\%$, shift $\alpha = 1\%$, $\sigma_s = 30\%$, $T = 5$ yr, $A(0) = 4.55$ yr.

Shifted forward: $F + \alpha = 0.80\%$. Shifted strike: $K + \alpha = 1.00\%$.

$$d_1 = \frac{\ln(0.008/0.010) + \tfrac{1}{2}(0.09)(5)}{0.30\sqrt{5}} = \frac{-0.223 + 0.225}{0.671} = 0.003$$

$$V \approx 4.55 \times [0.008 \times 0.501 - 0.010 \times 0.499] = 4.55 \times [0.00401 - 0.00499] = -4.5 \text{ bp}$$

The negative intrinsic ($F < K$) is partially offset by time value, giving a small but positive premium.

## Remember

The shifted Black model is a **pragmatic patch** rather than a fundamentally correct model for negative rates — it preserves the traders' familiar lognormal intuition and vol quoting conventions while sidestepping the mathematical breakdown of Black's model at zero. The shift $\alpha$ is a convention chosen by each market: ISDA and CME both standardised $\alpha = 1\%$ for EUR rates, allowing brokers to continue quoting shifted-Black vols. The key limitation is that the shift is fixed and arbitrary — it does not emerge from an economic theory of how rates behave near zero. For deeply negative rates, the normal model is more principled; for practical desk use, the shifted Black model's familiarity wins.
