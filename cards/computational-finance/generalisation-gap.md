# Generalisation Gap

**Topic:** Computational Finance
**Tags:** generalisation, overfitting, train error, test error, model complexity, backtesting
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

The **generalisation gap** is the difference between a model's in-sample (training) error and its out-of-sample (test) error. A large gap indicates overfitting: the model has memorised noise in the training data and fails to capture the true underlying pattern. A small gap alongside low test error indicates genuine predictive power.

## Key Formula

$$\text{Generalisation Gap} = \mathcal{L}_{\text{test}}(\hat{\boldsymbol{\theta}}) - \mathcal{L}_{\text{train}}(\hat{\boldsymbol{\theta}})$$

Theoretical bound (VC theory) for a model class of capacity $h$ trained on $N$ samples:

$$\mathcal{L}_{\text{test}} \leq \mathcal{L}_{\text{train}} + \mathcal{O}\!\left(\sqrt{\frac{h\ln N}{N}}\right)$$

The gap shrinks as $N$ grows and as model complexity $h$ decreases — the formal basis for regularisation and early stopping.

## Example

A gradient-boosted credit model: training AUC = 0.97, test AUC = 0.74 — generalisation gap of 0.23 AUC points, indicating severe overfitting. After adding L2 regularisation and reducing tree depth: training AUC = 0.85, test AUC = 0.82 — gap shrinks to 0.03, and the model is deployable.

## Remember

In quantitative finance the generalisation gap is the difference between a strategy's backtest Sharpe ratio and its live performance — the most common and costly failure mode in systematic trading. A large gap is not a model quality issue but an information leakage issue: the model has implicitly seen the future through lookahead bias, data snooping, or parameter overfitting to historical noise that does not repeat out-of-sample.
