# Regime-Switching Models

**Topic:** Stochastic Processes
**Tags:** regime switching, Markov chain, state-dependent dynamics, volatility regimes, hidden Markov model
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **regime-switching model** (also called a Markov-switching model) allows the parameters of a stochastic process — drift, volatility, or both — to depend on a discrete state variable $s_t$ that evolves as a finite-state Markov chain. Unlike constant-parameter models such as GBM, the dynamics themselves change over time as the system transitions between regimes. This provides a natural framework for modelling the observation that financial markets alternate between structurally different periods (e.g. low-volatility trending markets and high-volatility mean-reverting markets).

## Key Formula

**State-dependent GBM** with $N$ regimes:

$$dS_t = \mu_{s_t} S_t \, dt + \sigma_{s_t} S_t \, dW_t, \qquad s_t \in \{1, 2, \ldots, N\}$$

The regime $s_t$ follows a continuous-time Markov chain with **generator matrix** $\mathbf{Q}$:

$$\mathbf{Q} = \begin{pmatrix} -q_1 & q_{12} & \cdots \\ q_{21} & -q_2 & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}$$

where $q_{ij} \geq 0$ for $i \neq j$ and $q_i = \sum_{j \neq i} q_{ij}$. The expected time spent in regime $i$ before switching is $1/q_i$.

In the common **two-regime discrete-time** version the transition matrix is:

$$\mathbf{P} = \begin{pmatrix} p_{11} & 1 - p_{11} \\ 1 - p_{22} & p_{22} \end{pmatrix}$$

with expected regime durations $\frac{1}{1 - p_{11}}$ and $\frac{1}{1 - p_{22}}$ periods respectively.

## Example

Consider a two-regime model for a UK equity index with daily returns:

| Parameter | Regime 1 (Bull) | Regime 2 (Bear) |
|---|---|---|
| Annualised drift $\mu$ | 12% | $-8\%$ |
| Annualised volatility $\sigma$ | 14% | 32% |
| Self-transition probability $p_{ii}$ | 0.99 | 0.96 |

Expected durations: bull regime lasts $\frac{1}{0.01} = 100$ days, bear regime lasts $\frac{1}{0.04} = 25$ days.

Simulating one year: the process spends roughly 80% of the time in regime 1 (the stationary probability is $\frac{1 - p_{22}}{2 - p_{11} - p_{22}} = \frac{0.04}{0.05} = 0.80$). During a bear episode, daily returns have standard deviation $32\%/\sqrt{252} \approx 2.0\%$, more than double the bull-regime figure of $0.88\%$.

## Remember

Constant-parameter models like GBM assume a single volatility and drift for all time. In reality, equity markets exhibit distinct calm and crisis periods, and strategies calibrated to one regime can fail catastrophically when conditions change. Regime-switching models address this by letting the SDE parameters themselves be random — governed by an unobserved Markov chain. In quantitative finance they are used for dynamic asset allocation (reducing exposure when the bear-regime probability rises), risk management (VaR estimates that account for regime uncertainty are more conservative during transitions), and derivatives pricing (option values become path-dependent on the regime history). The key trade-off is that adding regimes increases the parameter count rapidly and introduces model risk around the number and interpretation of states.
