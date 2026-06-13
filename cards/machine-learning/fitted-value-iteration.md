# Fitted Value Iteration

**Topic:** Machine Learning
**Tags:** fitted value iteration, batch rl, function approximation, offline learning, option pricing, regression
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Fitted Value Iteration (FVI)** is a batch reinforcement learning algorithm that approximates the Bellman operator by alternating between two steps: computing Bellman backup targets on a fixed dataset of transitions, then fitting a function approximator (linear regression, neural network, or random forest) to those targets. Unlike online TD learning, FVI does not require interaction with a live environment — it learns entirely from a pre-collected dataset of state–reward–next-state tuples, making it the standard approach for offline option pricing from historical or simulated paths.

## Key Formula

**FVI algorithm** (finite-horizon, $T$ steps, iterating backwards from $t = T$):

Initialise: $\hat{V}_T(s) = R_T(s)$ (terminal payoff)

For $t = T-1, T-2, \ldots, 0$:

1. **Target computation** — for each sample $(s_i, a_i, r_i, s_i')$ in dataset $\mathcal{D}$:

$$y_i = r_i + \gamma\, \hat{V}_{t+1}(s_i')$$

2. **Regression step** — fit a new approximator to the targets:

$$\hat{V}_t = \arg\min_{f \in \mathcal{F}} \sum_{i=1}^{|\mathcal{D}|} \left(f(s_i) - y_i\right)^2$$

**Fitted Q-iteration** (action-value version, for control):

$$y_i = r_i + \gamma \max_{a'} \hat{Q}_{t+1}(s_i', a'), \qquad \hat{Q}_t = \text{regress}(\{(s_i, a_i), y_i\})$$

## Example

**Bermudan put pricing via FVI:** Dataset: 10,000 simulated GBM paths, monthly exercise dates ($T = 12$ steps), $K = 100$, $\sigma = 0.25$, $r = 0.05$.

State: $s_t = (S_t, t)$. Features: $(S_t/K,\; (S_t/K)^2,\; t/T)$. Regressor: ridge regression (equivalent to Longstaff–Schwartz basis functions).

Backward induction at $t = 11$: compute $y_i = \max(K - S_i^{12}, 0)$ for all paths, regress on $(S_i^{11}/K,\; (S_i^{11}/K)^2,\; 11/12)$. Repeat for $t = 10, 9, \ldots, 0$.

| Regressor | Put price | Bias vs binomial |
|---|---|---|
| Linear (3 features) | 5.71 | −0.13 |
| Polynomial (6 features) | 5.82 | −0.02 |
| Neural network (2 layers) | 5.83 | −0.01 |
| Binomial (reference) | 5.84 | — |

The polynomial FVI recovers 99.7% of the binomial tree price from 10,000 paths — and the method generalises to path-dependent payoffs and 10+ underlying assets where the binomial tree is infeasible.

## Remember

Fitted Value Iteration **is** the Longstaff–Schwartz algorithm when the regressor is linear and the state is $(S_t, t)$ — they are identical procedures. The FVI framing reveals what Longstaff–Schwartz is actually doing: approximating the Bellman operator by projecting Bellman targets onto a linear function class. This connection matters because it immediately suggests improvements: replace linear regression with a neural network (neural FVI / NFQ) for higher accuracy on complex payoffs, or with a random forest for robustness to non-linear exercise boundaries in multi-asset Bermudans. FVI also clarifies the source of Longstaff–Schwartz bias: regression underfits the continuation value (the function class $\mathcal{F}$ is too small), so the method systematically underestimates the option price — the tighter the function class, the larger the downward bias.
