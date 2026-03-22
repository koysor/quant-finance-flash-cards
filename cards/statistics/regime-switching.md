# Regime Switching

**Topic:** Statistics
**Level:** A Level Mathematics
**Tags:** regime switching, hidden markov model, market regimes, volatility regimes, state detection
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A regime-switching model assumes that financial markets alternate between a small number of discrete states (regimes) — such as a low-volatility "bull" regime and a high-volatility "bear" regime — with transitions governed by a Markov chain. The current regime is not directly observable; it must be inferred from the data. The most common implementation is the **hidden Markov model (HMM)**, where each regime has its own set of return parameters (mean and variance) and the system switches between regimes with estimated transition probabilities.

## Key Formula

For a two-regime model, returns conditional on regime $s_t$:

$$r_t | s_t = j \sim N(\mu_j, \sigma_j^2), \quad j \in \{1, 2\}$$

The **transition matrix**:

$$\mathbf{P} = \begin{pmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{pmatrix}$$

where $p_{ij} = P(s_{t+1} = j \mid s_t = i)$ and $p_{i1} + p_{i2} = 1$.

The **filtered probability** of being in regime $j$ at time $t$:

$$P(s_t = j \mid r_1, \ldots, r_t) \propto f(r_t \mid s_t = j) \sum_{i} p_{ij} P(s_{t-1} = i \mid r_1, \ldots, r_{t-1})$$

Parameters are estimated via the **Baum-Welch algorithm** (EM for HMMs).

## Example

Fitting a two-regime model to FTSE 100 daily returns:

| Parameter | Regime 1 (Bull) | Regime 2 (Bear) |
|-----------|----------------|----------------|
| Mean ($\mu$) | +0.05% | $-0.08\%$ |
| Volatility ($\sigma$) | 0.8% | 2.1% |
| Self-transition ($p_{ii}$) | 0.98 | 0.94 |

Expected duration in each regime: $\frac{1}{1-p_{ii}}$

- Bull: $\frac{1}{0.02} = 50$ days
- Bear: $\frac{1}{0.06} \approx 17$ days

Today's filtered probability of being in the bear regime is 0.85 (high volatility and negative returns observed recently). The model predicts that tomorrow's return distribution is a mixture: $0.15 \times N(0.05\%, 0.8\%) + 0.85 \times N(-0.08\%, 2.1\%)$.

## Remember

Regime-switching models capture one of the most important stylised facts in finance: markets behave fundamentally differently in calm versus stressed periods. A strategy calibrated to a single regime will underperform or blow up when the regime changes. For quant developers, regime detection enables dynamic strategy allocation — reducing risk exposure when the bear regime probability rises, switching between momentum and mean reversion, or adjusting volatility forecasts. The HMM is computationally lightweight (the forward-backward algorithm scales linearly in time) and integrates naturally with the Kalman filter and other sequential estimation tools. However, regime identification is inherently lagged — by the time the model confidently detects a regime change, the market has already moved significantly.
