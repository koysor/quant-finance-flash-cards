# Maximum Entropy Portfolio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** maximum entropy, diversification, portfolio weights, information theory, equal risk contribution, entropy
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **maximum entropy portfolio** is the portfolio whose weight distribution has the highest Shannon entropy, subject to the constraints that weights are non-negative and sum to one. It formalises diversification as an information-theoretic principle: maximum entropy weights are those that encode the least information — the portfolio that makes the fewest assumptions about which assets will outperform.

## Key Formula

Shannon entropy of portfolio weights $\mathbf{w} = (w_1, \ldots, w_n)$:

$$H(\mathbf{w}) = -\sum_{i=1}^n w_i \ln w_i$$

The maximum entropy portfolio solves:

$$\max_{\mathbf{w}} \; H(\mathbf{w}) \quad \text{subject to} \quad \sum_i w_i = 1, \quad w_i \geq 0$$

The analytic solution is the **equal-weight portfolio**: $w_i^* = \frac{1}{n}$ for all $i$, achieving $H^* = \ln n$.

With an additional volatility constraint $\mathbf{w}^\top \boldsymbol{\sigma} = $ constant, the solution tilts towards lower-volatility assets — recovering a risk-parity-like allocation.

## Example

For $n = 4$ assets, the equal-weight portfolio $\mathbf{w} = (0.25, 0.25, 0.25, 0.25)$ achieves $H = \ln 4 \approx 1.386$ bits. A concentrated portfolio $(0.70, 0.10, 0.10, 0.10)$ achieves only $H \approx 0.93$ bits — it encodes more information (a specific view on asset 1). A fully concentrated portfolio $(1, 0, 0, 0)$ achieves $H = 0$ — it encodes a certainty that a single asset dominates, the least diversified possible portfolio.

## Remember

The maximum entropy portfolio is the information-theoretic justification for equal weighting and risk parity. In quantitative portfolio management, it answers the question "what is the most agnostic portfolio I can hold?" — the one that requires the fewest assumptions. This matters because return forecasts are notoriously unreliable: a manager with no genuine edge should hold the maximum entropy portfolio rather than tilting on noise. Practitioners use entropy as a diversification diagnostic — comparing $H(\mathbf{w}) / \ln n$ to 1.0 measures how much of the theoretical maximum diversification a portfolio achieves.
