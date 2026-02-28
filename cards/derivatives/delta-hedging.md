# Delta Hedging

**Topic:** Derivatives
**Tags:** delta hedging, delta-neutral, Greeks, replication, options
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

**Delta hedging** is a strategy that makes a portfolio instantaneously insensitive to small changes in the underlying asset price. It exploits the fact that $\Delta = \partial V / \partial S$ measures the rate at which the option value changes with the stock price; holding $-\Delta$ units of the stock offsets that sensitivity.

A **delta-neutral** portfolio has $\Delta_{\text{portfolio}} = 0$.

## Key Formula

For a European call under Black-Scholes:

$$\Delta_{\text{call}} = N(d_1), \qquad \Delta_{\text{put}} = N(d_1) - 1 = -N(-d_1)$$

A delta-hedged portfolio $\Pi$ consisting of one long call and $-\Delta$ shares:

$$\Pi = V - \Delta \cdot S$$

Its value changes as:

$$d\Pi = dV - \Delta \, dS = \left(\Theta + \tfrac{1}{2}\Gamma \sigma^2 S^2\right)dt$$

The stochastic $dW$ term cancels — leaving a deterministic equation. Setting $d\Pi = r\Pi \, dt$ then yields the **Black-Scholes PDE**.

**Gamma** ($\Gamma = \partial^2 V / \partial S^2$) measures the rate of change of delta and determines how frequently the hedge must be rebalanced:

$$\Gamma_{\text{call}} = \frac{N'(d_1)}{S \, \sigma \sqrt{T}}$$

## Example

A trader is long one call with $\Delta = 0.60$ and $\Gamma = 0.04$. To delta-hedge, they **sell 0.60 shares** per option.

If $S$ rises by £2:
- Option gains: $\approx 0.60 \times 2 + \tfrac{1}{2} \times 0.04 \times 4 = £1.28$
- Stock hedge loses: $0.60 \times 2 = £1.20$
- Net $\Gamma$ profit: $\approx$ **£0.08** per option

This residual gain (long gamma) is offset by theta (time decay) — the two are in perpetual tension.

## Remember

- A long option position is **long gamma, short theta**: it benefits from large moves but bleeds value over time. A short option is the reverse.
- Continuous delta hedging is the theoretical foundation of the Black-Scholes derivation, but in practice hedges are rebalanced **discretely**, introducing **hedging error** that increases with gamma.
- Market makers who sell options and delta-hedge are effectively selling volatility: they profit if realised volatility is below the implied volatility at which they sold. This is called **short volatility** trading.
