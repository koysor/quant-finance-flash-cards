# Corporate Events in Pricing

**Topic:** Computational Finance
**Tags:** discrete dividends, corporate events, jump processes, option pricing, pure process, tdbp
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Corporate events** — discrete dividends, earnings announcements, or share buybacks — cause sudden discontinuous jumps in stock prices. Standard models such as Black-Scholes assume continuous log-normal dynamics and cannot handle these events without complex adjustments. RL-based models such as TDBP learn from training paths that contain the jumps directly, making them naturally robust to these events.

## Key Formula

When a discrete dividend $d_i$ is paid at time $t_i$, the ex-dividend stock price falls by:

$$S(t_i^+) = S(t_i^-) - d_i$$

The implied volatility surface (IVS) of the full stock process $S$ decomposes into a "censored" IVS from the **pure continuous process** $Y$ and a correction term $\mathcal{E}(K,T)$ capturing the event's impact:

$$\Sigma_S(K,T) = \Sigma_Y(K,T) + \mathcal{E}(K,T)$$

## Example

A stock at £50 pays a £2.50 dividend in 60 days. Under Black-Scholes a practitioner must adjust the forward or use a complex numerical tree, introducing discretisation error. Under TDBP, the model trains on thousands of simulated paths each containing a £2.50 drop on day 60. The neural network implicitly learns to lower option prices for all maturities $T > 60$ to account for the anticipated drop, without any explicit formula.

## Remember

RL handles corporate events by training on price paths that include the jumps — no explicit jump-diffusion SDE is required. This makes TDBP models naturally consistent with discrete dividends and earnings gaps, avoiding the calibration overhead of Merton jump-diffusion or the tree restructuring required at each dividend date in finite-difference methods.
