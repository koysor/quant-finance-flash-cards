# Statistical Arbitrage

**Topic:** Derivatives
**Tags:** pairs trading, mean reversion, cointegration, spread trading, z-score
**Created:** 2026-03-19
**Author:** Claude Sonnet 4.6

---

## Definition

Statistical arbitrage (stat arb) exploits mean-reverting price relationships between related securities using statistical models. Unlike pure (riskless) arbitrage, it is **not risk-free** — it bets that a temporary deviation from a historically stable spread will revert to the mean. If the historical relationship breaks down, the spread may diverge further and the strategy loses money.

The canonical implementation is **pairs trading**: if two stocks A and B are *cointegrated*, the spread $S_t = P_A - \beta P_B$ is stationary — it fluctuates around a long-run mean $\mu$ rather than drifting away. A trader goes long the underpriced leg and short the overpriced leg when the spread deviates beyond a threshold.

## Key Formula

The **z-score** measures how far the current spread is from its historical mean in units of standard deviation:

$$z_t = \frac{S_t - \mu}{\sigma}$$

where $S_t = P_{A,t} - \beta P_{B,t}$ is the spread, $\mu$ is its sample mean, and $\sigma$ is its sample standard deviation.

**Signal rules:**
- **Enter:** go long the spread when $z_t < -2$; go short the spread when $z_t > +2$
- **Exit:** close the position when $z_t \approx 0$ (spread reverts to mean)
- **Stop-loss:** exit if $|z_t|$ exceeds a wider threshold (e.g. $3$) to limit losses from a regime break

## Example

Stocks A and B have historically traded with $\beta = 1.2$, $\mu = 0$, $\sigma = \pounds1.00$.

| Time | $P_A$ | $P_B$ | $S_t = P_A - 1.2\,P_B$ | $z_t$ | Action |
|------|--------|--------|------------------------|--------|--------|
| $t_1$ | £10.00 | £8.00 | $-\pounds0.60$ | $-0.6$ | No trade |
| $t_2$ | £10.00 | £9.00 | $-\pounds0.80$ | $-0.8$ | No trade |
| $t_3$ | £9.50  | £9.80 | $-\pounds2.26$ | $-2.3$ | **Enter:** buy A, sell B |
| $t_4$ | £10.20 | £8.50 | $+\pounds0.00$ | $0.0$ | **Exit:** spread reverted |

Profit comes from A rising and B falling back to equilibrium.

## Remember

In quantitative trading desks, stat arb is the workhorse strategy of **quantitative equity hedge funds** (e.g. Renaissance Technologies). The key risk — often called *convergence risk* or *model risk* — is that the spread never reverts. This happened spectacularly during the **2007 quant meltdown**, when simultaneous deleveraging by multiple stat arb funds caused previously stable spreads to diverge sharply, turning what looked like a low-risk strategy into catastrophic losses. The z-score entry signal is simple, but robust cointegration testing (using the Augmented Dickey-Fuller test) and disciplined stop-losses are what separate viable stat arb from a reckless bet.
