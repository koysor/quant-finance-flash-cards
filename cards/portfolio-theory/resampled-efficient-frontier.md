# Resampled Efficient Frontier

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** resampled frontier, bootstrap, estimation error, robust optimisation, Michaud
**Author:** Claude Opus 4.6

---

## Definition

The **resampled efficient frontier**, introduced by Michaud (1998), addresses the instability of Markowitz optimisation by generating many alternative efficient frontiers from bootstrapped inputs and averaging the resulting portfolio weights. Each resample draws a new set of returns from a distribution calibrated to the original estimates, computes a new frontier, and the final portfolio at each risk level is the average of the corresponding portfolios across all resamples.

## Key Formula

**Algorithm:**

1. Estimate $\hat{\boldsymbol{\mu}}$ and $\hat{\Sigma}$ from historical data
2. For $b = 1, \ldots, B$ (typically $B = 500\text{--}1000$):
   - Draw simulated returns $\mathbf{r}^{(b)} \sim \mathcal{N}(\hat{\boldsymbol{\mu}}, \hat{\Sigma})$ of length $T$
   - Compute $\hat{\boldsymbol{\mu}}^{(b)}$ and $\hat{\Sigma}^{(b)}$ from the simulated sample
   - Solve the Markowitz problem to get weights $\mathbf{w}^{(b)}(\sigma)$ for each target risk $\sigma$
3. Average: $\mathbf{w}_{\text{resampled}}(\sigma) = \frac{1}{B} \sum_{b=1}^{B} \mathbf{w}^{(b)}(\sigma)$

## Example

A three-asset portfolio is optimised at target volatility $\sigma = 12\%$. Standard Markowitz produces weights $(0.65, \; -0.10, \; 0.45)$ — including a short position.

After 500 resamples, the averaged weights become $(0.48, \; 0.12, \; 0.40)$:
- The extreme long position in asset 1 has shrunk from 65% to 48%
- The short position in asset 2 has flipped to a small long position of 12%
- Asset 3 remains similar

The resampled weights are more diversified and avoid the extreme positions that arise from exploiting estimation noise.

## Remember

Standard Markowitz optimisation is an "error maximiser" — it overweights assets with overestimated returns and underweights those with underestimated returns, producing extreme, concentrated portfolios. Resampling acknowledges that the inputs are uncertain and averages over many plausible scenarios, producing weights that are more diversified, more stable through time, and less sensitive to small changes in inputs. The resampled frontier typically lies inside the classical frontier (lower return for the same risk), but this apparent inefficiency is actually a feature — the classical frontier is overfitted to noisy data and cannot be achieved out of sample.
