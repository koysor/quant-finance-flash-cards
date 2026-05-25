# Data Processing Inequality

**Topic:** Computational Finance
**Tags:** data processing inequality, mutual information, information theory, feature engineering, markov chain, pipeline
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

The **data processing inequality (DPI)** states that applying any deterministic or stochastic transformation to data cannot increase the mutual information it contains about a target variable. Processing can only destroy or preserve information — never create it.

## Key Formula

If $X \to Y \to Z$ forms a Markov chain (i.e. $Z$ depends on $X$ only through $Y$), then:

$$I(X; Z) \leq I(X; Y)$$

Equality holds if and only if $Z$ is a **sufficient statistic** of $Y$ for $X$ — that is, $Z$ captures all the information $Y$ has about $X$.

Equivalently for KL divergence: for any channel $p(y \mid x)$,

$$D_{\text{KL}}\!\left(p(x) \;\|\; q(x)\right) \geq D_{\text{KL}}\!\left(p(y) \;\|\; q(y)\right)$$

Transforming the data cannot make two distributions more distinguishable.

## Example

A factor model predicts stock returns $X$ from raw analyst forecasts $Y$. A pre-processing step PCA-reduces $Y$ to three components $Z$. The DPI guarantees $I(X; Z) \leq I(X; Y)$: the PCA step can retain all relevant information (if the discarded components are noise) or lose some (if they carried signal). The DPI makes this loss one-directional and irreversible — no further transformation of $Z$ can recover information already discarded.

A pipeline that first discretises a continuous factor into deciles, then applies a lookup table, satisfies $X \to \text{decile}(X) \to Z$: the DPI implies each step can only reduce information about the return.

## Remember

The data processing inequality is the information-theoretic argument against unnecessary feature transformations in quantitative factor research: every discretisation, normalisation, or dimensionality reduction step is a potential information sink. It explains why raw data (point-in-time prices, order book snapshots) tends to outperform heavily engineered features when model capacity is high — the model can learn the optimal transformation itself without the irreversible information loss from hand-crafted pre-processing. It also bounds the performance of any cascade of models: the final model in a pipeline cannot outperform the first model by more than the information the first model's output retains about the target. In practice, the DPI motivates checking mutual information $I(\text{feature}; \text{label})$ before and after each pipeline step to audit information loss.
