# Optimal Execution

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** optimal execution, almgren-chriss, market impact, execution risk, implementation shortfall
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Optimal execution theory determines how to trade a large order over time to minimise the total cost of execution, balancing two competing forces: **market impact** (trading too fast moves the price against you) and **timing risk** (trading too slowly exposes you to adverse price movements while the order is incomplete). The Almgren-Chriss (2000) framework is the standard model, producing a trading trajectory that minimises a mean-variance objective over the execution horizon.

## Key Formula

The **Almgren-Chriss objective** minimises expected cost plus a risk penalty:

$$\min_{\{n_t\}} \; E[C] + \lambda \cdot \text{Var}[C]$$

where $\{n_t\}$ is the trading schedule, $C$ is total cost, and $\lambda$ is the risk aversion parameter.

The **optimal trading trajectory** for liquidating $X$ shares over $T$ periods is:

$$x_t = X \cdot \frac{\sinh\bigl(\kappa(T - t)\bigr)}{\sinh(\kappa T)}$$

where $\kappa = \cosh^{-1}\!\left(\frac{\sigma^2}{2\eta} + 1\right)$ balances permanent impact $\gamma$, temporary impact $\eta$, and volatility $\sigma$.

When $\lambda \to 0$ (risk-neutral), the solution is TWAP (linear liquidation). When $\lambda \to \infty$ (maximally risk-averse), all shares are sold immediately.

## Example

A fund must sell 500,000 shares over 5 hours. Market parameters: $\sigma = 1.5\%$ daily, temporary impact $\eta = 0.1$ bps per share, permanent impact $\gamma = 0.05$ bps per share.

With moderate risk aversion ($\lambda = 10^{-6}$), the optimal trajectory is front-loaded — selling more in the early intervals to reduce exposure to price risk:

| Hour | Shares remaining | Shares to sell |
|------|-----------------|---------------|
| 0–1 | 500,000 | 150,000 |
| 1–2 | 350,000 | 120,000 |
| 2–3 | 230,000 | 100,000 |
| 3–4 | 130,000 | 80,000 |
| 4–5 | 50,000 | 50,000 |

The front-loading reduces timing risk but increases market impact in the first hour. A risk-neutral trader would sell 100,000 per hour (TWAP).

## Remember

Optimal execution is where quantitative finance meets engineering at a hedge fund. The Almgren-Chriss model is the starting point, but production systems extend it with real-time order book data, intraday volume forecasts, and adaptive algorithms that re-optimise as conditions change. For a quant developer, implementing an execution management system (EMS) requires understanding the model's assumptions (linear impact, Gaussian returns) and their violations in practice (concave impact, fat tails, discrete order books). The key insight is that execution is not free — the implementation shortfall between paper returns and realised returns can consume 30–50% of a strategy's gross alpha, making execution quality as important as signal quality.
