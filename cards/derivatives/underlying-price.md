# Underlying Price

**Topic:** Derivatives
**Tags:** underlying, spot price, derivatives, options, futures
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **underlying price** (or spot price) is the current market price of the asset on which a derivative contract is written. It is the most important input to any option or futures pricing model because the derivative's value is, by definition, derived from this price. In standard notation, $S$ (or $S_t$) denotes the underlying price at time $t$.

## Key Formula

The payoff of a European call option at expiry depends directly on the underlying price:

$$\text{Call payoff} = \max(S_T - K, \; 0)$$

$$\text{Put payoff} = \max(K - S_T, \; 0)$$

where $S_T$ is the underlying price at expiry and $K$ is the strike price. Under geometric Brownian motion, the underlying price evolves as:

$$dS = \mu S \, dt + \sigma S \, dW$$

where $\mu$ is the drift rate, $\sigma$ is the volatility, and $dW$ is a Wiener increment.

## Example

A trader holds a European call option with strike $K = 100$. At expiry, the underlying share price is $S_T = 108$.

$$\text{Payoff} = \max(108 - 100, \; 0) = £8$$

If the option premium paid was £3, the net profit is $£8 - £3 = £5$ per share. Had the underlying price finished at $S_T = 97$, the payoff would be zero and the trader would lose the £3 premium.

## Remember

Every derivative pricing model — Black-Scholes, binomial trees, Monte Carlo simulation — takes the underlying price as its central input. A one-unit change in $S$ shifts the option value by approximately $\Delta$ (delta), making the underlying price the single largest driver of day-to-day profit and loss on any options book. In practice, traders continuously monitor the underlying price to manage delta exposure and decide when to rebalance hedges.
