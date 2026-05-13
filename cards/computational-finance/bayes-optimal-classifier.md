# Bayes Optimal Classifier

**Topic:** Computational Finance
**Tags:** bayes classifier, optimal classifier, posterior probability, bayes error rate, classification, decision boundary
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Bayes optimal classifier** is the theoretical gold standard for classification: it assigns each observation to the class with the highest posterior probability given the observed features. No classifier can achieve a lower expected error rate than the Bayes classifier, making the **Bayes error rate** the irreducible minimum error — analogous to the noise floor in signal processing.

## Key Formula

Assign observation $\mathbf{x}$ to class $j$ where:

$$\hat{y} = \arg\max_{j} \Pr(Y = j \mid \mathbf{X} = \mathbf{x})$$

By Bayes' theorem:

$$\Pr(Y = j \mid \mathbf{X} = \mathbf{x}) = \frac{P(\mathbf{x} \mid Y = j)\,\Pr(Y = j)}{P(\mathbf{x})}$$

The **Bayes error rate** (irreducible error) is:

$$\epsilon^* = 1 - \mathbb{E}_{\mathbf{x}}\!\left[\max_{j}\, \Pr(Y = j \mid \mathbf{X} = \mathbf{x})\right]$$

## Example

A credit model uses two features: income $X_1$ and debt-to-income $X_2$. The Bayes classifier draws the decision boundary at the locus of points where $\Pr(\text{Default} \mid X_1, X_2) = \Pr(\text{No Default} \mid X_1, X_2) = 0.5$. If even with perfect knowledge of the class-conditional densities, 3% of borrowers are misclassified (e.g. due to intrinsic randomness in default behaviour), then $\epsilon^* = 3\%$ — no model, however complex, can do better.

## Remember

The Bayes optimal classifier is never achievable in practice because the true class-conditional densities $P(\mathbf{x} \mid Y = j)$ are unknown. All practical classifiers — logistic regression, SVMs, gradient-boosted trees — are approximations to it, and their out-of-sample error decomposes as: **Bayes error** (irreducible) + **bias** (model too simple) + **variance** (model too sensitive to training data). In quantitative finance, the Bayes error rate captures the intrinsic unpredictability of financial outcomes — a floor below which no alpha signal or default model can fall, no matter how sophisticated.
