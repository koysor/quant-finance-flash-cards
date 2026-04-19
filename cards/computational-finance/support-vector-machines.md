# Support Vector Machines

**Topic:** Computational Finance
**Tags:** SVM, classification, hyperplane, margin, kernel trick, credit scoring
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

A **Support Vector Machine (SVM)** is a supervised learning algorithm that finds the hyperplane separating two classes with the maximum margin. Only the training points closest to the boundary — the **support vectors** — determine the hyperplane; all other points are irrelevant once training is complete.

## Key Formula

**Hard-margin primal problem:**

$$\min_{\mathbf{w},b}\;\frac{1}{2}\|\mathbf{w}\|^2 \quad\text{subject to}\quad y_i(\mathbf{w}^{\top}\mathbf{x}_i + b) \ge 1 \;\forall i$$

**Soft-margin** (allows misclassifications with penalty $C$):

$$\min_{\mathbf{w},b,\boldsymbol{\xi}}\;\frac{1}{2}\|\mathbf{w}\|^2 + C\sum_i \xi_i$$

## Example

A binary credit classifier with two features (debt-to-income ratio, credit score). The SVM draws the widest possible dividing line between the "default" and "no-default" clouds. The kernel trick (RBF kernel) extends this to non-linearly separable data.

## Remember

SVMs are favoured in credit risk and fraud detection when the dataset is moderate-sized and high-dimensional (many financial features). Maximising the margin is a regularisation strategy equivalent to minimising model complexity — providing a theoretical justification for good out-of-sample generalisation, unlike neural networks which require separate regularisation.
