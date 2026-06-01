# MLOps

**Topic:** Computational Finance
**Tags:** mlops, model deployment, model monitoring, distribution shift, reproducibility, quantitative research
**Created:** 2026-05-29
**Author:** Claude Sonnet 4.6

---

## Definition

**MLOps** (Machine Learning Operations) is the discipline of deploying, monitoring, and maintaining ML models in production, bridging the gap between research and live systems. Its core concerns are reproducible experiment tracking, governed model promotion, low-latency serving, and automated retraining pipelines that respond to detected distribution shift or performance degradation.

## Key Formula

The MLOps lifecycle — research artefact to production loop:

```
Research
  └─► Experiment Tracking  (log parameters, metrics, artefacts — e.g. MLflow / W&B)
        └─► Model Registry  (version model; promote None → Staging → Production)
              └─► Deployment  (serve predictions: batch scoring or real-time API)
                    └─► Monitoring  (track live performance vs backtest; measure PSI)
                          └─► Retraining Trigger  (PSI > 0.2, Sharpe decay, scheduled)
                                └─► Research  (iterate on features, re-train, re-validate)
```

Each stage feeds back to the next; the loop closes when the retrained model re-enters the registry and is promoted to production.

## Example

A quant deploys a Ridge regression alpha signal trained on FTSE 100 momentum and valuation features. At deployment, the backtested annualised Sharpe ratio is **1.4**. An MLOps monitoring job runs nightly:

1. **Performance check** — computes the rolling 60-day live Sharpe and compares it to the backtest value; a drop below 0.8 flags a performance alert.
2. **Distribution check** — computes the Population Stability Index (PSI) between the training feature distribution and the last 30 days of live feature values. PSI is calculated per feature as:

$$\text{PSI} = \sum_{i} (A_i - E_i) \ln\!\left(\frac{A_i}{E_i}\right)$$

where $A_i$ is the actual (live) proportion in bin $i$ and $E_i$ is the expected (training) proportion.

3. **Retraining trigger** — if any feature's PSI exceeds **0.2** (indicating significant distribution shift), the pipeline automatically queues a retraining job, logs the new run to the model registry under a new version, and routes it through the Staging gate before any live promotion.

This closed loop means the desk is never silently running a stale signal.

## Remember

Without MLOps, a model that passed rigorous backtesting can silently degrade in live trading for three distinct reasons: **regime change** shifts the data distribution away from what the model was trained on; **data pipeline drift** means features computed in production differ subtly from how they were computed in research (e.g. different timestamp alignment or corporate action handling); and **feature computation differences** between the research notebook and the production ETL introduce silent discrepancies. MLOps closes the loop by making degradation observable (monitoring), diagnosable (distribution tracking via PSI), and automatically correctable (retraining pipelines) — turning model maintenance from a manual, ad-hoc process into an engineered, auditable system.
