# Black's Model for Swaptions

**Topic:** Fixed Income
**Tags:** Black's model, swaption, swap rate, annuity measure, implied vol, European swaption
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Black's model** applied to a European swaption treats the forward swap rate as the underlying, with the **annuity factor** as the numeraire. Under the annuity measure the swap rate is a martingale, so Black's lognormal formula applies directly. This gives a closed-form price for payer and receiver swaptions that is the market standard for quoting swaption implied volatilities.

## Key Formula

For a **payer swaption** (right to pay fixed rate $K$, receive floating, entering the swap at expiry $T$):

$$V_{\text{payer}} = A(0)\!\left[F_{\text{swap}}\,N(d_1) - K\,N(d_2)\right]$$

$$d_{1,2} = \frac{\ln(F_{\text{swap}}/K) \pm \tfrac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}$$

For a **receiver swaption** (right to receive fixed):

$$V_{\text{receiver}} = A(0)\!\left[K\,N(-d_2) - F_{\text{swap}}\,N(-d_1)\right]$$

**Put-call parity:** $V_{\text{payer}} - V_{\text{receiver}} = A(0)(F_{\text{swap}} - K)$ — the right-hand side is the value of the underlying forward swap.

| Symbol | Meaning |
|---|---|
| $A(0) = \sum_i \delta_i P(0,T_i)$ | Annuity factor (PV of \$1/yr over swap tenor) |
| $F_{\text{swap}}$ | Forward swap rate |
| $\sigma$ | Swaption implied volatility (Black vol) |
| $T$ | Swaption expiry |

## Example

5y × 5y payer swaption (5-year expiry, 5-year swap). $F_{\text{swap}} = 4\%$, $K = 4\%$ (ATM), $\sigma = 20\%$, $T = 5$, annuity $A(0) = 4.33$ years.

$$d_1 = d_2 = 0 \quad (\text{ATM, lognormal}), \quad N(d_1) - N(d_2) = 2N(d_1) - 1 \approx 0$$

$$d_1 = \tfrac{1}{2} \times 0.20 \times \sqrt{5} = 0.2236, \quad N(0.2236) \approx 0.5885$$

$$V_{\text{payer}} = 4.33 \times [0.04 \times 0.5885 - 0.04 \times 0.4115] = 4.33 \times 0.04 \times 0.177 = 30.7 \text{ bp}$$

## Remember

Black's swaption formula is structurally identical to Black-Scholes, but with two substitutions: the **stock price** is replaced by the forward swap rate $F_{\text{swap}}$, and the **risk-free discount factor** is replaced by the annuity $A(0)$. The annuity plays both roles simultaneously: it is the numeraire that makes the swap rate a martingale, and it is the discount factor that converts the payoff into a present value. Swaption implied vols quoted in this model form the "swaption cube" (expiry × tenor × moneyness) that dealers use to calibrate Bermudan swaption and callable bond models.
