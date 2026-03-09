# Sterling Ratio

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** sterling ratio, average drawdown, risk-adjusted return, hedge funds, performance, drawdown
**Author:** Claude Opus 4.6

---

## Definition

The Sterling ratio is a risk-adjusted performance measure that divides the annualised return by the average of the largest drawdowns over a specified period, rather than the single worst drawdown used by the Calmar ratio. This makes it less sensitive to a single extreme event and provides a more stable estimate of the return earned per unit of drawdown risk.

## Key Formula

The original Sterling ratio uses the average of the $k$ largest annual drawdowns (typically $k = 3$) minus an arbitrary 10% buffer:

$$\text{Sterling}_{\text{original}} = \frac{\bar{R}_{\text{annual}}}{\overline{\text{DD}}_k - 10\%}$$

The more common **modified Sterling ratio** drops the buffer:

$$\text{Sterling} = \frac{\bar{R}_{\text{annual}}}{\overline{\text{DD}}_k}$$

where $\overline{\text{DD}}_k = \frac{1}{k}\sum_{i=1}^{k} \text{DD}_i$ is the mean of the $k$ largest drawdowns.

## Example

A fund delivers an annualised return of 12% over three years. Its three largest drawdowns are 15%, 10%, and 8%:

$$\overline{\text{DD}}_3 = \frac{15 + 10 + 8}{3} = 11\%$$

$$\text{Sterling} = \frac{0.12}{0.11} = 1.09$$

Compare this to the Calmar ratio using only the worst drawdown:

$$\text{Calmar} = \frac{0.12}{0.15} = 0.80$$

The Sterling ratio is higher because it averages out the worst event. A fund with one anomalous large drawdown but otherwise good discipline will look better on Sterling than on Calmar.

## Remember

The Sterling ratio offers a middle ground between the Sharpe ratio (which ignores drawdowns entirely) and the Calmar ratio (which is dominated by a single worst case). For hedge fund due diligence, comparing Calmar and Sterling side by side reveals whether poor performance was a one-off or a pattern — if both ratios are low, the fund has a chronic drawdown problem; if Calmar is much worse than Sterling, a single event was the culprit and may be less likely to recur.
