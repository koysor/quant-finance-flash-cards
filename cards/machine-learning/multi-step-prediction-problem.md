# Multi-Step Prediction Problem

**Topic:** Machine Learning
**Tags:** multi-step prediction, n-step return, prediction horizon, recursive forecast, direct forecast, reinforcement learning
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **multi-step prediction problem** is the challenge of estimating a quantity $h > 1$ steps ahead, balancing two opposing forces: using more future steps reduces reliance on a (potentially inaccurate) bootstrap estimate but accumulates more noise and reward variance. In reinforcement learning the target is the $h$-step discounted return; in financial time-series forecasting the target is the return or price at holding horizon $h$.

## Key Formula

**$n$-step return** (RL context) — blend of real rewards and a bootstrap tail:

$$G_t^{(n)} = \sum_{k=0}^{n-1} \gamma^k R_{t+k+1} + \gamma^n V(S_{t+n})$$

As $n \to \infty$ (Monte Carlo): no bootstrap bias, maximum variance.  
As $n \to 1$ (TD(0)): minimum variance, maximum reliance on $V$.

**Direct forecast** (time-series context) — train a separate model per horizon, no error compounding:

$$\hat{x}_{t+h} = f_h(\mathbf{x}_t), \qquad h = 1, 2, \ldots, H$$

**Recursive forecast** — iterate a one-step model, compounding errors:

$$\hat{x}_{t+h} = f\!\left(\hat{x}_{t+h-1},\, \hat{x}_{t+h-2}, \ldots\right)$$

## Example

A TDBP option pricer trains each network against its immediate ($n=1$) neighbour. Suppose a $5$-step variant is tested for a European option (zero intermediate rewards):

$$G_t^{(5)} = \gamma^5 V(S_{t+5})$$

This is just the discounted network output 5 days later. Larger $n$ means each early-stage network sees payoff information from 5 steps ahead rather than 1, potentially converging faster — but requires path data of at least 5 steps and a reliable network at $t+5$ before training can start for earlier steps.

| $n$ | Bias | Variance | Dependency on later networks |
|---|---|---|---|
| 1 (TD) | High | Low | Only next step |
| 5 | Medium | Medium | 5 steps forward |
| $T$ (MC) | Low | High | Full trajectory |

## Remember

In TDBP, choosing $n = 1$ is an architectural decision: it allows backward induction one step at a time without running full trajectories. For exotic path-dependent payoffs (Asian, barrier) where intermediate rewards are non-zero, larger $n$ passes richer target information to earlier networks, potentially reducing training iterations at the cost of longer path requirements. In equity alpha research, the same trade-off appears as signal horizon choice: a 1-day return label has high noise but large sample size; a 20-day label is smoother but forces use of non-overlapping windows, shrinking the training set by a factor of 20. Getting the horizon right is typically the difference between a strategy that paper-trades well and one that generates real alpha.
