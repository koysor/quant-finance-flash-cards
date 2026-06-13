# Quanto Options

**Topic:** Derivatives
**Tags:** quanto, FX risk, correlation adjustment, foreign asset, domestic measure, cross-asset
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A quanto option pays the value of a foreign-currency asset in domestic currency at a fixed, pre-agreed exchange rate, eliminating FX exposure for the option holder; under the domestic risk-neutral measure, the foreign asset's drift gains a correlation adjustment term known as the quanto adjustment.

## Key Formula

Let $S^f$ = foreign asset price, $X$ = spot FX rate (domestic per foreign), $r_d$, $r_f$ = domestic/foreign risk-free rates, $\sigma_S$, $\sigma_X$ = respective vols, $\rho = \text{corr}(dS^f/S^f, dX/X)$.

Under the **domestic** risk-neutral measure $\mathbb{Q}^d$:

$$\frac{dS^f}{S^f} = \bigl(r_f - \rho\,\sigma_S\,\sigma_X\bigr)\,dt + \sigma_S\,dW^d$$

The quanto adjustment $-\rho\,\sigma_S\,\sigma_X$ shifts the drift relative to the unadjusted foreign drift $r_f$.

**Quanto call price** (fixed quanto factor $Q$ domestic units per foreign unit):

$$C_{\text{quanto}} = Q\,e^{-r_d T}\!\left[F_Q\,N(d_1) - K\,N(d_2)\right]$$

$$F_Q = S^f_0\,e^{(r_f - \rho\sigma_S\sigma_X)T}, \qquad d_1 = \frac{\ln(S^f_0/K) + (r_f - \rho\sigma_S\sigma_X + \tfrac{1}{2}\sigma_S^2)T}{\sigma_S\sqrt{T}}, \qquad d_2 = d_1 - \sigma_S\sqrt{T}$$

This is Black–Scholes with adjusted forward $F_Q$ replacing the standard foreign forward $S^f_0 e^{r_f T}$.

## Example

ATM quanto call on the Nikkei index, paying USD 1 per Nikkei point. $S^f_0 = 28{,}000$, $K = 28{,}000$, $T = 1$ yr, $r_d = 5\%$ (USD), $r_f = 0\%$ (JPY), $\sigma_S = 20\%$, $\sigma_X = 8\%$ (USD/JPY vol), $\rho = -0.3$ (Nikkei up → yen strengthens → USD/JPY falls).

Quanto adjustment: $-\rho\sigma_S\sigma_X = -(-0.3)(0.20)(0.08) = +0.48\%$ per year.

Adjusted forward: $F_Q = 28{,}000\,e^{0.0048} = 28{,}135$ (above the plain foreign forward of 28,000 at $r_f = 0$).

The positive adjustment reflects compensation for losing the FX upside: when the Nikkei is high, USD/JPY is typically low (yen strong), so without the quanto, a USD investor would receive even more — the quanto price is marked up accordingly.

## Remember

The quanto adjustment is the key exam result: $-\rho\sigma_S\sigma_X$ is subtracted from the foreign drift, so **negative correlation increases the quanto forward** and vice versa. For Nikkei quanto products sold to US investors, $\rho < 0$ (risk-off moves: stocks fall, yen strengthens) means the quanto forward exceeds the unadjusted foreign forward — the seller of the quanto implicitly gives the buyer credit for the lost FX upside. Banks use quantos to offer efficient exposure to foreign equity indices without requiring the client to manage currency risk, making them standard in structured retail products.
