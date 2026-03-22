# Implied vs Realised Volatility

**Topic:** Volatility
**Tags:** implied volatility, realised volatility, variance risk premium, volatility trading, options
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The relationship between **implied volatility** (the market's forward-looking expectation embedded in option prices) and **realised volatility** (the backward-looking measure of actual price moves) is central to volatility trading. The difference between the two — the **variance risk premium** — reflects the compensation investors demand for bearing volatility risk. Empirically, implied volatility exceeds realised volatility on average, meaning option sellers are systematically compensated for providing insurance.

## Key Formula

The **variance risk premium** (VRP) is defined as:

$$\text{VRP} = \sigma_{\text{impl}}^2 - \sigma_{\text{real}}^2$$

A positive VRP means options are, on average, overpriced relative to the volatility that materialises. The profit and loss from delta-hedging a long option position is approximately:

$$P\&L \approx \frac{1}{2} \Gamma S^2 \left(\sigma_{\text{real}}^2 - \sigma_{\text{impl}}^2\right) \, T$$

This shows that a delta-hedged long option position profits when realised volatility exceeds implied, and loses when it does not.

## Example

A trader buys a 3-month ATM call on a stock at 22% implied volatility. Over the life of the option, the stock realises 18% volatility.

$$\text{VRP} = 0.22^2 - 0.18^2 = 0.0484 - 0.0324 = 0.0160$$

In volatility points: $\sqrt{0.0484} - \sqrt{0.0324} = 22\% - 18\% = 4\%$.

The trader paid for 22% vol but only received 18% vol — the delta-hedged position loses money. The 4-point gap represents the variance risk premium captured by the option seller.

## Remember

The implied-vs-realised spread is the fundamental profit engine for systematic volatility strategies. Selling options (short vol) is profitable on average because implied persistently exceeds realised, but this strategy carries significant tail risk — during market crashes, realised volatility spikes far above implied, generating large losses for sellers. This asymmetry explains why the VRP exists: it is compensation for bearing crash risk. The VIX index, which measures S&P 500 implied volatility, almost always trades above subsequent realised volatility, making the VRP one of the most robust risk premia in finance.
