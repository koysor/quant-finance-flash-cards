# Parallel Simulation in Finance

**Topic:** Computational Finance
**Tags:** parallel simulation, vectorised environments, monte carlo, deep reinforcement learning, gpu, training speed
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Parallel simulation runs $N$ independent copies of a financial environment simultaneously — each with its own market state, position, and P&L — to generate $N$ independent experience trajectories per time step. It is the primary technique for scaling reinforcement learning and Monte Carlo pricing to practical training speeds, exploiting the fact that financial simulations (GBM paths, order book replays) are embarrassingly parallel and require no communication between instances.

## Key Formula

For $N$ parallel environments producing one step each, the effective sample rate is:

$$\text{Samples/second} = N \times f_{\text{env}} \times \eta_{\text{parallel}}$$

where $f_{\text{env}}$ is the single-environment step rate (steps/second) and $\eta_{\text{parallel}} \leq 1$ is the parallelisation efficiency (GPU: 0.85–0.99; CPU multi-process: 0.6–0.9 due to IPC overhead).

Monte Carlo convergence with $N$ parallel paths of length $T$:

$$\text{SE} = \frac{\sigma_{\text{payoff}}}{\sqrt{N \cdot T_{\text{independent}}}}$$

where the total independent samples grow linearly with $N$, halving standard error every time $N$ quadruples.

## Example

A delta-hedging RL agent requires 10 million environment steps to converge. Comparing parallelisation strategies:

| Setup | $N$ | Env steps/sec | Time to 10M steps |
|-------|-----|--------------|-------------------|
| Single CPU | 1 | 2,000 | 83 min |
| 16 CPU workers | 16 | 28,000 | 6 min |
| GPU vectorised (JAX) | 1,024 | 500,000 | 20 sec |

GPU vectorisation achieves 250× speedup over single-CPU by keeping the entire mini-batch computation on-device — no Python overhead, no inter-process communication. Libraries such as Brax (JAX) and Isaac Lab implement vectorised RL environments natively on GPU.

## Remember

Parallel simulation changes the economics of RL-based strategy research: a hyperparameter search that would take 3 days on a single CPU completes in 30 minutes on a GPU cluster. The key constraint is that each simulated environment must be **statistically independent** — correlated environments (e.g. all replaying the same historical path in lock-step) provide no extra information and inflate the apparent sample count. In financial RL, this means sampling different random seeds, different regime initialisations, or different historical windows for each parallel environment. For Monte Carlo option pricing, the same principle applies: parallel paths on a GPU evaluate thousands of payoffs simultaneously, making path-dependent exotic pricing (Asian, barrier, lookback) tractable in real-time risk management.

