# Approximate Entropy

**Topic:** Computational Finance
**Tags:** approximate entropy, time series, regularity, predictability, market efficiency, microstructure
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Approximate entropy (ApEn)** is a statistic that quantifies the regularity — or conversely the unpredictability — of a time series. A low ApEn indicates that similar patterns recur frequently and the sequence is predictable; a high ApEn indicates irregular, random-like behaviour. It was introduced by Pincus (1991) as a computationally tractable approximation to the entropy rate of a process.

## Key Formula

Given a time series $\{x_1, \ldots, x_N\}$, parameters $m$ (template length) and $r$ (tolerance):

1. Form all length-$m$ templates: $\mathbf{u}(i) = (x_i, \ldots, x_{i+m-1})$ for $i = 1, \ldots, N-m+1$

2. For each template, count matches within tolerance $r$:

$$C_i^m(r) = \frac{\#\{j : \max_k \lvert x_{i+k} - x_{j+k}\rvert \leq r\}}{N - m + 1}$$

3. Compute:

$$\Phi^m(r) = \frac{1}{N-m+1} \sum_{i=1}^{N-m+1} \ln C_i^m(r)$$

4. Approximate entropy:

$$\text{ApEn}(m, r, N) = \Phi^m(r) - \Phi^{m+1}(r)$$

Typical parameters: $m = 2$, $r = 0.1 \times \text{SD}(x)$. Higher ApEn means less regularity.

## Example

Two intraday price series over 500 ticks with $m = 2$, $r = 0.1\sigma$:

| Series | Description | ApEn |
|---|---|---|
| Trending market (strong momentum) | Returns cluster in direction | 0.18 |
| Efficient market (near-random walk) | No pattern recurs | 1.42 |

The trending series has low ApEn because the pattern "up tick followed by up tick" recurs often. The efficient market series has high ApEn close to its maximum — consistent with a random walk where each new tick is independent of the last.

## Remember

Approximate entropy has been used in market microstructure research as an empirical measure of market efficiency: a perfectly efficient market should have maximum ApEn (returns are unpredictable), whereas a market with informed trading or momentum effects should show lower ApEn. In practice, ApEn of tick-by-tick order flow declines before earnings announcements and other scheduled events, reflecting the information asymmetry between informed and uninformed traders. It has also been used to detect regime changes in volatility: periods of rising ApEn in realised volatility series signal the breakdown of volatility clustering (GARCH effects), while falling ApEn signals strengthening persistence that mean-reversion strategies can exploit.
