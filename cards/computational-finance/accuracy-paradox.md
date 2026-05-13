# Accuracy Paradox

**Topic:** Computational Finance
**Tags:** accuracy paradox, class imbalance, precision, recall, credit risk, classification
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **accuracy paradox** occurs when raw accuracy is a misleading performance metric for a classifier because the class distribution is highly imbalanced. A model that predicts the majority class for every observation achieves high accuracy whilst providing no predictive value whatsoever.

## Key Formula

For a dataset with 99% majority class (e.g. non-default) and 1% minority class (default):

$$\text{Accuracy of trivial classifier} = \frac{TN}{TN + FP + FN + TP} = \frac{990}{1000} = 99\%$$

Yet this classifier has $TP = 0$, meaning Recall $= 0$ and F1 $= 0$. The paradox: 99% accurate, zero useful predictions.

**Alternative metrics that resist the paradox:**

| Metric | Formula | What it measures |
|---|---|---|
| Recall | $TP / (TP+FN)$ | Fraction of actual positives found |
| Precision | $TP / (TP+FP)$ | Fraction of positive predictions correct |
| F1 Score | $2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision}+\text{Recall}}$ | Harmonic mean of both |
| ROC-AUC | Area under ROC curve | Rank ordering across all thresholds |

## Example

A fraud detection model applied to 10,000 transactions: 9,900 legitimate, 100 fraudulent. A trivial "always legitimate" classifier scores 99% accuracy. A genuine fraud detector catches 90 of the 100 frauds (TP=90) with 50 false alarms (FP=50): Accuracy 99.4%, but Recall 90%, Precision 64%, F1 75%. The F1 score distinguishes the useful model from the trivial one; accuracy cannot.

## Remember

Class imbalance is endemic in quantitative finance: defaults are rare, fraud is rare, and market crashes are rare. Accuracy is therefore almost always the wrong metric for financial classification models. Practitioners report Recall (to minimise missed defaults), Precision-Recall curves (to understand the trade-off at different thresholds), and AUC (for threshold-independent ranking) — matching the metric to the asymmetric cost of False Negatives versus False Positives in the specific application.
