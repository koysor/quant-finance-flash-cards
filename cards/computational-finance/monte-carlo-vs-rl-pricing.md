# Monte Carlo Simulation vs Reinforcement Learning

**Topic:** Computational Finance
**Tags:** monte carlo, reinforcement learning, option pricing, inference speed, value function, bellman equation
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Both **Monte Carlo (MC) simulation** and **Reinforcement Learning (RL)** use simulated paths to price derivatives, but they use those paths at different stages. MC averages payoffs over many paths at **inference time** — every new pricing request requires a fresh batch of simulations. RL learns the value function from paths during **training** and prices instruments in a single network forward pass at inference, amortising the simulation cost over all future queries.

## Key Formula

**Monte Carlo** pricing — average discounted payoffs across $N$ paths:

$$\hat{V}_0 = e^{-rT}\,\frac{1}{N}\sum_{i=1}^{N} g\!\left(S_T^{(i)}\right), \qquad \text{standard error} \propto \frac{1}{\sqrt{N}}$$

**RL (TDBP)** pricing — learn the value function by minimising the Bellman residual:

$$\mathcal{L}(\theta_t) = \mathbb{E}\!\left[\Bigl(f_t(S_t;\theta_t) - e^{-r\Delta t}\,f_{t+1}(S_{t+1};\theta_{t+1})\Bigr)^2\right]$$

After training, inference is: $\hat{V}_0 = f_0(S_0;\,\theta_0)$ — one forward pass, no simulation.

| Property | Monte Carlo | RL (TDBP) |
|---|---|---|
| Training cost | None | High (one-off) |
| Inference cost | High ($N$ paths) | Negligible (1 forward pass) |
| Error rate | $O(1/\sqrt{N})$ per query | Amortised over all queries |
| Path-dependent payoffs | Natural | Natural |
| New payoff | Immediate | Requires retraining |

## Example

Pricing a 100-day barrier call $10{,}000$ times across different spot/vol inputs for a risk report:

- **MC** ($N = 50{,}000$ paths each): $10{,}000 \times 50{,}000 = 5 \times 10^8$ path steps — roughly 20 minutes on a single CPU core
- **RL (TDBP)**: 30-minute one-off training, then $10{,}000$ forward passes at $< 1\,\text{ms}$ each — total 10 seconds for the full report

For a single query MC is competitive; for a pricing surface of thousands of queries the RL agent is faster by three orders of magnitude.

## Remember

The MC vs RL trade-off is fundamentally about **amortisation**. If a desk needs to price one instrument once, MC is simpler, requires no training infrastructure, and its $O(1/\sqrt{N})$ error is well-understood by regulators. If the desk needs to price the same instrument continuously — for real-time Greeks, scenario grids, or XVA calculations — the RL training cost is repaid within the first few hundred queries. This is why RL option pricers are deployed on XVA and CVA desks where the same pricing function is called millions of times per day, but vanilla flow desks continue to use MC for one-off structured product pricing where model interpretability and auditability matter more than speed.
