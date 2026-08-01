# Mean-Reversion Half-Life

**Topic:** Statistics
**Tags:** ornstein-uhlenbeck, half-life, ar1 regression, pairs trading, signal generation, holding period
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

The mean-reversion half-life is the expected time for a spread to close half of its current deviation from equilibrium. It is obtained by fitting an Ornstein-Uhlenbeck process to the cointegrating residual, and it is the single most useful number for deciding whether a statistically valid spread is actually tradeable.

## Key Formula

The OU process for the spread $z_t$ and its discrete solution:

$$dz_t = -\theta\,(z_t - \mu_e)\,dt + \sigma_{OU}\,dW_t \quad\Longrightarrow\quad z_{t+\tau} = \left(1-e^{-\theta\tau}\right)\mu_e + e^{-\theta\tau}z_t + \epsilon_{t,\tau}$$

This is an AR(1) regression $z_t = C + B z_{t-1} + \epsilon_t$, so the parameters follow directly:

$$\theta = -\frac{\ln B}{\tau}, \qquad \mu_e = \frac{C}{1-B}, \qquad \tilde\tau_{1/2} = \frac{\ln 2}{\theta}$$

The equilibrium standard deviation sets the trading bounds:

$$\sigma_{eq} = \sqrt{\frac{\mathrm{Var}[\epsilon_{t,\tau}]}{1 - e^{-2\theta\tau}}}, \qquad \text{entry at } \mu_e \pm Z\sigma_{eq}$$

## Example

An AR(1) fit on a daily spread gives $B = 0.968$ with $\tau = 1$ day.

$$\theta = -\ln(0.968) = 0.0325 \text{ per day} \quad\Longrightarrow\quad \tilde\tau_{1/2} = \frac{0.693}{0.0325} = 21.3 \text{ days}$$

A three-week half-life is workable. Contrast a second pair with $B = 0.9945$: $\theta = 0.00551$ and a half-life of 126 days — six months. That pair may pass every cointegration test and still be untradeable, because the capital is tied up far too long between round trips.

## Remember

This is the filter that separates statistically cointegrated pairs from tradeable ones, and most candidates fail it: genuine cointegration often only emerges over fifteen years or more, which produces half-lives measured in months. The half-life is roughly the holding period per position, so it directly determines how many round trips a backtest can generate — and a handful of trades is far too few to distinguish skill from luck. It also disciplines the entry threshold $Z$: widening the bounds raises profit per trade but cuts the number of trades sharply, with $Z > 0.8$ typically halving them, while simultaneously raising the chance that a spread which has moved that far has suffered a **structural break** rather than a temporary dislocation. Choose $Z$ by searching a range such as $[0.3, 1.4]$ against both P&L and trade count, never by assuming $Z = 1$.
