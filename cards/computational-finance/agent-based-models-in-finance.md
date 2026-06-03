# Agent-Based Models in Finance

**Topic:** Computational Finance
**Tags:** abm, market simulator, micro-structure, flash crash, emergent behaviour, abides
**Created:** 2026-06-03
**Author:** Gemini CLI

---

## Definition

An **Agent-Based Model (ABM)** is a computational simulation that models the financial market as a collection of autonomous "agents" (traders, market makers, speculators) who interact and compete based on specific behavioural rules. Unlike top-down equilibrium models (like Black-Scholes), ABMs are **bottom-up** systems where market phenomena, such as price formation and "flash crashes", emerge from the aggregate interactions of individual agents.

## Key Formula

There is no single "closed-form" formula for an ABM, as the system evolves through discrete simulation steps. The price at time $t+1$ is an emergent property of the agents' orders:

$$S_{t+1} = S_t + f(\text{OrderBook}_t, \{ \text{Agent}_i(\text{State}_t) \}_{i=1}^N)$$

where $\text{Agent}_i$ represents the decision logic of the $i$-th agent. Modern simulators like **ABIDES** (JP Morgan) use ML-trained agents whose objective is:

$$\max_{\pi_i} \mathbb{E} \left[ \sum_{t=0}^T R_t \right]$$

where $R_t$ is the agent's reward (e.g., P&L or market-making rebate).

## Example

The **Santa Fe Artificial Stock Market** was an early ABM that showed how price bubbles could form even when all agents are "rational", simply due to inductive learning and trend-following. In a more modern context, banks use the **ABIDES** simulator to test high-frequency trading (HFT) algorithms. By populating a simulated exchange with 1,000 "noise" traders and 10 "HFT" agents, researchers can observe how a specific HFT strategy might contribute to or prevent a **flash crash** under stressed liquidity conditions.

## Remember

ABMs are the "market simulators" used to train **Deep Hedging** and **RL Pricing** agents. They solve the "no perfect market simulator" challenge by providing a realistic environment that accounts for order book dynamics and market impact—features that are missing from standard stochastic processes. Their primary use in quantitative finance is for **stress testing** and understanding **market micro-structure** where traditional continuous-time mathematics fails.
