# Regime-Aware Allocation

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** regime-aware, hidden markov model, regime switching, asset allocation, bull market, bear market
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

Regime-aware allocation conditions portfolio weights on the estimated current market regime — typically identified by a Hidden Markov Model (HMM) — rather than on a single set of historical parameters. Each regime has its own estimated return vector $\mu_k$ and covariance matrix $\Sigma_k$, and the allocation blends regime-optimal portfolios weighted by the HMM's filtered regime probabilities.

## Key Formula

Let $K$ regimes be identified with current posterior probabilities $p_t(k) = P(\text{regime} = k \mid \mathcal{F}_t)$ updated by the HMM Bayes filter. The **regime-blended** mean-variance optimal weight is:

$$w_t^* = \sum_{k=1}^{K} p_t(k)\; w^*(k), \qquad w^*(k) = \frac{1}{\lambda} \Sigma_k^{-1} \mu_k$$

Transition between regimes follows a Markov chain with transition matrix $\Pi$, where $\Pi_{jk} = P(\text{next regime} = k \mid \text{current} = j)$. The filtered probabilities update each period via:

$$p_t(k) \propto f(x_t \mid \text{regime} = k) \sum_{j} \Pi_{jk}\, p_{t-1}(j)$$

## Example

Two-regime HMM fitted to monthly S&P 500 returns:
- **Bull regime** ($k=1$): $\mu_{\text{eq}} = +12\%$, $\sigma_{\text{eq}} = 10\%$ → $w^*(1) = $ 80% equities
- **Bear regime** ($k=2$): $\mu_{\text{eq}} = -6\%$, $\sigma_{\text{eq}} = 25\%$ → $w^*(2) = $ 20% equities

At a moment when $p_t(1) = 0.7$ and $p_t(2) = 0.3$:

$$w_t^* = 0.7 \times 80\% + 0.3 \times 20\% = 62\% \text{ equities}$$

As bearish signals accumulate over the next month (e.g. rising credit spreads, falling earnings), $p_t(2)$ might shift to 0.6, reducing equity to $0.4 \times 80\% + 0.6 \times 20\% = 44\%$.

## Remember

Regime-aware allocation sits conceptually between static mean-variance optimisation (single parameter set, no adaptation) and RL-based dynamic allocation (continuous state, learned policy). Its main practical limitation is **detection lag**: the HMM typically requires several weeks of data to assign high probability to a new regime — by which point the regime transition has already moved prices significantly. For this reason, regime-aware managers often layer in a **momentum signal** alongside the HMM, using price action to anticipate regime shifts before the probabilistic filter converges. This hybrid approach — systematic macro — is the dominant framework in quantitative multi-asset investing.
