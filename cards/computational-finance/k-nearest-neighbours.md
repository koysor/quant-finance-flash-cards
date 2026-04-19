# K-Nearest Neighbours

**Topic:** Computational Finance
**Tags:** knn, classification, non-parametric, supervised learning, credit scoring, lazy learner
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**K-Nearest Neighbours (KNN)** is a non-parametric supervised learning algorithm that classifies or regresses a new observation by aggregating the labels of the $K$ training points closest to it in feature space. No explicit model is fitted; all computation is deferred to prediction time.

## Key Formula

For classification, the predicted class is the majority vote among the $K$ nearest neighbours:

$$\hat{y} = \arg\max_{c} \sum_{i \in \mathcal{N}_K(\mathbf{x})} \mathbf{1}[y_i = c]$$

where $\mathcal{N}_K(\mathbf{x})$ denotes the indices of the $K$ nearest training points to $\mathbf{x}$.

## Example

$K=5$, new loan application. The five most similar past applications (by income, debt ratio, credit score) include 4 repaid and 1 defaulted — KNN classifies the new application as low-risk.

## Remember

KNN is used in credit scoring and anomaly detection in transaction data. Choosing $K$ controls the bias-variance trade-off: $K=1$ memorises every training point (high variance), while large $K$ smooths out local structure (high bias). Features must be scaled, as KNN is purely distance-based.
