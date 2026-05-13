# Reconstruction Error Threshold

**Topic:** Computational Finance
**Tags:** reconstruction error, anomaly detection, threshold calibration, false positive, false negative, surveillance
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **reconstruction error threshold** $\tau$ is the decision boundary in autoencoder-based anomaly detection: an observation $\mathbf{x}$ is flagged as anomalous when its reconstruction error $\|\mathbf{x} - \hat{\mathbf{x}}\|^2$ exceeds $\tau$. Choosing $\tau$ is a calibration problem that requires trading off the cost of false positives (unnecessary alerts) against the cost of false negatives (missed anomalies), and depends entirely on the business context.

## Key Formula

**Anomaly decision rule:**

$$\text{flag anomaly} \iff \|\mathbf{x} - \hat{\mathbf{x}}\|^2 > \tau$$

**Percentile-based calibration** — set $\tau$ at the $q$th percentile of training reconstruction errors:

$$\tau_q = F^{-1}(q), \qquad q \in \{0.95, 0.99, 0.999\}$$

**Expected cost** (asymmetric loss) as a function of $\tau$:

$$\text{Cost}(\tau) = c_{\text{FP}} \cdot \text{FPR}(\tau) + c_{\text{FN}} \cdot \text{FNR}(\tau)$$

where $c_{\text{FP}}$ and $c_{\text{FN}}$ are the per-alert costs of false positives and missed anomalies respectively.

## Example

An autoencoder trained on 3 years of intraday order flow vectors (500 stocks, 30-minute intervals). Training reconstruction errors: mean $0.0012$, 95th percentile $0.0031$, 99th percentile $0.0058$.

| Setting | $\tau$ | FPR | Use case |
|---|---|---|---|
| Sensitive | $0.0031$ | $\approx 5\%$ | End-of-day review; analyst filters alerts |
| Standard | $0.0058$ | $\approx 1\%$ | Daily automated surveillance report |
| High-precision | $0.0120$ | $\approx 0.1\%$ | Real-time halt trigger; must minimise false alarms |

The COVID crash produces reconstruction errors of $0.0180$ — flagged under all three settings.

## Remember

In financial surveillance, false positives and false negatives carry asymmetric costs that differ fundamentally by application. For **market abuse detection**, a missed manipulation episode (false negative) exposes the firm to regulatory sanction, so $\tau$ is set low and human review is applied to the resulting alert volume. For **real-time circuit breakers**, a false halt (false positive) is itself market-disruptive, so $\tau$ is set high. The correct approach is to estimate the cost ratio $c_{\text{FN}} / c_{\text{FP}}$ from the business context, sweep $\tau$ across the training distribution's quantiles, and minimise expected cost — the same framework as setting a credit score cut-off, not an arbitrary statistical rule of thumb.
