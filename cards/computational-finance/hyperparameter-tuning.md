# Hyperparameter Tuning

**Topic:** Computational Finance
**Tags:** hyperparameter, grid search, cross-validation, model selection, overfitting, regularisation
**Created:** 2026-04-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Hyperparameter tuning** is the process of searching for the model configuration settings (hyperparameters) that produce the best out-of-sample performance. Unlike model parameters (which are learned from data), hyperparameters — such as learning rate, regularisation strength, or tree depth — must be set before training and evaluated using held-out data.

## Key Formula

**$k$-fold cross-validation score** for a hyperparameter configuration $\lambda$:

$$\text{CV}(\lambda) = \frac{1}{k}\sum_{i=1}^{k} \mathcal{L}\!\left(f_\lambda^{(-i)},\, \mathcal{D}_i\right)$$

where $f_\lambda^{(-i)}$ is the model trained on all folds except the $i$-th, and $\mathcal{D}_i$ is the held-out fold. Select $\hat{\lambda} = \arg\min_\lambda\,\text{CV}(\lambda)$.

**Grid search**: evaluate all combinations on a discrete grid. **Random search**: sample configurations randomly — often more efficient in high-dimensional hyperparameter spaces.

## Example

Tuning a gradient-boosted credit model: hyperparameters are learning rate $\eta \in \{0.01, 0.05, 0.1\}$, tree depth $\in \{3, 5, 7\}$, and L2 penalty $\lambda \in \{0.1, 1, 10\}$. Grid search evaluates $3^3=27$ configurations via 5-fold CV on historical loan data, selecting the combination with the highest hold-out AUC.

## Remember

In quantitative finance, hyperparameter tuning is inseparable from avoiding look-ahead bias: the correct procedure is to tune on a validation window that precedes the test period, never using future data to select model settings. Walk-forward validation — re-tuning at each rebalancing date using only past data — is the standard approach for strategy backtesting and ensures the reported performance is genuinely out-of-sample.
