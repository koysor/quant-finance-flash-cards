# Dynamic Programming

**Topic:** Machine Learning
**Tags:** dynamic programming, optimisation, value function, bellman equation, optimal control
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Dynamic programming (DP)** is a method for solving multi-stage optimisation problems by breaking them into overlapping sub-problems, solving each sub-problem once, and caching the results. The foundation is Bellman's *principle of optimality*: an optimal policy must remain optimal for the sub-problem starting from any state it reaches — so a global optimum can be built by stitching together locally optimal one-step decisions, working backwards from the terminal condition.

## Key Formula

For a discrete-time problem with state $s_t$, action $a_t$, reward $r_t$, discount factor $\gamma \in [0,1]$, and transition function $f$, the **DP backward recursion** is:

$$V_t(s) = \max_{a \in \mathcal{A}(s)} \left[ r_t(s, a) + \gamma\, V_{t+1}(f(s, a)) \right], \quad t = T-1, \ldots, 0$$

with terminal condition $V_T(s) = g(s)$ (e.g. terminal payoff or bequest function). In a stochastic setting the deterministic successor $f(s,a)$ is replaced by an expectation:

$$V_t(s) = \max_{a} \left\{ r_t(s, a) + \gamma\, \mathbb{E}\left[V_{t+1}(S_{t+1}) \mid S_t = s,\, A_t = a\right] \right\}$$

## Example

An investor must allocate \$100 across two assets over $T = 2$ periods. Let state $s_t$ = capital at time $t$; action $a_t$ = fraction invested in the risky asset; and reward $r_t(s, a) = s \cdot [a \cdot R^{\text{risky}} + (1-a) \cdot R^{\text{safe}}]$.

**Period 2 (terminal):** For each capital level, pick $a_2^*(s) = \arg\max r_2(s, a)$ and set $V_2(s) = r_2(s, a_2^*)$.

**Period 1 (backward step):** For each capital level $s$, compute:
$$V_1(s) = \max_{a} \bigl[ r_1(s, a) + \gamma\, V_2(f(s, a)) \bigr]$$

**Period 0 (decision):** Apply the recursion once more to find the globally optimal first action $a_0^*$.

Each backward pass is a simple one-period optimisation; the full $T$-period optimisation is never solved directly.

## Remember

Dynamic programming is the algorithmic backbone of sequential decision-making in quantitative finance. Backward induction on a binomial tree is discrete DP: terminal option payoffs seed $V_T$, and each backward step applies the Bellman recursion — with an early-exercise check for American options. The Hamilton-Jacobi-Bellman PDE is its continuous-time limit, underpinning Merton's portfolio problem and optimal execution models. In machine learning-driven trading, every reinforcement learning algorithm — Q-learning, PPO, SAC — is ultimately approximating the DP solution to a financial Markov decision process.
