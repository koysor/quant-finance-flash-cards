# Market Price of Risk

**Topic:** Derivatives
**Tags:** market price of risk, drift, risk premium, girsanov, measure change, sharpe ratio
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **market price of risk** $\theta$ measures the excess return per unit of volatility that investors demand for bearing risk. It is the parameter that Girsanov's theorem uses to transform the physical measure $\mathbb{P}$ into the risk-neutral measure $\mathbb{Q}$ — it quantifies exactly how much drift must be removed from each asset to make discounted prices martingales.

## Key Formula

For an asset with drift $\mu$ and volatility $\sigma$ under $\mathbb{P}$:

$$\theta = \frac{\mu - r}{\sigma}$$

where $r$ is the risk-free rate. Under the change of measure:

$$dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} + \theta\,dt$$

so that $dS = rS\,dt + \sigma S\,dW_t^{\mathbb{Q}}$ under $\mathbb{Q}$.

The Radon–Nikodým derivative (change-of-measure density) is:

$$\frac{d\mathbb{Q}}{d\mathbb{P}} = \exp\!\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right)$$

## Example

A stock has $\mu = 10\%$, $\sigma = 25\%$, and the risk-free rate is $r = 4\%$.

$$\theta = \frac{0.10 - 0.04}{0.25} = 0.24$$

Investors demand 0.24 units of excess return per unit of volatility. Over one year, the drift removed by the measure change is $\theta \sigma = 0.24 \times 0.25 = 6\%$ — precisely the risk premium $\mu - r$.

For a second stock with $\mu = 15\%$ and $\sigma = 40\%$:

$$\theta = \frac{0.15 - 0.04}{0.40} = 0.275$$

If $\theta$ differs across assets, the market is not in equilibrium under a single equivalent martingale measure — this inconsistency signals either arbitrage or model misspecification.

## Remember

The market price of risk is the bridge between the real world and the pricing world. It is numerically identical to the **Sharpe ratio** of the asset, which is why Girsanov's theorem can be interpreted as saying "the measure change removes exactly one Sharpe ratio's worth of drift." In the Black–Scholes world, $\theta$ is constant and identical for all assets driven by the same Brownian motion — this is the one-factor consistency condition. When $\theta$ varies across assets, it indicates multiple sources of risk, each with its own price, leading to multi-factor models. Crucially, $\theta$ cancels out of the Black–Scholes formula: the option price depends on $\sigma$ but not on $\mu$ or $\theta$, because the hedging argument eliminates the risk premium entirely.
