# Distribution Shift

**Topic:** Computational Finance
**Tags:** distribution shift, covariate shift, concept drift, model degradation, regime change
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Distribution shift** occurs when the statistical properties of data at deployment differ from those seen during training. Three subtypes matter for finance: **covariate shift** ($P(X)$ changes, $P(y|X)$ stable — features appear with new frequencies); **concept drift** ($P(y|X)$ changes — the predictive relationship itself changes); and **label shift** ($P(y)$ changes, $P(X|y)$ stable). Concept drift is the most dangerous because no amount of re-weighting can recover a model trained on an obsolete signal.

## Key Formula

Under covariate shift, the model's risk at deployment time $t$ differs from its training risk:

$$R_t(f) = \int \ell(f(x), y)\, dP_t(x,y) \neq R_{\text{train}}(f)$$

**Importance-weighted risk** corrects for known covariate shift:

$$\hat{R}_t(f) = \frac{1}{n}\sum_{i=1}^{n} \underbrace{\frac{P_t(x_i)}{P_{\text{train}}(x_i)}}_{w(x_i)}\,\ell(f(x_i), y_i)$$

The density ratio $w(x) = P_t(x)/P_{\text{train}}(x)$ up-weights training examples that look like the current environment. In practice, $w$ is estimated by training a classifier to distinguish train-period from current-period observations.

## Example

A credit default model trained on 2015–2019 data uses debt-to-income ratio and employment tenure as features. In March 2020, unemployment hits 15% — a region of feature space almost absent from training. The feature distribution $P(X)$ has shifted (covariate shift). The model assigns near-zero default probabilities to newly unemployed borrowers because it has almost no training signal there, generating large unexpected losses. The Population Stability Index (PSI) on the employment-tenure feature spikes to 0.35, well above the 0.2 alert threshold.

## Remember

Distribution shift is the dominant cause of production model failure in quantitative finance — not overfitting (caught by cross-validation) but the world changing post-training. The three practical defences are: (1) **walk-forward retraining** — retrain on a rolling window so $P_{\text{train}}$ tracks the current regime; (2) **drift monitoring** — track PSI and KS statistics on input features and output distributions, with automated alerts when they exceed thresholds; (3) **regime-conditional models** — explicitly condition on detected market regimes so that structural breaks trigger a model switch rather than silent extrapolation into out-of-distribution territory. A model that passes rigorous walk-forward backtesting can still fail in production if the entire backtest period was a single regime.
