# Information Coefficient

**Topic:** Computational Finance
**Tags:** information coefficient, hit ratio, signal evaluation, alpha, active management, ic ir
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Information Coefficient (IC)** is the Spearman or Pearson correlation between a model's predicted returns and the subsequently realised returns. It measures the directional accuracy and magnitude alignment of a signal. The **Hit Ratio** (Success Rate) is the fraction of predictions where the predicted sign matches the realised sign — a simpler, direction-only measure of signal skill.

## Key Formula

$$\text{IC} = \text{corr}(\hat{r}_{t+h},\, r_{t+h}), \qquad \text{IC} \in [-1, 1]$$

$$\text{Hit Ratio} = \frac{\#\{i : \text{sign}(\hat{r}_i) = \text{sign}(r_i)\}}{N}$$

| IC | Interpretation |
|---|---|
| $> 0.05$ | Useful signal |
| $> 0.10$ | Strong signal (rare in practice) |
| $< 0$ | Reverse-direction prediction |

The IC feeds directly into the **Fundamental Law of Active Management**:
$$\text{IR} \approx \text{IC} \times \sqrt{\text{Breadth}}$$

A signal with IC $= 0.05$ applied across 500 stocks annually produces IR $\approx 0.05 \times \sqrt{500} \approx 1.12$.

## Example

An ML model predicts next-month equity returns for 200 stocks. Over 36 months: mean IC $= 0.06$, IC volatility $= 0.15$, IC $t$-statistic $= 0.06 / (0.15/\sqrt{36}) = 2.4$ — statistically significant. Hit Ratio $= 54\%$. MSE is low but misleading (dominated by market moves); IC and Hit Ratio confirm the model has genuine cross-sectional signal.

## Remember

IC is preferred over MSE for evaluating financial forecasting models because it measures what matters commercially: the rank ordering of predicted returns relative to actual returns. A model that predicts magnitude poorly but direction consistently (IC $= 0.06$, Hit Ratio $= 54\%$) is highly valuable in a long-short equity strategy, where only relative return rank determines portfolio construction. Reporting the IC $t$-statistic ($= \text{IC} \times \sqrt{T} / \sigma_{\text{IC}}$) is essential since a high mean IC over a short horizon can be statistically indistinguishable from zero.
