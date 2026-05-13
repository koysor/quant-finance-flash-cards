# Scikit-Learn

**Topic:** Computational Finance
**Tags:** scikit-learn, machine learning, python, model selection, cross-validation, pipeline
**Created:** 2026-04-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Scikit-Learn** is Python's standard machine learning library, providing consistent `fit`/`predict`/`transform` interfaces for algorithms spanning classification, regression, clustering, and dimensionality reduction. Its `Pipeline` and `GridSearchCV` utilities allow end-to-end model construction and hyperparameter optimisation in a few lines of code. In quantitative finance it is the default toolkit for traditional ML tasks such as credit scoring, return prediction, and factor selection.

## Key Formula

**Cross-validated generalisation score** for model selection:

$$\hat{R}(f) = \frac{1}{K} \sum_{k=1}^{K} \mathcal{L}\!\left(f_{\mathcal{D} \setminus \mathcal{D}_k},\; \mathcal{D}_k\right)$$

where $K$ is the number of folds, $\mathcal{D}_k$ is the $k$-th held-out fold, and $\mathcal{L}$ is the chosen loss function. The model trained on $\mathcal{D} \setminus \mathcal{D}_k$ is evaluated on $\mathcal{D}_k$; averaging across all $K$ folds estimates generalisation error on unseen data.

## Example

Predicting loan default using a random forest:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    RandomForestClassifier(n_estimators=200, random_state=42)),
])

scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring="roc_auc")
print(f"Mean AUC: {scores.mean():.3f} ± {scores.std():.3f}")
# Mean AUC: 0.832 ± 0.014
```

An AUC of 0.832 means the model correctly ranks a defaulting borrower above a non-defaulting one 83.2% of the time across five held-out folds.

## Remember

Scikit-Learn's consistent interface means a credit scoring model and a volatility regime detector share identical boilerplate — only the algorithm name changes, letting a quant compare a dozen classifiers on the same feature matrix in an afternoon. The `Pipeline` object is critical for preventing **data leakage**: wrapping the scaler inside the pipeline ensures that feature means and variances are computed only on training folds, not the held-out fold. This mistake — fitting the scaler on all data before splitting — is among the most common causes of inflated backtest performance in published financial ML research.
