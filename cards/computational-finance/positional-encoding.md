# Positional Encoding

**Topic:** Computational Finance
**Tags:** positional encoding, transformer, sequence modelling, nlp, sinusoidal embedding
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Positional encoding** injects information about token order into a transformer, which is otherwise permutation-invariant because attention has no built-in notion of sequence position. Fixed sinusoidal encodings add a deterministic positional signal to each token embedding; learnable positional embeddings treat position as a learnable parameter. Without positional encoding, "revenue grew despite headwinds" and "headwinds grew despite revenue" would produce identical attention outputs.

## Key Formula

The original transformer uses fixed sinusoidal encodings. For position $p$ and embedding dimension $i$:

$$\text{PE}(p, 2i) = \sin\!\left(\frac{p}{10000^{2i/d}}\right), \qquad \text{PE}(p, 2i+1) = \cos\!\left(\frac{p}{10000^{2i/d}}\right)$$

where $d$ is the model dimension. Each dimension oscillates at a different frequency, so that the encoding at any position is unique and the relative offset $\text{PE}(p+k)$ can be expressed as a linear function of $\text{PE}(p)$, enabling the model to attend by relative position.

The token representation fed into the first attention layer is:

$$\mathbf{x}_p^{\text{input}} = \mathbf{e}_p + \text{PE}(p)$$

## Example

A transformer trained on 10 years of daily returns processes a sequence of 252 trading days. Without positional encoding, returns from day 1 and day 252 of the training year are indistinguishable by position — the model cannot learn that recent observations are more relevant than distant ones. Adding sinusoidal encodings with $d = 64$ dimensions creates unique, smoothly varying position fingerprints: days 250 and 251 have highly correlated encodings (nearby positions → similar vectors), whilst days 1 and 251 have near-orthogonal encodings, giving the model the raw material to weight recent observations differently from distant ones.

## Remember

Positional encoding is the reason transformer architectures can be applied to financial time series despite the attention mechanism being inherently order-agnostic. In practice, **learnable positional embeddings** (as used in BERT) outperform fixed sinusoidal ones for financial NLP on fixed-length inputs such as earnings call paragraphs, because they adapt to the statistical patterns in the training corpus — certain positions (e.g. the first sentence of an MD&A section) carry systematic information. For time-series prediction, **relative positional encodings** (e.g. RoPE or ALiBi) are preferred over absolute encodings because they generalise better to sequence lengths not seen during training, which matters when models trained on quarterly earnings data are applied to longer annual reports.
