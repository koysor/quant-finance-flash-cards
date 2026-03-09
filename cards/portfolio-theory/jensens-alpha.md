# Jensen's Alpha

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** jensens alpha, capm, regression, excess return, performance attribution, active management
**Author:** Claude Opus 4.6

---

## Definition

Jensen's alpha is the intercept from regressing a portfolio's excess returns on the market's excess returns. It measures the average return earned above (or below) what the Capital Asset Pricing Model predicts for the portfolio's level of systematic risk. A statistically significant positive alpha indicates genuine skill; a negative alpha indicates the manager destroyed value relative to a passive beta exposure.

## Key Formula

The regression model is:

$$R_{p,t} - R_f = \alpha + \beta (R_{m,t} - R_f) + \epsilon_t$$

where $\alpha$ is Jensen's alpha, $\beta$ is the portfolio's sensitivity to the market, and $\epsilon_t$ is the residual. The alpha is:

$$\alpha = \overline{(R_p - R_f)} - \beta \cdot \overline{(R_m - R_f)}$$

Statistical significance is tested using the $t$-statistic:

$$t_\alpha = \frac{\hat{\alpha}}{\text{SE}(\hat{\alpha})}$$

## Example

A fund has an average monthly excess return of 0.8%. The market's average monthly excess return is 0.5%, and the fund's estimated beta is 1.2:

$$\alpha = 0.8\% - 1.2 \times 0.5\% = 0.8\% - 0.6\% = 0.2\% \text{ per month}$$

Annualised: $\alpha_{\text{annual}} = 0.2\% \times 12 = 2.4\%$.

If the standard error of $\hat{\alpha}$ is 0.09% per month:

$$t_\alpha = \frac{0.2}{0.09} = 2.22$$

With a $t$-statistic above 2, the alpha is statistically significant at the 5% level — there is evidence of genuine outperformance beyond market exposure.

## Remember

Jensen's alpha is the statistical test behind the claim that a fund manager has skill. Unlike raw outperformance, it adjusts for market risk — a fund that returns 15% when the market returns 10% has not necessarily generated alpha if its beta is 1.5 (the CAPM would predict exactly 15%). In practice, alpha estimates are noisy and require long track records to achieve significance, which is why many quantitative researchers argue that three to five years of data is the minimum needed to distinguish skill from luck.
