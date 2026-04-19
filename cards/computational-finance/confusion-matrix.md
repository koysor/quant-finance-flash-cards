# Confusion Matrix

**Topic:** Computational Finance
**Tags:** classification, precision, recall, accuracy, false positive, credit risk
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

A **confusion matrix** is a table that summarises the performance of a classification model by counting how many predictions fell into each of the four outcome cells: True Positive (TP), False Positive (FP), True Negative (TN), and False Negative (FN).

## Key Formula

$$\text{Precision} = \frac{TP}{TP + FP} \qquad \text{Recall} = \frac{TP}{TP + FN}$$

$$\text{Accuracy} = \frac{TP + TN}{TP + FP + TN + FN}$$

## Example

A credit-default model classifies 1,000 loan applications. Of 50 true defaults: 40 are caught (TP) and 10 are missed (FN). Of 950 non-defaults: 30 are wrongly flagged (FP) and 920 are correctly cleared (TN). Precision = 40/70 ≈ 57%; Recall = 40/50 = 80%.

## Remember

In credit risk and fraud detection, the cost of a False Negative (missed default) typically far exceeds that of a False Positive (wasted review), so banks optimise for high Recall rather than raw Accuracy. Class imbalance — defaults are rare — makes Accuracy a misleading headline metric.
