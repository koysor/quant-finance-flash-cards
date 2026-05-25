# Class Imbalance

**Topic:** Computational Finance
**Tags:** imbalanced classes, machine learning, classification, smote, class weights, resampling
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Class imbalance** occurs when one class in a classification dataset is substantially more frequent than others, causing a naive model to learn to predict the majority class almost exclusively. In financial prediction — detecting fraud, rare market regimes, or extreme price moves — the positive class can represent fewer than 1% of observations, making accuracy an unreliable metric and requiring explicit countermeasures.

## Key Formula

Three standard remediation strategies, in order of intrusiveness:

**Class weights:** Penalise misclassification of the minority class by a factor $w$:

$$w_{\text{minority}} = \frac{N}{2 \cdot N_{\text{minority}}}, \quad w_{\text{majority}} = \frac{N}{2 \cdot N_{\text{majority}}}$$

**Oversampling (SMOTE):** Synthesise new minority examples by interpolating between $k$-nearest minority neighbours:

$$\mathbf{x}_{\text{new}} = \mathbf{x}_i + \lambda\,(\mathbf{x}_j - \mathbf{x}_i), \quad \lambda \sim \text{Uniform}(0,1)$$

**Decision threshold tuning:** Instead of the default 0.5, choose threshold $\tau^*$ that maximises F1 or satisfies a precision-recall constraint:

$$\tau^* = \arg\max_\tau F_1(\tau) = \arg\max_\tau \frac{2 \cdot P(\tau) \cdot R(\tau)}{P(\tau) + R(\tau)}$$

## Example

Direction-prediction on NVDA daily closes: up-days = 53%, down-days = 47% — nearly balanced, so class imbalance is mild. But if the task were predicting large up-moves (top 5% of days):

| Strategy | Baseline accuracy | Minority recall |
|---|---|---|
| No correction | 95% (predicts "no big move" always) | 0% |
| Class weights | 88% | 62% |
| SMOTE | 85% | 68% |
| Threshold at 0.20 | 76% | 81% |

Accuracy falls but the model becomes genuinely useful.

## Remember

In financial ML, **class imbalance is the norm rather than the exception** for any event-driven prediction task — earnings surprises, circuit breakers, credit defaults, market crashes. The correct response is to: (1) switch from accuracy to PR-AUC as the primary metric, (2) apply class weights as a zero-cost first step (XGBoost's `scale_pos_weight` parameter), and (3) use SMOTE or threshold tuning only if class weights are insufficient. Avoid oversampling before time-series splitting — generating synthetic minority examples from the full dataset and then splitting introduces look-ahead bias by allowing future-period statistics to influence training-period synthetic samples.
