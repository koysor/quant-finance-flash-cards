# GARCH ACF of Squared Returns

**Topic:** Statistics
**Tags:** garch, autocorrelation, squared returns, volatility clustering, time series, arch effects
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The GARCH(1,1) model makes a precise prediction about the autocorrelation structure of squared returns. Whilst raw returns $r_t$ are approximately serially uncorrelated (consistent with market efficiency), squared returns $r_t^2$ exhibit significant positive autocorrelation that decays slowly and geometrically with lag $\tau$. This contrast is the empirical fingerprint of **volatility clustering**: large moves (of either sign) tend to cluster together in time.

The autocorrelation function (ACF) of squared returns encodes how persistent volatility shocks are. A high persistence parameter $\alpha + \beta$ (close to 1) means autocorrelations remain elevated even at long lags, implying that a volatility shock today still influences the risk environment weeks later.

## Key Formula

Under GARCH(1,1), the ACF of squared returns decays geometrically:

$$\rho_\tau(r^2) = C \cdot (\alpha + \beta)^\tau, \quad \tau = 1, 2, 3, \ldots$$

where:
- $\rho_\tau(r^2)$ is the autocorrelation of $r_t^2$ at lag $\tau$
- $\alpha$ is the ARCH coefficient (weight on lagged squared shock $\varepsilon_{t-1}^2$)
- $\beta$ is the GARCH coefficient (weight on lagged conditional variance $\sigma_{t-1}^2$)
- $C = \alpha^2 / (1 + \alpha^2 + 2\alpha\beta)$ for the lag-1 autocorrelation (the exact constant)
- $\alpha + \beta < 1$ is required for covariance stationarity

**Contrast with raw returns:**

$$\rho_\tau(r) \approx 0 \quad \text{for all } \tau \geq 1$$

Raw return autocorrelations are near zero — consistent with the Efficient Market Hypothesis (weak form). Squared return autocorrelations are positive and slowly decaying — revealing time-varying volatility.

## Example

Suppose $\alpha = 0.05$, $\beta = 0.92$, giving persistence $\alpha + \beta = 0.97$.

Computing $C$ at lag 1:

$$C = \frac{\alpha^2}{1 + \alpha^2 + 2\alpha\beta} = \frac{0.0025}{1 + 0.0025 + 0.092} \approx \frac{0.0025}{1.0945} \approx 0.0023$$

Autocorrelations at selected lags:

| Lag $\tau$ | $\rho_\tau(r^2) = 0.0023 \times 0.97^\tau$ |
|---|---|
| 1 | $0.0023 \times 0.97^1 \approx 0.0022$ |
| 10 | $0.0023 \times 0.97^{10} \approx 0.0017$ |
| 50 | $0.0023 \times 0.97^{50} \approx 0.00049$ |

The autocorrelations are small but statistically significant over a long sample — they decay slowly because $0.97^{50} \approx 0.22$, retaining 22% of the original magnitude even at lag 50. This is characteristic of high persistence: volatility conditions from 50 days ago still carry predictive information about today's variance.

## Remember

Use the ACF of squared returns as a **diagnostic test for ARCH effects**:

1. Compute log-returns $r_t = \ln(S_t / S_{t-1})$.
2. Compute the sample ACF of $r_t$ — expect values near zero (no predictability in returns).
3. Compute the sample ACF of $r_t^2$ — if positive and slowly decaying, ARCH effects are present.
4. Formally test with the **Ljung–Box test** on $r_t^2$, or the **ARCH-LM test**.

If squared return autocorrelations are significant and decay geometrically, this confirms that volatility is time-varying and that a GARCH-family model is appropriate — constant-volatility models such as basic VaR or Black–Scholes will understate risk in turbulent periods.
