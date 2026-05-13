# Recurrent Neural Network

**Topic:** Computational Finance
**Tags:** rnn, recurrent neural network, hidden state, sequential data, vanishing gradient, time series
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **recurrent neural network (RNN)** is a neural network designed for sequential data in which the output at each time step depends on both the current input and a **hidden state** carried forward from the previous step. This feedback loop gives the network a form of memory, allowing it to model temporal dependencies — making it the natural architecture for financial time series.

## Key Formula

**Hidden state update** at time step $t$:

$$\mathbf{h}_t = g\!\left(\mathbf{W}_h \mathbf{h}_{t-1} + \mathbf{W}_x \mathbf{x}_t + \mathbf{b}\right)$$

**Output** at time step $t$:

$$\hat{\mathbf{y}}_t = g_{\text{out}}\!\left(\mathbf{W}_y \mathbf{h}_t + \mathbf{b}_y\right)$$

where $\mathbf{W}_h$, $\mathbf{W}_x$, $\mathbf{W}_y$ are weight matrices shared across all time steps, $\mathbf{b}$ is a bias vector, and $g$ is an activation function (typically $\tanh$).

**Vanishing gradient problem** — backpropagation through time (BPTT) multiplies the gradient by $\mathbf{W}_h$ at each step. If the largest eigenvalue $|\lambda_{\max}(\mathbf{W}_h)| < 1$, the gradient shrinks exponentially over $T$ steps:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{h}_0} \propto \mathbf{W}_h^T \to \mathbf{0} \quad \text{as } T \to \infty$$

This limits the effective memory of a vanilla RNN to roughly 10–20 time steps.

## Example

An RNN trained to predict next-day S&P 500 returns using the last 20 trading days (sequence length $T = 20$). Input features: daily return, volume, VIX, yield spread — 4 features per step. Hidden state size: 64. After training: the RNN captures momentum effects (positive autocorrelation at lag 1–5) but fails to capture the monthly rebalancing cycle (lag $\approx 22$) because the vanishing gradient prevents the network from retaining information over 20+ steps. An LSTM on the same data with $T = 60$ successfully captures the monthly pattern.

## Remember

The vanishing gradient problem is the principal reason vanilla RNNs have been largely superseded by LSTMs and GRUs in financial time series applications. Financial series have dependencies at multiple time scales simultaneously: intraday momentum (lags 1–5), weekly mean reversion (lags 5–25), monthly rebalancing flows (lags 20–25), and quarterly earnings cycles (lags 60–65). A vanilla RNN can only capture the shortest-scale dependencies reliably. In practice, use a vanilla RNN only as a baseline; for production models, the gating mechanism of the LSTM — which explicitly controls what to retain and what to forget in the hidden state — is required to capture the multi-scale temporal structure of financial data.
