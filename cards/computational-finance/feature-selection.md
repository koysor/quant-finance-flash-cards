# Feature Selection

**Topic:** Computational Finance
**Tags:** feature selection, filter methods, wrapper methods, embedded methods, overfitting, factor model
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Feature selection** identifies the most informative subset of input variables for a predictive model, reducing noise, limiting overfitting, and improving interpretability. The three families of methods differ in whether they assess features independently of the model, use model performance as the scoring criterion, or integrate selection into the training process.

## Key Formula

| Family | Scoring mechanism | Examples |
|---|---|---|
| **Filter** | Statistical test on $X_j$ alone | Pearson correlation, mutual information, $F$-test |
| **Wrapper** | CV error of model trained on subset $S$ | Recursive Feature Elimination (RFE), forward selection |
| **Embedded** | Penalty during model training | LASSO ($\ell_1$), Random Forest importance, gradient boosting |

**Filter score** (correlation): $\rho_j = \text{corr}(X_j, y)$ — fast, model-agnostic, ignores feature interactions.

**Embedded** (LASSO) solution automatically zeros irrelevant coefficients: $\hat{w}_j = 0$ when $|\partial J/\partial w_j|_{\lambda} \leq \lambda$.

## Example

A quant tests 120 candidate signals for predicting next-month equity returns. **Filter stage**: discard 70 with $|\rho| < 0.05$. **Wrapper stage**: apply recursive feature elimination on the remaining 50, removing features until cross-validated $R^2$ stops improving — leaves 25. **Embedded stage**: fit LASSO on the 25; 10 coefficients shrink to zero, leaving 15 retained signals for the final model.

## Remember

Feature selection is essential in quantitative finance because financial data is low signal-to-noise by nature — adding irrelevant signals inflates in-sample performance whilst destroying out-of-sample alpha. In practice, filter methods (correlation screens) act as a cheap first pass to shrink the candidate universe, whilst embedded LASSO performs fine selection during estimation. This two-stage pipeline replicates the systematic process that top factor research desks use to separate genuine alpha signals from spurious ones.
