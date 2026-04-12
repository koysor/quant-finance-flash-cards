# Aggregational Gaussianity

**Topic:** Statistics
**Tags:** returns, normal-distribution, central-limit-theorem, fat-tails, var, volatility-clustering
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Aggregational Gaussianity is the empirical observation that, as the return horizon lengthens, the distribution of returns becomes progressively more normal. Fat tails and skewness diminish with aggregation.

The mechanism is the **Central Limit Theorem (CLT)**: a monthly return is approximately the sum of ~22 daily returns, and an annual return the sum of ~252. Summing many finite-variance random variables drives the distribution towards a normal.

| Horizon | Behaviour |
|---|---|
| Tick / minute | Extremely fat-tailed |
| Daily | Excess kurtosis $\approx 4$–$8$ |
| Weekly | Less fat-tailed |
| Monthly | Close to normal; kurtosis $\approx 3$–$4$ |
| Annual | Roughly normal (small samples make formal testing hard) |

**Caveat:** daily returns are not i.i.d. — volatility clustering violates independence. Convergence to normality is therefore *slower* than the i.i.d. CLT predicts.

## Key Formula

For i.i.d. returns $r_1, r_2, \ldots, r_T$ each with mean $\mu$ and variance $\sigma^2$, the $T$-period return $R_T = \sum_{t=1}^{T} r_t$ satisfies:

$$R_T \xrightarrow{d} \mathcal{N}(T\mu,\; T\sigma^2) \quad \text{as } T \to \infty$$

The square-root-of-time scaling for VaR follows directly:

$$\text{VaR}_T = \text{VaR}_1 \times \sqrt{T}$$

This rule is only valid when returns are **i.i.d. and normally distributed**. Volatility clustering breaks the independence assumption and makes $\sqrt{T}$ scaling unreliable.

## Example

A risk manager holds a portfolio with a 1-day 99% VaR of £1 m.

- **Naïve annual VaR** (i.i.d. assumption): $£1\text{m} \times \sqrt{252} \approx £15.9\text{m}$
- **Problem:** if daily volatility clusters — quiet patches followed by turbulent patches — the annual distribution is *not* normal and $\sqrt{T}$ understates true tail risk during stress periods.

At a 10-day regulatory horizon (Basel), the Basel III formula uses $\sqrt{10}$ scaling, but supervisors recognise it is approximate precisely because of volatility clustering.

## Remember

**Daily/weekly VaR** must account for fat tails explicitly (e.g. via historical simulation or $t$-distribution) because the CLT has not yet had enough summands to wash out the heavy tails present in high-frequency returns.

**Annual VaR** can *approximately* assume normality — the sum of ~252 daily returns is close enough to normal for many practical purposes — though fat tail risk never fully disappears.

**$\sqrt{T}$ scaling breaks** with volatility clustering: when a bad day is more likely to be followed by another bad day (persistence), the variance of the $T$-period return grows *faster* than $T\sigma^2$, so $\text{VaR}_1 \times \sqrt{T}$ underestimates true multi-day VaR during turbulent regimes.
