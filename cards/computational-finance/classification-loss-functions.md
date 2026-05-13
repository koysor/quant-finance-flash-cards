# Classification Loss Functions

**Topic:** Computational Finance
**Tags:** hinge loss, zero-one loss, classification, svm, loss function, margin
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Classification loss functions** measure the cost of a wrong (or insufficiently confident) prediction, using the **margin** $m = \hat{y} \cdot y$ where $y \in \{-1, +1\}$ is the true class label and $\hat{y}$ is the signed model score. A positive margin means the prediction is correct; a negative margin means it is wrong.

## Key Formula

| Loss | Formula | Used by |
|---|---|---|
| Zero-one | $\mathbf{1}(m \leq 0)$ | Theoretical baseline |
| Hinge | $\max(1 - m,\; 0)$ | SVM |
| Log-loss | $\ln(1 + e^{-m})$ | Logistic regression |

$$\underbrace{\max(1-m,\; 0)}_{\text{hinge}} \geq \underbrace{\mathbf{1}(m \leq 0)}_{\text{zero-one}}$$

Hinge loss is a convex upper bound on zero-one loss, which enables gradient-based optimisation. It penalises correct predictions with small margin ($0 < m < 1$) but ignores correctly confident ones ($m \geq 1$), producing **sparse solutions** — only support vectors contribute to the decision boundary.

## Example

Classifying bonds as investment-grade ($y=+1$) or high-yield ($y=-1$). Model score $\hat{y} = 0.6$ for a true high-yield bond ($y = -1$): $m = 0.6 \times (-1) = -0.6$. Hinge loss $= \max(1-(-0.6), 0) = 1.6$ — large penalty. For a correctly classified investment-grade bond with $\hat{y} = 1.5$: $m = 1.5$, hinge loss $= \max(1-1.5, 0) = 0$ — no penalty once the margin is satisfied.

## Remember

The choice of loss function determines the character of the resulting classifier. Hinge loss creates SVMs whose decision boundary is defined by a sparse set of support vectors — observations that sit near or on the wrong side of the margin. Log-loss creates logistic regression, which outputs calibrated probabilities useful for Expected Credit Loss (PD × LGD × EAD) calculations under IFRS 9. Zero-one loss, though intuitive, is non-differentiable and therefore replaced by its convex surrogates in practice. In regulatory model validation, understanding which loss function a model optimises is part of demonstrating model fit for purpose.
