# Funnelling Feature Selection

**Topic:** Computational Finance
**Tags:** feature selection, machine learning, filter methods, wrapper methods, embedded methods
**Created:** 2026-05-23
**Author:** Claude Sonnet 4.6

---

## Definition

**Funnelling feature selection** is a three-stage sequential approach that progressively reduces a large candidate feature set using methods of increasing computational cost: a fast statistical filter removes clearly irrelevant features first, a wrapper method (typically Recursive Feature Elimination) then selects from the survivors, and an embedded method (model-internal importance) performs final refinement on the reduced set.

## Key Formula

The three stages applied in sequence to a candidate set $\mathcal{F}$ of $p$ features, targeting a final set of size $k \ll p$:

**Stage 1 — Filter:** remove features where a univariate statistic (correlation, mutual information $I$, ANOVA $F$-score) falls below a threshold $\tau$:

$$\mathcal{F}_1 = \{f \in \mathcal{F} : I(f;\, y) > \tau\}$$

**Stage 2 — Wrapper (RFE):** train a base estimator repeatedly, dropping the lowest-ranked feature at each step:

$$\mathcal{F}_2 = \text{RFE}(\mathcal{F}_1,\; \text{n\_features} = m)$$

**Stage 3 — Embedded:** train the final model on $\mathcal{F}_2$ and retain only features with importance above a threshold $\delta$:

$$\mathcal{F}_3 = \{f \in \mathcal{F}_2 : \text{importance}(f) > \delta\}$$

## Example

Starting with 40 technical indicators for an NVDA direction model:

| Stage | Method | Features remaining |
|---|---|---|
| Raw | All candidates | 40 |
| Filter | Mutual information $> 0.01$ | 22 |
| Wrapper | RFE (XGBoost, 10 features) | 10 |
| Embedded | XGBoost importance $> 0.05$ | 7 |

Final 7 features might be: `rsi_14`, `macd_hist`, `bb_pct_b`, `atr_14`, `obv_diff`, `log_return_5d`, `volume_ratio`.

## Remember

Funnelling works because the three methods have complementary failure modes. Filters are fast but ignore feature interactions — `rsi_14` might score low in isolation yet be highly predictive in combination with `macd_hist`. RFE fixes this by evaluating subsets but is expensive for large $p$. Embedded importance (from XGBoost's gain-based split scores) then removes features that passed RFE but contribute negligibly once the other strong features are included. In a financial ML context, skipping the filter stage and running RFE directly on 200 features is computationally prohibitive with walk-forward cross-validation, so the funnel structure is both a statistical and an engineering necessity.
