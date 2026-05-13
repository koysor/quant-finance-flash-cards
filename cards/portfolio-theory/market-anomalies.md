# Market Anomalies

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** anomalies, market efficiency, factor investing, momentum, value, size premium
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Market anomalies are patterns in asset returns that cannot be explained by standard asset pricing models and persist after controlling for known risk factors. They represent apparent violations of the Efficient Markets Hypothesis (EMH) — either because markets are genuinely inefficient, or because the anomaly proxies for a priced risk not captured by existing models.

## Key Formula

An anomaly is typically identified by a statistically significant **alpha** in a factor regression:

$$R_{i,t} - R_{f,t} = \alpha_i + \beta_i (R_{m,t} - R_{f,t}) + \gamma_i \text{SMB}_t + \delta_i \text{HML}_t + \varepsilon_{i,t}$$

A persistent $\alpha_i \neq 0$ after controlling for known factors (market, size, value) signals an anomaly. Common anomalies have their own factor representations:

- **Momentum:** $\text{UMD}_t$ (Up-Minus-Down; past 12-month winners minus losers)
- **Quality/Profitability:** $\text{RMW}_t$ (Robust-Minus-Weak operating profitability)
- **Low volatility:** long low-$\beta$ stocks, short high-$\beta$ stocks

## Example

The **momentum anomaly**: stocks in the top decile of 12-month returns (winners) outperform stocks in the bottom decile (losers) by approximately 1% per month over the following 6–12 months (Jegadeesh and Titman, 1993). This persists after market, size, and value adjustments. However, momentum also exhibits sharp reversals — momentum crashes — during market rebounds following crises, making it a risky strategy despite its average return.

## Remember

The "factor zoo" — over 400 published anomalies — reflects both genuine market inefficiencies and data-mining. The Fama-French five-factor model absorbs many anomalies by adding profitability and investment factors, arguing they reflect **risk** rather than mispricing. The key unresolved question in quantitative finance is whether anomaly returns are compensation for genuine economic risk (which can be diversified away) or evidence of persistent mispricing (which can be exploited).
