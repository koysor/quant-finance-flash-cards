# Batch vs Layer Normalisation for Sequential Financial Data

**Topic:** Machine Learning
**Tags:** batch normalisation, layer normalisation, rnn, lstm, sequential data, non-stationarity, financial neural networks
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Batch normalisation (BN)** normalises activations across the batch dimension; **layer normalisation (LN)** normalises across the feature dimension of a single sample. For sequential financial data — time series, RL trajectories, option paths — this distinction is critical: BN's batch statistics become unreliable under non-stationarity, while LN normalises each sample independently and remains valid when batch size equals one.

## Key Formula

For a layer with activations $\mathbf{h} \in \mathbb{R}^d$ at position $t$ in a sequence:

**Batch norm** (statistics across batch $\mathcal{B}$):
$$\hat{h}_i = \frac{h_i - \mu_{\mathcal{B},i}}{\sqrt{\sigma^2_{\mathcal{B},i} + \epsilon}}, \qquad \mu_{\mathcal{B},i} = \frac{1}{\lvert\mathcal{B}\rvert}\sum_{b \in \mathcal{B}} h_i^{(b)}$$

**Layer norm** (statistics across features of one sample):
$$\hat{h}_i = \frac{h_i - \mu_t}{\sqrt{\sigma^2_t + \epsilon}}, \qquad \mu_t = \frac{1}{d}\sum_{i=1}^{d} h_i$$

Both apply learned scale $\gamma_i$ and shift $\beta_i$ after normalisation.

## Example

A recurrent network prices options along a simulated path, processing one $(S_t, \tau, \sigma_t)$ state at a time (batch size = 1 at inference). With BN: the running mean tracked during training may reflect a bull-market distribution; at inference in a crisis regime, the crisis activations are normalised by stale bull-market statistics — introducing systematic bias into every price estimate. With LN: each state vector is normalised by its own feature statistics, so the inference path is completely independent of training batch statistics.

## Remember

The rule of thumb for financial neural networks: use **batch norm for feedforward networks trained on i.i.d. cross-sectional data** (e.g. classifying earnings sentiment across many independent documents) and **layer norm for recurrent networks, Transformers, and any model evaluated one time step at a time** (e.g. TDBP, RNN hedgers, attention-based option pricers). The deeper issue is that financial return distributions are non-stationary — the batch statistics BN computes during training do not represent the test distribution after a regime change, while LN's per-sample normalisation is immune to this shift because it never uses statistics from other samples.
