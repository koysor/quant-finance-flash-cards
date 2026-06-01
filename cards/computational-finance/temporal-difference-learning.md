# Temporal Difference (TD) Learning

**Topic:** Computational Finance
**Tags:** reinforcement learning, td learning, bootstrapping, prediction, value function
**Author:** Gemini CLI

---

## Definition

**Temporal Difference (TD) Learning** is a reinforcement learning method that learns by updating its estimates based on other learned estimates, without waiting for the final outcome. This process of "learning a prediction from a prediction" is known as **bootstrapping**.

TD learning combines the ideas of Monte Carlo methods (learning from experience) and Dynamic Programming (bootstrapping). It updates the value of a state as soon as the next state and reward are observed.

## Key Formula

The simplest form, **TD(0)**, updates the value function $V(s_t)$ towards a target that includes the immediate reward $R_{t+1}$ and the discounted estimate of the next state's value:

$$V(s_t) \leftarrow V(s_t) + \alpha \underbrace{\left[ R_{t+1} + \gamma V(s_{t+1}) - V(s_t) \right]}_{\text{TD Error}}$$

where:
- $\alpha$ is the **learning rate**.
- The term in brackets is the **TD Error**, representing the difference between the new estimate and the old one.

## Example

Imagine predicting the closing price of a stock at the end of the day. A Monte Carlo approach waits until the market closes to update its model. A TD approach updates its prediction every hour (or even every tick) based on the price movement and its own updated prediction for the rest of the day.

## Remember (Finance application)

TD learning is highly efficient for financial time series because it allows an agent to learn intra-day or mid-sequence. In trading, this is like updating the valuation of a **forward start contract** as new market data arrives, rather than waiting for the contract to mature to see the final payoff. It enables "on-line" learning in rapidly changing markets.
