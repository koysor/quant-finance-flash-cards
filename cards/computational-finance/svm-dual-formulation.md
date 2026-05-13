# SVM Dual Formulation

**Topic:** Computational Finance
**Tags:** svm, dual problem, lagrange multipliers, support vectors, kernel trick, convex optimisation
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **SVM dual formulation** rewrites the primal optimisation problem — which is expressed in terms of the weight vector $\mathbf{w}$ — into an equivalent problem expressed in terms of **Lagrange multipliers** $\alpha_i \ge 0$, one per training point. The dual form has two critical properties: only training points with $\alpha_i > 0$ (the **support vectors**) matter for the solution, and all data appears only as dot products $\mathbf{x}_i^\top \mathbf{x}_j$, which can be replaced by a kernel function.

## Key Formula

**Dual problem** (maximise over $\boldsymbol{\alpha}$):

$$\max_{\boldsymbol{\alpha}} \sum_{i=1}^{n} \alpha_i - \frac{1}{2}\sum_{i=1}^{n}\sum_{j=1}^{n} \alpha_i \alpha_j y_i y_j\, \mathbf{x}_i^\top \mathbf{x}_j$$

subject to $\displaystyle\sum_{i=1}^{n} \alpha_i y_i = 0$ and $\alpha_i \ge 0$ (hard margin) or $0 \le \alpha_i \le C$ (soft margin).

Once solved, the weight vector and decision function are recovered as:

$$\mathbf{w} = \sum_{i=1}^{n} \alpha_i y_i \mathbf{x}_i, \qquad f(\mathbf{x}) = \text{sign}\!\left(\sum_{i:\,\alpha_i>0} \alpha_i y_i\, \mathbf{x}_i^\top \mathbf{x} + b\right)$$

Replacing $\mathbf{x}_i^\top \mathbf{x}_j$ with $k(\mathbf{x}_i, \mathbf{x}_j)$ gives the **kernelised SVM** with no extra computational cost.

## Example

A credit dataset has $n = 10{,}000$ training loans with $p = 50$ features. After solving the dual, only 180 training points have $\alpha_i > 0$ — these are the support vectors (the borderline credit cases). The prediction for a new applicant requires computing just 180 dot products rather than using all 10,000 training points, making inference fast despite the large training set.

## Remember

The dual formulation is the reason SVMs are practical at scale in quantitative finance. Three finance-specific benefits: (1) **sparsity** — predictions depend only on support vectors (the most ambiguous cases near the decision boundary), not the entire training history; (2) **kernel extensibility** — replacing dot products with a kernel function costs nothing extra in the dual, unlocking non-linear SVM at no additional complexity; (3) **interpretability** — support vectors with large $\alpha_i$ are the training examples most influential to the model, analogous to flagging the borderline loans that define the credit boundary. Solving the dual is a quadratic programme (QP), which convex optimisation solvers handle efficiently.
