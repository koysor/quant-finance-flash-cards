# Mean Reversion

**Topic:** Stochastic Processes
**Tags:** mean reversion, Ornstein-Uhlenbeck, interest rates, Vasicek, speed of reversion, long-run mean

---

## Definition

**Mean reversion** is the property of a stochastic process that is pulled back towards a long-run equilibrium level. Unlike geometric Brownian motion, where prices can drift indefinitely, a mean-reverting process has a restoring force: the further the current value deviates from the mean, the stronger the pull back. It is the standard model for interest rates, volatility, and spreads.

## Key Formula

The **Ornstein-Uhlenbeck** (OU) process is the simplest mean-reverting SDE:

$$dX = \kappa(\theta - X) \, dt + \sigma \, dW$$

where:
- $\kappa > 0$ is the **speed of mean reversion** (higher = faster pull-back)
- $\theta$ is the **long-run mean** (equilibrium level)
- $\sigma$ is the volatility of the process

The expected value at time $t$ given $X_0$ is:

$$\mathbb{E}[X_t] = \theta + (X_0 - \theta) \, e^{-\kappa t}$$

The long-run variance converges to:

$$\text{Var}(X_\infty) = \frac{\sigma^2}{2\kappa}$$

## Example

Suppose the short rate follows an OU process with $\theta = 5\%$, $\kappa = 0.8$, and $\sigma = 1.5\%$, starting at $X_0 = 7\%$.

After 1 year:

$$\mathbb{E}[X_1] = 5\% + (7\% - 5\%) \times e^{-0.8} = 5\% + 2\% \times 0.449 = 5.90\%$$

The rate has been pulled roughly halfway back towards 5%. The long-run standard deviation is:

$$\sqrt{\frac{0.015^2}{2 \times 0.8}} = \sqrt{0.000141} \approx 1.19\%$$

So rates fluctuate around 5% with a standard deviation of about 1.2 percentage points.

## Remember

Mean reversion is why interest rate models differ fundamentally from equity models. GBM lets stock prices grow without bound, which is reasonable for equities, but interest rates cannot drift to 50% or −20% indefinitely. The Vasicek and Hull-White models build on the OU process to capture this pull-back to equilibrium, and the speed of mean reversion $\kappa$ is the key calibration parameter — it determines how quickly mispricings in the yield curve are expected to correct.
