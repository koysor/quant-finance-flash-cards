# F1 Score

**Topic:** Computational Finance
**Tags:** f1 score, precision, recall, harmonic mean, class imbalance, credit scoring
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **F1 score** is the harmonic mean of Precision and Recall, combining both into a single metric that penalises classifiers which sacrifice one for the other. It is the standard evaluation metric for classification tasks with imbalanced classes, where raw accuracy is misleading.

## Key Formula

$$\text{F1} = 2 \cdot \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\,TP}{2\,TP + FP + FN}$$

The harmonic mean weights the lower of the two values more heavily than the arithmetic mean — a model with Precision 0.9 and Recall 0.1 scores F1 $= 0.18$, not the misleading arithmetic average $0.5$.

**Generalisation — $F_\beta$ score** weights Recall $\beta$ times as important as Precision:

$$F_\beta = (1+\beta^2)\cdot\frac{\text{Precision} \times \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}$$

$\beta > 1$ emphasises Recall (preferred when missing a default is costly); $\beta < 1$ emphasises Precision.

## Example

A fraud detection model on 10,000 transactions: 100 true frauds. Model A: catches 90 frauds (TP=90), raises 50 false alarms (FP=50). Precision = 90/140 = 64%; Recall = 90/100 = 90%; F1 = 2×0.64×0.90/(0.64+0.90) = **74.8%**. Model B catches all 100 frauds (TP=100) but raises 200 false alarms: F1 = 2×0.33×1.0/(0.33+1.0) = **50%**. F1 correctly penalises Model B's poor precision.

## Remember

F1 is the default single metric for financial classification models where class imbalance is severe — credit default (1–5% base rate), fraud detection (<0.1%), and rare event prediction. Because the harmonic mean is dominated by the smaller of Precision and Recall, a model cannot inflate F1 by simply classifying everything as positive (boosting Recall at the cost of Precision). In practice, $F_2$ is often preferred in credit risk to weight Recall more heavily, reflecting the asymmetric regulatory and capital cost of a missed default versus a false alarm.
