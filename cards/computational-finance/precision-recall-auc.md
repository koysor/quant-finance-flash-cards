# Precision-Recall AUC (PR-AUC)

**Topic:** Computational Finance
**Tags:** model evaluation, classification, imbalanced classes, machine learning, performance metrics
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Precision-Recall AUC (PR-AUC)** is the area under the precision-recall curve, a performance metric for binary classifiers that measures the trade-off between precision (fraction of positive predictions that are correct) and recall (fraction of true positives detected). Unlike ROC-AUC, it is sensitive to class imbalance and provides a more informative evaluation when the positive class is rare.

## Key Formula

$$\text{Precision} = \frac{TP}{TP + FP}, \qquad \text{Recall} = \frac{TP}{TP + FN}$$

The PR curve plots Precision (y-axis) against Recall (x-axis) as the decision threshold sweeps from 1 to 0. PR-AUC is computed by the trapezoid rule or equivalent:

$$\text{PR-AUC} = \int_0^1 P(r)\,dr \approx \sum_{k} (r_k - r_{k-1})\,\frac{P_k + P_{k-1}}{2}$$

A baseline random classifier achieves PR-AUC $\approx p$ where $p$ is the prevalence of the positive class; a perfect classifier achieves PR-AUC $= 1$.

## Example

For a direction-prediction model with 52% up-days and 48% down-days (near-balanced), ROC-AUC and PR-AUC tell a similar story. But if the task were predicting large up-moves (top 10% of days), the positive class prevalence drops to 10%:

| Metric | Random classifier | Good classifier |
|---|---|---|
| ROC-AUC | 0.50 | 0.75 |
| PR-AUC | 0.10 | 0.45 |

ROC-AUC of 0.75 sounds strong; PR-AUC of 0.45 (versus baseline 0.10) tells you the model is actually quite useful, catching 4.5× more signal than chance.

## Remember

Report PR-AUC alongside ROC-AUC whenever your financial prediction task is imbalanced — which is most of the time. In a daily direction model for NVDA, the up/down split is roughly 53/47, so both metrics matter. But if the model is adapted to predict rare events — extreme moves, earnings surprises, circuit breakers — PR-AUC becomes the primary metric because ROC-AUC can remain high even when the model consistently misses the rare class. Regulatory model validation and internal risk model governance increasingly require PR-AUC reporting precisely because it does not flatter models on imbalanced tasks the way ROC-AUC can.
