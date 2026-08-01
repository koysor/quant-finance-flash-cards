# Variance Ratio Test

**Topic:** Statistics
**Tags:** random walk, mean reversion, regime filter, autocorrelation, market efficiency, lo-mackinlay
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The variance ratio test compares the variance of $q$-period returns with $q$ times the variance of one-period returns. Under a random walk the two are equal, so the ratio is one; departures from one indicate mean reversion or trending behaviour.

## Key Formula

$$VR(q) = \frac{\mathrm{Var}\!\left[r_t(q)\right]}{q\,\mathrm{Var}\!\left[r_t(1)\right]}, \qquad r_t(q) = \sum_{i=0}^{q-1} r_{t-i}$$

Because variance accumulates linearly only when increments are uncorrelated, the ratio can be written in terms of autocorrelations $\rho_k$:

$$VR(q) = 1 + 2\sum_{k=1}^{q-1}\left(1 - \frac{k}{q}\right)\rho_k$$

| $VR(q)$ | Autocorrelation | Behaviour |
|---|---|---|
| $= 1$ | zero | random walk |
| $< 1$ | negative | mean-reverting |
| $> 1$ | positive | trending |

Lo and MacKinlay's heteroskedasticity-robust statistic $z(q) = (VR(q)-1)/\sqrt{\theta(q)}$ is asymptotically standard normal.

## Example

Daily returns on a spread over 500 days: one-day variance $2.5\times10^{-5}$, five-day variance $8.75\times10^{-5}$.

$$VR(5) = \frac{8.75\times10^{-5}}{5 \times 2.5\times10^{-5}} = \frac{8.75}{12.5} = 0.70$$

Five-day moves are 30% smaller than a random walk implies, so the series pulls back on itself — mean-reverting, and a favourable regime for a Bollinger or Z-score entry rule. Had the same computation returned 1.35, the series would be trending and reversion entries would keep firing into continuing moves.

## Remember

The value of $VR$ in a trading system is as a **regime filter, not a signal**: it says whether to trade at all, while the Bollinger band or Z-score rule says when. Gating reversion entries on $\widehat{VR}_t(q) < 1 - \epsilon$ computed on a rolling window suppresses exactly the losing trades that occur when a range-bound market starts to trend — the situation in which price rides the upper band for many bars and every reversion entry is a false signal. The window length is the real design decision: too short and the estimate flips around one on noise, too long and it confirms a regime only after the profitable part has passed. Because the filter changes trade frequency rather than direction, the honest way to demonstrate it earns its keep is to report backtests both with and without it.
