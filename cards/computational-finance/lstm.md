# LSTM (Long Short-Term Memory)

**Topic:** Computational Finance
**Tags:** lstm, recurrent neural network, time series, sequence modelling, gating, deep learning
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

A **Long Short-Term Memory (LSTM)** network is a type of recurrent neural network (RNN) that uses learnable **gates** to control what information is stored, forgotten, and output at each timestep, solving the vanishing-gradient problem that prevents plain RNNs from learning long-range dependencies in sequences.

## Key Formula

At each timestep $t$, the LSTM computes four quantities from the current input $\mathbf{x}_t$ and previous hidden state $\mathbf{h}_{t-1}$:

$$\mathbf{f}_t = \sigma(\mathbf{W}_f[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) \quad \text{(forget gate)}$$

$$\mathbf{i}_t = \sigma(\mathbf{W}_i[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i) \quad \text{(input gate)}$$

$$\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c) \quad \text{(candidate cell)}$$

$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t \quad \text{(cell state update)}$$

$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t), \quad \mathbf{o}_t = \sigma(\mathbf{W}_o[\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) \quad \text{(output)}$$

where $\odot$ is element-wise multiplication and $\sigma$ is the sigmoid function.

## Example

An LSTM is trained on 10 years of daily S&P 500 returns, volume, and VIX readings (3 features, sequence length 60 days). The forget gate learns to discard pre-crisis regimes when a new trend begins, while the cell state retains the long-run volatility level. On a held-out test period, a one-layer LSTM with 128 hidden units achieves a directional accuracy of 53% — enough to generate a positive Sharpe ratio after transaction costs when combined with position sizing.

## Remember

LSTMs are used in quantitative finance primarily for **time-series forecasting** where the signal depends on history beyond a short window: predicting next-day returns using the past 60 days of price and macro data, modelling intraday order-flow patterns, or forecasting credit-spread regimes. The gating mechanism is the key advantage over a plain feedforward network — the forget gate lets the model automatically discount stale information (e.g., pre-shock price levels) while retaining relevant context (e.g., trend direction). A practical limitation is that LSTMs are slower to train and harder to tune than Transformer-based models, which now dominate longer-horizon financial forecasting tasks.
