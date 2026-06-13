# TRPO (Trust Region Policy Optimisation)

**Topic:** Machine Learning
**Tags:** trpo, trust region, policy gradient, kl divergence, deep reinforcement learning, constrained optimisation
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

**TRPO (Trust Region Policy Optimisation)** is a policy gradient algorithm that constrains each update so the new policy stays within a "trust region" — a ball of bounded KL divergence from the current policy. This prevents the destructively large updates that collapse training in standard policy gradient methods, at the cost of requiring second-order optimisation (conjugate gradient) to solve the constrained problem exactly.

## Key Formula

TRPO maximises a surrogate objective subject to a KL constraint:

$$\max_\theta \;\mathcal{L}(\theta) = \mathbb{E}_t\!\left[\frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_\text{old}}(a_t \mid s_t)}\hat{A}_t\right]$$

$$\text{subject to} \quad D_{\text{KL}}\!\left(\pi_{\theta_\text{old}} \,\|\, \pi_\theta\right) \leq \delta$$

where $D_{\text{KL}}(\pi_{\text{old}} \| \pi) = \mathbb{E}_s\!\left[\sum_a \pi_{\text{old}}(a\mid s)\log\dfrac{\pi_{\text{old}}(a\mid s)}{\pi(a\mid s)}\right]$ is the KL divergence and $\delta \approx 0.01$ is the trust region radius. The constraint is enforced via conjugate gradient to compute the natural policy gradient, followed by a backtracking line search.

## Example

A TRPO agent learns to allocate between equities and bonds (continuous action: weight $w \in [0,1]$). Standard policy gradient occasionally proposes $\Delta w = 0.6$ (jumping from 30% to 90% equities), destabilising the policy. TRPO's KL constraint with $\delta = 0.01$ limits this to roughly $\Delta w \leq 0.05$ per update — the agent learns cautiously and converges to a stable allocation policy in 500 iterations. PPO achieves similar stability in 600 iterations with only first-order optimisation, making it the preferred practical alternative.

## Remember

TRPO provided the theoretical foundation for safe policy updates in deep RL: its monotonic improvement guarantee states that if the KL constraint is satisfied, the true policy performance cannot decrease. PPO achieves a similar result approximately by clipping the probability ratio instead of solving the KL-constrained optimisation exactly — trading mathematical rigour for computational tractability. In quantitative finance, TRPO's natural policy gradient is equivalent to Fisher information matrix pre-conditioning, which adjusts gradient steps for the curvature of the policy space rather than the parameter space — geometrically, it finds the steepest ascent in the space of distributions rather than in the space of neural network weights.

