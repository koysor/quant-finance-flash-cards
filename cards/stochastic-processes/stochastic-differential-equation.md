# Stochastic Differential Equation

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** SDE, stochastic, differential equation, GBM, continuous time

---

## Definition

The **stochastic differential equation** (SDE) for asset prices is the continuous-time model that describes how prices evolve under both a deterministic drift and random fluctuations. It is the limiting form of the discrete random walk as the time step $\delta t \to 0$.

## Key Formula

$$dS = \mu S \, dt + \sigma S \, dX$$

where:
- $dS$ is the infinitesimal price change
- $\mu S \, dt$ is the drift (predictable growth)
- $\sigma S \, dX$ is the diffusion (random noise)
- $dX \sim N(0, dt)$ is a Wiener process increment

Changes are **proportional to the current price** $S$, producing percentage-style returns rather than fixed-size movements.

## Example

For a stock at $S = 100$ with $\mu = 0.10$ and $\sigma = 0.20$, over $dt = 0.01$ years:

- Drift contribution: $0.10 \times 100 \times 0.01 = £0.10$
- Diffusion contribution (if $dX = 0.1$): $0.20 \times 100 \times 0.1 = £2.00$

The random component dominates at short time scales, consistent with the square-root rule.

## Remember

This SDE is the single most important equation in quantitative finance. Applying Ito's Lemma to it yields the Black-Scholes PDE; discretising it gives the Monte Carlo simulation algorithm; and its parameters $\mu$ and $\sigma$ are the inputs to virtually every pricing and risk model.
