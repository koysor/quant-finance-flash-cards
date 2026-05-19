# Population Stability Index

**Topic:** Computational Finance
**Tags:** population stability index, model monitoring, covariate shift, scorecard, credit risk
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

The **Population Stability Index (PSI)** measures how much the distribution of a variable has shifted between a reference period (typically training data) and a current period (live deployment data). It is the standard metric in bank model risk management for detecting covariate shift in credit scorecards and machine learning models under IFRS 9 and Basel requirements.

## Key Formula

Partition the variable into $B$ bins. Let $p_i^{\text{ref}}$ and $p_i^{\text{cur}}$ be the proportions of observations falling in bin $i$ in the reference and current periods respectively:

$$\text{PSI} = \sum_{i=1}^{B} \left(p_i^{\text{cur}} - p_i^{\text{ref}}\right) \ln\!\left(\frac{p_i^{\text{cur}}}{p_i^{\text{ref}}}\right)$$

PSI is a symmetrised KL divergence — it is zero when the distributions are identical and increases as they diverge.

**Standard thresholds used in bank model risk management:**

| PSI | Interpretation | Action |
|---|---|---|
| $< 0.10$ | No significant shift | Monitor as usual |
| $0.10$–$0.20$ | Minor shift | Investigate; consider recalibration |
| $> 0.20$ | Major shift | Redevelop or recalibrate model |

## Example

A bank's retail credit scorecard was trained on 2019 income data using 10 bins of equal width. After the 2020 pandemic, PSI is computed for the debt-to-income ratio feature:

- Bins $1$–$3$ (low DTI): $p^{\text{cur}} < p^{\text{ref}}$ — fewer low-DTI borrowers
- Bins $8$–$10$ (high DTI): $p^{\text{cur}} > p^{\text{ref}}$ — many more high-DTI borrowers

$$\text{PSI} = \sum_{i=1}^{10}(p_i^{\text{cur}} - p_i^{\text{ref}})\ln(p_i^{\text{cur}}/p_i^{\text{ref}}) = 0.38$$

PSI $= 0.38 \gg 0.20$: the model must be redeveloped.

## Remember

PSI is the lingua franca of model risk monitoring in banking. Under IFRS 9, lenders must demonstrate that their PD models remain representative of current borrower populations; a PSI breach is the primary quantitative trigger for a model review or redevelopment. PSI is computed monthly for every input feature and the model score itself — it is both an early warning system for covariate shift and a regulatory documentation requirement. Its connection to information theory is useful: PSI $\approx 2 \times D_{\text{KL}}$ when the distributions are close, so it has a natural interpretation as the information lost by using the reference distribution to describe current data. For ML models with many features, PSI is computed feature-by-feature and the maximum PSI across features is the headline monitoring statistic.
