# Exotic Options

**Topic:** Derivatives
**Tags:** exotic options, path-dependent, barrier option, asian option, binary option, structured products
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An **exotic option** is any derivative whose payoff, exercise conditions, or underlying reference differs from a standard (vanilla) European or American call or put. Exotics fall into two broad families: **path-independent** exotics, whose payoff depends only on $S_T$ (e.g. binary, spread), and **path-dependent** exotics, whose payoff depends on the full price trajectory $\{S_t : 0 \leq t \leq T\}$ (e.g. Asian, barrier, lookback).

## Key Formula

| Type | Payoff |
|------|--------|
| Vanilla call (benchmark) | $\max(S_T - K,\; 0)$ |
| Binary call (cash-or-nothing) | $Q \cdot \mathbf{1}\{S_T > K\}$ |
| Asian call (arithmetic average) | $\max\!\left(\bar{S} - K,\; 0\right),\quad \bar{S} = \tfrac{1}{n}\sum_{i=1}^{n} S_{t_i}$ |
| Down-and-out barrier call | $\max(S_T - K,\; 0)\cdot \mathbf{1}\!\left\{\min_{0 \leq t \leq T} S_t > B\right\}$ |

where $K$ is the strike, $Q$ the cash payout, $B$ the knock-out barrier, and $\mathbf{1}\{\cdot\}$ is the indicator function.

## Example

A commodity trader buys an Asian call on WTI crude oil with strike $K = \$80$/bbl, $n = 3$ monthly fixings at \$82, \$84, and \$95. The arithmetic average is $\bar{S} = (82 + 84 + 95)/3 = \$87$/bbl, giving a payoff of $\max(87 - 80, 0) = \$7$/bbl. The equivalent vanilla call would have paid $\max(95 - 80, 0) = \$15$/bbl — the Asian option was cheaper to buy because averaging reduces the effective volatility.

## Remember

Exotic options dominate structured products and commodity markets because their payoffs align more closely with real business exposures than vanilla options do. A mining company's quarterly revenue tracks the average spot price over the period, not the closing price on a single day — so an Asian option is the natural hedge. Pricing exotics almost always requires numerical methods (Monte Carlo for path-dependent, finite-difference PDEs for barrier), and the resulting **model risk** is reflected in wide bid–offer spreads and dedicated model-risk reserves on bank trading desks.
