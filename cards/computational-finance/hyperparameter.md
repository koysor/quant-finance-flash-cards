# Hyperparameter

**Topic:** Computational Finance
**Tags:** hyperparameter, model selection, regularisation, learning rate, deep learning, machine learning
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

A **hyperparameter** is a configuration setting chosen *before* training that controls the learning process itself — such as learning rate, regularisation strength, or number of layers — as opposed to a **parameter** (weight or bias), which is a value learned from data by minimising the loss function.

## Key Formula

A model with parameters $\boldsymbol{\theta}$ and hyperparameters $\boldsymbol{\lambda}$ is trained by:

$$\hat{\boldsymbol{\theta}}(\boldsymbol{\lambda}) = \arg\min_{\boldsymbol{\theta}}\; \mathcal{L}_{\text{train}}(\boldsymbol{\theta};\,\boldsymbol{\lambda})$$

The hyperparameters $\boldsymbol{\lambda}$ are then chosen separately by minimising a validation loss:

$$\hat{\boldsymbol{\lambda}} = \arg\min_{\boldsymbol{\lambda}}\; \mathcal{L}_{\text{val}}\!\left(\hat{\boldsymbol{\theta}}(\boldsymbol{\lambda})\right)$$

This two-level optimisation — inner loop over $\boldsymbol{\theta}$, outer loop over $\boldsymbol{\lambda}$ — is why hyperparameters cannot be set by gradient descent on training data: evaluating $\hat{\boldsymbol{\theta}}(\boldsymbol{\lambda})$ requires completing a full training run first.

Common hyperparameter types in financial ML:

| Type | Examples |
|---|---|
| Architecture | number of layers, hidden units, attention heads |
| Training | learning rate $\eta$, batch size, number of epochs |
| Regularisation | L2 penalty $\lambda$, dropout rate $p$, weight decay |
| Algorithm | tree depth, number of estimators, kernel bandwidth |

## Example

A gradient-boosted model for credit default prediction has three hyperparameters: learning rate $\eta = 0.05$, tree depth $d = 5$, and L2 regularisation $\lambda = 1.0$. These are fixed before fitting. During training, the 500 tree weights are learned to minimise log-loss on the training set. Changing $\eta$ from 0.05 to 0.1 does not update any weights directly — it changes *how fast* the weights are updated, producing a different $\hat{\boldsymbol{\theta}}$ entirely.

## Remember

The parameter/hyperparameter distinction matters acutely in quant finance because it determines *where* the look-ahead bias enters. Parameters are learned from data — they cannot introduce future information if the training set is correctly windowed. Hyperparameters are chosen by the practitioner, often informally, on the basis of full backtest performance — and this is where silent over-fitting hides. A model whose hyperparameters (depth, regularisation, features used) were selected by repeatedly inspecting the same backtest period has effectively been optimised on test data, inflating the reported Sharpe ratio without any technical mistake in the training loop. The fix is to treat hyperparameter selection with the same walk-forward discipline as parameter estimation.
