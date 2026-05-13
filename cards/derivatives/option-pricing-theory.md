# Option Pricing Theory

**Topic:** Derivatives
**Tags:** option pricing, no-arbitrage, replication, risk-neutral, Black-Scholes
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

Option pricing theory is the framework for determining the fair value of a derivative contract using **no-arbitrage principles**. The central idea is that an option's payoff can be replicated by a continuously adjusted portfolio of the underlying asset and a risk-free bond; the cost of that replicating portfolio equals the option price.

Two complementary approaches underpin all option pricing:
1. **Replication / no-arbitrage** — construct a self-financing portfolio that matches the option payoff at expiry
2. **Risk-neutral pricing** — value the option as the discounted expected payoff under a probability measure that makes all assets earn the risk-free rate

## Key Formula

The **Black-Scholes formula** for a European call is the canonical result:

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}$$

Where:
- $S_0$ — current asset price; $K$ — strike price; $T$ — time to expiry
- $r$ — continuously compounded risk-free rate; $\sigma$ — asset volatility
- $N(\cdot)$ — standard normal CDF

More generally, any derivative price satisfies:

$$V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\text{payoff at }T]$$

Where $\mathbb{Q}$ is the risk-neutral measure.

## Example

Price a European call with $S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year:

$$d_1 = \frac{0 + (0.05 + 0.02) \times 1}{0.20} = \frac{0.07}{0.20} = 0.35, \quad d_2 = 0.35 - 0.20 = 0.15$$

$$C = 100 \times N(0.35) - 100 e^{-0.05} \times N(0.15) \approx 100(0.637) - 95.12(0.560) \approx 63.7 - 53.3 = \pounds10.40$$

## Remember

The power of option pricing theory is that the risk-neutral probability $\mathbb{Q}$ is not the real-world probability — it is an artificial measure chosen to make discounting simple. This is why the drift of the underlying asset ($\mu$) does not appear in the Black-Scholes formula: the price is determined entirely by no-arbitrage replication, independent of investor risk preferences. This result underpins the entire derivatives industry.
