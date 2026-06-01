# Feature Store

**Topic:** Computational Finance
**Tags:** mlops, point-in-time data, feature engineering, data leakage, reproducibility, quantitative research
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

A **feature store** is a centralised MLOps infrastructure component that stores, versions, and serves machine learning features — ensuring that every feature value is labelled with the timestamp at which it became known, so that training and live inference consume the exact same point-in-time-correct computation. By decoupling feature production from model training and serving, a feature store eliminates train/serve skew and enforces reproducibility across the model lifecycle.

## Key Formula

A feature store exposes two complementary planes:

| Plane | Storage | Access pattern | Use case |
|---|---|---|---|
| **Offline store** | Columnar (Parquet, Hive) | Batch, high-latency | Historical training datasets, point-in-time joins |
| **Online store** | Key-value (Redis, DynamoDB) | Row, low-latency ($<$10 ms) | Live inference, real-time model serving |

Point-in-time join (pseudocode):

```
training_df = feature_store.get_historical_features(
    entity_df   = label_df,          # rows: (entity_id, event_timestamp)
    feature_refs = ["vol_20d", "rsi_14", "spread_bps"],
    as_of       = event_timestamp    # retrieves feature value known at that time
)
```

The `as_of` parameter guarantees that for each row the store returns the feature value that was available immediately before `event_timestamp` — no subsequent updates or corrections leak through.

## Example

A quant research team models next-month FTSE 100 constituent returns. They register a feature `vol_20d` — the 20-day rolling realised volatility — and materialise it daily with an ingestion timestamp.

To build a training set for the period ending 2023-06-01:

```
entity_df = pd.DataFrame({
    "ric":             ["HSBA.L", "BP.L", ...],
    "event_timestamp": pd.Timestamp("2023-06-01")
})

features = store.get_historical_features(
    entity_df=entity_df,
    feature_refs=["vol_20d"]
)
```

The store returns each constituent's `vol_20d` as computed on 2023-05-31 close — not the value updated on 2023-06-02. Any volatility spike on 2 June is invisible, preventing look-ahead bias. When the model is deployed live, the same `vol_20d` computation runs in the online store so the live feature is byte-for-byte identical to the training feature.

## Remember

In quantitative finance, a feature store solves two related problems simultaneously. First, **point-in-time correctness**: using the offline store's `as_of` join means a training dataset cannot incorporate data that would have been unavailable to a trader on the decision date, preventing the look-ahead bias that inflates backtest Sharpe ratios. Second, **train/serve consistency**: because the online and offline stores share the same feature definitions and transformation logic, a signal that performed well in research is guaranteed to be computed identically in live execution — eliminating the silent drift between a researcher's Jupyter notebook and the production system that is one of the most common causes of live underperformance.
