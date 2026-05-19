# Soft Margin SVM

**Topic:** Computational Finance
**Tags:** svm, soft margin, slack variables, regularisation, c parameter, classification
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **soft-margin SVM** extends the hard-margin SVM to non-linearly separable data by introducing **slack variables** $\xi_i \ge 0$ that allow training points to violate the margin. A penalty parameter $C > 0$ controls the trade-off: large $C$ tolerates few violations (low bias, high variance); small $C$ allows many violations (high bias, low variance).

## Key Formula

**Primal optimisation problem:**

$$\min_{\mathbf{w},\,b,\,\boldsymbol{\xi}} \;\frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{i=1}^{n}\xi_i \quad \text{subject to} \quad y_i\!\left(\mathbf{w}^\top \mathbf{x}_i + b\right) \ge 1 - \xi_i,\quad \xi_i \ge 0 \quad \forall\, i$$

$\xi_i = 0$: point correctly classified outside the margin.  
$0 < \xi_i \le 1$: point inside the margin but correctly classified.  
$\xi_i > 1$: point misclassified.

The sum $\sum_i \xi_i$ is an upper bound on the number of training errors.

## Example

Fraud detection model with 10,000 transactions (500 fraudulent). The two classes overlap in feature space.

| $C$ | Training accuracy | Test accuracy | Support vectors |
|-----|------------------|---------------|-----------------|
| 0.01 | 87% | 86% | 4,200 (many violations allowed) |
| 1 | 94% | 93% | 850 |
| 100 | 98% | 91% | 120 (nearly hard margin) |

At $C = 100$ the model memorises noisy training points and generalises poorly — classic overfitting. At $C = 1$ the model achieves the best out-of-sample performance. Tuning $C$ via cross-validation is mandatory.

## Remember

In quantitative finance the soft-margin SVM is the practical version used for **credit scoring, fraud detection, and binary event classification** (e.g. predicts earnings beat/miss). The parameter $C$ is directly analogous to the regularisation strength in ridge regression: it prevents the model from over-fitting to idiosyncratic noise in financial data. A useful intuition: $C$ answers "how much do I trust each individual training label?" — in financial data where labels are noisy (defaults are often misreported, fraud labels are incomplete), a smaller $C$ is usually better.
