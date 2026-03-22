# Stochastic Volatility Models

**Topic:** Volatility
**Tags:** stochastic volatility, volatility smile, options pricing, mean reversion, vol of vol
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Stochastic volatility models allow the volatility of an asset's returns to follow its own random process rather than being treated as a fixed constant. This captures the empirical observation that market volatility clusters, varies over time, and correlates with the underlying asset price — phenomena that the constant-volatility Black-Scholes framework cannot reproduce.

## Key Formula

The general two-factor stochastic volatility framework couples the asset price $S$ with a variance (or volatility) process $v$:

$$dS_t = \mu \, S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^S$$

$$dv_t = \alpha(v_t) \, dt + \beta(v_t) \, dW_t^v$$

$$dW_t^S \cdot dW_t^v = \rho \, dt$$

where $\alpha(v_t)$ is the drift of the variance process, $\beta(v_t)$ is the diffusion of the variance process (vol of vol), and $\rho$ is the correlation between the asset and variance shocks.

Different model choices for $\alpha$ and $\beta$ give rise to specific models:

| Model | Variance drift $\alpha(v)$ | Variance diffusion $\beta(v)$ |
|---|---|---|
| Heston | $\kappa(\theta - v)$ | $\xi\sqrt{v}$ |
| SABR | $0$ | $\nu \, \sigma^\beta$ (on vol, not variance) |

## Example

Consider a generic stochastic volatility setting with current variance $v_0 = 0.0625$ (vol $= 25\%$) and vol of vol parameter producing $\beta(v_0) = 0.15$.

Over a small step $\delta t = 0.01$ with a variance shock $\epsilon^v = 1.0$:

$$\delta v \approx \alpha(v_0) \cdot 0.01 + 0.15 \times 1.0 \times \sqrt{0.01}$$

If mean reversion pulls variance toward $\theta = 0.04$ with speed $\kappa = 3$:

$$\alpha(v_0) = 3(0.04 - 0.0625) = -0.0675$$

$$\delta v = -0.0675 \times 0.01 + 0.15 \times 0.1 = -0.000675 + 0.015 = 0.01433$$

$$v_{0.01} = 0.0625 + 0.01433 = 0.0768 \quad (\text{vol} \approx 27.7\%)$$

The large positive variance shock has pushed volatility up despite mean reversion pulling it down, illustrating how randomness in the variance process generates the fat tails and volatility clustering seen in real markets.

## Remember

- The constant-volatility assumption in Black-Scholes produces flat implied volatility across strikes, contradicting the **volatility smile** observed in every liquid options market. Stochastic volatility models were developed specifically to explain and fit this smile.
- On trading desks, stochastic volatility models are calibrated to the observed **volatility surface** — the matrix of implied volatilities across strikes and maturities — to price and risk-manage exotic options consistently.
- The **correlation parameter** $\rho$ between asset returns and volatility shocks is the primary driver of skew: negative $\rho$ (typical for equities) means volatility rises when prices fall, making downside puts more expensive than upside calls.
- The Heston model is the most widely used stochastic volatility model for equities because it admits semi-analytical option prices via characteristic functions, while SABR dominates rates and FX markets for its tractable smile dynamics.
