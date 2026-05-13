# Gated Recurrent Unit

**Topic:** Computational Finance
**Tags:** gru, gated recurrent unit, hidden state, reset gate, update gate, time series
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gated Recurrent Unit (GRU)** is a simplified recurrent architecture that addresses the vanishing gradient problem of vanilla RNNs using two gates: an **update gate** that controls how much of the previous hidden state to carry forward, and a **reset gate** that controls how much past information to discard when computing a candidate state. The GRU achieves similar performance to the LSTM with fewer parameters and faster training.

## Key Formula

At each time step $t$, given input $\mathbf{x}_t$ and previous hidden state $\mathbf{h}_{t-1}$:

**Reset gate** (how much past to forget):
$$\mathbf{r}_t = \sigma\!\left(\mathbf{W}_r \mathbf{x}_t + \mathbf{U}_r \mathbf{h}_{t-1} + \mathbf{b}_r\right)$$

**Update gate** (how much of old state to keep):
$$\mathbf{z}_t = \sigma\!\left(\mathbf{W}_z \mathbf{x}_t + \mathbf{U}_z \mathbf{h}_{t-1} + \mathbf{b}_z\right)$$

**Candidate hidden state**:
$$\tilde{\mathbf{h}}_t = \tanh\!\left(\mathbf{W}_h \mathbf{x}_t + \mathbf{U}_h (\mathbf{r}_t \odot \mathbf{h}_{t-1}) + \mathbf{b}_h\right)$$

**New hidden state** (interpolation between old and candidate):
$$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

**Comparison with LSTM:**

| Architecture | Gates | Parameters | Typical use |
|---|---|---|---|
| Vanilla RNN | 0 | Fewest | Short sequences only |
| GRU | 2 (reset, update) | Moderate | Most financial series |
| LSTM | 3 (input, forget, output) | Most | Long sequences, complex patterns |

## Example

Predicting daily FX returns using a 30-day window (4 features: return, realised vol, interest rate differential, risk sentiment). GRU hidden size 64, LSTM hidden size 64, trained on 8 years of data.

| Model | Parameters | Validation RMSE | Training time |
|---|---|---|---|
| GRU | 18,600 | 0.0047 | 4.2 min |
| LSTM | 24,800 | 0.0046 | 5.8 min |

The GRU uses 25% fewer parameters and trains 38% faster with essentially identical accuracy — a common result on financial time series where the shorter-range temporal dependencies do not require the LSTM's additional cell state.

## Remember

In quantitative finance the GRU vs LSTM choice is an empirical hyperparameter decision, not a theoretical one. For daily financial series with moderate lookback windows (20–60 steps), GRUs consistently match LSTMs whilst being faster to train and easier to regularise — making GRUs the preferred default. LSTMs are warranted when the sequence contains very long-range dependencies: tick-by-tick microstructure data with order book patterns that only resolve over hundreds of ticks, or multi-year macroeconomic sequences where a regime shift 200 periods ago influences the current state. The update gate is the GRU's key innovation: when $z_t \approx 0$, the model keeps $\mathbf{h}_{t-1}$ unchanged — equivalent to the LSTM forget gate setting information to be retained indefinitely without decay.
