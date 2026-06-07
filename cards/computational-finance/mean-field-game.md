# Mean-Field Game

**Topic:** Computational Finance
**Tags:** mean-field game, nash equilibrium, agent interactions, systemic risk, order flow, competitive execution
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **mean-field game (MFG)** is the limiting model for a large population of $N \to \infty$ strategically interacting agents, where each agent optimises its own objective against the aggregate ("mean-field") distribution of all other agents' states and actions, rather than tracking each opponent individually. Introduced by Lasry–Lions and Huang–Malhamé–Caines (2006), MFGs reduce an intractable $N$-player game to a fixed-point problem between a single representative agent and the population distribution.

## Key Formula

An MFG is characterised by a coupled system of two PDEs:

**Hamilton–Jacobi–Bellman** (backward in time — value function of the representative agent):

$$-\partial_t V + H(x, \nabla_x V, m) = 0, \quad V(x, T) = g(x, m_T)$$

**Fokker–Planck** (forward in time — evolution of the population distribution $m$):

$$\partial_t m - \nu\,\Delta m - \nabla_x \cdot (m\, \nabla_p H) = 0, \quad m(x, 0) = m_0$$

**MFG equilibrium:** a pair $(V^*, m^*)$ such that:
1. $V^*$ is the value function for a representative agent facing distribution $m^*$
2. $m^*$ is the distribution induced when all agents follow the policy $\pi^* = \nabla_p H(\cdot, \nabla V^*, m^*)$

In discrete/RL settings, the fixed point is computed iteratively: solve agent's MDP given current $m$, update $m$ using agents' induced policies, repeat until convergence.

## Example

**Competitive liquidation (Predatory Trading):** $N = 200$ institutional traders each need to liquidate $Q_0 = 10{,}000$ shares before $T = 1$ day. Each trader's execution causes market impact $\eta \sum_j a_j^t$ (proportional to total market sell pressure). Single-agent optimal solution: sell at uniform rate $10{,}000/T$. But at MFG equilibrium, each trader front-runs the others:

| Horizon $\tau$ | Single-agent rate | MFG equilibrium rate |
|---|---|---|
| $\tau = T$ | 10,000/day | 10,000/day |
| $\tau = 0.5T$ | 10,000/day | 14,200/day (accelerated) |
| $\tau = 0.1T$ | 10,000/day | 31,600/day (fire sale) |

The MFG equilibrium generates a **fire sale**: each agent accelerates liquidation to avoid the impact from others accelerating — a self-fulfilling crash consistent with observed market liquidity spirals.

## Remember

Mean-field games formalise why **individually rational behaviour can be collectively catastrophic** in financial markets. The fire-sale equilibrium is not caused by irrationality — each trader is optimising correctly given the others' strategies. The MFG framework also underlies **systemic risk models**: when banks' balance sheet decisions interact through asset price channels, the MFG equilibrium predicts pro-cyclical deleveraging spirals that no individual bank has an incentive to avoid. In practice, the regulator's role is to shift the MFG equilibrium — capital buffers and leverage limits change the Hamiltonian $H$ so that the new fixed point has less aggregate impact. For the CQF, the key result is that the MFG liquidation equilibrium is always *worse* (higher total market impact) than the socially optimal coordinated solution, with the gap growing as $N$ increases — the tragedy of the commons applied to liquidity.
