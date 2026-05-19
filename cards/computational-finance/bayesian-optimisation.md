# Bayesian Optimisation

**Topic:** Computational Finance
**Tags:** hyperparameter, optimisation, gaussian process, acquisition function, model selection, machine learning
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Bayesian optimisation** is a sequential, sample-efficient strategy for finding the hyperparameter configuration $\boldsymbol{\lambda}^*$ that minimises an expensive black-box objective (such as cross-validation loss) by maintaining a probabilistic surrogate model — typically a Gaussian Process — that predicts the objective at unvisited points, then querying the next candidate where an **acquisition function** balances exploration and exploitation.

## Key Formula

The surrogate is a Gaussian Process $f(\boldsymbol{\lambda}) \sim \mathcal{GP}(\mu(\boldsymbol{\lambda}),\, k(\boldsymbol{\lambda}, \boldsymbol{\lambda}'))$, giving at any untested point a predictive distribution:

$$f(\boldsymbol{\lambda}) \mid \mathcal{D}_n \sim \mathcal{N}\!\left(\mu_n(\boldsymbol{\lambda}),\; \sigma_n^2(\boldsymbol{\lambda})\right)$$

The next hyperparameter configuration to evaluate is chosen by maximising the **Expected Improvement (EI)** acquisition function:

$$\text{EI}(\boldsymbol{\lambda}) = \mathbb{E}\!\left[\max\!\left(f^* - f(\boldsymbol{\lambda}),\; 0\right)\right]$$

where $f^* = \min_{i \leq n} f(\boldsymbol{\lambda}_i)$ is the best observed value so far. EI is high where the surrogate predicts a good mean (exploitation) or high uncertainty (exploration), resolving the trade-off automatically.

## Example

Tuning a gradient-boosted credit model with three hyperparameters: learning rate $\eta \in [0.001, 0.5]$, tree depth $d \in \{2, \ldots, 10\}$, L2 penalty $\lambda \in [10^{-3}, 10^2]$. Grid search over $10 \times 9 \times 20 = 1{,}800$ points requires 1,800 training runs. Bayesian optimisation finds a configuration within 3% of the grid-search optimum in only 40 evaluations — a 97% reduction in compute — because the GP surrogate steers search away from regions already shown to be poor.

## Remember

Bayesian optimisation is the standard approach when each function evaluation (a full training run on historical financial data) takes minutes to hours. It matters most for deep learning models fine-tuned on financial text — tuning FinBERT with 8 hyperparameters via random search over 200 runs is infeasible in a one-week research sprint, but Bayesian optimisation reaches near-optimal performance in 30–50 evaluations. The key practical constraint in finance is that the objective — out-of-sample Sharpe or validation AUC on a walk-forward window — must be computed on held-out data from the correct time period; plugging in backtest Sharpe calculated on the full history makes the surrogate model fit to look-ahead-biased noise.
