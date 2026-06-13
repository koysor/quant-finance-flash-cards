# Bachelier (Normal) Interest Rate Model

**Topic:** Fixed Income
**Tags:** Bachelier, normal model, negative rates, caplet, swaption, normal vol, arithmetic Brownian motion, EURIBOR, Black model
**Created:** 2026-06-14
**Author:** Claude Sonnet 4.6

---

## Definition

The **Bachelier model** assumes the forward rate follows **arithmetic Brownian motion**, making rates normally distributed and allowing them to go negative. After 2008, when European and Japanese rates turned negative, Black's lognormal formula broke down and the Bachelier model became the market standard for quoting cap and swaption volatilities — especially for EUR and JPY.

## Key Formula

Bachelier caplet price (forward rate $F$, strike $K$, expiry $T$, annuity factor $A$):

$$\text{Caplet} = A\!\left[(F-K)\,N(d) + \sigma_N\sqrt{T}\,\phi(d)\right], \qquad d = \frac{F - K}{\sigma_N\sqrt{T}}$$

where $\sigma_N$ is the **normal (Bachelier) volatility** in units of rate per $\sqrt{\text{year}}$, $N$ is the standard normal CDF, and $\phi$ is its density. At-the-money ($F = K$), the link to Black vol is approximately:

$$\sigma_N \approx F \cdot \sigma_{Black}$$

## Example

EURIBOR 3-month rate $F = -0.30\%$, cap strike $K = -0.50\%$, $\sigma_N = 40$ bps/yr, $T = 1$ year:

$$d = \frac{-0.30\% - (-0.50\%)}{0.40\%} = 0.50$$

$$\text{Caplet} = A\bigl[(0.20\%)N(0.50) + (0.40\%)\phi(0.50)\bigr] = A\bigl[0.138\% + 0.141\%\bigr] \approx 28\text{ bps} \times A$$

Under Black's formula this caplet would require $\ln(F/K)$ with $F < 0$ — undefined.

## Remember

Bachelier is the **additive-increment** counterpart to Black's multiplicative model: $dF = \sigma_N\,dW_t$ vs $dF = \sigma F\,dW_t$. The distinction matters when rates can be zero or negative. Bloomberg and major banks adopted Bachelier vol as the standard quoting convention for EUR, JPY, and CHF rate options post-2014, and the normal-vol convention has since spread to USD products as a more robust alternative.
