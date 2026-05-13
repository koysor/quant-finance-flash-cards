# Data Normalisation

**Topic:** Computational Finance
**Tags:** normalisation, standardisation, min-max scaling, log transform, feature scaling, preprocessing
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Data normalisation** (or feature scaling) transforms raw input variables onto a common numerical scale before feeding them into a machine learning model. Without it, features with larger magnitudes dominate distance calculations and gradient updates, causing biased coefficient estimates and slow convergence.

## Key Formula

**Standardisation (Z-score)** — centres to zero mean, unit variance:
$$x' = \frac{x - \hat{\mu}}{\hat{\sigma}}$$

**Min-max scaling** — compresses to $[0, 1]$:
$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

**Log transform** — compresses right-skewed distributions:
$$x' = \ln(x), \quad x > 0$$

| Algorithm | Scaling needed? | Reason |
|---|---|---|
| Ridge, LASSO, KNN, SVM | Yes | Distance / penalty is magnitude-sensitive |
| Decision trees, XGBoost | No | Split-based, scale-invariant |
| Neural networks | Yes | Gradient steps depend on input scale |

## Example

A credit model uses two features: income ($\£$50,000) and debt-to-income ratio (0.35). Without scaling, the model's gradient steps are dominated by the income feature because it is 100,000× larger numerically. After Z-score standardisation: income $\approx 0$ (mean removed, unit std), DTI $\approx 0$ — Ridge regression now penalises both coefficients equally per unit of predictive variance.

## Remember

In quantitative finance, standardisation must always be fitted on the training set and applied — without refitting — to the validation and test sets. Fitting the scaler on the full dataset before splitting is a form of look-ahead bias: the scaler learns mean and standard deviation from future observations, leaking future statistical properties into the training process. Scikit-learn pipelines with `Pipeline([('scaler', StandardScaler()), ('model', Ridge())])` enforce this correctly by design.
