# Limitations of VaR

**Topic:** Risk
**Tags:** var, limitations, subadditivity, tail risk, model risk, coherent risk measure
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Value at Risk (VaR)** is a threshold measure, not a worst-case measure. It answers "what is the most I can lose 99% of the time?" but says nothing about the size of losses in the remaining 1%.

Six key limitations practitioners must understand:

1. **History ≠ future** — historical simulation uses past returns; unprecedented regimes (e.g. negative oil prices) lie outside the training window.
2. **Unusual conditions underweighted** — short look-back windows or equally-weighted histories give crises (2008 Lehman collapse, March 2020 COVID) little influence on today's estimate.
3. **Non-linear payoffs poorly captured** — parametric VaR assumes a linear P&L. Options require at least a delta–gamma correction; even then, the approximation breaks down for large moves.
4. **Liquidity assumption** — VaR assumes positions can be closed at mid-market over the holding period. In a crisis, bid–offer spreads widen and markets dry up entirely.
5. **Gap risk** — VaR models continuous price movements. Overnight sovereign defaults or circuit breakers produce jump discontinuities that the model does not anticipate.
6. **Not coherent** — VaR violates the subadditivity axiom: combining two portfolios can produce a higher VaR than the sum of the individual VaRs, penalising diversification.

## Key Formula

**Subadditivity failure — a concrete counter-example.**

Consider two single-bond portfolios $A$ and $B$, each with face value £100. Each bond defaults independently with probability $p = 2\%$; loss-given-default is 100%.

$$\text{95\% VaR}(A) = 0, \qquad \text{95\% VaR}(B) = 0$$

Because $P(\text{loss} > 0) = 2\% < 5\%$, neither bond individually breaches the 95% VaR threshold — so standalone VaR is zero for each.

Now consider the combined portfolio $A + B$. A loss occurs if **either** bond defaults:

$$P(\text{at least one default}) = 1 - (1 - 0.02)^2 = 3.96\%$$

Since $3.96\% < 5\%$, the combined portfolio also has £0 loss at the 95th percentile — wait, not quite. The combined notional is £200 and the combined loss-at-default events is:

| Event | Probability | Loss |
|---|---|---|
| Neither defaults | 96.04% | £0 |
| Only $A$ defaults | 1.96% | £100 |
| Only $B$ defaults | 1.96% | £100 |
| Both default | 0.04% | £200 |

The 95th-percentile loss of $A + B$ corresponds to the scenarios beyond the top 5%. Cumulating from the worst: $P(\text{loss} \geq £100) = 1.96 + 1.96 + 0.04 = 3.96\% < 5\%$, so 95% VaR($A+B$) = £0.

Now raise confidence to **99%**. $P(\text{loss} \geq £100) = 3.96\% > 1\%$, so:

$$\text{99\% VaR}(A) = 0, \qquad \text{99\% VaR}(B) = 0$$

$$\text{99\% VaR}(A + B) = £100$$

$$\boxed{\text{VaR}(A+B) = £100 \;>\; £0 + £0 = \text{VaR}(A) + \text{VaR}(B)}$$

Subadditivity is violated. Merging two portfolios appears riskier than holding them separately — diversification is penalised.

**Expected Shortfall (ES/CVaR) is coherent** and always satisfies $\text{ES}(A+B) \leq \text{ES}(A) + \text{ES}(B)$, which is why FRTB replaced 99% VaR with 97.5% ES.

## Example

**JP Morgan's London Whale (2012).** Bruno Iksil's synthetic credit portfolio at JP Morgan's Chief Investment Office accumulated positions whose tail risk was masked by VaR. The desk switched to a VaR model that used shorter historical windows and smoother correlations, which mechanically reduced reported VaR by approximately 50% even as the actual position size grew. When markets moved against the trades, the realised loss reached $6.2 billion — far beyond anything the revised VaR indicated. The episode illustrates limitations 1, 2, and 3 simultaneously: the model used favourable recent history, understated non-linear credit-index payoffs, and gave management a false sense of security.

## Remember

VaR is a regulatory convenience, not a complete risk picture. The six limitations cluster into three themes:

- **Data problems** (history, unusual conditions) — garbage in, garbage out.
- **Model problems** (non-linearity, liquidity, gap risk) — the maths doesn't match reality.
- **Axiomatic failure** (non-coherent) — VaR can actively mis-rank portfolios.

The London Whale and 2008 crisis both showed that institutions relying solely on VaR were blindsided. **Expected Shortfall** corrects the coherence failure and forces attention on the severity of tail losses, not just their probability.
