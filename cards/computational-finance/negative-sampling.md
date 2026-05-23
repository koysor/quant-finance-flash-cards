# Negative Sampling

**Topic:** Computational Finance
**Tags:** word2vec, nlp, training efficiency, word embeddings, neural networks, optimisation
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Negative sampling** is a training approximation used in Word2Vec that replaces the computationally expensive full softmax over the entire vocabulary with a binary classification problem: for each observed word–context pair, the model is trained to distinguish it from a small number of randomly drawn "negative" word pairs. This makes training on large corpora tractable.

## Key Formula

Instead of maximising $P(w_c \mid w_t)$ with a full softmax denominator summing over all $|V|$ words, the negative sampling objective maximises:

$$\mathcal{L}_{\text{NS}} = \log \sigma\!\left(\mathbf{v}_{w_c}^\top \mathbf{v}_{w_t}\right) + \sum_{k=1}^{K} \mathbb{E}_{w_k \sim P_n}\!\left[\log \sigma\!\left(-\mathbf{v}_{w_k}^\top \mathbf{v}_{w_t}\right)\right]$$

where $\sigma$ is the sigmoid function, $K$ is the number of negative samples (typically 5–20), and $P_n(w) \propto f(w)^{3/4}$ is the noise distribution — word unigram frequency raised to the $\tfrac{3}{4}$ power, which over-samples rare words relative to their frequency.

## Example

Training on the pair ("stock", "market") with $K = 3$ negative samples:

| Pair | Label | $\sigma(\mathbf{v}_c^\top \mathbf{v}_t)$ | Gradient direction |
|---|---|---|---|
| ("stock", "market") | 1 — real | 0.85 | Push vectors closer |
| ("stock", "banana") | 0 — fake | 0.12 | Push vectors apart |
| ("stock", "rainfall") | 0 — fake | 0.08 | Push vectors apart |
| ("stock", "purple") | 0 — fake | 0.06 | Push vectors apart |

Each update touches only $K + 1$ embedding rows rather than all $|V|$ rows, reducing per-step cost from $O(|V|)$ to $O(K)$.

## Remember

Negative sampling is what made Word2Vec fast enough to train on billions of financial news articles and SEC filings. Without it, updating the full vocabulary softmax for every training step would be computationally prohibitive. The $\tfrac{3}{4}$-power noise distribution is a deliberate design choice: raising frequency to $\tfrac{3}{4}$ (rather than 1) gives rare financial terms like "haircut" or "repo" a better chance of being selected as negatives, which improves their embedding quality because they receive more gradient signal than their raw frequency would otherwise permit.
