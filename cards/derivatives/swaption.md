# Swaption

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** swaption, interest rate option, volatility, rates, Black model, exercise
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A swaption is an option to enter into an interest rate swap at a predetermined fixed rate (the strike) on a future date. A **payer swaption** gives the holder the right to pay fixed and receive floating; a **receiver swaption** gives the right to receive fixed and pay floating. Swaptions are the primary instrument for trading interest rate volatility and are used to hedge callable bonds, mortgage prepayment risk, and optionality in structured products. They are quoted in a matrix of expiry × underlying swap tenor (e.g. "5y into 10y" means an option expiring in 5 years to enter a 10-year swap).

## Key Formula

Under the **Black (1976) model**, the price of a payer swaption is:

$$V_{\text{payer}} = A \cdot \bigl[F \cdot N(d_1) - K \cdot N(d_2)\bigr]$$

where:

$$d_1 = \frac{\ln(F/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

$F$ is the forward swap rate, $K$ is the strike, $\sigma$ is the swaption implied volatility, $T$ is the option expiry, and $A$ is the **annuity factor** (PV of a £1 annuity over the swap tenor):

$$A = \sum_{i=1}^{n} \tau_i \cdot d(t_i)$$

where $\tau_i$ is the year fraction for period $i$ and $d(t_i)$ is the discount factor.

## Example

A 1-year expiry payer swaption on a 5-year annual swap. Market data: forward swap rate $F = 4.5\%$, strike $K = 4.5\%$ (ATM), implied vol $\sigma = 22\%$, annuity factor $A = 4.30$ (per £1 notional).

Since $F = K$ (ATM), $d_1 = \frac{\sigma\sqrt{T}}{2} = \frac{0.22}{2} = 0.11$ and $d_2 = -0.11$:

$$V_{\text{payer}} = 4.30 \times [0.045 \times N(0.11) - 0.045 \times N(-0.11)]$$
$$= 4.30 \times 0.045 \times [N(0.11) - N(-0.11)]$$
$$= 0.1935 \times [0.5438 - 0.4562] = 0.1935 \times 0.0876 = 0.01695$$

On £100 million notional: $V = £100{,}000{,}000 \times 0.01695 = £1{,}695{,}000$.

## Remember

Swaptions are to the rates market what equity options are to the stock market — they are the primary volatility instrument and the building block for pricing and hedging anything with embedded optionality. The swaption volatility cube (expiry × tenor × strike) is the rates equivalent of the equity vol surface, and it is calibrated daily using either the SABR model or shifted Black vols. For quant developers on a rates desk, swaption pricing is a core competency: the annuity factor connects the option to the underlying curve, the Black model provides the baseline, and SABR provides the smile. Understanding the payer-receiver parity ($V_{\text{payer}} - V_{\text{receiver}} = A \cdot (F - K)$) is essential for consistency checking and arbitrage detection across the swaption grid.
