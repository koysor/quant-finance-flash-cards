# Daily Price Limits

**Topic:** Computational Finance
**Tags:** daily price limits, market microstructure, regulatory constraints, non-markovian, option pricing
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Daily price limits (DPL)** are regulatory rules that prevent an asset's price from moving beyond a fixed percentage band relative to the previous session's closing price. Common in Asian and emerging-market exchanges (e.g. China, South Korea, Taiwan), they create a **stochastic corridor** within which the price must remain each trading day, breaking standard diffusion model assumptions.

## Key Formula

The corridor for trading day $n$ is:

$$[L_n, U_n] = \bigl[S_{t_{n-1}}(1 - \alpha),\; S_{t_{n-1}}(1 + \beta)\bigr]$$

where $S_{t_{n-1}}$ is the previous day's closing price and $\alpha, \beta$ are the downside and upside limit fractions (e.g. $\alpha = \beta = 0.10$ for a ±10% rule). The corridor resets daily, so tomorrow's boundaries depend on today's close — introducing **path dependence**.

## Example

A stock closes at £100. The next day's corridor is [£90, £110] under a ±10% rule. A call with strike £105 can still expire in the money, but if the stock hits £110 at the open and the boundary is absorbing, further upside is cut off. Black-Scholes prices this call as though the stock could reach £130 — it therefore overprices the call by an amount measured by the **price limit effect**.

## Remember

DPLs make the return distribution **non-Markovian** (tomorrow's corridor depends on today's close, not just the instantaneous price), break continuous no-arbitrage conditions, and produce log-return distributions with truncated tails or spikes at ±$\alpha, \beta$. Black-Scholes prices are systematically biased when limits are active — RL models such as TDBP capture constrained dynamics automatically by training on corridor-restricted paths without requiring a modified SDE.
