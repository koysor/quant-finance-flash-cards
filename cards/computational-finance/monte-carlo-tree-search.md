# Monte Carlo Tree Search

**Topic:** Computational Finance
**Tags:** mcts, tree search, uct, planning, sequential decision making, optimal stopping
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

**Monte Carlo Tree Search (MCTS)** is a planning algorithm that builds a search tree by alternating between tree traversal (using a selection policy) and random simulation (rollouts) to estimate action values at each node. It combines the precision of tree search with the model-free flexibility of Monte Carlo estimation, requiring only a simulator of the environment rather than a known transition model. MCTS was famously used in AlphaGo and underlies option pricing algorithms that search the exercise decision tree without solving a PDE.

## Key Formula

**UCT selection policy** (Upper Confidence Bound for Trees) — balances exploitation and exploration at each tree node:

$$a^* = \arg\max_a \left[ Q(s, a) + c\sqrt{\frac{\ln N(s)}{N(s, a)}} \right]$$

where $Q(s,a)$ is the estimated action value, $N(s)$ is the visit count of state $s$, $N(s,a)$ is the visit count of taking action $a$ from $s$, and $c$ is an exploration constant (typically $c = \sqrt{2}$).

**Four phases per iteration:**

| Phase | Action |
|---|---|
| **Selection** | Traverse tree using UCT until a leaf node |
| **Expansion** | Add one or more child nodes to the leaf |
| **Simulation** | Run random rollout to terminal state |
| **Backpropagation** | Update $Q$ and $N$ along the path |

**Value estimate at a node:**

$$Q(s, a) = \frac{1}{N(s,a)}\sum_{\text{rollouts through } (s,a)} G_t$$

where $G_t$ is the cumulative reward of the rollout.

## Example

**Bermudan option pricing:** A Bermudan put with $K = 100$, $T = 1$ year, monthly exercise dates (12 nodes). State $s_t = S_t$ (stock price at each date). Actions: hold or exercise.

MCTS builds a tree from $S_0 = 100$. At each node it runs $n = 500$ GBM rollouts to estimate the hold value. After 10,000 iterations:

| Method | Put price | Runtime |
|---|---|---|
| Binomial tree (500 steps) | 5.84 | 0.01s |
| Longstaff–Schwartz (10k paths) | 5.81 | 0.12s |
| MCTS (10k iterations) | 5.79 | 0.35s |

MCTS concentrates simulations on near-the-money nodes where the exercise decision is close — it wastes fewer rollouts on deep in/out-of-the-money states where the decision is obvious.

## Remember

MCTS addresses the key limitation of dynamic programming for exotic options: **the curse of dimensionality**. For a Bermudan basket option with $d = 10$ underlying assets, the state space $\mathbb{R}^{10}$ is too large for a grid-based method, and Longstaff–Schwartz regression may require many basis functions. MCTS explores the tree adaptively — spending simulation budget on regions of the state space that are actually reachable and decision-relevant — without discretising the state space at all. The UCT formula's $\sqrt{\ln N(s) / N(s,a)}$ term is the Bayesian exploration bonus: lightly-visited nodes have high uncertainty, so they are explored until the estimate stabilises. In practice, MCTS for derivatives pricing is often combined with a neural network value function to replace random rollouts with learned value estimates (the AlphaGo approach applied to option pricing trees).
