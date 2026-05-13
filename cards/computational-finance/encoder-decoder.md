# Encoder-Decoder Architecture

**Topic:** Computational Finance
**Tags:** encoder-decoder, seq2seq, sequence modelling, latent representation, forecasting, deep learning
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **encoder-decoder architecture** (also called seq2seq) processes a variable-length input sequence through an **encoder** network that compresses it into a fixed-length **context vector**, which a **decoder** network then uses to generate a variable-length output sequence. Originally designed for machine translation, it is applied in finance for multi-step return forecasting, yield curve scenario generation, and option path simulation.

## Key Formula

**Encoder** — reads input sequence $(\mathbf{x}_1, \ldots, \mathbf{x}_T)$ and produces context vector $\mathbf{c}$:

$$\mathbf{h}_t^{\text{enc}} = f_{\text{enc}}(\mathbf{x}_t, \mathbf{h}_{t-1}^{\text{enc}}), \qquad \mathbf{c} = \mathbf{h}_T^{\text{enc}}$$

**Decoder** — generates output sequence $(\hat{\mathbf{y}}_1, \ldots, \hat{\mathbf{y}}_{T'})$ conditioned on $\mathbf{c}$:

$$\mathbf{h}_t^{\text{dec}} = f_{\text{dec}}(\hat{\mathbf{y}}_{t-1}, \mathbf{h}_{t-1}^{\text{dec}}, \mathbf{c}), \qquad \hat{\mathbf{y}}_t = g(\mathbf{h}_t^{\text{dec}})$$

**With attention** — context vector is a weighted sum of all encoder hidden states, not just the last:

$$\mathbf{c}_t = \sum_{\tau=1}^{T} \alpha_{t\tau} \mathbf{h}_\tau^{\text{enc}}, \qquad \alpha_{t\tau} = \text{softmax}(\mathbf{h}_{t-1}^{\text{dec}} \cdot \mathbf{h}_\tau^{\text{enc}})$$

## Example

A seq2seq model for 5-day-ahead equity return forecasting. Encoder: 2-layer GRU reading a 60-day history of daily returns and risk factor scores (20 features). Context vector: 128-dimensional. Decoder: 1-layer GRU generating 5 sequential day-ahead return forecasts. The model is trained to minimise MSE on the 5-day forecast window simultaneously. On a held-out test year: the encoder-decoder achieves a 5-day directional accuracy of 56% versus 52% for 5 independent single-step GRUs — the shared context vector allows the decoder to maintain coherent cross-day forecasts (e.g., momentum that builds over days 1–3 is consistently reflected in days 4–5).

## Remember

The encoder-decoder architecture is the natural solution when the output horizon has a different length from the input window, or when outputs at different future steps should be jointly consistent. In quantitative finance, the critical advantage over fitting one model per horizon is **cross-horizon coherence**: a standalone 5-day model is unrelated to a standalone 1-day model, so combining their predictions can produce scenarios where the 5-day return is inconsistent with the sequence of 1-day returns. An encoder-decoder generates all horizons from the same context vector, enforcing internal consistency. The bottleneck limitation — compressing all relevant history into a single fixed-size vector — is addressed by adding attention, which allows the decoder to selectively attend to the most relevant past time steps at each forecast horizon (e.g., attending to the most recent volatility spike when forecasting near-term returns).
