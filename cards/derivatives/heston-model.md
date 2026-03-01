# Heston Model

**Topic:** Derivatives
**Tags:** stochastic volatility, Heston, volatility smile, options, pricing, mean reversion

---

## Definition

The **Heston model** (1993) is a stochastic volatility model in which the variance of the asset price follows its own random process. Unlike Black-Scholes, which assumes constant volatility, the Heston model lets volatility itself fluctuate randomly over time, producing the volatility smiles and skews observed in real option markets.

## Key Formula

The asset price $S$ and its instantaneous variance $v$ evolve as a pair of coupled SDEs:

$$dS_t = \mu \, S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^S$$

$$dv_t = \kappa (\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^v$$

where:

| Symbol | Meaning |
|---|---|
| $\mu$ | Drift of the asset price |
| $v_t$ | Instantaneous variance at time $t$ |
| $\kappa$ | Speed of mean reversion of variance |
| $\theta$ | Long-run average variance |
| $\xi$ | Volatility of variance (vol of vol) |
| $\rho$ | Correlation between $dW_t^S$ and $dW_t^v$ |

The two Brownian motions are correlated: $dW_t^S \cdot dW_t^v = \rho \, dt$.

The **Feller condition** $2\kappa\theta > \xi^2$ ensures that the variance process stays strictly positive.

## Example

Suppose $v_0 = 0.04$ (i.e. current vol $= 20\%$), $\theta = 0.04$, $\kappa = 2$, $\xi = 0.3$, $\rho = -0.7$.

Over a small step $\delta t = 0.01$ with random draws $\epsilon^S = 0.5$, $\epsilon^v = -0.3$:

$$\delta v = 2(0.04 - 0.04)(0.01) + 0.3\sqrt{0.04}(-0.3)\sqrt{0.01} = 0 - 0.0018 = -0.0018$$

$$v_{0.01} = 0.04 - 0.0018 = 0.0382 \quad (\text{vol} \approx 19.5\%)$$

The variance has drifted slightly below its long-run level and will be pulled back toward $\theta = 0.04$ by the mean-reversion term.

## Remember

- The **negative correlation** ($\rho < 0$) between asset returns and variance is the key mechanism that produces the **volatility skew**: when the stock drops, variance tends to rise, making out-of-the-money puts more expensive — exactly the pattern seen in equity markets.
- The Heston model is popular because it admits a **semi-analytical** pricing formula for European options via characteristic functions and Fourier inversion, making it much faster to calibrate than models that require full Monte Carlo simulation.
- Calibrating the five parameters ($v_0$, $\kappa$, $\theta$, $\xi$, $\rho$) to the observed implied volatility surface is a core task on derivatives desks — the model must reproduce both the smile across strikes and the term structure across maturities.
