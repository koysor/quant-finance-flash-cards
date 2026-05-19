# Rotary Positional Encoding

**Topic:** Computational Finance
**Tags:** rotary positional encoding, rope, transformer, relative position, llm
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Rotary Positional Encoding (RoPE)** encodes the absolute position of a token by rotating its query and key vectors in embedding space. The key property is that the inner product between a rotated query at position $m$ and a rotated key at position $n$ depends only on the **relative offset** $m - n$, not on absolute positions. This makes attention naturally relative without adding extra parameters, and enables generalisation to sequence lengths beyond those seen during training.

## Key Formula

For a 2D subspace of the query vector, define the rotation matrix at position $p$:

$$R_\theta^p = \begin{pmatrix} \cos p\theta & -\sin p\theta \\ \sin p\theta & \cos p\theta \end{pmatrix}$$

Apply independently to each pair of dimensions with frequency $\theta_i = 10000^{-2i/d}$. The rotated inner product satisfies:

$$\langle R_\theta^m \mathbf{q},\; R_\theta^n \mathbf{k} \rangle = \langle \mathbf{q},\; R_\theta^{n-m} \mathbf{k} \rangle$$

The attention score between positions $m$ and $n$ is a function of $m - n$ only — **translation equivariance** is built in by construction. RoPE is used in LLaMA, GPT-NeoX, and Mistral in place of the sinusoidal encodings from the original transformer.

## Example

A transformer trained on financial news articles of up to 512 tokens is applied at inference to an annual report of 4,096 tokens. Absolute sinusoidal encodings (positions 513–4,096) were never seen during training, causing significant performance degradation. With RoPE, the model only ever sees the rotation $R_\theta^{m-n}$ between two positions — it never attends to "position 3,000" in isolation. Because the rotation frequencies $\theta_i$ are fixed and periodic, the model can extrapolate to unseen relative distances much more gracefully, enabling reliable extraction of financial information from long filings.

## Remember

RoPE is the standard positional encoding for modern large language models applied to long financial documents — annual reports, prospectuses, regulatory filings — where the document length at inference time may exceed the training context window. Absolute encodings (sinusoidal or learnable) break because the model has no training signal for absolute positions beyond the training length. RoPE's relative structure is also theoretically motivated: in finance, the relevance of two sentences typically depends on how far apart they are (nearby sentences discuss the same topic) rather than their absolute positions in the document. This relative inductive bias aligns well with the sequential structure of earnings call transcripts and regulatory filings, where material information is clustered by section rather than distributed uniformly across positions.
