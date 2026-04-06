# Machine Learning

**Topic:** Computational Finance
**Tags:** machine learning, supervised learning, regression, loss function, regularisation, prediction
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Machine learning** (ML) is a class of algorithms that build predictive models by optimising a loss function over training data, without being explicitly programmed with rules. In **supervised learning** — the most common paradigm in finance — the algorithm learns a mapping $f(\mathbf{x}) \approx y$ from input features $\mathbf{x}$ (e.g. financial ratios) to a target $y$ (e.g. default probability) by minimising prediction error.

## Key Formula

**Mean squared error loss** (regression):

$$\mathcal{L}(\mathbf{w}) = \frac{1}{n}\sum_{i=1}^{n}\bigl(y_i - \mathbf{w}^\top \mathbf{x}_i\bigr)^2$$

**Regularised loss** (Ridge / LASSO — prevents overfitting):

$$\mathcal{L}_\text{Ridge} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda\sum_{j}w_j^2, \qquad \mathcal{L}_\text{LASSO} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda\sum_{j}|w_j|$$

**Bias-variance decomposition:**

$$\mathbb{E}\!\left[(y - \hat{y})^2\right] = \text{Bias}^2 + \text{Variance} + \text{Irreducible noise}$$

## Example

A credit analyst trains a logistic regression on 10,000 loan applications using features: debt-to-income ratio, credit score, and employment length. With $\lambda = 0.01$ Ridge regularisation, the model achieves 87% accuracy on the hold-out test set, versus 91% on training data — the 4% gap is the generalisation error, a signal that mild overfitting is present. Increasing $\lambda$ reduces this gap at the cost of slightly higher training error.

## Remember

ML has three major roles in quantitative finance. First, **credit scoring**: banks use gradient-boosted trees and logistic regression to predict default probability, replacing the older scorecard approach. Second, **alpha signal generation**: hedge funds train ML models on alternative data (satellite imagery, web traffic, sentiment) to predict stock returns — the features $\mathbf{x}$ are engineered from raw data and the target $y$ is the next-period return. Third, **volatility forecasting**: LSTM networks and random forests outperform GARCH on out-of-sample realised volatility prediction for short horizons. The bias-variance tradeoff is the central design decision in all three: a high-capacity model memorises noise; a regularised model generalises.
