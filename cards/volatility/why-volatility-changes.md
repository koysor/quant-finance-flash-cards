# Why Volatility Changes

**Topic:** Volatility
**Tags:** leverage effect, correlation, volatility clustering, macro risk, information flow
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Equity volatility is not constant — it clusters in bursts and spikes around identifiable events. Four mechanisms drive this: crises and macro shocks, the leverage effect (falling prices raise a firm's debt-to-equity ratio, increasing equity risk), information flow (high news volume raises price discovery activity), and — crucially for indices — correlation amplification (in downturns, cross-stock correlations rise, amplifying index variance beyond the sum of individual firm effects).

## Key Formula

For a portfolio of $n$ stocks with weights $w_i$, individual volatilities $\sigma_i$, and pairwise correlations $\rho_{ij}$:

$$\text{Var}(R_P) = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \sigma_i \sigma_j \rho_{ij}$$

The **correlation amplification channel**: even with constant $\sigma_i$, a rise in $\rho_{ij}$ from calm (0.3) to stress (0.7) roughly doubles the covariance contribution — and for a large index the $\tfrac{n(n-1)}{2}$ cross terms dominate the $n$ variance terms.

The leverage effect predicts a negative return–volatility correlation:

$$\text{D/E ratio} = \frac{\text{Debt}}{\text{Equity value}} \uparrow \quad \text{when prices fall}$$

## Example

Two equal-weight stocks, each with daily $\sigma = 2\%$.

**Calm** ($\rho = 0.3$): $\sigma_P = \sqrt{0.0002 + 0.00006} = 1.61\%$

**Stress** ($\rho = 0.7$): $\sigma_P = \sqrt{0.0002 + 0.00014} = 1.84\%$

A 14% rise in index vol is driven entirely by rising correlation — not by any increase in individual firm volatility. Scaled to 500 stocks, the effect is far more dramatic.

## Remember

The leverage explanation for index asymmetry is insufficient: the observed asymmetry is too large to come from D/E changes alone, and is present even in debt-free firms. The dominant mechanism is **correlation amplification** — markets move together in a crash, so index variance spikes far more than individual firm models predict. This is why bottom-up VaR aggregation (summing desk VaRs using calm-period correlations) systematically understates portfolio tail risk in a crisis.
