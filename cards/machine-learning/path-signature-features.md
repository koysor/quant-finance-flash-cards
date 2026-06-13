# Path Signature Features

**Topic:** Machine Learning
**Tags:** path signature, rough path, feature engineering, time series, universal approximation, trading signals
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Path signature features** are the sequence of iterated integrals of a multivariate time series, derived from rough path theory. They provide a **universal, coordinate-free representation** of a path: any continuous functional of the path can be approximated by a linear map on a finite truncation of its signature. In quantitative finance this replaces hand-engineered technical indicators with a principled, theoretically grounded feature set.

## Key Formula

For a path $X = (X^1, \ldots, X^d): [0,T] \to \mathbb{R}^d$ (e.g. log-price, volume, bid-ask spread), the **signature** up to depth $N$ is the collection of iterated integrals:

$$S(X)^{i_1, i_2, \ldots, i_k}_{0,T} = \int_{0 < t_1 < \cdots < t_k < T} dX^{i_1}_{t_1}\cdots dX^{i_k}_{t_k}, \quad k = 1, \ldots, N$$

The depth-1 terms are the increments $\Delta X^i$; depth-2 terms $\int_0^T X^i_s\,dX^j_s$ encode covariation and trend; depth-3 terms encode higher-order dependencies. For $d$ channels and depth $N$, the signature has $(d^{N+1}-1)/(d-1)$ terms.

## Example

A trading signal is built from $(S_t, V_t, \text{bid-ask}_t)$ — a 3-channel path over 60-minute windows. Depth-3 signature gives $1 + 3 + 9 + 27 = 40$ features. A linear model (ridge regression) on these 40 features achieves an information coefficient (IC) of 0.048 on 5-minute S&P 500 returns — outperforming a hand-engineered set of 25 OHLCV technical indicators (IC = 0.031) with fewer features and no domain knowledge. The depth-2 cross-term $\int S\,dV$ encodes volume-weighted price movement, automatically discovering a VWAP-like feature.

## Remember

Path signatures are the feature engineering tool that rough path theory makes principled: the **Chen identity** $S(X \frown Y) = S(X) \otimes S(Y)$ (concatenation maps to tensor product) means signatures can be combined across windows, and the **universal approximation theorem for signatures** guarantees that no relevant path information is lost in a sufficiently deep truncation. In practice, depth 3–4 suffices for most financial signals, keeping the feature count manageable. The key advantage over RNNs for sequential financial data is **interpretability**: each signature term has a concrete financial meaning (e.g. second-order cross-terms capture momentum-volume interactions), and the model remains linear — auditable under SR 11-7 in a way that an LSTM is not.
