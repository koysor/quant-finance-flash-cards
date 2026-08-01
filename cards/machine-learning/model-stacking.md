# Model Stacking

**Topic:** Machine Learning
**Tags:** ensemble learning, meta-model, blending, out-of-fold predictions, base learners, overfitting
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Stacking is an ensemble technique in which the predictions of several diverse base learners become the input features of a second-stage **meta-model** that learns how to combine them. Unlike averaging or majority voting, which apply fixed weights, the meta-model learns weights that vary with the observation.

## Key Formula

For $m$ base learners producing predictions on an unseen slice, the meta-feature matrix is $n \times m$:

$$\mathbf{z}_t = \left[\hat{p}^{(1)}_t,\ \hat{p}^{(2)}_t,\ \dots,\ \hat{p}^{(m)}_t\right], \qquad \hat{y}_t = g(\mathbf{z}_t;\ \boldsymbol{\theta})$$

The meta-model $g$ is deliberately simple — logistic regression, or a shallow gradient-boosted tree.

The critical requirement is that base predictions be generated on data the base learners never saw, otherwise the meta-model learns from over-confident in-sample predictions. Two designs achieve this:

| | Blending (single holdout) | Stacking (k-fold) |
|---|---|---|
| Data split | train / holdout / test | $k$ folds + test fold |
| Base fitting | once, on the train subset | $k$ times, once per fold |
| Meta-features | from one holdout set | out-of-fold for every sample |
| Suits | large data, quick prototyping | smaller data, more rigorous |

## Example

Three base learners predict the probability that tomorrow's return is positive:

$$\mathbf{z}_t = [\,\underbrace{0.71}_{\text{XGBoost}},\ \underbrace{0.43}_{\text{LSTM}},\ \underbrace{0.66}_{\text{logit}}\,] \ \longrightarrow\ g(\mathbf{z}_t) = 0.68$$

A simple mean would return $0.60$. The meta-model has learnt from the holdout that when the tree is confident and the LSTM disagrees, the tree is usually right in this regime — so it pulls the blend towards the tree rather than splitting the difference.

## Remember

Stacking works only when the base learners make **different mistakes**, which is why a mixture of model families — a tree ensemble, a linear model with Lasso, a recurrent network — beats three variants of the same algorithm however well tuned. In financial applications the two failure modes are specific and both concern data. Meta-model overfitting is severe when the holdout is small, since the meta-model sees only as many rows as the holdout has: regularise it, or reduce it to logistic regression. And the holdout size is a genuine trade-off rather than a tuning detail — every observation given to the meta-model is taken from base-learner training, and with financial series already short on independent observations, the split has to be chosen deliberately. Where returns are serially correlated, the folds must also be purged and embargoed, or out-of-fold predictions leak information across the boundary and the whole construction reports a performance it will not repeat.
