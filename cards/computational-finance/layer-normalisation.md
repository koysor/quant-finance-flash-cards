# Layer Normalisation

**Topic:** Computational Finance
**Tags:** normalisation, transformers, deep learning, training stability, nlp, bert
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Layer Normalisation (LayerNorm)** is a technique that normalises the activations across the feature dimension within a single training example, making each layer's inputs have zero mean and unit variance before applying learned scale ($\gamma$) and shift ($\beta$) parameters, which stabilises and accelerates training of deep networks such as Transformers.

## Key Formula

For a single example with $d$-dimensional activation vector $\mathbf{x} \in \mathbb{R}^d$, compute the mean and variance across features:

$$\mu = \frac{1}{d}\sum_{i=1}^{d} x_i, \qquad \sigma^2 = \frac{1}{d}\sum_{i=1}^{d}(x_i - \mu)^2$$

Then normalise and rescale:

$$\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2 + \varepsilon}}, \qquad y_i = \gamma \hat{x}_i + \beta$$

where $\varepsilon \approx 10^{-5}$ prevents division by zero, and $\gamma, \beta \in \mathbb{R}^d$ are learnable parameters that allow the network to undo the normalisation if the task requires it. Unlike **Batch Normalisation**, which normalises across the batch dimension, LayerNorm operates independently on each example — making it well-suited to variable-length sequences.

## Example

A Transformer processing an earnings transcript has a hidden state $\mathbf{x} = [2.1,\; -0.8,\; 3.4,\; 0.1]$ after attention ($d = 4$):

$$\mu = \frac{2.1 - 0.8 + 3.4 + 0.1}{4} = 1.2, \qquad \sigma^2 = \frac{(0.9)^2 + (-2)^2 + (2.2)^2 + (-1.1)^2}{4} = 2.915$$

$$\hat{\mathbf{x}} = \left[\frac{0.9}{1.707},\; \frac{-2.0}{1.707},\; \frac{2.2}{1.707},\; \frac{-1.1}{1.707}\right] \approx [0.53,\; -1.17,\; 1.29,\; -0.64]$$

With $\gamma = \mathbf{1}$ and $\beta = \mathbf{0}$ (initial values), the output is $\hat{\mathbf{x}}$ directly. The network learns $\gamma$ and $\beta$ from data.

## Remember

LayerNorm is why **BERT and GPT can be trained at all** on financial text. Without it, gradients in 12- or 96-layer Transformers would either explode or vanish — making convergence impossible at the scale needed to process millions of SEC filings. The "Add & Norm" block in each Transformer layer applies a residual connection followed by LayerNorm, keeping gradient magnitudes stable regardless of depth. When fine-tuning FinBERT on labelled sentiment data, LayerNorm's learned $\gamma$ and $\beta$ parameters are updated alongside the attention weights — they are not frozen — because the distribution of financial activations differs from the general-domain pre-training distribution.
