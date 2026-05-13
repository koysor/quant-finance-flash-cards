# Linear Discriminant Analysis

**Topic:** Computational Finance
**Tags:** lda, classification, dimensionality reduction, covariance, decision boundary, credit scoring
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Linear Discriminant Analysis (LDA)** is a supervised classification and dimensionality reduction technique that finds the linear combination of features which maximises the ratio of **between-class variance** to **within-class variance**, producing a decision boundary that best separates classes according to their covariance structure.

## Key Formula

For two classes with means $\boldsymbol{\mu}_1$, $\boldsymbol{\mu}_2$ and shared covariance matrix $\boldsymbol{\Sigma}$, the **LDA discriminant direction** is:

$$\mathbf{w} = \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)$$

A new observation $\mathbf{x}$ is classified by computing the **linear score**:

$$\delta(\mathbf{x}) = \mathbf{x}^\top \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_k - \frac{1}{2}\boldsymbol{\mu}_k^\top \boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_k + \ln P(C_k)$$

and assigning $\mathbf{x}$ to the class $k$ with the highest $\delta_k(\mathbf{x})$, where $P(C_k)$ is the prior probability of class $k$.

**Fisher's criterion** (the objective LDA maximises):

$$J(\mathbf{w}) = \frac{\mathbf{w}^\top \mathbf{S}_B \mathbf{w}}{\mathbf{w}^\top \mathbf{S}_W \mathbf{w}}$$

where $\mathbf{S}_B$ is the between-class scatter matrix and $\mathbf{S}_W$ is the within-class scatter matrix.

## Example

A credit model has two features: debt-to-income ratio ($x_1$) and credit utilisation ($x_2$).

- Class 1 (no default): $\boldsymbol{\mu}_1 = (0.3,\; 0.4)^\top$
- Class 2 (default): $\boldsymbol{\mu}_2 = (0.7,\; 0.8)^\top$
- Shared covariance: $\boldsymbol{\Sigma} = \begin{pmatrix}0.04 & 0.01 \\ 0.01 & 0.09\end{pmatrix}$

Computing $\mathbf{w} = \boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)$ gives the direction that maximally separates the two groups. The decision boundary is the hyperplane perpendicular to $\mathbf{w}$ passing through the midpoint — borrowers on one side are classified as likely defaulters, the other as creditworthy.

## Remember

LDA is one of the oldest tools in credit scoring (Altman's Z-score, the famous 1968 bankruptcy prediction model, is essentially a weighted LDA applied to five financial ratios). Its key advantage over logistic regression is that it explicitly models the covariance structure of the features — when class covariances are genuinely equal, LDA is the optimal Bayes classifier. Its key limitation is the **equal covariance assumption**: if defaulters and non-defaulters have very different feature dispersions, Quadratic Discriminant Analysis (QDA) is preferred. As a dimensionality reduction tool, LDA finds the $K-1$ directions (for $K$ classes) that best preserve class separability — used in multi-asset regime classification to reduce a large set of macro factors to a low-dimensional discriminant space.
