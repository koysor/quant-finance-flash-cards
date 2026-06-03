# Conditional Expectations in Trading

**Topic:** Computational Finance
**Tags:** conditional expectation, filtration, reinforcement learning, option pricing, trading signals
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

In trading and RL-based pricing, the **conditional expectation** $\mathbb{E}[X_T \mid \mathcal{F}_t]$ is the best estimate of a future payoff $X_T$ given all market information $\mathcal{F}_t$ available at time $t$. RL agents are fundamentally conditional expectation machines: the network learns to output $\mathbb{E}[\text{payoff} \mid \text{state}]$ from simulated or historical paths.

## Key Formula

$$\mathbb{E}[X_T \mid \mathcal{F}_t]$$

where $\mathcal{F}_t$ is the filtration (all information available up to time $t$). The tower property ensures consistency as information accumulates:

$$\mathbb{E}\!\left[\mathbb{E}[X_T \mid \mathcal{F}_t] \,\middle|\, \mathcal{F}_s\right] = \mathbb{E}[X_T \mid \mathcal{F}_s], \quad s \le t$$

In the TDBP model, each recursive step is one application of this identity:

$$P_t = e^{-r\Delta t}\,\mathbb{E}[P_{t+1} \mid \mathcal{F}_t]$$

## Example

A European call with $K = 100$ on a stock at $S_0 = 95$ has price $C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[\max(S_T - 100,0) \mid \mathcal{F}_0]$. After 50 days the stock rises to $S_{50} = 104$. The conditional expectation is recomputed using $\mathcal{F}_{50}$ — incorporating the new price, updated volatility, and reduced time — raising the option price. A trading agent acts on the difference between this updated expectation and the market quote.

## Remember

A profitable trading signal arises whenever the market price deviates from the trader's conditional expectation of the future payoff. RL pricing agents internalise this directly: the TDBP network at each time step $t$ is trained to output the risk-neutral conditional expectation $e^{-r\Delta t}\mathbb{E}^{\mathbb{Q}}[P_{t+1} \mid S_t]$, turning the abstract probability concept into a computable function of observable market state.
