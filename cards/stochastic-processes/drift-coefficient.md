# Drift Coefficient

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** drift, SDE, risk-neutral, mu, deterministic, continuous time
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

The **drift coefficient** is the function that multiplies the deterministic $dt$ term in a stochastic differential equation. It controls the expected rate of change of the process per unit time. In the standard asset price SDE $dS = \mu S \, dt + \sigma S \, dW$, the drift coefficient is $\mu S$ — the product of the expected return and the current price.

## Key Formula

For a general SDE:

$$dX = a(X, t) \, dt + b(X, t) \, dW$$

$a(X, t)$ is the **drift coefficient**. For geometric Brownian motion:

$$a(S, t) = \mu S$$

Under the **risk-neutral measure** $\mathbb{Q}$, the drift changes from $\mu S$ to $rS$:

$$dS = rS \, dt + \sigma S \, dW^{\mathbb{Q}}$$

where $r$ is the risk-free rate. This change of drift is the essence of the Girsanov theorem.

## Example

A stock at $S = 150$ has expected return $\mu = 0.08$ per annum and risk-free rate $r = 0.04$.

- **Real-world drift coefficient:** $a(150) = 0.08 \times 150 = £12.00$ per year
- **Risk-neutral drift coefficient:** $a^{\mathbb{Q}}(150) = 0.04 \times 150 = £6.00$ per year

Over $dt = 0.01$ years, the expected price change under the real-world measure is $12.00 \times 0.01 = £0.12$, while under the risk-neutral measure it is only £0.06.

## Remember

The drift coefficient is the part of the SDE that **disappears from option prices**. When deriving the Black-Scholes PDE, the delta-hedged portfolio eliminates the random term, and no-arbitrage forces the remaining deterministic growth to equal the risk-free rate — so the real-world drift $\mu$ is replaced by $r$. This is why you do not need to estimate expected returns to price options, only volatility.
