# Black–Derman–Toy Model

**Topic:** Fixed Income
**Tags:** BDT, binomial tree, short rate, lognormal, yield curve, volatility structure, calibration
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **Black–Derman–Toy (BDT) model** is a discrete-time, lognormal short-rate model that constructs a binomial recombining tree calibrated simultaneously to the current yield curve and the term structure of yield volatilities. Because it is lognormal, rates are always positive, and the tree is tractable enough to price callable bonds and American-style interest rate options directly.

## Key Formula

At each node $(i, j)$ (time step $i$, position $j$ from the bottom), the short rate is:

$$r_{i,j} = r_{i,0}\,e^{2j\sigma_i\sqrt{\Delta t}}$$

where $r_{i,0}$ is the lowest rate at time step $i$ and $\sigma_i$ is the yield volatility at maturity $i\,\Delta t$.

Up and down moves are **equal probability** ($p = \frac{1}{2}$), and the tree **recombines** (up then down = down then up). At each time step, $r_{i,0}$ and $\sigma_i$ are jointly calibrated so that:

1. The model price of a zero-coupon bond maturing at $(i+1)\Delta t$ equals the market price.
2. The model yield volatility at maturity $(i+1)\Delta t$ equals the market cap volatility.

## Example

With $\Delta t = 1$ year, $r = 5\%$, $\sigma_1 = 20\%$: at time 1 the tree has two nodes $r_{1,1} = r_{1,0}\,e^{2 \times 0.20 \times 1} = r_{1,0} \times 1.492$ and $r_{1,0}$. Setting the discounted average of $\frac{1}{2}(\frac{1}{1+r_{1,1}} + \frac{1}{1+r_{1,0}})$ equal to the 2-year discount factor pins $r_{1,0}$, and the ratio $r_{1,1}/r_{1,0} = e^{2\sigma_1}$ pins $\sigma_1$.

## Remember

BDT occupies a unique niche: it is the simplest model that fits **both** the yield curve and the cap/floor volatility surface, and it produces a lognormal (non-negative) rate distribution. The price is that the mean-reversion speed is determined by the volatility term structure rather than being a free parameter — if the volatility structure is humped, BDT can produce negative mean reversion at long maturities. In practice BDT is used for callable bond pricing where the discreteness of the tree enables early-exercise optimisation at each node.
