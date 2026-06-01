# Meta-Labelling

**Topic:** Computational Finance
**Tags:** label construction, supervised learning, financial machine learning, position sizing, ensemble, precision
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Meta-labelling** is a two-stage supervised learning framework where a **primary model** predicts the direction (side) of a trade and a **secondary (meta) model** learns to predict whether the primary model's directional bet will be profitable, outputting a confidence score that can be used to filter trades and size positions.

## Key Formula

Let the primary model produce a side prediction $\hat{s}_t \in \{+1, -1\}$. The meta-label is:

$$z_t = \mathbf{1}\!\left[\hat{s}_t = \text{sign}(r_{t,t+\Delta})\right] \in \{0, 1\}$$

The secondary model is trained to predict $\Pr(z_t = 1 \mid \mathbf{x}_t,\, \hat{s}_t)$ — the probability that the primary model is correct given the features and the predicted side. The final trade signal is:

$$\text{bet}_t = \hat{s}_t \cdot \mathbf{1}\!\left[\hat{p}_t \geq \theta\right]$$

where $\hat{p}_t$ is the meta-model's output probability and $\theta$ is a confidence threshold; setting $\theta > 0.5$ increases precision at the cost of recall.

## Example

A momentum model predicts 60\% of trades correctly (precision = 0.60, recall = 1.0). Training a meta-model on top produces $\hat{p}_t$ for each signal. Setting $\theta = 0.65$ filters out 30\% of signals. Of the remaining 70\% of signals, 78\% are correct: precision rises from 0.60 to 0.78 while recall falls to 0.70. The F1 score improves from $2(0.60 \cdot 1.0)/(0.60+1.0) = 0.75$ to $2(0.78 \cdot 0.70)/(0.78+0.70) = 0.74$ — roughly flat, but the higher-precision trades carry larger position sizes, improving the strategy's risk-adjusted return.

## Remember

In quantitative finance, a directional model and a sizing/filtering model solve fundamentally different problems. The primary model asks "which way will the market move?" — a question where feature sets like technical indicators or macro signals are relevant. The meta-model asks "is this a good time to trust the primary model?" — where features like volatility regime, recent model accuracy, and market microstructure conditions are more predictive. Separating these two questions prevents each model from being distracted by the other's signal, and allows the meta-model's confidence output to scale position size continuously rather than applying a binary on/off filter.
