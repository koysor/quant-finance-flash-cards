# Feature Vector

**Topic:** Computational Finance
**Tags:** feature vector, input vector, machine learning, normalisation, input representation, data preprocessing, supervised learning
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

A **feature vector** is an ordered list of numeric values that encodes a single observation — such as a stock or a trading day — as a point in $d$-dimensional space. Each element of the vector corresponds to one measured attribute (a feature), allowing machine learning algorithms to operate on structured numeric inputs.

## Key Formula

An observation is represented as a column vector:

$$\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_d \end{pmatrix} \in \mathbb{R}^d$$

Before modelling, each feature is typically **z-score normalised** to zero mean and unit variance:

$$\tilde{x}_j = \frac{x_j - \mu_j}{\sigma_j}$$

where $\mu_j$ and $\sigma_j$ are the mean and standard deviation of feature $j$ computed over the training set.

## Example

A daily feature vector for a single equity might contain $d = 5$ features:

$$\mathbf{x} = \begin{pmatrix} 0.023 \\ 1{,}450{,}000 \\ 0.18 \\ 0.61 \\ -0.04 \end{pmatrix} \leftarrow \begin{array}{l} \text{1-day return} \\ \text{trading volume (shares)} \\ \text{30-day realised volatility} \\ \text{RSI(14)} \\ \text{3-month momentum} \end{array}$$

After z-score normalisation, all five elements are dimensionless and comparable in magnitude.

## Remember

Feature vectors are the fundamental unit of input to every supervised learning model in quantitative finance — from logistic regression for credit scoring to neural networks for return prediction. Without normalisation, a volume feature measured in millions will numerically dominate a return measured in percentage points, causing gradient-based optimisers to update parameters unevenly and degrading model performance.
