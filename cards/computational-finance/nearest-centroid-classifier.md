# Nearest Centroid Classifier

**Topic:** Computational Finance
**Tags:** nearest centroid, classification, inner product, decision boundary, credit scoring, machine learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **nearest centroid classifier** assigns each class its centroid (the mean of its training points) and predicts the class of a new observation as the class whose centroid is closest. It produces a linear decision boundary — a hyperplane equidistant from the two centroids.

## Key Formula

For binary classification, compute class centroids $\mathbf{c}_+$ and $\mathbf{c}_-$ from labelled training data. Define the direction vector and midpoint:

$$\mathbf{w} = \mathbf{c}_+ - \mathbf{c}_-, \qquad \mathbf{c} = \tfrac{1}{2}(\mathbf{c}_+ + \mathbf{c}_-)$$

Classify a new point $\mathbf{z}$ by the sign of the inner product with the centred observation:

$$\hat{y} = \operatorname{sign}\!\left(\langle \mathbf{z} - \mathbf{c},\, \mathbf{w} \rangle\right)$$

A positive value means $\mathbf{z}$ is closer to $\mathbf{c}_+$; negative means closer to $\mathbf{c}_-$.

## Example

Credit scoring with three features: income ($x_1$), debt-to-income ratio ($x_2$), credit score ($x_3$). From 200 training loans, the defaulter centroid is $\mathbf{c}_- = (32, 0.45, 580)$ and the non-defaulter centroid is $\mathbf{c}_+ = (65, 0.22, 720)$. A new applicant with $\mathbf{z} = (50, 0.30, 680)$ is classified by evaluating $\langle \mathbf{z} - \mathbf{c}, \mathbf{w} \rangle > 0$, placing them in the non-defaulter class.

## Remember

The nearest centroid classifier is the simplest instance of a linear classifier built from inner products, making it the geometric foundation for understanding SVMs and linear discriminant analysis. In quantitative finance it serves as a fast, interpretable baseline for binary classification (default/no-default, fraud/legitimate) before deploying more complex models — its decision boundary is a hyperplane that can be expressed entirely in terms of summary statistics of the training classes.
