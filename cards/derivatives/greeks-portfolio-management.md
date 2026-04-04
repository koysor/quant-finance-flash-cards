# Greeks Portfolio Management

**Topic:** Derivatives
**Tags:** Greeks, portfolio risk, delta, gamma, vega, theta, risk management
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Greeks portfolio management is the practice of monitoring and controlling the aggregate sensitivities — delta, gamma, vega, and theta — across an entire book of options positions. Rather than managing each trade individually, the portfolio manager views the book as a single entity with net Greek exposures that must be kept within risk limits. The goal is to understand how the total portfolio value will change in response to moves in the underlying, volatility, and time, and to hedge or adjust positions to maintain the desired risk profile.

## Key Formula

The **portfolio Greeks** are the position-weighted sums of individual option Greeks:

$$\Delta_{\text{port}} = \sum_{k=1}^{n} N_k \Delta_k, \qquad \Gamma_{\text{port}} = \sum_{k=1}^{n} N_k \Gamma_k$$

$$\mathcal{V}_{\text{port}} = \sum_{k=1}^{n} N_k \mathcal{V}_k, \qquad \Theta_{\text{port}} = \sum_{k=1}^{n} N_k \Theta_k$$

The **portfolio P&L approximation** for small changes $\Delta S$, $\Delta\sigma$, and $\Delta t$:

$$\Delta\text{P\&L} \approx \Delta_{\text{port}} \cdot \Delta S + \frac{1}{2}\Gamma_{\text{port}} \cdot (\Delta S)^2 + \mathcal{V}_{\text{port}} \cdot \Delta\sigma + \Theta_{\text{port}} \cdot \Delta t$$

To simultaneously neutralise delta and gamma using the underlying (zero gamma contribution) and one option with known Greeks $(\Delta_H, \Gamma_H)$:

$$N_H = -\frac{\Gamma_{\text{port}}}{\Gamma_H}, \qquad N_S = -(\Delta_{\text{port}} + N_H \Delta_H)$$

## Example

A derivatives desk holds three positions on a £100 stock:

| Position | $N$ | $\Delta$ | $\Gamma$ | $\mathcal{V}$ | $\Theta$ |
|---|---|---|---|---|---|
| Short 200 calls (K=100) | $-200$ | 0.55 | 0.03 | 0.25 | $-0.04$ |
| Long 100 puts (K=95) | $+100$ | $-0.30$ | 0.02 | 0.20 | $-0.03$ |
| Long 50 calls (K=110) | $+50$ | 0.30 | 0.025 | 0.22 | $-0.035$ |

Portfolio Greeks:

$$\Delta_{\text{port}} = (-200)(0.55) + (100)(-0.30) + (50)(0.30) = -110 - 30 + 15 = -125$$

$$\Gamma_{\text{port}} = (-200)(0.03) + (100)(0.02) + (50)(0.025) = -6 + 2 + 1.25 = -2.75$$

The book is short 125 deltas and short 2.75 gammas. If the stock rises £2:

$$\Delta\text{P\&L} \approx -125 \times 2 + \frac{1}{2}(-2.75)(4) = -250 - 5.50 = -£255.50$$

To gamma-hedge, the desk buys ATM calls ($\Gamma_H = 0.03$, $\Delta_H = 0.50$): $N_H = 2.75/0.03 \approx 92$ calls. Then delta-hedge the residual with stock.

## Remember

Greeks portfolio management is the daily reality of options market-making and structured products desks. The key insight is that individual trades may have uncomfortable Greeks, but the portfolio-level Greeks are what determine actual P&L risk. A desk might be short gamma on one strike but long gamma on another, with the net exposure being what matters for risk limits. In practice, desks decompose Greeks not just as single numbers but by **bucket** — grouping by underlying, expiry, and strike region — because aggregate neutrality can mask concentrated risks. The P&L approximation formula is the trader's mental model: "if the stock moves £X and vol moves Y points, my book makes or loses approximately £Z." For quant developers, building real-time Greek aggregation dashboards and what-if scenario tools is one of the highest-value deliverables on a trading desk.
