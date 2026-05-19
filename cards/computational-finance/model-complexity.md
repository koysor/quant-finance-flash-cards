# Model Complexity

**Topic:** Computational Finance
**Tags:** model complexity, vc dimension, bias-variance, overfitting, regularisation, capacity
**Created:** 2026-05-18
**Author:** Claude Sonnet 4.6

---

## Definition

**Model complexity** (or **capacity**) is a measure of the richness of the set of functions a model class can express; formally characterised by the **VC dimension** — the largest dataset size $h$ on which some model in the class can achieve zero training error for every possible labelling — and practically governed by the number of parameters, depth, or regularisation strength.

## Key Formula

The **VC bound** relates generalisation error to training error and model complexity:

$$R(f) \leq \hat{R}(f) + \sqrt{\frac{h\!\left(\ln\!\frac{2N}{h} + 1\right) - \ln\!\frac{\delta}{4}}{N}}$$

where $R(f)$ is the true risk, $\hat{R}(f)$ is the training error, $h$ is the VC dimension, $N$ is the number of training examples, and $\delta$ is the failure probability. The complexity penalty $\sqrt{h/N}$ quantifies the trade-off: higher $h$ allows a richer model but increases the gap between training and generalisation error. The **bias-variance decomposition** captures the same idea:

$$\mathbb{E}[\text{error}] = \text{Bias}^2 + \text{Variance} + \sigma^2_{\varepsilon}$$

Low complexity → high bias (underfitting); high complexity → high variance (overfitting).

## Example

VC dimensions for common financial ML model classes:

| Model | VC dimension $h$ |
|---|---|
| Linear classifier in $\mathbb{R}^d$ | $d + 1$ |
| Decision tree (depth $D$, $d$ features) | $\sim 2^D \cdot d$ |
| Neural network ($L$ layers, $W$ weights) | $O(W \log W)$ |
| RBF-SVM | $\infty$ (kernel-dependent) |

A linear model predicting credit default from 50 features has $h = 51$. Fitting it on $N = 500$ historical loans gives a complexity penalty of $\approx 0.35$, meaning the out-of-sample AUC could be up to 0.35 lower than the training AUC — a meaningful warning for production deployment.

## Remember

Model complexity is the theoretical underpinning of why over-fitted quant strategies fail out-of-sample. The VC bound makes precise what practitioners know informally: a model with too many parameters relative to the number of historical data points will find spurious patterns. In finance, $N$ is chronically small — a monthly rebalancing strategy with 20 years of data has only 240 observations — while feature sets are often large (hundreds of factors). This $h \gg N$ regime is where the complexity penalty dominates and where regularisation, feature selection, and early stopping earn their keep. The deflated Sharpe ratio is the financial industry's practical substitute for the VC bound: it adjusts the reported Sharpe downward in proportion to the number of trials (model configurations) tested, operationalising the same complexity-generalisation trade-off.
