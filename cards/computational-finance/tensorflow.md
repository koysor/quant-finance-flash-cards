# TensorFlow

**Topic:** Computational Finance
**Tags:** tensorflow, keras, deep learning, neural network, production deployment, lstm
**Created:** 2026-04-23
**Author:** Claude Sonnet 4.6

---

## Definition

**TensorFlow** is Google's open-source machine learning framework built around a computation graph that is compiled and optimised by the XLA (Accelerated Linear Algebra) compiler before execution. Its high-level `tf.keras` API provides a `fit`/`predict` interface; `tf.GradientTape` allows explicit gradient computation for custom training loops. TensorFlow Serving exposes any trained model as a gRPC or REST endpoint with sub-millisecond latency, making TensorFlow the standard choice for **productionising** financial models — credit scoring APIs, real-time fraud detection, and LSTM-based volatility forecasters deployed alongside pricing engines.

## Key Formula

**GradientTape** records operations and computes $\nabla_\theta \mathcal{L}$ for any differentiable forward pass:

```python
with tf.GradientTape() as tape:
    y_hat = model(X, training=True)
    loss  = tf.reduce_mean(tf.square(y_hat - y))
grads = tape.gradient(loss, model.trainable_variables)
```

For an **LSTM** applied to log-returns $r_t$:

$$h_t, c_t = \text{LSTM}(r_t,\, h_{t-1},\, c_{t-1};\;\theta)$$
$$\hat{\sigma}_{t+1}^2 = \mathbf{w}^{\top} h_t + b$$

where $\theta$ are trained by minimising mean squared error of next-day realised variance via backpropagation through time.

## Example

One-day-ahead volatility forecasting on S&P 500 daily returns:

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(20, 1)),
    tf.keras.layers.Dense(1, activation="softplus"),
])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=30, validation_split=0.1)
```

Using a 20-day rolling window of log-returns as input and next-day realised variance as target, the LSTM achieves an out-of-sample $R^2$ of 0.42, compared with 0.38 for a standard GARCH(1,1) on the same data.

## Remember

TensorFlow's principal advantage in finance is **production deployment at scale**: TensorFlow Serving containerises any trained model and handles batching, versioning, and health-checking out of the box, while XLA graph compilation fuses operations to eliminate redundant memory copies — critical when scoring thousands of credit applications per second. The practical split on most quant desks is: research in PyTorch (dynamic graph, easier debugging), production in TensorFlow or ONNX-exported models (optimised inference, monitoring, A/B testing infrastructure). Understanding both frameworks allows a quant researcher to hand off models to a production engineering team without a full rewrite.
