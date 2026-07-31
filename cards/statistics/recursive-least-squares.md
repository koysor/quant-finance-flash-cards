# Recursive Least Squares

**Topic:** Statistics
**Tags:** recursive least squares, forgetting factor, online estimation, regression, kalman filter, coefficient stability
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

**Recursive least squares (RLS)** updates a regression's coefficient estimates one observation at a time, without re-fitting from scratch, using an exponential **forgetting factor** $\lambda \in (0, 1]$ to progressively down-weight older data. It sits between two extremes: full-sample ordinary least squares, refit on a rolling window, treats all included data equally and drops old data abruptly at the window edge; RLS instead lets influence decay smoothly, so coefficient estimates adapt to changing market conditions without the jumps a rolling window produces when an influential old observation exits.

## Key Formula

At each new observation $(x_t, y_t)$, the coefficient vector $\hat{\theta}_t$ and its covariance $P_t$ update via:

$$K_t = \frac{P_{t-1}\,x_t}{\lambda + x_t^\top P_{t-1}\,x_t}$$

$$\hat{\theta}_t = \hat{\theta}_{t-1} + K_t\left(y_t - x_t^\top \hat{\theta}_{t-1}\right)$$

$$P_t = \frac{1}{\lambda}\left(P_{t-1} - K_t\, x_t^\top P_{t-1}\right)$$

where $K_t$ is the gain vector and $\lambda$ controls the effective memory: an observation $\tau$ steps in the past carries weight $\lambda^\tau$, giving an effective window length of roughly $\dfrac{1}{1-\lambda}$ observations. $\lambda = 1$ recovers ordinary recursive least squares with no forgetting (all data weighted equally).

## Example

Daily re-estimation of the Hull-White minimum-variance-delta coefficients $a_t, b_t, c_t$ for one delta-and-maturity bucket, with $\lambda = 0.97$: the effective memory is $1/(1-0.97) = 33$ trading days, roughly 6-7 weeks. If plain OLS is refit on a fixed 60-day rolling window instead, a single extreme day (e.g. a March 2023-style regime shift) enters and exits the window abruptly, causing $\hat{a}_t$ to jump sharply on both the day it enters and the day it drops out 60 days later. RLS with $\lambda = 0.97$ instead lets that day's influence fade out smoothly over subsequent weeks — no cliff-edge jump on either side.

## Remember

RLS is the natural first upgrade when an OLS-fitted coefficient time series looks noisy from one re-fit to the next: rather than a full state-space model, it needs only one tuning parameter ($\lambda$) and reduces exactly to a Kalman filter with a particular, restricted noise structure (constant-covariance state evolution, no explicit process noise term). Use RLS when the goal is a lightweight, easy-to-explain smoothing of coefficients that are believed to drift slowly — such as the Hull-White MVD quadratic's $a, b, c$ — and reach for a full Kalman filter only when the drift dynamics themselves need to be modelled explicitly (e.g. different noise variance per coefficient, or a mean-reverting rather than random-walk state).
