# Portfolio Weights

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** portfolio weights, budget constraint, short selling, leverage, allocation
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Portfolio weights** express each asset's share of total portfolio value. They are the fundamental language of portfolio construction — every allocation decision is a choice of weights, and the budget constraint requires them to sum to one.

$$w_i = \frac{\text{Market Value of Asset } i}{\text{Total Portfolio Value}}$$

## Key Formula

**Budget constraint** (the defining constraint of any portfolio):

$$\sum_{i=1}^{N} w_i = 1 \qquad \Longleftrightarrow \qquad \mathbf{w}^\top \mathbf{1}_N = 1$$

| Weight range | Interpretation |
|---|---|
| $0 < w_i < 1$ | Long position (own the asset) |
| $w_i < 0$ | Short position (borrow and sell) |
| $w_i > 1$ | Leveraged long (borrow to buy more) |
| $w_i = 0$ | Asset excluded from portfolio |

## Example

A portfolio worth £100,000 holds £60,000 in equities, £30,000 in bonds, and £10,000 in cash:

$$w_{\text{eq}} = 0.60, \quad w_{\text{bond}} = 0.30, \quad w_{\text{cash}} = 0.10$$

$$w_{\text{eq}} + w_{\text{bond}} + w_{\text{cash}} = 1.00 \checkmark$$

A long-short hedge fund holds 130% in longs and −30% in shorts: $0.30 - (-0.30)... $ wait — weights still sum to 1: $1.30 + (-0.30) = 1.00 \checkmark$

## Remember

The budget constraint $\sum w_i = 1$ is the single equation that turns any collection of assets into a portfolio. Short weights ($w_i < 0$) and leverage ($w_i > 1$) are both permitted — they just shift some weights outside $[0, 1]$ while preserving the sum. In matrix form, $\mathbf{w}^\top \mathbf{1} = 1$ is the constraint that every MVO optimisation must satisfy alongside the target return condition.
