# Binary Option

**Topic:** Derivatives
**Tags:** digital option, exotic derivatives, Black-Scholes, risk-neutral probability, payoff
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

A **binary option** (also called a **digital option**) pays a fixed amount if a condition is met at expiry, and zero otherwise. It is the simplest exotic derivative.

There are two main types:

- **Cash-or-nothing call:** pays a fixed cash amount $Q$ if $S_T > K$ at expiry, zero otherwise.
- **Asset-or-nothing call:** pays the asset value $S_T$ if $S_T > K$ at expiry, zero otherwise.

The binary call has a step-function payoff: $\text{Payoff} = Q \cdot \mathbf{1}_{S_T > K}$, in contrast to the ramp-shaped payoff of a vanilla call.

## Key Formula

Under Black-Scholes, the price of a **cash-or-nothing call** is:

$$C_{\text{binary}} = Q \cdot e^{-rT} \cdot N(d_2)$$

where

$$d_2 = \frac{\ln(S/K) + (r - \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

and $N(\cdot)$ is the standard normal cumulative distribution function.

**Interpretation:** $N(d_2)$ is the **risk-neutral probability** that $S_T > K$, so the binary call price is simply the discounted expected payoff:

$$C_{\text{binary}} = e^{-rT} \cdot \mathbb{E}^{\mathbb{Q}}[Q \cdot \mathbf{1}_{S_T > K}] = Q \cdot e^{-rT} \cdot N(d_2)$$

The binary call is also the negative derivative of the vanilla call price with respect to strike $K$:

$$C_{\text{binary}} = -\frac{\partial C_{\text{vanilla}}}{\partial K}$$

making it central to understanding the volatility smile.

## Example

Suppose $S = 100$, $K = 105$, $r = 0.05$, $\sigma = 0.20$, $T = 1$ year, and $Q = £1{,}000$.

$$d_2 = \frac{\ln(100/105) + (0.05 - 0.02) \times 1}{0.20 \times 1} = \frac{-0.0488 + 0.03}{0.20} = \frac{-0.0188}{0.20} \approx -0.094$$

$$N(-0.094) \approx 0.4626$$

$$C_{\text{binary}} = 1{,}000 \times e^{-0.05} \times 0.4626 \approx £440$$

The option is worth about £440 because there is roughly a 46% risk-neutral chance the stock finishes above 105 in one year.

## Remember

Binary options appear naturally in **merger arbitrage**: if an acquirer offers a fixed price $Q$ per share contingent on deal completion, the target's shares behave like a binary option — paying $Q$ if the deal closes, near zero if it breaks. Pricing this risk using $Q \cdot e^{-rT} \cdot N(d_2)$ captures the market's implied probability of deal success, making the binary option a direct bridge between derivatives pricing and event-driven investing.
