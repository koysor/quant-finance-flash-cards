# Kalman Filter

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** kalman filter, state estimation, signal extraction, pairs trading, time series
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The Kalman filter is a recursive algorithm that estimates the hidden state of a linear dynamical system from a series of noisy observations. It maintains a probability distribution over the state — characterised by a mean (best estimate) and covariance (uncertainty) — and updates this distribution each time a new observation arrives. In quantitative finance, it is used for signal extraction (separating the true hedge ratio from noise in pairs trading), estimating time-varying betas, and tracking unobservable quantities like the "fair value" of a spread.

## Key Formula

**Predict step** (propagate state forward):

$$\hat{x}_{t|t-1} = A \hat{x}_{t-1|t-1} + B u_t$$
$$P_{t|t-1} = A P_{t-1|t-1} A^\top + Q$$

**Update step** (incorporate new observation $z_t$):

$$K_t = P_{t|t-1} H^\top (H P_{t|t-1} H^\top + R)^{-1}$$
$$\hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t (z_t - H \hat{x}_{t|t-1})$$
$$P_{t|t} = (I - K_t H) P_{t|t-1}$$

where $K_t$ is the **Kalman gain**, $Q$ is the process noise covariance, and $R$ is the observation noise covariance.

## Example

A pairs trading strategy tracks the spread between two cointegrated stocks. The state is the hedge ratio $\beta$, which evolves slowly:

- State equation: $\beta_t = \beta_{t-1} + w_t$, where $w_t \sim N(0, Q = 0.0001)$
- Observation: $Y_t = \beta_t X_t + \epsilon_t$, where $\epsilon_t \sim N(0, R = 1.0)$

Starting with $\hat{\beta}_0 = 0.8$ and $P_0 = 1.0$. After observing $Y_1 = 52$, $X_1 = 60$:

$$\text{Innovation} = 52 - 0.8 \times 60 = 52 - 48 = 4$$

$$K_1 = \frac{P_0 \cdot X_1}{X_1^2 \cdot P_0 + R} = \frac{1.0 \times 60}{3600 \times 1.0 + 1.0} = \frac{60}{3601} = 0.0167$$

$$\hat{\beta}_1 = 0.8 + 0.0167 \times 4 = 0.867$$

The filter adjusts the hedge ratio upward, responding to the observation that the spread was wider than predicted.

## Remember

The Kalman filter is the optimal linear estimator when the system is linear and noise is Gaussian — but even when these assumptions are violated (as they often are in finance), it remains a powerful and computationally efficient tool. For quant developers, its main applications are: (1) estimating time-varying hedge ratios in pairs trading and stat arb, avoiding the lookback-window problem of rolling OLS; (2) tracking unobservable state variables like the "true" mean-reversion level of a spread; and (3) fusing data from multiple noisy sources. The extended Kalman filter and unscented Kalman filter handle nonlinear systems, while the particle filter handles non-Gaussian noise — all are part of the quant dev toolkit for real-time signal processing.
