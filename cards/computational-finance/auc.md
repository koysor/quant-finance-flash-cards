# AUC (Area Under the Curve)

**Topic:** Computational Finance
**Tags:** auc, model evaluation, rank statistic, gini coefficient, credit scoring, classification
**Created:** 2026-05-24
**Author:** Claude Sonnet 4.6

---

## Definition

**AUC** (Area Under the Curve) is a threshold-independent scalar summary of a binary classifier's ability to rank positive examples above negative ones. Its fundamental interpretation is probabilistic: AUC equals the probability that the model assigns a higher score to a randomly chosen positive example than to a randomly chosen negative example.

## Key Formula

$$\text{AUC} = P\!\left(s^+ > s^-\right)$$

where $s^+$ is the model's score for a randomly chosen positive and $s^-$ for a randomly chosen negative. This is equivalent to the normalised **Wilcoxon-Mann-Whitney U statistic**:

$$\text{AUC} = \frac{U}{n_+ \cdot n_-}, \qquad U = \sum_{i=1}^{n_+} \sum_{j=1}^{n_-} \mathbf{1}\!\left[s_i^+ > s_j^-\right]$$

where $n_+$ and $n_-$ are the counts of positives and negatives, and $U$ counts all concordant (correctly ranked) pairs.

The **Gini coefficient**, the regulatory equivalent, is a linear rescaling:

$$G = 2 \cdot \text{AUC} - 1$$

A random classifier has AUC = 0.5, $G = 0$; a perfect classifier has AUC = 1, $G = 1$.

## Example

A credit scorecard is evaluated on a test set of 100 defaults ($n_+ = 100$) and 900 non-defaults ($n_- = 900$), giving $n_+ \cdot n_- = 90{,}000$ possible pairs.

The model correctly ranks the defaulter above the non-defaulter in 78,300 pairs:

$$U = 78{,}300 \qquad \text{AUC} = \frac{78{,}300}{90{,}000} = 0.870 \qquad G = 2(0.870) - 1 = 0.740$$

Interpretation: the scorecard ranks a random defaulter above a random non-defaulter 87% of the time, a Gini of 74%. The class imbalance (10:1) does not affect the AUC calculation — it counts pairs, not raw accuracy.

## Remember

Basel's Internal Ratings-Based (IRB) approach requires banks to validate their PD (probability of default) models using discriminatory power metrics; the **Gini coefficient** ($G = 2\text{AUC} - 1$) is the standard regulatory expression. Supervisors typically expect $G \geq 0.30$ for retail credit models and $G \geq 0.25$ for corporate models. The Wilcoxon formulation reveals why AUC is robust to class imbalance: it counts pairwise comparisons between classes rather than requiring balanced class representation, making it valid even when defaults are 0.5% of the portfolio.
