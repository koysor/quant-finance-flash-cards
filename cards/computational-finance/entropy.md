# Entropy (Information Theory)

**Topic:** Computational Finance
**Tags:** entropy, information gain, decision tree, impurity, classification, uncertainty
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Entropy** (Shannon entropy) measures the average uncertainty or disorder in a dataset. In machine learning it quantifies the impurity of a node in a decision tree: zero entropy means all samples belong to one class; maximum entropy means classes are equally represented.

## Key Formula

$$H(S) = -\sum_{i=1}^{K} p_i \log_2 p_i$$

where $p_i$ is the proportion of samples in class $i$ and $K$ is the number of classes. **Information gain** from a split on feature $A$ is:

$$IG(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$$

## Example

A node with 50 defaults and 50 non-defaults has $H = -0.5\log_2 0.5 - 0.5\log_2 0.5 = 1$ bit. Splitting on "credit score > 700" produces a near-pure node of 45 defaults and a near-pure node of 45 non-defaults — high information gain.

## Remember

Entropy and information gain are the selection criterion that drives decision-tree splits in credit-scoring and fraud-detection models. Minimising entropy at each split is equivalent to maximising the predictive power extracted from each feature — the same intuition as maximising the signal-to-noise ratio when constructing factor models.
