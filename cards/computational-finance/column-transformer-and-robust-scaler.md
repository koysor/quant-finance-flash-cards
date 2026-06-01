# ColumnTransformer and RobustScaler

**Topic:** Computational Finance
**Tags:** preprocessing, feature scaling, outliers, scikit-learn, pipeline, data normalisation
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**`ColumnTransformer`** is a scikit-learn meta-estimator that applies different preprocessing transformations to different subsets of features in a single pipeline step. **`RobustScaler`** is a scaling transformer that centres and scales each feature using its median and interquartile range (IQR) rather than mean and standard deviation, making it resistant to outliers.

## Key Formula

For a feature column $\mathbf{x}$ with median $\tilde{x}$ and interquartile range $\text{IQR} = Q_3 - Q_1$, RobustScaler transforms each value as:

$$x_{\text{scaled}} = \frac{x - \tilde{x}}{\text{IQR}(\mathbf{x})}$$

Compare with StandardScaler, which uses $\mu$ and $\sigma$:

$$x_{\text{std}} = \frac{x - \mu}{\sigma}$$

A single extreme value shifts $\mu$ and inflates $\sigma$, compressing all other values toward zero. The median and IQR are unaffected by outliers beyond $Q_1$ and $Q_3$.

## Example

A credit default model uses three features: 1-year return (numeric, occasional extreme values during crises), debt-to-equity ratio (numeric, right-skewed with occasional values above 50), and sector (categorical, one-hot encoded). A `ColumnTransformer` applies `RobustScaler` to the two numeric columns and `OneHotEncoder` to the sector column, producing a clean combined feature matrix in one step. Without `RobustScaler`, a Lehman-era return of $-90\%$ would dominate the mean and collapse the scaled returns of all other observations.

## Remember

Financial data is structurally outlier-prone: earnings surprises, index rebalancings, flash crashes, and reporting errors all produce extreme values that are real but not representative of the typical data-generating process. Using `StandardScaler` on returns during a stress period inflates $\sigma$ for the entire training set, causing the model to treat normal moves as near-zero after scaling. `RobustScaler` handles this gracefully because the IQR captures typical variation without being distorted by the tails. The `ColumnTransformer` wrapper is essential in practice because financial ML pipelines almost always mix numeric signals (returns, ratios) with categorical features (sector, credit rating), and applying the same scaler to both would be incorrect.
