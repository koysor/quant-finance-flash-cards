# Agent-Based Models in Finance

**Topic:** Computational Finance
**Tags:** agent-based model, market microstructure, heterogeneous agents, emergent behaviour, simulation
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

An **agent-based model (ABM)** simulates a financial market as a system of interacting autonomous agents — traders, market makers, regulators — each following their own rules and responding to prices and information. Unlike equilibrium models, ABMs make no assumption that markets are in equilibrium; instead, macro-level phenomena (price dynamics, volatility clustering, flash crashes) emerge from micro-level interactions between heterogeneous agents.

## Key Formula

A typical agent $i$ updates its demand $d_i$ based on a mix of fundamental and trend-following signals:

$$d_{i,t} = w_i^f \cdot (V_i - P_t) + w_i^m \cdot \frac{P_t - P_{t-1}}{P_{t-1}} + \varepsilon_{i,t}$$

where $V_i$ is agent $i$'s private valuation, $P_t$ is the current price, $w_i^f$ weights fundamental trading, $w_i^m$ weights momentum trading, and $\varepsilon_{i,t}$ is noise. The market-clearing price is set by aggregating all agents' orders through an order book mechanism.

## Example

The 2010 Flash Crash ABM (Kirilenko et al.): a simulation with heterogeneous agents (fundamentalists, high-frequency traders, noise traders) reproduces the 9% Dow Jones drop in 36 minutes. When a large sell order triggers HFT market makers to withdraw liquidity simultaneously, the model produces a cascade identical in shape to the real event — despite no single agent "causing" the crash. No equilibrium model can generate this emergent instability.

## Remember

Agent-based models are the primary tool for studying systemic risk and market microstructure phenomena that equilibrium models cannot explain. The **Bank of England** and **ESMA** use ABMs to stress-test financial stability scenarios — simulating how fire sales, margin calls, and herding propagate through interconnected institutions. In quantitative trading, ABMs are used to simulate realistic order flow for training RL execution agents: instead of training on historical data, the agent learns in a synthetic market where adversarial HFT agents, noise traders, and momentum traders interact, producing richer and more stress-tested training environments than any historical replay.
