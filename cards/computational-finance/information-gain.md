# Information Gain

**Topic:** Computational Finance
**Tags:** information gain, decision tree, entropy, feature selection, id3, classification
**Created:** 2026-04-26
**Author:** Claude Sonnet 4.6

---

## Definition

**Information gain** measures the reduction in entropy of a target variable $Y$ achieved by splitting a dataset on a feature $A$. It is the standard criterion used by the ID3 and C4.5 decision tree algorithms to select the most informative feature at each node, maximising the purity improvement per split.

## Key Formula

$$IG(Y, A) = H(Y) - H(Y \mid A)$$

where the conditional entropy after splitting on $A$ is:

$$H(Y \mid A) = \sum_{v \in \text{vals}(A)} \frac{|S_v|}{|S|} \, H(S_v)$$

and the entropy of a subset $S$ with class proportions $p_k$ is:

$$H(S) = -\sum_k p_k \log_2 p_k$$

The feature chosen at each split is:

$$A^* = \underset{A}{\arg\max} \; IG(Y, A)$$

**Gain Ratio** (C4.5 correction for high-cardinality features):

$$GR(Y, A) = \frac{IG(Y, A)}{H(A)}, \quad H(A) = -\sum_v \frac{|S_v|}{|S|} \log_2 \frac{|S_v|}{|S|}$$

## Example

A credit dataset has 1,000 loans: 400 defaulted ($p_{\text{def}} = 0.4$), 600 did not.

Pre-split entropy: $H(Y) = -0.4 \log_2 0.4 - 0.6 \log_2 0.6 = 0.971$ bits.

Two candidate features:
- **Debt-to-income $> 40\%$**: splits into 300 high (60% default) and 700 low (29% default).  
  $H(Y \mid \text{DTI}) = \frac{300}{1000}(0.971) + \frac{700}{1000}(0.895) = 0.917$ bits.  
  $IG = 0.971 - 0.917 = 0.054$ bits.
- **Employment status**: splits into 200 self-employed (55% default) and 800 employed (36% default).  
  $H(Y \mid \text{Emp}) = \frac{200}{1000}(0.993) + \frac{800}{1000}(0.954) = 0.962$ bits.  
  $IG = 0.971 - 0.962 = 0.009$ bits.

The tree selects debt-to-income as the first split: it extracts 0.054 bits of information vs 0.009 bits for employment status.

## Remember

Information gain is the **feature selection engine** inside every gradient-boosted tree model used for credit scoring and default prediction. When XGBoost or LightGBM reports "feature importance by gain", it is reporting the total $IG$ attributable to each feature across all splits in all trees — a direct measure of how much each feature reduced classification uncertainty. High information gain does not imply causal impact: a feature like postcode may have high $IG$ (it correlates strongly with default) whilst being legally impermissible under fair lending rules. Quant risk teams therefore distinguish between predictive power (information gain) and permissible use, stripping legally protected attributes before reporting feature importance to regulators.
