# Hard Margin SVM

**Topic:** Computational Finance
**Tags:** svm, hard margin, support vectors, maximum margin, linearly separable, classification
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **hard-margin SVM** finds the unique hyperplane that separates two linearly separable classes with the **maximum geometric margin** — the widest possible gap between the hyperplane and the nearest training points. Points lying exactly on the margin boundary are the **support vectors** and are the only training points that determine the solution.

## Key Formula

**Primal optimisation problem:**

$$\min_{\mathbf{w},\,b} \;\frac{1}{2}\|\mathbf{w}\|^2 \quad \text{subject to} \quad y_i\!\left(\mathbf{w}^\top \mathbf{x}_i + b\right) \ge 1 \quad \forall\, i$$

where $y_i \in \{-1, +1\}$ is the class label. The geometric margin equals $\dfrac{2}{\|\mathbf{w}\|}$, so minimising $\|\mathbf{w}\|^2$ is equivalent to maximising the margin.

The constraint $y_i(\mathbf{w}^\top \mathbf{x}_i + b) \ge 1$ enforces correct classification with a margin of at least 1 (in the normalised feature space).

## Example

A toy credit dataset with two perfectly separable groups:
- Class $+1$ (no default): points at $(2, 3)$, $(3, 4)$, $(4, 3)$
- Class $-1$ (default): points at $(0, 1)$, $(1, 0)$, $(1, 1)$

The hard-margin SVM finds $\mathbf{w} = (1, 1)$, $b = -3$ giving hyperplane $x_1 + x_2 = 3$. The two support vectors closest to the boundary are $(2,1)$ and $(1,2)$, each at distance $\frac{2}{\sqrt{2}} \approx 1.41$ from the hyperplane.

## Remember

Hard margin works only when training data is **perfectly linearly separable** — a condition that almost never holds in real financial data, where noise, outliers, and overlapping feature distributions are the norm. A single mis-labelled loan application or fraudulent transaction causes the hard-margin SVM to fail entirely (the optimisation becomes infeasible). This brittleness motivates the **soft-margin SVM**, which allows a controlled number of violations. Understanding the hard margin provides the theoretical baseline: maximising margin is equivalent to L2 regularisation, which is why SVMs generalise well even in high-dimensional financial feature spaces.
