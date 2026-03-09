# Calmar Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** calmar ratio, maximum drawdown, risk-adjusted return, hedge funds, performance, trend following
**Author:** Claude Opus 4.6

---

## Definition

The Calmar ratio is a risk-adjusted performance measure that divides the annualised rate of return by the maximum drawdown over the same period (typically three years). Unlike the Sharpe ratio, which uses volatility as its risk denominator, the Calmar ratio penalises the worst peak-to-trough loss — making it particularly informative for strategies where drawdown discipline matters more than day-to-day volatility.

## Key Formula

$$\text{Calmar} = \frac{\bar{R}_{\text{annual}}}{\text{MDD}}$$

where $\bar{R}_{\text{annual}}$ is the compound annualised return and $\text{MDD}$ is the maximum drawdown over the measurement period.

Some practitioners use excess return over the risk-free rate in the numerator:

$$\text{Calmar}_{\text{excess}} = \frac{\bar{R}_{\text{annual}} - R_f}{\text{MDD}}$$

## Example

A trend-following fund delivers a compound annualised return of 14% over three years. During that period, its worst peak-to-trough drawdown was 18%:

$$\text{Calmar} = \frac{0.14}{0.18} = 0.78$$

A second fund returns 10% with a maximum drawdown of 8%:

$$\text{Calmar} = \frac{0.10}{0.08} = 1.25$$

Despite lower absolute returns, the second fund has a superior Calmar ratio — it delivered each unit of return with less drawdown pain. A Calmar ratio above 1.0 means the annualised return exceeded the worst drawdown.

## Remember

The Calmar ratio is the preferred metric for managed futures and trend-following strategies (CTAs), where returns can be lumpy and volatility is a poor proxy for risk. An investor who experienced a 40% drawdown may never recover psychologically, even if the strategy's Sharpe ratio looks attractive. By anchoring risk to the actual worst-case loss rather than a statistical average, the Calmar ratio captures what matters most to real investors: the maximum pain they must endure to earn their returns.
