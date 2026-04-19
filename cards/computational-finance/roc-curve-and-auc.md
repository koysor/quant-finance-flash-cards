# ROC Curve and AUC

**Topic:** Computational Finance
**Tags:** ROC, AUC, classification, threshold, sensitivity, credit scoring
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **Receiver Operating Characteristic (ROC) curve** plots the True Positive Rate (Recall) against the False Positive Rate at every possible classification threshold, tracing the full trade-off between sensitivity and specificity. The **Area Under the Curve (AUC)** summarises this into a single threshold-independent performance metric.

## Key Formula

$$\text{TPR}(\tau) = \frac{TP(\tau)}{TP(\tau)+FN(\tau)} \qquad \text{FPR}(\tau) = \frac{FP(\tau)}{FP(\tau)+TN(\tau)}$$

$$\text{AUC} = \int_0^1 \text{TPR}\,d(\text{FPR})$$

AUC interpretation: the probability that the model ranks a randomly chosen positive example above a randomly chosen negative example.

## Example

A loan default model produces probability scores. At threshold $\tau = 0.5$: TPR = 0.70, FPR = 0.12. At $\tau = 0.3$: TPR = 0.88, FPR = 0.25. The ROC curve connects all such points; AUC = 0.87 means the model correctly ranks 87% of (default, non-default) pairs.

## Remember

AUC is the standard headline metric for credit scorecards and fraud detection models because it is invariant to class imbalance and requires no threshold choice — defaults are rare (1–5% of loans) so raw accuracy is uninformative. Regulators increasingly require AUC alongside the Gini coefficient (Gini = 2·AUC − 1) when approving internal rating-based credit models.
