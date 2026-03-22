# Option Payoff Diagrams

**Topic:** Derivatives
**Tags:** options, payoff, profit and loss, call option, put option, strategy
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

An **option payoff diagram** plots the option's value (or profit/loss) at expiry against the underlying asset price $S_T$. Payoff diagrams make the asymmetric, non-linear nature of options immediately visible and are the standard tool for analysing single-leg and multi-leg option strategies.

## Key Formula

**Long call** payoff at expiry:

$$\text{Payoff} = \max(S_T - K, \; 0)$$

$$\text{Profit} = \max(S_T - K, \; 0) - C_0$$

**Long put** payoff at expiry:

$$\text{Payoff} = \max(K - S_T, \; 0)$$

$$\text{Profit} = \max(K - S_T, \; 0) - P_0$$

where $C_0$ and $P_0$ are the premiums paid. The **break-even** prices are:

- Long call: $S_T = K + C_0$
- Long put: $S_T = K - P_0$

## Example

A trader buys a European call with $K = £100$ for a premium of $C_0 = £5$.

| $S_T$ | Payoff | Profit |
|---|---|---|
| £90 | £0 | $-$£5 |
| £100 | £0 | $-$£5 |
| £105 | £5 | £0 (break-even) |
| £115 | £15 | £10 |

The diagram is flat at $-$£5 for $S_T \le 100$, then rises at 45° — unlimited upside, capped downside.

## Remember

Payoff diagrams reveal the fundamental asymmetry that makes options valuable: the buyer's loss is capped at the premium, while the potential gain is theoretically unlimited (calls) or substantial (puts, down to zero). In quantitative finance, combining payoff diagrams graphically is how traders construct and analyse strategies such as spreads, straddles, and collars — the combined P&L is simply the vertical sum of the individual legs.
