# Recursive Feature Elimination (RFE)

**Topic:** Computational Finance
**Tags:** recursive feature elimination, feature selection, wrapper method, factor model, linear model, svm
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Recursive Feature Elimination (RFE)** is a wrapper-based feature selection method that fits a model on the full feature set, removes the least important feature (or batch of features), retrains, and repeats until the desired number of features remains. Importance is measured by the model's own internal ranking — typically coefficient magnitude for linear models, or feature weights for SVMs.

## Key Formula

Given $p$ features and a target count $k$, RFE iterates:

$$\hat{\mathbf{w}}^{(t)} = \arg\min_{\mathbf{w}} J(\mathbf{w};\, \mathcal{F}^{(t)}), \quad \mathcal{F}^{(t+1)} = \mathcal{F}^{(t)} \setminus \left\{\arg\min_{j \in \mathcal{F}^{(t)}} |\hat{w}_j^{(t)}|\right\}$$

until $|\mathcal{F}^{(t)}| = k$. With cross-validation (**RFECV**), each candidate feature set is scored by out-of-fold performance, and the optimal $k$ is selected automatically rather than specified in advance.

## Example

A quant tests 80 candidate alpha signals for one-month equity return prediction. RFE with a Ridge regression estimator: fit on all 80, drop the 10 signals with smallest $|\hat{w}_j|$, refit on 70, repeat. After 14 iterations, 10 signals remain. RFECV — running each subset through 5-fold time-series CV — confirms 12 signals maximise out-of-sample $R^2$, preventing the manual $k$-specification error of stopping too early or too late.

## Remember

RFE is the canonical wrapper method in quantitative finance because it integrates the model's own fit into the elimination decision — unlike filter methods that assess signals in isolation, RFE accounts for redundancy between factors. When combined with an SVM or Ridge estimator and time-series cross-validation (RFECV), it simultaneously selects signals and tunes the feature count, mimicking the systematic signal-culling process used by factor research desks. Scikit-learn's `RFECV` class makes this a one-line operation.
