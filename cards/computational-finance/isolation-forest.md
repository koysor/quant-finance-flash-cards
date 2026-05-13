# Isolation Forest

**Topic:** Computational Finance
**Tags:** isolation forest, anomaly detection, ensemble method, decision tree, unsupervised learning, outlier detection
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

An **isolation forest** detects anomalies by measuring how quickly an observation can be **isolated** by random binary splits. Normal observations are similar to many neighbours and require many splits to separate; anomalies are rare and distinct and are isolated in very few splits. The anomaly score is derived from the average path length across an ensemble of random trees.

## Key Formula

**Anomaly score** for observation $\mathbf{x}$:

$$s(\mathbf{x}, n) = 2^{-\,\mathbb{E}[h(\mathbf{x})] \,/\, c(n)}$$

where $h(\mathbf{x})$ is the path length in a tree (number of splits to isolate $\mathbf{x}$), $\mathbb{E}[h(\mathbf{x})]$ is the mean over the ensemble, and $c(n)$ is the expected path length for a dataset of size $n$:

$$c(n) = 2H(n-1) - \frac{2(n-1)}{n}, \qquad H(k) = \ln k + 0.5772$$

**Score interpretation:**
- $s \to 1$: very short path — anomalous
- $s \approx 0.5$: average path — normal
- $s \to 0$: very long path — deeply normal

## Example

Isolation forest trained on 5 years of daily equity market microstructure features (bid-ask spread, order imbalance, trade size, intraday volatility — 4 features, 1,250 days). Contamination parameter set to $0.01$ (expect 1% anomalies). Anomaly scores:

| Date | Score | Verdict |
|---|---|---|
| Normal trading day | $0.48$ | Normal |
| 9 August 2011 (US downgrade) | $0.91$ | Anomalous |
| 15 March 2020 (COVID crash) | $0.96$ | Anomalous |
| Pre-open auction spike | $0.73$ | Borderline |

## Remember

Isolation forest is the practical first choice for anomaly detection in financial tabular data because it requires no distributional assumption, scales linearly in both training and inference time (unlike kernel methods), and handles high-dimensional feature vectors without the reconstruction training required by autoencoders. Its key advantage over autoencoder-based detection is robustness: it does not require the normal data to be reconstructable by a neural network — useful when the "normal" regime itself is heterogeneous. The trade-off is interpretability: isolation forest gives a score but not a reconstruction, so it cannot explain *why* an observation is anomalous (which feature deviated). For financial surveillance where regulators require explanatory rationale, combine isolation forest screening with SHAP feature attribution on flagged observations.
