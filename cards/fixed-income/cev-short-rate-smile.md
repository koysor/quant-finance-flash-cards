# CEV Short-Rate Model and the Cap Smile

**Topic:** Fixed Income
**Tags:** CEV, volatility smile, cap, floor, elasticity, short rate, lognormal, normal
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

In the constant-elasticity-of-variance (CEV) short-rate model $dr = u\,dt + \nu r^\beta\,dW$, the volatility elasticity $\beta$ controls not only the rate distribution but also the **shape of the implied volatility smile** for caps and floors. Higher $\beta$ produces a steeper downward-sloping smile (higher implied vol for in-the-money caps) because the rate distribution has a fatter right tail.

## Key Formula

The CEV diffusion $\nu r^\beta$ gives an instantaneous rate standard deviation of $\nu r^\beta$. For cap pricing, the model implies an **ATM implied volatility** of approximately:

$$\sigma_{\text{imp}}(K) \approx \nu r_{\text{fwd}}^{\beta-1}\left[1 + \tfrac{1}{2}(\beta-1)\frac{K - r_{\text{fwd}}}{r_{\text{fwd}}} + \cdots\right]$$

| $\beta$ | Rate distribution | Smile shape |
|---|---|---|
| 0 (Vasicek) | Normal | Flat smile (no skew) |
| 0.5 (CIR) | Non-central chi-squared | Mild downward slope |
| 1 (lognormal) | Lognormal (BGDM) | Stronger downward slope |
| 1.13 (empirical) | Super-lognormal | Steep downward slope |

## Example

With $r_{\text{fwd}} = 4\%$, $\nu = 0.126$, $\beta = 1.13$: ATM cap implied vol $\approx 0.126 \times (0.04)^{0.13} = 0.126 \times 0.75 \approx 9.5\%$. A 6% strike cap (150 bp OTM) sees implied vol $\approx 8.2\%$ — a downward slope of roughly $-0.85\%$ per 100 bp strike, consistent with market observations in pre-NIRP USD cap markets.

## Remember

The CEV elasticity $\beta$ is the single parameter that links the **time-series behaviour of rates** (estimated via the bucketing method) to the **cross-section of cap and floor implied vols**. If the estimated $\beta \approx 1.13$ from historical data, then the model predicts a downward-sloping smile — consistent with what markets typically show. A Vasicek model ($\beta = 0$) implies no smile at all, making it unsuitable for pricing options at different strikes even if it fits ATM instruments well.
