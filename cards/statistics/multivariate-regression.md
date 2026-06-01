# Multivariate Regression

**Topic:** Statistics
**Tags:** regression, multiple predictors, factor model, adjusted R-squared, partial slope
**Created:** 2026-05-30
**Author:** Claude Sonnet 4.6

---

## Definition

**Multivariate regression** (or multiple regression) extends the linear model to $k > 1$ predictors, fitting $\hat{y}_i = \hat{\alpha} + \hat{\beta}_1 x_{1i} + \cdots + \hat{\beta}_k x_{ki}$ via OLS. Each coefficient $\hat{\beta}_j$ is a **partial slope**: the expected change in $y$ for a one-unit increase in $x_j$ with all other predictors held constant.

## Key Formula

The model in compact notation:

$$y_i = \alpha + \sum_{j=1}^{k} \beta_j x_{ji} + \varepsilon_i$$

Adjusted $R^2$ penalises for the number of predictors, preventing overfitting from adding irrelevant variables:

$$\bar{R}^2 = 1 - \frac{\text{RSS}/(n - k - 1)}{\text{TSS}/(n - 1)} = 1 - (1 - R^2)\frac{n - 1}{n - k - 1}$$

The F-statistic tests whether the model explains any variance at all (joint significance):

$$F = \frac{R^2 / k}{(1 - R^2)/(n - k - 1)}$$

## Example

A small-cap value fund is regressed on the Fama–French three factors (market, SMB, HML) using $n = 60$ monthly observations ($k = 3$):

$$r_i - r_f = 0.12\% + 1.10\,(r_m - r_f) + 0.65\,\text{SMB} + 0.45\,\text{HML} + \varepsilon_i$$

The fit gives $R^2 = 0.92$.

$$\bar{R}^2 = 1 - (1 - 0.92)\frac{59}{56} = 1 - 0.08 \times 1.054 = 0.916$$

$$F = \frac{0.92/3}{0.08/56} = \frac{0.307}{0.00143} \approx 215$$

The high F-statistic confirms that the three factors jointly explain the fund's returns far beyond chance; the market beta of 1.10 reflects modest leverage, while the positive SMB and HML loadings identify the fund's size and value tilts.

## Remember

Multivariate regression is the workhorse of quantitative factor investing. By regressing an asset's excess return on multiple factor returns simultaneously, you obtain factor exposures (betas) that are purged of the other factors — the market beta changes when you add SMB and HML because partial slopes isolate each factor's independent contribution. Adjusted $R^2$ is the practitioner's measure of fit: adding a spurious fifth factor can raise $R^2$ but will lower $\bar{R}^2$, flagging that the extra predictor adds noise rather than signal. An $F$-statistic below its critical value means the full factor set is not jointly significant — a red flag for any quantitative model.
