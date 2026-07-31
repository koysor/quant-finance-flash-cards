# Box Rate Method

**Topic:** Derivatives
**Tags:** put-call parity, forward price, discount factor, regression, no-arbitrage, calibration
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **Box Rate method** extracts the forward price $F_T$ and discount factor $D_T$ for an expiry directly from listed option prices, using put-call parity, without needing an external interest rate curve or a dividend forecast. It regresses the call-minus-put spread against strike across all quoted strikes at that expiry; because the parity relationship is exactly linear in strike, a single ordinary least squares fit recovers both quantities at once. The name nods to the "box spread" options structure, which similarly locks in a financing rate from option prices alone.

## Key Formula

Put-call parity states $C(K) - P(K) = D_T(F_T - K)$, which rearranges to a straight line in $K$:

$$C(K) - P(K) = D_T F_T - D_T K$$

Regressing $(C_j - P_j)$ on $K_j$ across strikes at one expiry:

$$\text{slope} = -D_T, \qquad \text{intercept} = D_T F_T$$

so that

$$D_T = -\text{slope}, \qquad F_T = \frac{\text{intercept}}{D_T}$$

## Example

At a given expiry, mid prices for three strikes give call-minus-put spreads: $K=4{,}400 \Rightarrow C-P = 105.2$; $K=4{,}500 \Rightarrow C-P = 15.6$; $K=4{,}600 \Rightarrow C-P = -73.9$.

A linear regression of $(C-P)$ against $K$ gives slope $\approx -0.8955$ and intercept $\approx 4046.2$ (illustrative fit). Then:

$$D_T = -(-0.8955) = 0.8955, \qquad F_T = \frac{4046.2}{0.8955} \approx 4{,}518.4$$

This $F_T$ and $D_T$, read straight from the market's own call and put quotes, can now be used consistently to compute log-moneyness, recompute implied volatilities, and run no-arbitrage diagnostics — all from the same internally consistent snapshot.

## Remember

The value of the Box Rate method is *consistency*, not novelty: any volatility surface pipeline needs a forward and a discount factor to convert strikes to log-moneyness and to compute implied volatility, and if those inputs come from a mismatched external curve, the mismatch shows up downstream as spurious calendar or butterfly arbitrage that has nothing to do with the actual option quotes. By deriving $F_T$ and $D_T$ from the same options being surfaced, the Box Rate method removes one whole source of false-positive arbitrage signals before the harder work of regularising and differentiating the surface even begins — a cheap, model-free first step that every serious local volatility pipeline performs before building the total variance surface.
