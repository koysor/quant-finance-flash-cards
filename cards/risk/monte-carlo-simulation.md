# Monte Carlo Simulation

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** Monte Carlo, simulation, random paths, pricing, risk

---

## Definition

**Monte Carlo simulation** is a computational method that generates thousands of possible future price paths by repeatedly applying the discrete random walk model with fresh random numbers. The resulting distribution of outcomes provides probability estimates for pricing, risk measurement, and scenario analysis.

## Key Formula

For each simulated path, at each time step:

$$S_{i+1} = S_i \left(1 + \mu \, \delta t + \sigma \, \phi \sqrt{\delta t}\right)$$

where $\phi \sim N(0,1)$ is drawn independently at every step. Repeat for $N$ paths (typically $N = 10{,}000$ or more) to build a distribution of $S(T)$.

## Example

Simulating 10,000 paths for a stock at $S_0 = 100$ with $\mu = 0.10$, $\sigma = 0.20$ over $T = 1$ year (252 daily steps) produces a fan of paths. At $T = 1$, the simulated prices form a lognormal distribution. The fraction of paths ending below £90 gives an estimate of $P(S(1) < 90)$.

## Remember

Monte Carlo is the workhorse of modern risk management — it computes Value at Risk, prices exotic options with path-dependent payoffs (barriers, lookbacks, Asians), and stress-tests portfolios under thousands of scenarios. Its accuracy improves with more paths, scaling as $1/\sqrt{N}$.
