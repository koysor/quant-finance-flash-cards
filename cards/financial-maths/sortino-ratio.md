# Sortino Ratio

**Topic:** Financial Mathematics
**Tags:** sortino ratio, downside risk, risk-adjusted return, semi-deviation, performance
**Author:** Claude Opus 4.6

---

## Definition

The Sortino ratio is a risk-adjusted performance measure that modifies the Sharpe ratio by replacing total volatility with **downside deviation** — the volatility of returns that fall below a target or minimum acceptable return (MAR). This penalises only harmful volatility (losses) rather than all volatility, making it a better measure for strategies with asymmetric return profiles.

## Key Formula

$$\text{Sortino} = \frac{\bar{R}_p - R_{\text{MAR}}}{\sigma_d}$$

where $R_{\text{MAR}}$ is the minimum acceptable return (often the risk-free rate) and $\sigma_d$ is the **downside deviation**:

$$\sigma_d = \sqrt{\frac{1}{n} \sum_{t=1}^{n} \left[\min(R_{p,t} - R_{\text{MAR}},\, 0)\right]^2}$$

Note that periods where $R_{p,t} > R_{\text{MAR}}$ contribute zero to the sum — only underperformance counts.

## Example

A fund has monthly returns (%) of: 3, $-1$, 5, $-2$, 4, 1 over six months. The monthly MAR is 0.25% (3% annualised ÷ 12):

Shortfalls below MAR: $\min(-1 - 0.25, 0) = -1.25$, $\min(-2 - 0.25, 0) = -2.25$. The other months contribute zero.

$$\sigma_d = \sqrt{\frac{(-1.25)^2 + (-2.25)^2}{6}} = \sqrt{\frac{1.5625 + 5.0625}{6}} = \sqrt{1.104} = 1.05\%$$

Mean monthly return $= 1.67\%$:

$$\text{Sortino} = \frac{1.67 - 0.25}{1.05} = 1.35$$

Compare to the Sharpe ratio using total volatility ($\sigma = 2.73\%$): $S = \frac{1.67 - 0.25}{2.73} = 0.52$. The Sortino ratio is much higher because the upside volatility (the large positive months) is not penalised.

## Remember

The Sortino ratio addresses a fundamental flaw in the Sharpe ratio: treating upside and downside volatility as equally undesirable. For hedge fund strategies that have positive skew — such as trend-following or options selling with protective hedges — the Sharpe ratio understates risk-adjusted performance by penalising large gains. The Sortino ratio is increasingly preferred by sophisticated investors and is particularly informative when comparing strategies with different return distributions, because it focuses on what investors actually fear: losing money.
