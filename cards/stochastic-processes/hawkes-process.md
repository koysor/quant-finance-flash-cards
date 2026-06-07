# Hawkes Process

**Topic:** Stochastic Processes
**Tags:** hawkes process, self-exciting, point process, clustering, order book, contagion
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Hawkes process** is a self-exciting point process in which each event temporarily raises the rate of future events: the conditional intensity $\lambda(t)$ jumps upward with every arrival and then decays back toward a baseline level $\mu$. Unlike the Poisson process (constant intensity) or Cox process (random but externally driven intensity), the Hawkes process generates endogenous clustering — bursts of activity caused by the events themselves, not by an external shock.

## Key Formula

The **conditional intensity** at time $t$ (the instantaneous rate of events, given history $\mathcal{H}_t$):

$$\lambda(t) = \mu + \sum_{t_i < t} \alpha\, e^{-\beta(t - t_i)}$$

where:
- $\mu > 0$ — baseline (background) intensity
- $\alpha > 0$ — jump size; each event raises $\lambda$ by $\alpha$ immediately
- $\beta > 0$ — decay rate; the excitation fades at rate $e^{-\beta s}$ over time $s$
- $t_i$ — times of past events

**Stationarity condition** (process does not explode): $\alpha / \beta < 1$, equivalently the **branching ratio** $n^* = \alpha/\beta < 1$.

**Mean intensity** (long-run average): $\bar{\lambda} = \mu / (1 - n^*)$.

## Example

An equity order book with baseline arrival rate $\mu = 10$ orders/second, excitation $\alpha = 5$, decay $\beta = 8$. Branching ratio $n^* = 5/8 = 0.625 < 1$ (stationary). Long-run mean: $\bar{\lambda} = 10/(1 - 0.625) = 26.7$ orders/second.

At $t = 0$, suppose three large orders arrive simultaneously (a block trade). The intensity immediately jumps to:

$$\lambda(0^+) = 10 + 3 \times 5 = 25 \text{ orders/s}$$

After 0.5 seconds with no further arrivals:

$$\lambda(0.5) = 10 + 15\,e^{-8 \times 0.5} = 10 + 15 \times 0.018 = 10.27 \text{ orders/s}$$

The burst of activity triggered by the block trade dissipates within half a second, consistent with the typical lifespan of order-book microstructure impact.

## Remember

The Hawkes process is the workhorse model for **high-frequency order book dynamics** because real trading activity clusters: a large order execution triggers market makers to update quotes, which triggers further reactions, creating a self-exciting cascade. Fitting $\mu$, $\alpha$, $\beta$ to tick data consistently produces branching ratios $n^* \approx 0.9$ in liquid equity markets, meaning roughly 90% of all orders are "endogenous" — triggered by previous orders — and only 10% are exogenous information-driven. This has a direct implication for market impact: a single large order excites many subsequent orders, temporarily elevating the effective bid-ask spread and increasing the cost of further execution. High-frequency market-making algorithms use Hawkes process fits to calibrate optimal quoting strategies, and regulators use the branching ratio as a fragility indicator — a market with $n^* \to 1$ is on the edge of an explosive feedback loop (a flash crash).
