# Decision Threshold

**Topic:** Computational Finance
**Tags:** decision threshold, classification, roc curve, precision-recall, credit risk, cost-sensitive learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **decision threshold** $\tau$ is the probability cut-off above which a classifier assigns the positive class label. The default threshold of 0.5 (predict positive if $\hat{p} > 0.5$) is rarely optimal in finance because the costs of False Positives and False Negatives are asymmetric — moving $\tau$ trades off Precision against Recall to minimise the actual business cost.

## Key Formula

$$\hat{y} = \begin{cases} 1 & \text{if } \hat{p} \geq \tau \\ 0 & \text{if } \hat{p} < \tau \end{cases}$$

**Optimal threshold under asymmetric costs** — minimise expected cost:

$$\tau^* = \arg\min_{\tau}\; \left[C_{FN} \cdot FN(\tau) + C_{FP} \cdot FP(\tau)\right]$$

where $C_{FN}$ is the cost of a missed positive (e.g. undetected default) and $C_{FP}$ is the cost of a false alarm (e.g. wasted investigation). As $\tau$ increases: Precision rises, Recall falls.

## Example

A default prediction model outputs $\hat{p}$ for each borrower. At $\tau = 0.5$: Precision 70%, Recall 60%. The bank estimates $C_{FN} = £50{,}000$ (missed default, expected loss) and $C_{FP} = £500$ (unnecessary credit review). Setting $\tau = 0.2$ catches more defaults (Recall 85%) at the cost of more reviews (Precision 40%) — the lower Precision is acceptable given the 100:1 cost ratio.

## Remember

The 0.5 default threshold is almost never appropriate in financial applications because the cost of a missed default (or missed fraud) vastly exceeds the cost of a false alarm. Threshold selection is therefore a business decision, not a statistical one: the ROC curve maps out the full Recall–FPR trade-off across all possible $\tau$, and the Precision–Recall curve maps Precision vs Recall, enabling practitioners to pick the threshold that minimises regulatory capital impact, expected loss, or operational review costs. Under IFRS 9, institutions must demonstrate that their PD model thresholds are consistent with observed default rates over economic cycles.
