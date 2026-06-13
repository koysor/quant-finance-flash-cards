# Policy Evaluation vs Control

**Topic:** Machine Learning
**Tags:** policy evaluation, policy control, reinforcement learning, policy iteration, value iteration
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Policy evaluation** (the prediction problem) computes the value function $V^\pi$ for a *fixed* policy $\pi$ — it answers "how good is this strategy?" **Policy control** (the control problem) finds the *optimal* policy $\pi^*$ that maximises the value function — it answers "what is the best strategy?" Every RL algorithm alternates between these two tasks: evaluate the current policy, improve it, repeat.

## Key Formula

**Iterative policy evaluation** — repeatedly apply the Bellman expectation operator until convergence:

$$V_{k+1}(s) = \sum_a \pi(a \mid s) \sum_{s'} P(s' \mid s, a)\left[R(s,a) + \gamma V_k(s')\right]$$

**Policy improvement** — given $V^\pi$, the greedy improved policy is:

$$\pi'(s) = \arg\max_a \sum_{s'} P(s' \mid s, a)\left[R(s,a) + \gamma V^\pi(s')\right]$$

**Policy iteration** alternates evaluation and improvement until $\pi' = \pi$ (convergence guaranteed). **Value iteration** collapses both steps by using $\max_a$ directly in the Bellman update, reaching $V^*$ in one pass.

## Example

A daily rebalancing agent evaluates the "60/40 fixed-weight" policy: run iterative policy evaluation using a month of simulated transitions (state = factor scores, action = rebalance to 60/40, reward = Sharpe increment). This gives $V^{60/40}(s)$ for all states. Policy improvement then checks: is there any action $a$ such that $R(s,a) + \gamma V^{60/40}(s') > V^{60/40}(s)$? If yes, the policy is updated to prefer that action — e.g., tilting to 70/30 during high-momentum regimes. Repeating until no improvement gives the optimal policy $\pi^*$.

## Remember

The evaluation-vs-control distinction maps directly onto two practical questions quant researchers ask: "how well does this strategy perform?" (evaluation) and "what is the best strategy?" (control). In live trading systems, full policy iteration is rarely feasible because the transition model $P(s' \mid s, a)$ is unknown — instead, model-free algorithms like Q-learning and SARSA perform implicit policy improvement online, updating the policy after every trade rather than running full sweeps. Understanding this distinction is essential for debugging RL trading agents: a poorly converged value estimate (bad evaluation) will produce a suboptimal policy even with correct improvement steps.
