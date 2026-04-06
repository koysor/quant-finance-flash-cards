# Hat, Bar, and Tilde Notation

**Topic:** Mathematical Notation
**Tags:** notation, estimator, hat, bar, tilde, sample mean, adjusted, approximation
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

Accents placed above a letter modify its meaning in a standard way across statistics and finance:

| Accent | Symbol | Convention | Finance example |
|---|---|---|---|
| Hat $\hat{\phantom{x}}$ | $\hat{\theta}$ | Estimated or fitted value | $\hat{\beta}$ — OLS slope estimate |
| Bar $\bar{\phantom{x}}$ | $\bar{x}$ | Sample mean or time average | $\bar{r}$ — average return |
| Tilde $\tilde{\phantom{x}}$ | $\tilde{X}$ | Transformed, risk-adjusted, or approximate quantity | $\tilde{S}_t = S_t / B_t$ — discounted price |
| Check $\check{\phantom{x}}$ | $\check{V}$ | Predicted / model value (rare) | Model price vs market price |

## Key Formula

**Sample mean** (bar notation):

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**OLS fitted value** (hat notation):

$$\hat{y}_i = \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}, \qquad \hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{y}$$

**Discounted asset price** (tilde notation):

$$\tilde{S}_t = e^{-rt} S_t$$

Under the risk-neutral measure, $\tilde{S}_t$ is a martingale.

## Example

In the Capital Asset Pricing Model:

$$R_i = \alpha + \hat{\beta}_i R_m + \varepsilon_i$$

Here $\hat{\beta}_i$ is the **estimated** beta (slope), computed from historical returns. The true (population) beta is $\beta_i$ — the hat signals estimation uncertainty. Residuals are $\hat{\varepsilon}_i = R_i - \hat{\alpha} - \hat{\beta}_i R_m$, always written with hats because they are fitted, not observed.

## Remember

The **tilde** is the notation workhorse for risk-neutral pricing: $\tilde{S}_t = e^{-rt} S_t$ is the discounted (numeraire-deflated) price process, and $\tilde{S}_t$ being a $\mathbb{Q}$-martingale is the fundamental theorem of asset pricing expressed in one symbol. The distinction between $S_t$ (undiscounted, real-world dynamics) and $\tilde{S}_t$ (discounted, risk-neutral martingale) is one of the most important conceptual divides in derivatives pricing — the tilde encodes the entire change-of-measure argument in a single accent.
