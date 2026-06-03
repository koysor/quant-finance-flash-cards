# Fractional Brownian Motion

**Topic:** Stochastic Processes
**Tags:** fractional brownian motion, hurst exponent, long memory, rough volatility, self-similarity, non-semimartingale
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Fractional Brownian motion** $W^H = \{W^H_t,\, t \ge 0\}$ with **Hurst exponent** $H \in (0,1)$ is the unique (up to scaling) Gaussian process with zero mean, stationary increments, and self-similarity $W^H_{ct} \stackrel{d}{=} c^H W^H_t$. For $H = \tfrac{1}{2}$ it reduces to standard Brownian motion. For $H \ne \tfrac{1}{2}$ its increments are correlated — and it is not a semimartingale, placing it outside classical Itô calculus.

## Key Formula

The covariance structure that defines $W^H$:

$$\text{Cov}(W^H_t, W^H_s) = \frac{1}{2}\!\left(t^{2H} + s^{2H} - \lvert t - s\rvert^{2H}\right)$$

Increment correlation between non-overlapping intervals:

$$\text{Corr}\!\left(\Delta W^H_{[0,1]},\, \Delta W^H_{[n, n+1]}\right) \sim H(2H-1)\,n^{2H-2} \quad \text{as } n \to \infty$$

- $H > \tfrac{1}{2}$: positive correlations, **long memory** — trends persist
- $H < \tfrac{1}{2}$: negative correlations, **anti-persistence** — increments reverse, paths are rougher than Brownian motion
- $H = \tfrac{1}{2}$: zero correlations, standard Brownian motion

## Example

Realised variance of SPX over rolling 1-day windows, measured daily for 10 years. Fit the autocorrelation decay of log-variance: $\text{Corr}(\log V_0, \log V_n) \approx n^{2H-2}$ with $H \approx 0.1$. The negative exponent $2H - 2 = -1.8$ means variance shocks decay faster than BM ($-1$), confirming rough dynamics. A 10-day vol spike reverts toward baseline much faster than a Heston CIR process would predict, and the fractional model with $H = 0.1$ matches the empirical reversion speed.

## Remember

The $H < \tfrac{1}{2}$ regime of fBm is the mathematical foundation of rough volatility — the roughness of realised variance paths is precisely the anti-persistence captured by the Hurst exponent below $\tfrac{1}{2}$. The critical implication for pricing is that **fBm is not a semimartingale** for $H \ne \tfrac{1}{2}$: classical Itô's lemma and the Black-Scholes no-arbitrage argument both fail, because the quadratic variation of $W^H$ is zero for $H > \tfrac{1}{2}$ and infinite for $H < \tfrac{1}{2}$. This forces rough volatility models to use Volterra processes (fBm represented as a moving average of standard BM) rather than fBm directly, preserving a degree of tractability while retaining the roughness.
