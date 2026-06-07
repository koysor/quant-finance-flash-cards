# KPSS Test

**Topic:** Statistics
**Tags:** kpss test, stationarity test, unit root, adf test, trend stationarity, time series
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Kwiatkowski–Phillips–Schmidt–Shin (KPSS) test** tests $H_0$: the series is stationary (level- or trend-stationary) against $H_1$: the series has a unit root. This is the **opposite null** to the ADF test: KPSS failure to reject is evidence *for* stationarity, not against it. Using ADF and KPSS jointly gives a more reliable classification of integration order than either test alone.

## Key Formula

Decompose $X_t = \xi t + r_t + \varepsilon_t$, where $r_t = r_{t-1} + u_t$ is a random walk and $\varepsilon_t$ is stationary noise. The test statistic checks whether $\sigma_u^2 = 0$ (no random walk component):

$$\text{KPSS} = \frac{T^{-2} \displaystyle\sum_{t=1}^{T} \hat{S}_t^2}{\hat{s}^2}$$

where $\hat{S}_t = \sum_{j=1}^{t} \hat{e}_j$ is the partial-sum process of OLS residuals and $\hat{s}^2$ is a HAC long-run variance estimator. Reject $H_0$ (stationarity) at 5% if the statistic exceeds 0.463 (level-stationary) or 0.146 (trend-stationary).

**Decision table:**

| ADF result | KPSS result | Conclusion |
|---|---|---|
| Reject $H_0$ (no unit root) | Fail to reject $H_0$ (stationary) | $I(0)$ stationary |
| Fail to reject $H_0$ (unit root) | Reject $H_0$ (non-stationary) | $I(1)$ unit root |
| Both reject | Both reject | Conflicting — inconclusive |
| Both fail to reject | Both fail to reject | Insufficient power |

## Example

FTSE 100 daily log-returns (2000–2020):  
ADF: $t = -42.3$, $p < 0.01$ → reject unit root.  
KPSS (level): statistic $= 0.12 < 0.463$ → fail to reject stationarity.  
**Conclusion: $I(0)$ stationary.**

FTSE 100 daily log-prices:  
ADF: $t = -1.2$, $p = 0.67$ → fail to reject unit root.  
KPSS: statistic $= 1.84 > 0.463$ → reject stationarity.  
**Conclusion: $I(1)$ unit root confirmed.**

## Remember

The single most common mistake with the KPSS test is reversing the null: because ADF has $H_0 =$ unit root, practitioners sometimes assume "fail to reject" = evidence of non-stationarity for both tests — but for KPSS, "fail to reject" is evidence **of** stationarity. Applying the decision table above eliminates this confusion. In quantitative finance, the KPSS test is indispensable for cointegration analysis: ADF on the residuals of a long-run regression tests for cointegration, but KPSS provides a complementary check that the spread itself is genuinely stationary rather than merely failing the lower-powered ADF unit root null.
