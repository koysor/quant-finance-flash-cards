# CV AUC

**Topic:** Computational Finance
**Tags:** cv auc, cross-validation, model validation, credit scoring, gini, discriminatory power
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**CV AUC** is the mean AUC (Area Under the ROC Curve) computed across the held-out folds of a cross-validation procedure. It replaces a single train/test AUC with a stable, variance-reduced estimate of a classifier's discriminatory power, and its per-fold standard deviation measures how consistently the model performs across different data segments — in finance, different market regimes or economic cycles.

## Key Formula

For a $k$-fold cross-validation procedure, the CV AUC is:

$$\overline{\text{AUC}}_{\text{CV}} = \frac{1}{k}\sum_{j=1}^{k} \text{AUC}_j$$

where $\text{AUC}_j = P\!\left(s^+ > s^- \mid \text{fold } j\right)$ is the AUC of the model trained on all folds except $j$, evaluated on fold $j$.

The standard deviation across folds measures **regime stability**:

$$\sigma_{\text{AUC}} = \sqrt{\frac{1}{k-1}\sum_{j=1}^{k}\left(\text{AUC}_j - \overline{\text{AUC}}_{\text{CV}}\right)^2}$$

The result is reported as $\overline{\text{AUC}}_{\text{CV}} \pm \sigma_{\text{AUC}}$. A large $\sigma_{\text{AUC}}$ relative to $\overline{\text{AUC}}_{\text{CV}}$ signals regime-dependent performance.

## Example

A credit default model is evaluated using 5-fold time-series cross-validation over 10 years of loan data (each fold covers a 2-year window):

| Fold | Period | AUC |
|---|---|---|
| 1 | 2014–2015 | 0.83 |
| 2 | 2016–2017 | 0.85 |
| 3 | 2018–2019 | 0.84 |
| 4 | 2020–2021 | 0.71 |
| 5 | 2022–2023 | 0.82 |

$$\overline{\text{AUC}}_{\text{CV}} = 0.810, \qquad \sigma_{\text{AUC}} = 0.054$$

The high $\sigma_{\text{AUC}}$ flags Fold 4 (COVID shock) as a regime breakdown. Reporting only the mean would mask this instability.

## Remember

Regulatory model validation under IRB (Basel) and SR 11-7 (Federal Reserve) requires evidence of **through-the-cycle discriminatory power** — that the model works not just on average but across economic regimes. A CV AUC of $0.81 \pm 0.05$ is weaker evidence of robustness than $0.80 \pm 0.01$: the lower mean with tight standard deviation is often preferred because it signals a model that degrades predictably rather than catastrophically. When presenting credit model validation results, the fold-level AUC table is as important as the headline figure — regulators inspect individual folds to identify the specific periods where the model underperforms, and require documented explanations before approving the model for capital calculation.
