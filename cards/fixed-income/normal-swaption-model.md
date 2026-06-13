# Normal Swaption Model

**Topic:** Fixed Income
**Tags:** normal model, Bachelier, swaption, negative rates, Black vol, normal vol, NIRP
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **normal (Bachelier) swaption model** assumes the forward swap rate follows arithmetic Brownian motion — constant absolute moves in rate space rather than constant proportional moves. It produces a closed-form swaption price analogous to Black's formula but with normal volatility $\sigma_N$ measured in basis points per year, and is the market standard when rates are near zero or negative because it does not require taking the logarithm of the swap rate.

## Key Formula

For a payer swaption with forward swap rate $F$, strike $K$, expiry $T$, and annuity $A(0)$:

$$V_{\text{payer}} = A(0)\!\left[(F - K)\,N(d) + \sigma_N\sqrt{T}\,\varphi(d)\right]$$

$$d = \frac{F - K}{\sigma_N\sqrt{T}}$$

where $\varphi$ is the standard normal PDF and $N$ the CDF.

**Black–Normal vol conversion** (approximate, valid near ATM):

$$\sigma_N \approx \sigma_{\text{Black}} \times F \qquad \text{(for } F > 0\text{)}$$

$$\sigma_{\text{Black}} \approx \frac{\sigma_N}{F}$$

| Regime | Preferred model | Reason |
|---|---|---|
| $F \gg 0$ (pre-2015) | Black lognormal | Standard, positive-rate assumption holds |
| $F \approx 0$ or $F < 0$ (post-NIRP) | Normal (Bachelier) | Black vol becomes infinite or undefined at low strikes |

## Example

EUR 5y5y payer swaption. $F = -0.10\%$, $K = 0\%$, $T = 5$ yr, $\sigma_N = 55$ bp/yr, $A(0) = 4.60$ yr.

$$d = \frac{-0.001 - 0}{0.0055 \times \sqrt{5}} = \frac{-0.001}{0.01230} = -0.081$$

$$V_{\text{payer}} = 4.60 \times [(-0.001)(0.468) + 0.0055\sqrt{5}\,(0.397)] = 4.60 \times [-0.000468 + 0.00489] = 4.60 \times 0.00442 = 2.03\%$$

The swaption has positive value despite a negative forward rate, because there is a non-trivial probability that the swap rate rises above 0% by expiry.

## Remember

The shift from Black to normal vol in the post-2015 EUR market was not just a modelling choice but a practical necessity: when 5-year EUR swap rates fell below zero, Black's model implied vol exploded to hundreds of per cent and became meaningless as a risk metric. Normal vol (quoted in basis points per year) remained well-behaved at any rate level. The ISDA 2021 fallback protocol and most modern swaption term sheets now quote normal vols for EUR rates. The key insight is that normal vol is an **absolute** measure of rate uncertainty (bp/yr), while Black vol is a **relative** measure (%/yr) — in a zero-rate world, a relative measure of an infinitesimally small number is uninformative.
