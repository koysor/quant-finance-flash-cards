# Gradient Boosting

**Topic:** Computational Finance
**Tags:** gradient boosting, ensemble, weak learners, XGBoost, sequential learning, credit scoring
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Gradient Boosting** is a supervised ensemble method that builds a strong predictor by combining many weak learners (typically shallow decision trees) in sequence. Each new tree is trained to correct the residual errors of the ensemble so far, using gradient descent in function space to minimise a differentiable loss function.

## Key Formula

At step $m$, the model is updated by fitting a new tree $h_m$ to the negative gradient of the loss $L$:

$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta\, h_m(\mathbf{x})$$

$$h_m \approx -\nabla_{F} L\!\left(y,\, F_{m-1}(\mathbf{x})\right)$$

where $\eta$ is the learning rate and $h_m$ is fit to the pseudo-residuals $r_i = -\partial L / \partial F_{m-1}(\mathbf{x}_i)$.

## Example

A credit default model uses gradient boosting with 500 trees of depth 3. At each round a new tree targets the cases the current ensemble mis-scores most. XGBoost (an optimised implementation) achieves an AUC of 0.89 on the hold-out set — outperforming a single decision tree (0.72) and logistic regression (0.81).

## Remember

Gradient boosting and its variants (XGBoost, LightGBM) consistently top Kaggle leaderboards for structured tabular data — the kind most prevalent in finance (loan features, trade attributes, market microstructure variables). Unlike random forests, which reduce variance by averaging parallel trees, boosting reduces bias by iteratively correcting errors, making it particularly powerful when the signal is complex and non-linear.
