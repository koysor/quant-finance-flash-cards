# Decision Trees

**Topic:** Computational Finance
**Tags:** decision tree, classification, regression tree, gini impurity, credit scoring, interpretable
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **decision tree** is a supervised learning model that partitions the feature space using a recursive sequence of binary splits, assigning a prediction to each leaf node. At each split, the algorithm selects the feature and threshold that best separates the target classes (classification) or minimises prediction error (regression). The result is an interpretable, rule-based model that can be read as a flowchart.

## Key Formula

**Gini impurity** (split quality for classification):

$$G = 1 - \sum_{k=1}^{K} p_k^2$$

where $p_k$ is the proportion of class $k$ in a node. A pure node (one class only) has $G = 0$; maximum impurity is $G = 1 - 1/K$.

**Information gain** at a split:

$$\Delta G = G_\text{parent} - \frac{n_L}{n}G_L - \frac{n_R}{n}G_R$$

The algorithm chooses the split maximising $\Delta G$ at each node.

## Example

A bank builds a credit decision tree on two features: credit score and debt-to-income (DTI) ratio.

```
Credit score < 650?
├── Yes → DTI > 0.45? → Yes: Decline (85% default rate)
│                     → No:  Review  (40% default rate)
└── No  → DTI > 0.60? → Yes: Review  (22% default rate)
                      → No:  Approve (6% default rate)
```

Each leaf gives an actionable decision with an interpretable rule — critical for regulatory compliance under SR 11-7 model risk guidance.

## Remember

Decision trees are the **most interpretable** ML model in finance, which makes them the preferred choice wherever regulators require explainability. Under Basel and IFRS 9, banks must be able to explain individual credit decisions to applicants and auditors — a deep neural network cannot do this, but a decision tree produces literal if-then rules. However, individual trees overfit badly: a single tree grown to full depth memorises training data. The solution is **ensembling** — averaging many trees (Random Forest) or sequentially correcting errors (Gradient Boosting), which dramatically improves predictive power while partially sacrificing interpretability.
